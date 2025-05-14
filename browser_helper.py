import platform
import time
from datetime import datetime, timedelta

from selenium.webdriver import Keys

from framework.custom_selenium import CustomWebElement


def switch_to_new_tab(driver, website_url=""):
    time.sleep(3)

    # Get the current window handles
    window_handles = driver.window_handles
    original_window = driver.current_window_handle

    # Switch to the new tab
    for handle in window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            time.sleep(2)
            break

    # Close the original tab and switch back to new tab
    # driver.switch_to.window(original_window)
    # driver.close()
    # driver.switch_to.window(driver.window_handles[0])
    return driver


def switch_to_new_tab_and_close_old(driver, website_url=""):
    time.sleep(3)

    # Get the current window handles
    window_handles = driver.window_handles
    original_window = driver.current_window_handle

    # Switch to the new tab
    for handle in window_handles:
        if handle != original_window:
            driver.close()
            time.sleep(2)
            driver.switch_to.window(handle)
            time.sleep(2)
            break

    # Close the original tab and switch back to new tab
    # driver.switch_to.window(original_window)
    # driver.close()
    # driver.switch_to.window(driver.window_handles[0])
    return driver


def switch_to_new_tab_and_return_old(driver, website_url=""):
    time.sleep(3)

    # Get the current window handles
    window_handles = driver.window_handles
    original_window = driver.current_window_handle

    # Switch to the new tab
    for handle in window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            time.sleep(2)
            break

    return original_window


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


def calculate_dates_full_month_name(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    # do not return leading 0 before a single digit
    start_date_str = start_date.strftime('%B ') + str(start_date.day) + start_date.strftime(', %Y')
    end_date_str = end_date.strftime('%B ') + str(end_date.day) + end_date.strftime(', %Y')

    return start_date_str, end_date_str


def calculate_dates_slash_format(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    start_date_str = start_date.strftime('%m/%d/%Y')
    end_date_str = end_date.strftime('%m/%d/%Y')

    return start_date_str, end_date_str


def calculate_dates_weekday_format(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    start_date_str = start_date.strftime('%A, %B %d, %Y')
    end_date_str = end_date.strftime('%A, %B %d, %Y')

    return start_date_str, end_date_str


def calculate_dates_weekday_mta_format(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    # Format the dates as '15, Thursday August 2024'
    start_date_str = start_date.strftime('%d, %A %B %Y')
    end_date_str = end_date.strftime('%d, %A %B %Y')

    return start_date_str, end_date_str


def calculate_dates_weekday_abbr_format(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    start_date_str = start_date.strftime('%a %b %d %Y')
    end_date_str = end_date.strftime('%a %b %d %Y')

    return start_date_str, end_date_str


def calculate_dates_weekday_abbr_without_year_format(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    start_date_str = start_date.strftime('%a, %B %-d')
    end_date_str = end_date.strftime('%a, %B %-d')

    return start_date_str, end_date_str


def get_day_suffix(day):
    if 11 <= day <= 13:
        return 'th'
    elif day % 10 == 1:
        return 'st'
    elif day % 10 == 2:
        return 'nd'
    elif day % 10 == 3:
        return 'rd'
    else:
        return 'th'


def format_date_with_suffix(date):
    day = date.day
    suffix = get_day_suffix(day)
    formatted_date = date.strftime(f'%-d{suffix} %B (%A)')
    return formatted_date


def calculate_dates_with_suffix(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    start_date_str = format_date_with_suffix(start_date)
    end_date_str = format_date_with_suffix(end_date)

    return start_date_str, end_date_str


def format_date_with_suffix_webmd(date):
    day = date.day
    suffix = get_day_suffix(day)
    formatted_date = date.strftime(f'%B {day}{suffix}, %Y')
    return formatted_date


def calculate_dates_with_suffix_webmd(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    start_date_str = format_date_with_suffix(start_date)
    end_date_str = format_date_with_suffix(end_date)

    return start_date_str, end_date_str


def calculate_dates_day_month_format(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    # Determine the correct format for the day
    if platform.system() == "Windows":
        day_format = '%#d'
    else:
        day_format = '%-d'

    start_day = start_date.strftime(day_format)
    start_month = start_date.strftime('%B')

    end_day = end_date.strftime(day_format)
    end_month = end_date.strftime('%B')

    return start_day, start_month, end_day, end_month


def calculate_first_last_dates():
    current_date = datetime.now()

    # Calculate the first day of the next month
    if current_date.month == 12:  # if December, next month is January of next year
        first_day_next_month = datetime(current_date.year + 1, 1, 1)
    else:
        first_day_next_month = datetime(current_date.year, current_date.month + 1, 1)

    # Calculate the last day of the next month
    if first_day_next_month.month == 12:  # if next month is December, end of December is 31st
        last_day_next_month = datetime(first_day_next_month.year, 12, 31)
    else:
        # Go to the first day of the month after the next, then subtract one day
        first_day_of_following_month = datetime(first_day_next_month.year, first_day_next_month.month + 1, 1)
        last_day_next_month = first_day_of_following_month - timedelta(days=1)

    start_date_str = first_day_next_month.strftime('%Y-%m-%d')
    end_date_str = last_day_next_month.strftime('%Y-%m-%d')

    return start_date_str, end_date_str


def calculate_dates_ticketcenter_format(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    start_day = start_date.strftime('%-d')  # Day of the month without leading zeros
    start_month_year = start_date.strftime('%b %Y')  # Month and year

    end_day = end_date.strftime('%-d')  # Day of the month without leading zeros
    end_month_year = end_date.strftime('%b %Y')  # Month and year

    return start_day, start_month_year, end_day, end_month_year


def calculate_dates_without_space(days_from_now_start=7, days_from_now_end=14):
    current_date = datetime.now()
    start_date = current_date + timedelta(days=days_from_now_start)
    end_date = current_date + timedelta(days=days_from_now_end)

    start_date_str = start_date.strftime('%Y%m%d')
    end_date_str = end_date.strftime('%Y%m%d')

    return start_date_str, end_date_str


def calculate_next_first_last_day():
    current_date = datetime.now()
    # Calculate the first day of the next month
    first_of_next_month = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)
    # Calculate the last day of the next month by finding the first day of the following month and subtracting a day
    last_of_next_month = (first_of_next_month.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    first_date_str = first_of_next_month.strftime('%a %b %d %Y')
    last_date_str = last_of_next_month.strftime('%a %b %d %Y')

    return first_date_str, last_date_str


def scroll_to_element(driver, element):
    if isinstance(element, CustomWebElement):
        element = element.get_native_element()
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
    time.sleep(1)


def scroll_down(driver, distance):
    driver.execute_script(f"window.scrollBy(0, {distance});")
    time.sleep(1)


def scroll_inside_element(driver, element):
    """
    Scrolls to the bottom inside a scrollable element.

    :param driver: The Selenium WebDriver instance.
    :param element: The WebElement to scroll inside.
    """
    # time.sleep(2)
    # driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", element)
    driver.execute_script("arguments[0].scrollBy(0, 500);", element)
    time.sleep(2)


def get_control_key():
    if platform.system() == 'Darwin':
        return Keys.COMMAND
    else:
        return Keys.CONTROL
