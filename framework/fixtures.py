import logging
import os
import shutil

import pytest
import undetected_chromedriver as uc
from dotenv import load_dotenv

from framework.config import DEFAULT_CHROME_OPTION_ARGS, CHROME_PREFS, MAX_FIX_ATTEMPTS_PER_FAILURE_POINT
from framework.custom_selenium import CustomWebDriver
from framework.logger_setup import logger, get_list_handler
from util.agent import call_gpt_for_candidate_fixes, classify_failure_source
from util.llm_helper import get_web_element_rect, gather_test_code_and_failing_line
from util.patch_manager import parse_gpt_suggestions, apply_fix_to_method_source, replace_method_in_file_ast, run_specific_test


@pytest.fixture(scope="class", autouse=True)
def driver_session(request):
    # start display
    # https://stackoverflow.com/questions/72853097/pyvirtual-display-and-xvfb-on-macos-latest
    # display = Display(visible=DISPLAY_VISIBLE, size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))
    # display.start()
    # chrome_binary_path = '/Applications/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
    # service = Service(executable_path=chrome_binary_path)
    logger.info("Initializing WebDriver for class.")
    tmp_opts = uc.ChromeOptions()
    tmp_opts.add_argument("--headless")
    chrome_driver = uc.Chrome(options=tmp_opts)
    # Get user agent
    user_agent = chrome_driver.execute_script("return navigator.userAgent;")
    user_agent = user_agent.replace("Headless", "")
    # Quit the temporary driver
    chrome_driver.quit()

    opts = uc.ChromeOptions()
    # https://stackoverflow.com/questions/76627992/selenium-webdriver-headless-mode-shows-blank-page-selenium-web-element
    # TODO opts.add_argument("--headless=new")
    # no need to set headless when running on server as we are using xvfb

    # opts.add_argument("--disable-features=DownloadBubble,DownloadBubbleV2")

    for arg in DEFAULT_CHROME_OPTION_ARGS:
        opts.add_argument(arg)
    opts.add_argument(f"--user-agent={user_agent}")

    opts.add_experimental_option("prefs", CHROME_PREFS)

    driver = CustomWebDriver(options=opts)
    driver.execute_cdp_cmd("Page.setGeolocationOverride", {
        "latitude": 39.98,
        "longitude": -82.98,
        "accuracy": 100
    })

    request.cls.driver = driver
    yield driver

    logger.info("Quitting WebDriver for class.")
    try:
        driver.delete_all_cookies()
        driver.execute_script('window.localStorage.clear();')
        driver.execute_script('window.sessionStorage.clear();')
    except Exception as e:
        logger.warning(f"Exception during class driver cleanup (cookies/storage): {e}")
    finally:
        driver.quit()
    # display.stop()


@pytest.fixture(autouse=True)
def auto_fix_on_failure(request, driver_session: CustomWebDriver):
    driver = driver_session
    autofix_mode = request.config.getoption("--autofix-mode")
    is_internal_rerun = request.config.getoption("--internal-rerun")

    # Clear logs only if we are in a primary run, not an internal rerun
    current_list_handler_instance = get_list_handler()
    if not is_internal_rerun:
        if current_list_handler_instance:
            current_list_handler_instance.log_list.clear()
        else:
            logger.warning("Could not find ListHandler to clear messages.")

    yield
    # if not request.node.rep_call.failed:
    #     return
    failure_file_handler = None
    original_handlers_snapshot = list(logger.handlers)
    if is_internal_rerun:
        logger.debug(f"Internal re-run for verifying{request.node.name}. Skipping auto-fix logic in this nested run.")
        return

    if autofix_mode == "none":
        if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
            logger.info(f"Test {request.node.name} failed. Auto-fix mode is 'none'. Skipping fix attempts.")
        return

    call_report = getattr(request.node, "rep_call", None)

    if not (call_report and call_report.failed):
        if not call_report:
            logger.warning(f"Could not find call report (rep_call) for test {request.node.name}. Skipping auto-fix.")
        else:
            logger.info(f"Test {request.node.name} did not fail the call phase. Skipping auto-fix.")

        return

    try:
        logger.info(f"Test {request.node.name} failed. Auto-fix mode: {autofix_mode}. Initiating process.")
        collected_logs_from_list_handler = []
        if current_list_handler_instance:
            collected_logs_from_list_handler = list(current_list_handler_instance.log_list)
        else:
            logger.warning("ListHandler instance was None during teardown; cannot retrieve its logs.")

        # Data gathering
        execution_folder = request.config.execution_folder
        test_class_name = request.node.cls.__name__ if request.node.cls else "UnknownClass"
        class_folder = f"{execution_folder}/{test_class_name}"
        os.makedirs(f"{class_folder}/screenshots", exist_ok=True)
        os.makedirs(f"{class_folder}/logs", exist_ok=True)
        os.makedirs(f"{class_folder}/dom", exist_ok=True)
        try:
            _, _, web_elements_text = get_web_element_rect(driver)
            screenshot_path = f"{class_folder}/screenshots/{request.node.name}.png"
            driver.save_screenshot(screenshot_path)
            dom_path = f"{class_folder}/dom/{request.node.name}.html"
            with open(dom_path, "w", encoding="utf-8") as dom_file:
                dom_file.write(driver.page_source)
            current_url_at_failure = driver.current_url
        except Exception as e:
            logger.error(f"Error during data gathering for failed test: {e}")
            return

        for h in logger.handlers:
            if not isinstance(h, logging.FileHandler):
                logger.removeHandler(h)

        # Setup dedicated failure log handler
        log_path = f"{execution_folder}/{test_class_name}/logs/{request.node.name}.log"

        failure_file_handler = logging.FileHandler(log_path, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        failure_file_handler.setFormatter(formatter)
        # Modify global logger: remove non-FileHandlers, add our failure_file_handler
        for h in list(logger.handlers):
            logger.removeHandler(h)
        logger.addHandler(failure_file_handler)

        logger.error(f"--- Test {request.node.name} FAILED ---")
        logger.error(f"URL at failure: {current_url_at_failure}")
        logger.error(f"Traceback:\n{request.node.rep_call.longreprtext}")

        # list_handler_instance = get_list_handler()
        # formatted_logs = "\n".join(list_handler_instance.log_list)
        # with open(log_path, "a", encoding="utf-8") as f:
        #     f.write(formatted_logs + "\n")

        if collected_logs_from_list_handler:
            tmp_log = "\n".join(collected_logs_from_list_handler)
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(tmp_log + "\n")
        else:
            logger.info("No logs were collected by ListHandler during the test run.")

        # For LLM
        formatted_logs = "\n".join(collected_logs_from_list_handler)

        # Get fix from LLM
        test_method_source, failing_line_code, original_failing_line_in_file_abs = gather_test_code_and_failing_line(request)
        load_dotenv()
        suggestions = call_gpt_for_candidate_fixes(
            test_name=request.node.name,
            class_name=request.node.cls.__name__,
            failing_url=driver.current_url,
            screenshot_path=screenshot_path,
            web_elements_text=web_elements_text,
            traceback_text=request.node.rep_call.longreprtext,
            logging_output=formatted_logs,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            test_method_source=test_method_source,
            failing_line_code=failing_line_code
        )

        if not suggestions:
            logger.error("No suggestions received from LLM. Aborting auto-fix.")
            return

        logger.info("GPT suggestions:\n" + suggestions)

        if autofix_mode == "suggest":
            logger.info("Auto-fix mode is 'suggest'. Suggestions displayed. No patching or re-run will occur.")
            return

        parsed_suggestions = parse_gpt_suggestions(suggestions)

        if not parsed_suggestions:
            logger.error("Could not parse LLM suggestions. Aborting auto-fix.")
            return

        # --- Attempt to apply fixes and verify ---
        test_file_path = str(request.node.fspath)
        test_node_id = request.node.nodeid
        backup_file_path = test_file_path + ".autofix_backup"
        shutil.copy2(test_file_path, backup_file_path)
        logger.info(f"Backed up original test file to {backup_file_path}")

        original_failure_resolved = False
        attempt_count = 0

        for idx, fix_detail in enumerate(parsed_suggestions):
            if attempt_count >= MAX_FIX_ATTEMPTS_PER_FAILURE_POINT:
                logger.warning(f"Reached max fix attempts ({MAX_FIX_ATTEMPTS_PER_FAILURE_POINT}) for this failure point.")
                break

            attempt_count += 1
            logger.info(f"\n--- Attempting Fix #{attempt_count} (Suggestion {idx + 1}) ---")
            logger.info(f"Description: {fix_detail['description']}")
            logger.info(f"Original Code:\n{fix_detail['original_code']}")
            logger.info(f"Fixed Code:\n{fix_detail['fixed_code']}")

            # Apply the fix to the method source string
            patched_method_source = apply_fix_to_method_source(
                test_method_source,
                fix_detail['original_code'],
                fix_detail['fixed_code']
            )

            if not patched_method_source:
                logger.warning("Failed to apply fix to method source string. Skipping this suggestion.")
                # Restore original file for next attempt if it was modified by a previous AST attempt that failed badly
                shutil.copy2(backup_file_path, test_file_path)
                continue

            # Replace the entire method in the file using AST
            # Note: `request.node.cls` can be None for tests not in a class.
            method_class_name = request.node.cls.__name__ if request.node.cls else None

            # Ensure patched_method_source is a full method definition for AST replacement
            # If LLM provides only snippets, apply_fix_to_method_source should yield the full patched method.
            # This requires original_test_method_source to be the full method source.
            if not replace_method_in_file_ast(test_file_path, method_class_name, request.node.name, patched_method_source):
                logger.error("Failed to replace method in file using AST. Reverting and skipping suggestion.")
                shutil.copy2(backup_file_path, test_file_path)
                continue

            logger.info(f"Successfully patched file: {test_file_path}")

            # Re-run the test
            # Before re-running, ensure WebDriver is in a clean state if possible, or re-initialize.
            # For simplicity now, assume test re-run handles its own setup.
            # If test needs driver, it's already in request.cls.driver. Subprocess run won't share it.
            # The re-run test MUST be self-contained in its setup.
            # This implies the test being fixed should handle its own driver setup if run in isolation.
            # OR, the run_specific_test needs to manage the PyTest context more deeply (harder).
            # The current `run_specific_test` calls pytest CLI, which is fine.

            logger.info(f"Re-running test: {test_node_id} (with --internal-rerun flag)")
            passed, new_traceback, new_failing_line_abs = run_specific_test(test_node_id, test_file_path, is_verification_run=True)

            # Verify
            if passed:
                logger.info(f"SUCCESS! Fix #{attempt_count} worked. Test {request.node.name} PASSED after auto-fix.")
                original_failure_resolved = True

                if os.path.exists(backup_file_path):
                    os.remove(backup_file_path)

                call_report_to_modify = getattr(request.node, "rep_call", None)
                if call_report_to_modify:
                    call_report_to_modify.outcome = "passed"
                else:
                    logger.warning(f"Could not find rep_call for {request.node.name} to update its outcome to passed.")

                break
            else:
                logger.warning(f"Fix #{attempt_count} did NOT resolve the test. Test still FAILED.")
                if new_traceback:
                    logger.debug(f"New traceback after fix attempt:\n{new_traceback}")

                if new_failing_line_abs is not None and original_failing_line_in_file_abs is not None:
                    if new_failing_line_abs > original_failing_line_in_file_abs:
                        logger.info(
                            f"PROGRESS: Test failed at a LATER line "
                            f"({new_failing_line_abs} vs original {original_failing_line_in_file_abs}). "
                            "Considering original issue resolved."
                        )
                        original_failure_resolved = True
                        if os.path.exists(backup_file_path):
                            os.remove(backup_file_path)
                        # The test is still marked as failed overall for this run, but the autofix made progress.
                        # We can update the original report's traceback to the new one for clarity.
                        request.node.rep_call.longrepr = new_traceback
                        break
                    elif new_failing_line_abs == original_failing_line_in_file_abs:
                        logger.info(f"NO PROGRESS: Test failed at the SAME line ({new_failing_line_abs}).")
                    else:
                        logger.info(
                            f"REGRESSION: Test failed at an EARLIER line "
                            f"({new_failing_line_abs} vs original {original_failing_line_in_file_abs})."
                        )
                else:
                    logger.warning("Could not determine new failing line for comparison.")

                # If not passed and no progress, revert the file for the next suggestion
                logger.info(f"Reverting {test_file_path} from backup.")
                shutil.copy2(backup_file_path, test_file_path)

        # --- After loop ---
        if not original_failure_resolved:
            logger.error(
                f"Auto-fix FAILED for {request.node.name}. "
                f"Tried {attempt_count} suggestions. Restoring original file from backup."
            )
            if os.path.exists(backup_file_path):  # Ensure original is restored
                shutil.copy2(backup_file_path, test_file_path)
            if attempt_count >= MAX_FIX_ATTEMPTS_PER_FAILURE_POINT:
                logger.error(f"LLM failed to fix {request.node.name} after exhausting retries for the initial failure point.")

        if os.path.exists(backup_file_path):
            os.remove(backup_file_path)
            logger.info(f"Removed backup file: {backup_file_path}")
    finally:
        if failure_file_handler:
            logger.removeHandler(failure_file_handler)
            failure_file_handler.close()

        for h_exist in list(logger.handlers):
            logger.removeHandler(h_exist)
            if h_exist not in original_handlers_snapshot:
                h_exist.close()

        for h_orig in original_handlers_snapshot:
            logger.addHandler(h_orig)

        try:
            logger.debug(f"Cleaning up cookies/storage for driver after test {request.node.name}")
            driver.delete_all_cookies()
            driver.execute_script('window.localStorage.clear();')
            driver.execute_script('window.sessionStorage.clear();')
        except Exception as e:
            logger.warning(f"Error during post-test cleanup of driver for {request.node.name}: {e}")
