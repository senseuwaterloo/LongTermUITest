import logging
import os
import shutil

import pytest
import undetected_chromedriver as uc
from dotenv import load_dotenv

from framework.config import DEFAULT_CHROME_OPTION_ARGS, CHROME_PREFS, MAX_FIX_ATTEMPTS_PER_FAILURE_POINT
from framework.custom_selenium import CustomWebDriver
from framework.logger_setup import logger, get_list_handler
from util.agent import call_gpt_for_candidate_fixes
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
    # test_class_name = request.node.cls.__name__
    # website_domain_name = convert_class_name(test_class_name)
    # website_url = get_website_url(website_domain_name)
    # driver = request.cls.driver
    # # open_url_and_handle_cookie(driver, website_url)
    #
    # execution_folder = request.config.execution_folder

    driver = driver_session

    # Clear the global_logging_messages list for each test
    list_handler_instance = get_list_handler()
    if list_handler_instance:
        list_handler_instance.log_list.clear()
    else:
        logger.warning("Could not find ListHandler to clear messages.")

    yield
    # if not request.node.rep_call.failed:
    #     return

    call_report = getattr(request.node, "rep_call", None)
    if call_report and call_report.failed:

        logger.info(f"Test {request.node.name} failed. Initiating auto-fix process.")
        execution_folder = request.config.execution_folder
        test_class_name = request.node.cls.__name__ if request.node.cls else "UnknownClass"

        class_folder = f"{execution_folder}/{test_class_name}"
        os.makedirs(f"{class_folder}/screenshots", exist_ok=True)
        os.makedirs(f"{class_folder}/logs", exist_ok=True)
        os.makedirs(f"{class_folder}/dom", exist_ok=True)

        # Data gathering
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

        original_handlers = list(logger.handlers)
        for h in original_handlers:
            if not isinstance(h, logging.FileHandler):
                logger.removeHandler(h)
        # logger.removeHandler(handler)
        log_path = f"{execution_folder}/{test_class_name}/logs/{request.node.name}.log"
        # file_handler = logging.FileHandler(log_path)
        # file_handler.setLevel(logging.INFO)
        # file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        # logger.addHandler(file_handler)
        # logger.error(f"Test {request.node.name} failed.")
        # logger.error(f"URL at failure: {driver.current_url}")
        # logger.error(f"Exception traceback: {request.node.rep_call.longreprtext}")
        failure_file_handler = logging.FileHandler(log_path, mode='a')  # Append to allow multiple entries if needed
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        failure_file_handler.setFormatter(formatter)
        logger.addHandler(failure_file_handler)

        logger.error(f"--- Test {request.node.name} FAILED ---")
        logger.error(f"URL at failure: {current_url_at_failure}")
        logger.error(f"Traceback:\n{request.node.rep_call.longreprtext}")

        # formatted_logs = "\n".join(logging_messages)

        # Write in-memory logs (from ListHandler)
        formatted_logs = "\n".join(list_handler_instance.log_list)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(formatted_logs + "\n")

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

        # if suggestions:
        #     logger.info("GPT suggestions:\n" + suggestions)
        # else:
        #     logger.error("No GPT suggestions available.")

        if not suggestions:
            logger.error("No suggestions received from LLM. Aborting auto-fix.")
            logger.removeHandler(failure_file_handler)
            failure_file_handler.close()
            # Restore original handlers
            for h_orig in original_handlers:
                if not any(isinstance(h_orig, type(h_exist)) for h_exist in logger.handlers):
                    logger.addHandler(h_orig)

            driver.delete_all_cookies()
            driver.execute_script('window.localStorage.clear();')
            driver.execute_script('window.sessionStorage.clear();')
            return

        logger.info("GPT suggestions:\n" + suggestions)
        parsed_suggestions = parse_gpt_suggestions(suggestions)

        if not parsed_suggestions:
            logger.error("Could not parse LLM suggestions. Aborting auto-fix.")
            logger.removeHandler(failure_file_handler)
            for h_orig in original_handlers:
                if not any(isinstance(h_orig, type(h_exist)) for h_exist in logger.handlers):
                    logger.addHandler(h_orig)

            driver.delete_all_cookies()
            driver.execute_script('window.localStorage.clear();')
            driver.execute_script('window.sessionStorage.clear();')
            return

        # --- Attempt to apply fixes and verify ---
        test_file_path = str(request.node.fspath)
        # e.g. path/to/file.py::TestClass::test_method
        test_node_id = request.node.nodeid
        # Backup the original test file
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

            # 1. Apply the fix to the method source string
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

            # 2. Replace the entire method in the file using AST
            # Note: `request.node.cls` can be None for tests not in a class.
            method_class_name = request.node.cls.__name__ if request.node.cls else None

            # Ensure patched_method_source is a full method definition for AST replacement
            # If LLM provides only snippets, apply_fix_to_method_source should yield the full patched method.
            # This requires original_test_method_source to be the full method source.
            if not replace_method_in_file_ast(test_file_path, method_class_name, request.node.name, patched_method_source):
                logger.error("Failed to replace method in file using AST. Reverting and skipping suggestion.")
                shutil.copy2(backup_file_path, test_file_path)  # Restore from backup
                continue

            logger.info(f"Successfully patched file: {test_file_path}")

            # 3. Re-run the test
            # Before re-running, ensure WebDriver is in a clean state if possible, or re-initialize.
            # For simplicity now, assume test re-run handles its own setup.
            # If test needs driver, it's already in request.cls.driver. Subprocess run won't share it.
            # The re-run test MUST be self-contained in its setup.
            # This implies the test being fixed should handle its own driver setup if run in isolation.
            # OR, the run_specific_test needs to manage the PyTest context more deeply (harder).
            # The current `run_specific_test` calls pytest CLI, which is fine.

            logger.info(f"Re-running test: {test_node_id}")
            passed, new_traceback, new_failing_line_abs = run_specific_test(test_node_id, test_file_path)

            # 4. Verify
            if passed:
                logger.info(f"SUCCESS! Fix #{attempt_count} worked. Test {request.node.name} PASSED.")
                original_failure_resolved = True
                # Keep the patched file. The backup can be removed or kept.
                # For now, let's remove the backup on success.
                if os.path.exists(backup_file_path): os.remove(backup_file_path)
                request.node.rep_call.passed = True  # Mark as passed for reporting
                request.node.rep_call.outcome = "passed"
                break  # Exit suggestion loop
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
                        original_failure_resolved = True  # The specific point of failure moved
                        # Keep the patched file. The next failure will be handled by a subsequent pytest run.
                        if os.path.exists(backup_file_path): os.remove(backup_file_path)
                        # The test is still marked as failed overall for this run, but the autofix made progress.
                        # We can update the original report's traceback to the new one for clarity.
                        request.node.rep_call.longrepr = new_traceback
                        break  # Exit suggestion loop
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
                # This could be a place to raise a specific exception if strict failure is needed
                logger.error(f"LLM failed to fix {request.node.name} after exhausting retries for the initial failure point.")
                # raise Exception(f"Auto-fix failed for {request.node.name} after {MAX_FIX_ATTEMPTS_PER_FAILURE_POINT} retries.")

        if os.path.exists(backup_file_path):  # Clean up backup if loop finished (either success or all attempts failed)
            os.remove(backup_file_path)
            logger.info(f"Removed backup file: {backup_file_path}")

        # Finalize logging for this failure
        logger.removeHandler(failure_file_handler)
        failure_file_handler.close()
        # Restore original logger handlers (e.g., ListHandler, console handler)
        # Clear existing handlers that might have been added by mistake or are the failure_file_handler
        for h in logger.handlers[:]:
            logger.removeHandler(h)
            h.close()
        for h_orig in original_handlers:
            logger.addHandler(h_orig)
    elif not call_report:
        logger.warning(f"Could not find call report (rep_call) for test {request.node.name}. Skipping auto-fix.")
    else:  # call_report exists but not call_report.failed
        logger.info(f"Test {request.node.name} did not fail the call phase (or rep_call missing failed attribute). Skipping auto-fix.")



    # Cleanup selenium state (cookies, local storage) if test failed or even if passed via autofix
    # This was in your original code for handling failures.
    # if request.node.rep_call.failed and not original_failure_resolved:  # Only if truly failed and not fixed
    #     logger.removeHandler(handler)  # Remove list handler
    #     # Log to dedicated file as in your original snippet
    #     log_path = f"{execution_folder}/{test_class_name}/logs/{request.node.name}_final_fail.log"
    #     file_handler = logging.FileHandler(log_path)
    #     # ... (set formatter, add handler, log final failure details, remove handler) ...
    #     logger.addHandler(file_handler)
    #     logger.error(f"Test {request.node.name} ultimately failed.")
    #     # ...
    #     logger.removeHandler(file_handler)
    #     logger.addHandler(handler)  # Re-add original handler for other tests
    #
    # if hasattr(request.cls, 'driver'):  # Check if driver exists
    #     driver = request.cls.driver
    #     driver.delete_all_cookies()
    #     driver.execute_script('window.localStorage.clear();')
    #     driver.execute_script('window.sessionStorage.clear();')
    try:
        logger.debug(f"Cleaning up cookies/storage for driver after test {request.node.name}")
        driver.delete_all_cookies()
        driver.execute_script('window.localStorage.clear();')
        driver.execute_script('window.sessionStorage.clear();')
    except Exception as e:
        logger.warning(f"Error during post-test cleanup of driver for {request.node.name}: {e}")
