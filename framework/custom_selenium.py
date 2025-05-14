import time

import polling2
import undetected_chromedriver as uc
from selenium.common.exceptions import (
    NoSuchElementException, StaleElementReferenceException,
    TimeoutException, ElementClickInterceptedException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .logger_setup import logger
from .config import WAIT_TIMEOUT, SHADOW_WAIT_TIMEOUT
from util.website_config import cookie_locator_dict


class CustomWebDriver(uc.Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.logging_messages = []

    def get(self, website_url):
        try:
            log_message_attempt = f"Attempting to navigate to URL: {website_url}"
            logger.info(log_message_attempt)

            super().get(website_url)

            log_message_success = f"Successfully navigated to URL: {website_url}"
            logger.info(log_message_success)

        except Exception as e:
            error_message = f"Exception occurred while trying to navigate to URL: {website_url}"
            logger.error(error_message)
            raise e

        if website_url in cookie_locator_dict:
            locators = cookie_locator_dict[website_url]
            for by, locator in locators:
                try:
                    element = WebDriverWait(super(), 9).until(EC.element_to_be_clickable((by, locator)))
                    element.click()
                except (NoSuchElementException, TimeoutException, StaleElementReferenceException, AttributeError):
                    error_message = f"handle cookie window error, element located by {by} with locator {locator} not found, continue without dismissing cookie window"
                    logger.warning(error_message)
        time.sleep(2)

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


def open_url_and_handle_cookie(driver, website_url):
    # print(website_url)
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
