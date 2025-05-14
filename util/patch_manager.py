import ast
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from typing import List, Tuple, Optional, TypedDict

# Try to import astor, fallback or raise if ast.unparse (Python 3.9+) is not available
try:
    import astor
    _HAS_ASTOR = True
except ImportError:
    _HAS_ASTOR = False

if not hasattr(ast, 'unparse') and not _HAS_ASTOR:
    logging.warning("Neither ast.unparse (Python 3.9+) nor astor library is available. AST-based patching will fail.")

logger = logging.getLogger(__name__)


class Suggestion(TypedDict):
    description: str
    original_code: str
    fixed_code: str


def parse_gpt_suggestions(suggestions_text: str) -> List[Suggestion]:
    suggestions: List[Suggestion] = []
    # Regex to capture each fix block, more robust to varying newlines in code
    pattern = re.compile(
        r"Potential fix \((?P<id>\d+)\):\s*(?P<description>[^\n]*)\n"  # Description (assumed single line)
        r"Original code line/lines:\s*\n(?P<original_code>.*?)\s*\n"  # Matches "line:" or "lines:", then captures code
        r"Fixed code line/lines:\s*\n(?P<fixed_code>.*?)\s*\n"  # Matches "line:" or "lines:", then captures code
        r"^\s*-{5,}\s*$",
        re.DOTALL | re.MULTILINE
    )

    matches = pattern.finditer(suggestions_text)
    for match in matches:
        # suggestions.append({
        #     "description": match.group("description").strip(),
        #     "original_code": match.group("original_code").strip(),
        #     "fixed_code": match.group("fixed_code").strip()
        # })
        description = match.group("description").strip()
        original_code = match.group("original_code")
        fixed_code = match.group("fixed_code")
        if original_code.endswith('\n'):
            original_code = original_code[:-1]
        if fixed_code.endswith('\n'):
            fixed_code = fixed_code[:-1]

        suggestions.append({
            "description": description,
            "original_code": original_code,
            "fixed_code": fixed_code
        })
    if not suggestions and suggestions_text.strip():  # If regex failed but there's text
        logger.warning(f"Could not parse GPT suggestions with regex. Full text: {suggestions_text[:500]}")
    return suggestions


def apply_fix_to_method_source(
        original_method_source: str,
        original_code_snippet: str,  # The "Original code line/lines" from LLM
        fixed_code_snippet: str  # The "Fixed code line/lines" from LLM
) -> Optional[str]:
    """
    Applies the fix snippet to the original method source.
    This assumes original_code_snippet is an exact substring.
    """
    if original_code_snippet == fixed_code_snippet:
        logger.info("Original and fixed code snippets are identical. No changes.")
        return None  # Or original_method_source if we want to indicate "no effective change"

    # Normalize line endings for robust replacement
    norm_original_method_source = original_method_source.replace('\r\n', '\n')
    norm_original_snippet = original_code_snippet.replace('\r\n', '\n')
    # fixed_code_snippet should be used as is, assuming LLM provides correct newlines.

    if norm_original_snippet not in norm_original_method_source:
        logger.warning(
            "Original code snippet not found in method source.\n"
            f"--- Snippet ---\n{original_code_snippet}\n"
            f"--- Method Source (first 500 chars) ---\n{original_method_source[:500]}"
        )
        # Try a more flexible approach: line-based diff if snippets are multi-line
        # For now, require exact substring match for simplicity of the LLM's task
        return None

    # Replace the first occurrence. If the snippet can appear multiple times, this might be an issue.
    # The prompt should ideally guide the LLM to provide unambiguous original_code_snippet.
    count = norm_original_method_source.count(norm_original_snippet)
    if count > 1:
        logger.warning(f"Original code snippet appears {count} times. Replacing the first instance.")

    # Perform replacement on the normalized source, then potentially restore original newlines if needed
    # However, it's usually fine to proceed with normalized '\n' newlines.
    patched_method_source = norm_original_method_source.replace(norm_original_snippet, fixed_code_snippet, 1)

    if patched_method_source == norm_original_method_source:  # Replacement had no effect
        logger.warning("Applying fix resulted in no change to the method source. Check snippets.")
        return None

    return patched_method_source


def replace_method_in_file_ast(
        file_path: str,
        class_name: Optional[str],  # Name of the class if method is part of a class
        method_name: str,
        new_method_full_source: str
) -> bool:
    """
    Replaces a method/function in a Python file using AST.
    `new_method_full_source` should be the complete source code of the new method
    (e.g., "def test_something(self):\n  ...")
    """
    logger.info(f"AST Patcher: Raw new_method_full_source: {repr(new_method_full_source)}")

    dedented_source = textwrap.dedent(new_method_full_source)
    cleaned_source = dedented_source.strip()

    logger.info(f"AST Patcher: Cleaned new_method_full_source for parsing (repr): {repr(cleaned_source)}")

    if not cleaned_source:  # Handle empty string after cleaning
        logger.error("AST Patcher: New method source is empty after cleaning.")
        return False
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()

        original_tree = ast.parse(file_content, filename=file_path)
        # Parse the new method source. It should be a FunctionDef or AsyncFunctionDef.
        # Wrap in a dummy class/module if it's just a method snippet to make it parseable standalone.
        # However, new_method_full_source should be "def foo(): ..."
        new_method_node_list = ast.parse(cleaned_source).body
        if not new_method_node_list or not isinstance(new_method_node_list[0], (ast.FunctionDef, ast.AsyncFunctionDef)):
            logger.error(f"AST Patcher: New method source is not a valid function definition: {cleaned_source[:100]}")
            return False
        new_method_ast_node = new_method_node_list[0]

    except Exception as e:
        logger.error(f"AST Patcher: Error parsing source file or new method: {e}. Parsed source (repr): {repr(cleaned_source)}")
        return False

    class MethodReplacerTransformer(ast.NodeTransformer):
        def __init__(self, target_name, replacement_node):
            self.target_name = target_name
            self.replacement_node = replacement_node
            self.replaced_in_class = False  # Specific for methods in classes

        def visit_FunctionDef(self, node):
            if node.name == self.target_name:
                self.replaced_in_class = True
                return self.replacement_node
            return self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node):
            if node.name == self.target_name:
                self.replaced_in_class = True
                return self.replacement_node
            return self.generic_visit(node)

    class TopLevelTransformer(ast.NodeTransformer):
        def __init__(self, target_class_name, target_method_name, replacement_method_node):
            self.target_class_name = target_class_name
            self.target_method_name = target_method_name
            self.replacement_method_node = replacement_method_node
            self.replaced = False

        def visit_ClassDef(self, node):
            if self.target_class_name and node.name == self.target_class_name:
                # We are inside the target class, now look for the method
                method_replacer = MethodReplacerTransformer(self.target_method_name, self.replacement_method_node)
                node.body = [method_replacer.visit(item) for item in node.body]
                if method_replacer.replaced_in_class:
                    self.replaced = True
            return self.generic_visit(node)  # Important to visit children if not the target class

        def visit_FunctionDef(self, node):  # For top-level functions
            if not self.target_class_name and node.name == self.target_method_name:
                self.replaced = True
                return self.replacement_method_node
            return self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node):  # For top-level async functions
            if not self.target_class_name and node.name == self.target_method_name:
                self.replaced = True
                return self.replacement_method_node
            return self.generic_visit(node)

    transformer = TopLevelTransformer(class_name, method_name, new_method_ast_node)
    new_tree = transformer.visit(original_tree)

    if transformer.replaced:
        try:
            if hasattr(ast, 'unparse'):  # Python 3.9+
                new_code = ast.unparse(new_tree)
            elif _HAS_ASTOR:
                new_code = astor.to_source(new_tree)
            else:
                logger.error("AST Patcher: No unparsing capability (ast.unparse or astor). Cannot write changes.")
                return False

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_code)
            logger.info(f"AST Patcher: Successfully replaced method '{method_name}' in '{file_path}'.")
            return True
        except Exception as e:
            logger.error(f"AST Patcher: Error unparsing or writing modified code: {e}")
            return False
    else:
        logger.warning(f"AST Patcher: Method '{method_name}' (Class: {class_name}) not found or not replaced in '{file_path}'.")
        return False


def get_failing_line_number_from_traceback(traceback_text: str, target_file_abs_path: str) -> Tuple[Optional[str], Optional[int]]:
    """
    Parses traceback to find the failing line number in the specified target file.
    Returns (failing_file_path, line_number) or (None, None).
    Searches from the bottom of the traceback upwards.
    """
    normalized_target_file_path = os.path.normpath(target_file_abs_path)

    for line in reversed(traceback_text.strip().split('\n')):
        # Match "  File "<path>", line <num>, in <func>"
        file_line_match = re.search(r'^\s*File\s*"(.+?)",\s*line\s*(\d+)', line)
        if file_line_match:
            file_path_in_tb = os.path.normpath(file_line_match.group(1))
            line_num = int(file_line_match.group(2))
            if file_path_in_tb == normalized_target_file_path:
                return file_path_in_tb, line_num

        # Match "path/file.py:lineno: Error" (less common for deep tracebacks but good for summaries)
        # Ensure this path is absolute or comparable to target_file_abs_path
        file_colon_line_match = re.match(r'^([^:]+):(\d+):', line.strip())
        if file_colon_line_match:
            file_path_in_tb_rel = os.path.normpath(file_colon_line_match.group(1))
            line_num = int(file_colon_line_match.group(2))
            # If path from traceback is relative, see if it matches end of absolute path
            if normalized_target_file_path.endswith(file_path_in_tb_rel):
                # This is a heuristic. Be cautious if filename isn't unique.
                # Prefer the "File ..." format if available.
                return normalized_target_file_path, line_num
    return None, None


def run_specific_test(
        test_node_id: str,
        test_file_abs_path: str,
        is_verification_run: bool = False
) -> Tuple[bool, Optional[str], Optional[int]]:
    """
    Runs a specific test using a subprocess call to pytest.
    Returns: (passed: bool, traceback_text: Optional[str], failing_line_in_file_abs: Optional[int])
    """
    passed = False
    traceback_text = None
    failing_line_in_file_abs = None

    # Use a temporary file for pytest-reportlog's JSONL output
    # Ensure the pytest-reportlog plugin is installed: pip install pytest-reportlog
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".jsonl") as tmp_report_file_obj:
        report_log_path = tmp_report_file_obj.name

    python_executable_dir = os.path.dirname(sys.executable)
    pytest_executable = os.path.join(python_executable_dir, "pytest")

    # Fallback if it's not directly there (e.g. installed differently or not in venv)
    if not os.path.exists(pytest_executable):
        pytest_executable_from_path = shutil.which("pytest")  # Check PATH
        if pytest_executable_from_path:
            pytest_executable = pytest_executable_from_path
            logger.info(f"Using pytest from PATH: {pytest_executable}")
        else:
            logger.error("Could not find pytest executable. Falling back to just 'pytest'.")
            pytest_executable = "pytest"  # Hope for the best via PATH
    else:
        logger.info(f"Using pytest from current Python environment: {pytest_executable}")

    # Command to run pytest
    # Using the node ID is the most specific way to target a test.
    cmd = [pytest_executable, test_node_id, f"--report-log={report_log_path}", "-v"]
    if is_verification_run:
        cmd.append("--internal-rerun")
    logger.info(f"Executing test with command: {' '.join(cmd)}")

    try:
        project_root = os.path.abspath(os.path.join(os.path.dirname(test_file_abs_path), ".."))
        process = subprocess.run(cmd, capture_output=True, text=True, check=False, cwd=project_root)  # Run from test file's dir

        if process.returncode == 0:  # Pytest exit code 0 means all tests passed
            passed = True
            logger.info(f"Test {test_node_id} PASSED after patching.")
        else:
            logger.info(f"Test {test_node_id} FAILED after patching. Exit code: {process.returncode}")
            # Parse the report log to get failure details
            if os.path.exists(report_log_path):
                with open(report_log_path, 'r') as f_report:
                    for line in f_report:
                        try:
                            report_item = json.loads(line)
                            # We are interested in the 'call' phase of our specific test
                            if report_item.get("nodeid") == test_node_id and \
                                    report_item.get("when") == "call" and \
                                    report_item.get("outcome") == "failed":

                                longrepr = report_item.get("longrepr")
                                if isinstance(longrepr, dict):  # Standard pytest-reportlog format
                                    # Construct a readable traceback
                                    tb_message = longrepr.get("reprcrash", {}).get("message", "")
                                    tb_entries = "\n".join(
                                        f"  File \"{entry['path']}\", line {entry['lineno']}, in {entry['message'] if entry['message'] != '??' else longrepr.get('reprcrash', {}).get('path', '').split('/')[-1]}"
                                        # Use filename if func name is '??'
                                        for entry in longrepr.get("reprtraceback", {}).get("reprentries", [])
                                    )
                                    traceback_text = f"{longrepr.get('reprcrash', {}).get('exconly', tb_message)}\n{tb_entries}"

                                    # Extract failing line from this structured traceback
                                    _, failing_line_in_file_abs = get_failing_line_number_from_traceback(traceback_text, test_file_abs_path)
                                    break
                                elif isinstance(longrepr, str):  # Fallback for simpler string representation
                                    traceback_text = longrepr
                                    _, failing_line_in_file_abs = get_failing_line_number_from_traceback(traceback_text, test_file_abs_path)
                                    break
                        except json.JSONDecodeError:
                            logger.warning(f"Could not decode JSON line from report log: {line}")
            if not traceback_text:  # Fallback if parsing report log failed
                traceback_text = f"STDOUT:\n{process.stdout}\nSTDERR:\n{process.stderr}"
                logger.warning(f"Could not extract detailed traceback from report log. Using stdout/stderr for {test_node_id}.")
                _, failing_line_in_file_abs = get_failing_line_number_from_traceback(traceback_text, test_file_abs_path)

    except FileNotFoundError:
        logger.error("`pytest` command not found. Ensure pytest is installed and in PATH.")
        traceback_text = "`pytest` command not found."
    except Exception as e:
        logger.error(f"Exception running specific test {test_node_id}: {e}")
        traceback_text = f"Exception during test re-run: {e}"
    finally:
        if os.path.exists(report_log_path):
            os.remove(report_log_path)

    return passed, traceback_text, failing_line_in_file_abs
