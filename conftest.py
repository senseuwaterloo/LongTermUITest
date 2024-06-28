import re
import pytest
import os
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from util.website_config import website_dict, cookie_locator_dict
from datetime import datetime

DISPLAY_VISIBLE = False
DISPLAY_WIDTH = 2560
DISPLAY_HEIGHT = 1440


@pytest.fixture(scope="class", autouse=True)
def setup_class(request):

    # start display
    # https://stackoverflow.com/questions/72853097/pyvirtual-display-and-xvfb-on-macos-latest
    # display = Display(visible=DISPLAY_VISIBLE, size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))
    # display.start()
    tmp_opts = webdriver.ChromeOptions()
    tmp_opts.add_argument("--headless")
    chrome_driver = webdriver.Chrome(options=tmp_opts)
    # Get user agent
    user_agent = chrome_driver.execute_script("return navigator.userAgent;")
    user_agent = user_agent.replace("Headless", "")
    # Quit the temporary driver
    chrome_driver.quit()

    opts = webdriver.ChromeOptions()
    # https://stackoverflow.com/questions/76627992/selenium-webdriver-headless-mode-shows-blank-page-selenium-web-element
    opts.add_argument("--headless=new")
    # Add user agent to options
    opts.add_argument(f"--user-agent={user_agent}")
    # Disable cache
    opts.add_argument("--disable-cache")
    opts.add_argument("--disable-application-cache")
    opts.add_argument("--disk-cache-size=0")
    # opts.add_argument("--disable-gpu")
    opts.add_argument("--ignore-certificate-errors")
    opts.add_argument('--disable-blink-features=AutomationControlled')

    opts.add_argument("--window-size=1920,1080")
    # opts.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0")

    # Geolocation preferences
    prefs = {
        "profile.default_content_setting_values.geolocation": 1,  # 1 = allow, 2 = block
        "profile.default_content_setting_values.notifications": 2,  # Disable notifications
    }
    opts.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=opts)
    request.cls.driver = driver
    yield
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
        screenshot_path = f"{class_folder}/screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)

        dom_path = f"{class_folder}/dom/{request.node.name}.html"
        with open(dom_path, "w", encoding="utf-8") as dom_file:
            dom_file.write(driver.page_source)

        log_path = f"{class_folder}/logs/{request.node.name}.log"
        with open(log_path, "w") as log_file:
            log_file.write(f"Test {request.node.name} failed.\n")
            log_file.write(f"URL at failure: {driver.current_url}\n")
            log_file.write(f"Exception: {request.node.rep_call.longreprtext}\n")


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
    driver.get(website_url)
    time.sleep(5)
    # print("In method open_url_and_handle_cookie")
    # print(website_url)
    # print(cookie_locator_dict.get(website_url))
    if website_url in cookie_locator_dict:
        locators = cookie_locator_dict[website_url]
        for by, locator in locators:
            if is_cookie_displayed(driver, by, locator):
                try:
                    element = driver.find_element(by, locator)
                    element.click()
                except NoSuchElementException:
                    print(f"Element located by {by} with locator {locator} not found")


def is_cookie_displayed(driver: webdriver, by, locator) -> bool:
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
