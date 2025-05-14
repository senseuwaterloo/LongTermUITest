import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_slash_format


@pytest.mark.usefixtures("driver_session")
class TestSpothero:
    def test_spothero_749dfeeb(self):
        self.driver.get("https://spothero.com/")

        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()

        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("Smithsonian National Air")

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()

        self.driver.find_element(By.XPATH, "//button[@data-testid='QuickFilters-filter']").click()

        self.driver.find_element(By.XPATH, "//label[@for='Checkbox-FilterItem-ev']").click()

        self.driver.find_element(By.XPATH, "//button[@data-testid='FiltersModal-button']").click()

        self.driver.find_element(By.XPATH, "//input[@value='Today' and @type='text' and @placeholder='Start Date']").click()

        start_date_str, end_date_str = calculate_dates_slash_format(7, 7)
        if self.driver.find_element(By.XPATH, f"//span[@data-date='{start_date_str}']") is None:
            self.driver.find_element(By.XPATH, "//button[contains(@class, 'DayPicker-NavButton--next')]").click()
        self.driver.find_element(By.XPATH, f"//span[@data-date='{start_date_str}']").click()

        start_time_dropdown = self.driver.find_element(By.XPATH, "//select[@class='FormElement-item' and @aria-label='Start Time']")
        start_time_select = Select(start_time_dropdown)
        start_time_select.select_by_value("09:00 AM")

        end_time_dropdown = self.driver.find_element(By.XPATH, "//select[@class='FormElement-item' and @aria-label='End Time']")
        end_time_select = Select(end_time_dropdown)
        end_time_select.select_by_value("06:00 PM")

        self.driver.find_element(By.XPATH, "//button[@data-testid='SearchActions-submit-button']").click()

        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[@class='FormElement-item' and @data-testid='SpotListSorter-select']")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_value("distance")
