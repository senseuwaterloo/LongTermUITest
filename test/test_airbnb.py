import time

import pytest
from selenium.webdriver.common.by import By
from browser_helper import calculate_dates


@pytest.mark.usefixtures("setup_class")
class TestAirbnb:
    def test_airbnb_cdf4d2ec(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//input[@data-testid='structured-search-input-field-query']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='header-tab-search-block-tab-EXPERIENCES']").click()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").clear()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").send_keys("portugal")
        self.driver.find_element(By.XPATH, "//div[@id='bigsearch-query-location-suggestion-0']/div[2]/div[1]").click()
        start_date_str, end_date_str = calculate_dates(7, 8)
        self.driver.find_element(By.CSS_SELECTOR, f"div[data-testid='calendar-day-{start_date_str}']").click()
        self.driver.find_element(By.CSS_SELECTOR, f"div[data-testid='calendar-day-{end_date_str}']").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='structured-search-input-field-guests-button']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='stepper-adults-increase-button']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='stepper-children-increase-button']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='structured-search-input-search-button']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='menuItemButton-Language offered']").click()
        self.driver.find_element(By.ID, "filter-item-experience_languages-1-row-title").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='filter-panel-save-button']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='menuItemButton-Time of day']").click()
        self.driver.find_element(By.ID, "filter-item-experience_time_of_day-morning-row-title").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='filter-panel-save-button']").click()
        self.driver.find_element(By.ID, "menuItemButton-search-filter-bar-quick-filters-Sports").click()
