import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_full_month_name, scroll_to_element


@pytest.mark.usefixtures("driver_session")
class TestResy:
    def test_resy_75db63ac(self):
        self.driver.get("https://resy.com")

        nearby_restaurants_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Nearby Restaurants')]")
        scroll_to_element(self.driver, nearby_restaurants_link)
        nearby_restaurants_link.click()

        self.driver.find_element(By.XPATH, "//button[contains(@class, 'LocationsContainer__click-container') and contains(@aria-label, 'Location')]").click()

        self.driver.find_element(By.XPATH, "//button[text()='Chicago']").click()

        if self.driver.find_element(By.XPATH, "//button[@data-test-id='announcement_modal-button-close']") is not None:
            self.driver.find_element(By.XPATH, "//button[@data-test-id='announcement_modal-button-close']").click()

        self.driver.find_element(By.ID, "DateSelector__button").click()

        start_date_str, _ = calculate_dates_full_month_name(7, 7)
        if self.driver.find_element(By.XPATH, f"//button[contains(@aria-label, '{start_date_str}')]") is None:
            self.driver.find_element(By.XPATH, "//button[@aria-label='Next month']").click()
        self.driver.find_element(By.XPATH, f"//button[contains(@aria-label, '{start_date_str}')]").click()

        party_size_dropdown = self.driver.find_element(By.ID, "party_size")
        party_size_select = Select(party_size_dropdown)
        party_size_select.select_by_value("7")

        top_rated_restaurant = self.driver.find_element(By.XPATH, "//article[@aria-labelledby='region-top-rated']/div[1]/div[1]/div[1]")
        scroll_to_element(self.driver, top_rated_restaurant)
        top_rated_restaurant.click()

        time.sleep(2)
        party_time_dropdown = self.driver.find_element(By.ID, "time")
        party_time_select = Select(party_time_dropdown)
        party_time_select.select_by_value("1400")
        self.driver.find_element(By.XPATH, "//button[@data-test-id='venue-page-save']").click()
