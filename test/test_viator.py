import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_next_first_last_day


@pytest.mark.usefixtures("driver_session")
class TestViator:
    def test_viator_8308d10f(self):
        self.driver.get("https://www.viator.com/")

        time.sleep(2)
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("India")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='react-select-homepageTypeaheadSearch-option-1']/button[1]").click()
        time.sleep(2)

        first_date_str, last_date_str = calculate_next_first_last_day()
        self.driver.find_element(By.XPATH, "//button[@data-automation='experiences-search-datepicker-calendar-next']").click()
        self.driver.find_element(By.XPATH, f"//div[@aria-label='{first_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//div[@aria-label='{last_date_str}']").click()
        self.driver.find_element(By.XPATH, "//button[@data-automation='experiences-search-datepicker-calendar-apply-btn']").click()

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//a[@data-automation='filter-panel-filter-set-TAGS' and text()='Tours, Sightseeing & Cruises']/following-sibling::*[1]").click()
        self.driver.find_element(By.XPATH, "//a[@data-automation='filter-panel-filter-set-TAGS' and text()='Sightseeing Tours']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[./div[1]/h5[text()='Specials']]//div[text()='Show more']").click()
        self.driver.find_element(By.XPATH, "//div[@data-automation='filter-panel-filter-set-SPECIALS-PRIVATE_TOUR-label']").click()
        time.sleep(2)

        sort_dropdown = self.driver.find_element(By.NAME, "sortBy")
        sort_select = Select(sort_dropdown)
        sort_select.select_by_value("DURATION_DESC")
        time.sleep(2)
