import logging
import os
import re
import time
from datetime import datetime
from typing import List

from dotenv import load_dotenv
import polling2
import pytest
import undetected_chromedriver as uc
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util.llm_helper import get_web_element_rect, gather_test_code_and_failing_line
from util.agent import call_gpt_for_candidate_fixes
from util.website_config import website_dict, cookie_locator_dict

DISPLAY_VISIBLE = False
DISPLAY_WIDTH = 2560
DISPLAY_HEIGHT = 1440
WAIT_TIMEOUT = 30
SHADOW_WAIT_TIMEOUT = 15

logging_messages: List[str] = []


class ListHandler(logging.Handler):
    """Custom handler to append logs to a list."""
    def __init__(self, log_list: List[str]):
        super().__init__()
        self.log_list = log_list

    def emit(self, record):
        try:
            msg = self.format(record)
            self.log_list.append(msg)
        except Exception:
            self.handleError(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Add the custom handler with the desired format
handler = ListHandler(logging_messages)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

option_args = [
        "--enable-automation",
        "--disable-field-trial-config",
        # "--disable-background-networking",
        "--enable-features=NetworkService,NetworkServiceInProcess",
        "--disable-features="
        + (
            "ImprovedCookieControls"
            ",LazyFrameLoading"
            ",GlobalMediaControls"
            ",DestroyProfileOnBrowserClose"
            ",MediaRouter"
            ",DialMediaRouteProvider"
            ",AcceptCHFrame"
            ",AutoExpandDetailsElement"
            ",CertificateTransparencyComponentUpdater"
            ",AvoidUnnecessaryBeforeUnloadCheckSync"
            ",Translate"
        ),
        "--disable-background-timer-throttling",
        "--disable-backgrounding-occluded-windows",
        "--disable-back-forward-cache",
        "--disable-breakpad",
        "--disable-client-side-phishing-detection",
        "--disable-component-extensions-with-background-pages",
        "--disable-component-update",
        "--no-default-browser-check",
        "--disable-default-apps",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--disable-features",
        "--allow-pre-commit-input",
        "--disable-hang-monitor",
        "--disable-ipc-flooding-protection",
        "--disable-popup-blocking",
        "--disable-prompt-on-repost",
        "--disable-renderer-backgrounding",
        "--disable-sync",
        "--force-color-profile",
        "--metrics-recording-only",
        "--no-first-run",
        "--password-store",
        "--use-mock-keychain",
        "--no-service-autorun",
        "--export-tagged-pdf",
        "--no_sandbox",
        "--ignore-certificate-errors",
        "--disable-blink-features=AutomationControlled",
        "--incognito",
        "--disable-extensions",
        "--disable-infobars",
        "--start-maximized",
        "--disable-dev-shm-usage",
        "--window-size=1920,1080"
    ]


# override find_element and click to wait for element to be clickable before clicking
class CustomWebDriver(uc.Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.logging_messages = []

    def find_element(self, by=By.ID, value=None):
        try:
            attempt_find_element_info = f"Attempting to find element: {by} = {value}"
            logger.info(attempt_find_element_info)
            # logging_messages.append(attempt_find_element_info)

            element = WebDriverWait(super(), WAIT_TIMEOUT).until(
                EC.presence_of_element_located((by, value))
                # lambda d: parent_presence_of_element_located((by, value), self)
            )

            element_found_info = f"Successfully find element: {by} = {value}"
            logger.info(element_found_info)
            # logging_messages.append(element_found_info)

            return CustomWebElement(element, self, by, value)
        except TimeoutException as e:
            current_url = self.current_url
            error_message = (f"TimeoutException: Element not found within {WAIT_TIMEOUT} seconds: {by} = {value} "
                             f"(Current page URL: {current_url})")
            logger.error(error_message)
            # logging_messages.append(error_message)
            raise e

    def find_elements(self, by=By.ID, value=None):
        try:
            attempt_find_element_info = f"Attempting to find elements: {by} = {value}"
            logger.info(attempt_find_element_info)
            # logging_messages.append(attempt_find_element_info)

            elements = WebDriverWait(super(), WAIT_TIMEOUT).until(
                EC.presence_of_all_elements_located((by, value))
            )

            element_found_info = f"Successfully find elements: {by} = {value}"
            logger.info(element_found_info)
            # self.logging_messages.append(element_found_info)

            return [CustomWebElement(el, self, by, value) for el in elements]
        except TimeoutException as e:
            current_url = self.current_url
            error_message = (f"TimeoutException: Elements not found within {WAIT_TIMEOUT} seconds: {by} = {value} "
                             f"(Current page URL: {current_url})")
            logger.error(error_message)
            # self.logging_messages.append(error_message)
            raise e


class CustomWebElement:
    def __init__(self, element, driver, by, value, is_shadow_element=False):
        self.element = element
        self.driver = driver
        self.by = by
        self.value = value
        self.is_shadow_element = is_shadow_element

    def click(self):
        try:
            attempt_click_element_info = f"Attempting to click element: {self.by} = {self.value}"
            logger.info(attempt_click_element_info)
            # self.driver.logging_messages.append(attempt_click_element_info)

            if self.is_shadow_element:
                polling2.poll(
                    lambda: self.element.is_displayed() and self.element.is_enabled(),
                    step=0.5,
                    timeout=SHADOW_WAIT_TIMEOUT
                )
                self.element.click()
            else:
                WebDriverWait(self.driver, WAIT_TIMEOUT).until(EC.element_to_be_clickable((self.by, self.value)))
                self.element.click()

            element_clicked_info = f"Element clicked: {self.by} = {self.value}"
            logger.info(element_clicked_info)
            # self.driver.logging_messages.append(element_clicked_info)
        except polling2.TimeoutException as e:
            current_url = self.driver.current_url
            error_message = (f"TimeoutException: Shadow Element not clickable within {SHADOW_WAIT_TIMEOUT} seconds: {self.by} = {self.value} " 
                             f"(Current page URL: {current_url})")
            logger.error(error_message)
            # self.driver.logging_messages.append(error_message)
            raise e
        except TimeoutException as e:
            current_url = self.driver.current_url
            error_message = (f"TimeoutException: Element not clickable within {WAIT_TIMEOUT} seconds: {self.by} = {self.value} "
                             f"(Current page URL: {current_url})")
            logger.error(error_message)
            # self.driver.logging_messages.append(error_message)
            raise e
        except ElementClickInterceptedException as e:
            current_url = self.driver.current_url
            error_message = (f"ElementClickInterceptedException: Element click intercepted: {self.by} = {self.value} "
                             f"(Current page URL: {current_url})")
            logger.error(error_message)
            # self.driver.logging_messages.append(error_message)
            raise e
        except StaleElementReferenceException as e:
            current_url = self.driver.current_url
            error_message = (f"StaleElementReferenceException: Element became stale: {self.by} = {self.value} "
                             f"(Current page URL: {current_url})")
            logger.error(error_message)
            # self.driver.logging_messages.append(error_message)
            raise e

    def find_element(self, by=By.ID, value=None):
        try:
            attempt_find_element_info = f"Attempting to find element: {by} = {value} within element: {self.by} = {self.value}"
            logger.info(attempt_find_element_info)
            # self.driver.logging_messages.append(attempt_find_element_info)

            element = WebDriverWait(self.element, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((by, value))
            )

            element_found_info = f"Successfully find element: {by} = {value} within element: {self.by} = {self.value}"
            logger.info(element_found_info)
            # self.driver.logging_messages.append(element_found_info)

            return CustomWebElement(element, self, by, value)
        except TimeoutException:
            current_url = self.driver.current_url
            error_message = (f"TimeoutException: Element not found within {WAIT_TIMEOUT} seconds: {by} = {value} "
                             f"(Current page URL: {current_url})")
            logger.error(error_message)
            # self.driver.logging_messages.append(error_message)
            return None

    def find_elements(self, by=By.ID, value=None):
        try:
            attempt_find_element_info = f"Attempting to find elements: {by} = {value} within element: {self.by} = {self.value}"
            logger.info(attempt_find_element_info)
            # self.driver.logging_messages.append(attempt_find_element_info)

            elements = WebDriverWait(self.element, WAIT_TIMEOUT).until(
                EC.presence_of_all_elements_located((by, value))
            )

            element_found_info = f"Successfully find elements: {by} = {value} within element: {self.by} = {self.value}"
            logger.info(element_found_info)
            # self.driver.logging_messages.append(element_found_info)

            return [CustomWebElement(el, self, by, value) for el in elements]
        except TimeoutException:
            current_url = self.driver.current_url
            error_message = (f"TimeoutException: Elements not found within {WAIT_TIMEOUT} seconds: {by} = {value} "
                             f"(Current page URL: {current_url})")
            logger.error(error_message)
            # self.driver.logging_messages.append(error_message)
            return []

    @property
    def shadow_root(self):
        attempt_shadow_root_info = f"Getting the shadow root of current element: {self.by} = {self.value}"
        logger.info(attempt_shadow_root_info)
        # self.driver.logging_messages.append(attempt_shadow_root_info)

        shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", self.element)
        return CustomShadowRoot(shadow_root, self.driver, self.by, self.value)

    def get_native_element(self):
        return self.element

    def __getattr__(self, item):
        return getattr(self.element, item)


class CustomShadowRoot:
    def __init__(self, shadow_root, driver, by, value):
        self.shadow_root = shadow_root
        self.driver = driver
        self.by = by
        self.value = value

    def find_element(self, by=By.ID, value=None):
        try:
            attempt_find_element_info = f"Attempting to find element in shadow root: {by} = {value}"
            logger.info(attempt_find_element_info)
            # self.driver.logging_messages.append(attempt_find_element_info)

            element = polling2.poll(
                lambda: self._find_element_in_shadow_root(by, value),
                step=0.5,
                timeout=SHADOW_WAIT_TIMEOUT,
                check_success=lambda x: x is not None
            )

            element_found_info = f"Element found in shadow root: {by} = {value}"
            logger.info(element_found_info)
            # self.driver.logging_messages.append(element_found_info)
            return CustomWebElement(element, self.driver, by, value, is_shadow_element=True)
        except polling2.TimeoutException:
            current_url = self.driver.current_url
            error_message = (f"TimeoutException: Element not found in shadow root within {SHADOW_WAIT_TIMEOUT} seconds: {by} = {value} "
                             f"(Current page URL: {current_url})")
            logger.error(error_message)
            # self.driver.logging_messages.append(error_message)
            return None

    def _find_element_in_shadow_root(self, by, value):
        try:
            return self.shadow_root.find_element(by, value)
        except NoSuchElementException:
            return None

    def find_elements(self, by=By.ID, value=None):
        try:
            attempt_find_element_info = f"Attempting to find elements in shadow root: {by} = {value}"
            logger.info(attempt_find_element_info)
            # self.driver.logging_messages.append(attempt_find_element_info)

            elements = polling2.poll(
                lambda: self._find_elements_in_shadow_root(by, value),
                step=0.5,
                timeout=SHADOW_WAIT_TIMEOUT,
                check_success=lambda x: x is not None and len(x) > 0
            )

            element_found_info = f"Elements found in shadow root: {by} = {value}"
            logger.info(element_found_info)
            # self.driver.logging_messages.append(element_found_info)

            return [CustomWebElement(el, self.driver, by, value, is_shadow_element=True) for el in elements]
        except polling2.TimeoutException:
            current_url = self.driver.current_url
            error_message = (f"TimeoutException: Elements not found in shadow root within {SHADOW_WAIT_TIMEOUT} seconds: {by} = {value} "
                             f"(Current page URL: {current_url})")
            logger.error(error_message)
            # self.driver.logging_messages.append(error_message)
            return []

    def _find_elements_in_shadow_root(self, by, value):
        try:
            return self.shadow_root.find_elements(by, value)
        except NoSuchElementException:
            return None


@pytest.fixture(scope="class", autouse=True)
def setup_class(request):
    # start display
    # https://stackoverflow.com/questions/72853097/pyvirtual-display-and-xvfb-on-macos-latest
    # display = Display(visible=DISPLAY_VISIBLE, size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))
    # display.start()
    # chrome_binary_path = '/Applications/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
    # service = Service(executable_path=chrome_binary_path)

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

    for arg in option_args:
        opts.add_argument(arg)
    opts.add_argument(f"--user-agent={user_agent}")

    download_path = 'testoutput'
    absolute_download_path = os.path.abspath(download_path)
    prefs = {
        "download.default_directory": absolute_download_path,  # Set the download path
        "download.prompt_for_download": False,  # Don't ask for download location
        "download.directory_upgrade": True,  # Automatically download to the specified directory
        "safebrowsing.enabled": True,  # Allow downloading without safety check
        "profile.default_content_settings.popups": 0,  # Disable popups
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,  # Allow automatic downloads
        "download.extensions_to_open": "",  # Leave empty to avoid automatically opening files after download
        "download.restrictions": 0,  # To allow all downloads
        # no effective way to disable the chrome save as dislog now......
        'browser.enabled_labs_experiments': ['download-bubble@2', 'download-bubble-v2@2'],

        "profile.default_content_setting_values.cookies": 1,  # 1 = Allow, 2 = Block
        "profile.default_content_setting_values.images": 1,
        "profile.default_content_setting_values.javascript": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.automatic_downloads": 1,
        "profile.default_content_setting_values.mixed_script": 1,
        "profile.default_content_setting_values.media_stream": 1,
        "profile.default_content_setting_values.stylesheets": 1,
        "profile.managed_default_content_settings": {
            "cookies": 1,  # Allow cookies
            "images": 1,
            "javascript": 1,
            "geolocation": 1,
            "automatic_downloads": 1,
            "mixed_script": 1,
            "media_stream": 1,
            "stylesheets": 1
        }
    }
    opts.add_experimental_option("prefs", prefs)

    driver = CustomWebDriver(options=opts)
    driver.execute_cdp_cmd("Page.setGeolocationOverride", {
        "latitude": 39.98,
        "longitude": -82.98,
        "accuracy": 100
    })

    request.cls.driver = driver
    yield

    driver.delete_all_cookies()
    driver.execute_script('window.localStorage.clear();')
    driver.execute_script('window.sessionStorage.clear();')
    driver.quit()
    # display.stop()


@pytest.fixture(autouse=True)
def setup_method(request):
    test_class_name = request.node.cls.__name__
    website_domain_name = convert_class_name(test_class_name)
    website_url = get_website_url(website_domain_name)
    driver = request.cls.driver
    open_url_and_handle_cookie(driver, website_url)

    execution_folder = request.config.execution_folder

    yield
    if request.node.rep_call.failed:
        class_folder = f"{execution_folder}/{test_class_name}"
        os.makedirs(f"{class_folder}/screenshots", exist_ok=True)
        os.makedirs(f"{class_folder}/logs", exist_ok=True)
        os.makedirs(f"{class_folder}/dom", exist_ok=True)

        rects, web_elements, web_elements_text = get_web_element_rect(driver)
        # print(web_elements_text)
        screenshot_path = f"{class_folder}/screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)

        dom_path = f"{class_folder}/dom/{request.node.name}.html"
        with open(dom_path, "w", encoding="utf-8") as dom_file:
            dom_file.write(driver.page_source)

        logger.removeHandler(handler)
        log_path = f"{execution_folder}/{test_class_name}/logs/{request.node.name}.log"
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)
        logger.error(f"Test {request.node.name} failed.")
        logger.error(f"URL at failure: {driver.current_url}")
        logger.error(f"Exception traceback: {request.node.rep_call.longreprtext}")

        formatted_logs = "\n".join(logging_messages)

        with open(log_path, "a", encoding="utf-8") as f:
            f.write(formatted_logs + "\n")

        test_method_source, failing_line_code = gather_test_code_and_failing_line(request)
        # print("test_method_source:")
        # print(test_method_source)
        # print(failing_line_code)
        # print("OPENAI KEY:")
        # print(os.getenv("OPENAI_API_KEY"))
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
        if suggestions:
            logger.info("GPT suggestions:\n" + suggestions)
        else:
            logger.error("No GPT suggestions available.")

        logger.removeHandler(file_handler)

        driver.delete_all_cookies()
        driver.execute_script('window.localStorage.clear();')
        driver.execute_script('window.sessionStorage.clear();')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set an attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


def convert_class_name(class_name):
    if class_name.startswith("Test"):
        class_name = class_name[4:]

    domain_name = re.findall(r'[A-Z][a-z]*', class_name)
    result = ''.join(domain_name).lower()
    return result


def get_website_url(website_name):
    if website_name in website_dict:
        confirmed_website_url = website_dict[website_name]
    elif (website_name.endswith('.gov') or website_name.endswith('.edu') or website_name.endswith('.org') or
          website_name.endswith('.uk') or website_name.endswith('.fm') or website_name.endswith('.info')):
        confirmed_website_url = "https://" + website_name
    else:
        confirmed_website_url = "https://" + website_name + ".com"

    return confirmed_website_url


def open_url_and_handle_cookie(driver, website_url):
    print(website_url)
    driver.get(website_url)
    if website_url == 'https://www.jetblue.com/':
        try:
            frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "trustarc_cm")))
            driver.switch_to.frame(frame.get_native_element())
            if website_url in cookie_locator_dict:
                locators = cookie_locator_dict[website_url]
                for by, locator in locators:
                    try:
                        element = WebDriverWait(driver, 9).until(EC.element_to_be_clickable((by, locator)))
                        element.click()
                    except (NoSuchElementException, TimeoutException, StaleElementReferenceException, AttributeError):
                        error_message = f"handle cookie error, element located by {by} with locator {locator} not found"
                        logger.warning(error_message)
                        # logging_messages.append(error_message)
        finally:
            driver.switch_to.default_content()

    elif website_url in cookie_locator_dict:
        locators = cookie_locator_dict[website_url]
        for by, locator in locators:
            # if is_cookie_displayed(driver, by, locator):
            try:
                element = WebDriverWait(driver, 9).until(EC.element_to_be_clickable((by, locator)))
                element.click()
            except (NoSuchElementException, TimeoutException, StaleElementReferenceException, AttributeError):
                error_message = f"handle cookie error, element located by {by} with locator {locator} not found"
                logger.warning(error_message)
                # logging_messages.append(error_message)
    time.sleep(2)


def is_cookie_displayed(driver: uc, by, locator) -> bool:
    try:
        element = driver.find_element(by, locator)
        return element.is_displayed()
    except (NoSuchElementException, StaleElementReferenceException):
        return False


def get_next_execution_number():
    testoutput_dir = "testoutput"
    if not os.path.exists(testoutput_dir):
        os.makedirs(testoutput_dir)
        return 1
    existing_folders = [name for name in os.listdir(testoutput_dir) if os.path.isdir(os.path.join(testoutput_dir, name))]
    execution_numbers = [int(folder.replace("execution", "").split('_')[0]) for folder in existing_folders if folder.startswith("execution")]
    if execution_numbers:
        return max(execution_numbers) + 1
    return 1


def pytest_configure(config):
    execution_number = get_next_execution_number()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    execution_folder = f"testoutput/execution{execution_number}_{timestamp}"
    os.makedirs(execution_folder, exist_ok=True)
    config.execution_folder = execution_folder
