import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_full_month_name, scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestResy:
    def test_resy_75db63ac(self):
        # self.driver.get("https://resy.com")

        nearby_restaurants_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Nearby Restaurants')]")
        scroll_to_element(self.driver, nearby_restaurants_link)
        nearby_restaurants_link.click()

        # self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
        # //div[@id="page-wrapper"]/resy-nav/header/div[2]/div[1]/resy-locations-container/div/div/button/div/div
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'LocationsContainer__click-container') and contains(@aria-label, 'Location')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Chicago')]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Chicago']").click()

        # add extra step to handle possible popups
        if self.driver.find_element(By.XPATH, "//button[@data-test-id='announcement_modal-button-close']") is not None:
            self.driver.find_element(By.XPATH, "//button[@data-test-id='announcement_modal-button-close']").click()

        self.driver.find_element(By.ID, "DateSelector__button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='DayPicker']/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[5]/button[1]").click()
        start_date_str, _ = calculate_dates_full_month_name(7, 7)
        if self.driver.find_element(By.XPATH, f"//button[contains(@aria-label, '{start_date_str}')]") is None:
            self.driver.find_element(By.XPATH, "//button[@aria-label='Next month']").click()
        self.driver.find_element(By.XPATH, f"//button[contains(@aria-label, '{start_date_str}')]").click()

        # self.driver.find_element(By.ID, "party_size").clear()
        # self.driver.find_element(By.ID, "party_size").select("7 Guests")
        party_size_dropdown = self.driver.find_element(By.ID, "party_size")
        party_size_select = Select(party_size_dropdown)
        party_size_select.select_by_value("7")

        # self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[5]/i[1]/i[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/div[4]/div[5]/div[2]/div[2]/div[4]/button[5]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='rgs://resy/61091/1808411/3/2023-04-20/2023-04-20/14:00:00/7/Dining Room']/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[2]/div[4]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/confirmation-page[1]/div[1]/div[2]/div[3]/button[1]/span[1]").click()
        top_rated_restaurant = self.driver.find_element(By.XPATH, "//article[@aria-labelledby='region-top-rated']/div[1]/div[1]/div[1]")
        scroll_to_element(self.driver, top_rated_restaurant)
        top_rated_restaurant.click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        party_time_dropdown = self.driver.find_element(By.ID, "time")
        party_time_select = Select(party_time_dropdown)
        party_time_select.select_by_value("1400")
        self.driver.find_element(By.XPATH, "//button[@data-test-id='venue-page-save']").click()
    