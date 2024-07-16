import time
from datetime import datetime, timedelta

from conftest import CustomWebElement


def switch_to_new_tab(driver, website_url=""):
    time.sleep(3)

    # Get the current window handles
    window_handles = driver.window_handles
    original_window = driver.current_window_handle

    # Switch to the new tab
    for handle in window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break
    # if website_url in cookie_locator_dict:
    #     locators = cookie_locator_dict[website_url]
    #     for by, locator in locators:
    #         # if is_cookie_displayed(driver, by, locator):
    #         try:
    #             # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, locator)))
    #             element = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((by, locator)))
    #             element.click()
    #         except (NoSuchElementException, TimeoutException, StaleElementReferenceException, AttributeError):
    #             error_message = f"handle cookie error, element located by {by} with locator {locator} not found"
    #             logger.warning(error_message)
    #             driver.error_messages.append(error_message)

    return driver


def calculate_budget_dates(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    # Adjust the month to be the previous month
    start_date_month_adjusted = (start_date.month - 1) if start_date.month > 1 else 12
    end_date_month_adjusted = (end_date.month - 1) if end_date.month > 1 else 12

    start_date_year = start_date.year
    start_date_day = start_date.day

    end_date_year = end_date.year
    end_date_day = end_date.day

    return (start_date_year, start_date_month_adjusted, start_date_day), (end_date_year, end_date_month_adjusted, end_date_day)


def calculate_dates(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    return start_date_str, end_date_str


def calculate_dates_slash_format(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    start_date_str = start_date.strftime('%m/%d/%Y')
    end_date_str = end_date.strftime('%m/%d/%Y')

    return start_date_str, end_date_str


def scroll_to_element(driver, element):
    if isinstance(element, CustomWebElement):
        element = element.get_native_element()
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
    time.sleep(1)
