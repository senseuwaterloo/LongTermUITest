import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_next_first_last_day


@pytest.mark.usefixtures("setup_class")
class TestViator:
    def test_viator_8308d10f(self):
        # self.driver.get("https://www.viator.com/")
        # TODO: Blocked by viator...... Consider remove this subject

        time.sleep(2)
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("India")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='react-select-homepageTypeaheadSearch-option-1']/button[1]").click()
        time.sleep(2)

        # self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@role='gridcell']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[5]/div[6]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[2]/button[2]/span[1]").click()
        first_date_str, last_date_str = calculate_next_first_last_day()
        self.driver.find_element(By.XPATH, "//button[@data-automation='experiences-search-datepicker-calendar-next']").click()
        self.driver.find_element(By.XPATH, f"//div[@aria-label='{first_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//div[@aria-label='{last_date_str}']").click()
        self.driver.find_element(By.XPATH, "//button[@data-automation='experiences-search-datepicker-calendar-apply-btn']").click()
        # avoid anti-robot
        time.sleep(2)

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/circle[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='heading21913']/div[1]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='collapseGroup21913']/div[1]/div[7]/div[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='specialsFilterOptions']/div[3]/div[3]/label[1]/span[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//a[@data-automation='filter-panel-filter-set-TAGS' and text()='Tours, Sightseeing & Cruises']/following-sibling::*[1]").click()
        self.driver.find_element(By.XPATH, "//a[@data-automation='filter-panel-filter-set-TAGS' and text()='Sightseeing Tours']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[./div[1]/h5[text()='Specials']]//div[text()='Show more']").click()
        self.driver.find_element(By.XPATH, "//div[@data-automation='filter-panel-filter-set-SPECIALS-PRIVATE_TOUR-label']").click()
        time.sleep(2)

        # self.driver.find_element(By.ID, "displayed-sort").click()
        # self.driver.find_element(By.XPATH, "//div[@id='dropdown-option']/span[1]").click()
        sort_dropdown = self.driver.find_element(By.NAME, "sortBy")
        sort_select = Select(sort_dropdown)
        sort_select.select_by_value("DURATION_DESC")
        time.sleep(2)
