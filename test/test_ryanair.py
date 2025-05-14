import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates, switch_to_new_tab


@pytest.mark.usefixtures("driver_session")
class TestRyanair:
    def test_ryanair_edf748d4(self):
        self.driver.get("http://ryanair.com/")

        self.driver.find_element(By.XPATH, "//button[@aria-label='hotels']").click()

        self.driver.find_element(By.ID, "input-button__locations-or-properties").clear()
        self.driver.find_element(By.ID, "input-button__locations-or-properties").send_keys("Jakarta")
        self.driver.find_element(By.XPATH, "//div[@class='tooltip-inner']//div[text()='Jakarta, Special Capital Region of Jakarta']").click()

        self.driver.find_element(By.CSS_SELECTOR, "hp-input-button[uniqueid='check-in']").click()
        start_date_str, end_date_str = calculate_dates(14, 17)
        self.driver.find_element(By.XPATH, f"//div[@class='tooltip-inner']//div[@data-id='{start_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//div[@class='tooltip-inner']//div[@data-id='{end_date_str}']").click()
        self.driver.find_element(By.XPATH, "//button[@data-ref='rooms-search-widget__cta']").click()

        if self.driver.find_element(By.ID, "onetrust-accept-btn-handler") is not None:
            time.sleep(2)
            self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

        sort_by_dropdown = self.driver.find_element(By.ID, "sort-filter-dropdown-sort")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_value("PRICE_LOW_TO_HIGH")

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@data-stid='property-listing-results']/div[1]//a[@data-stid='open-hotel-information']").click()
        switch_to_new_tab(self.driver)

        self.driver.find_element(By.XPATH, "//button[@data-stid='sticky-button']").click()
        self.driver.find_element(By.XPATH, "//button[@data-stid='submit-hotel-reserve']").click()
        self.driver.find_element(By.XPATH, "//button[@data-stid='submit-hotel-reserve' and @type='submit' and ./span[text()='Pay now']]").click()

        self.driver.find_element(By.NAME, "tripPreferencesRequest.hotelTripPreferences.hotelRoomPreferences[0].firstName").clear()
        self.driver.find_element(By.NAME, "tripPreferencesRequest.hotelTripPreferences.hotelRoomPreferences[0].firstName").send_keys("Joe")
        self.driver.find_element(By.NAME, "tripPreferencesRequest.hotelTripPreferences.hotelRoomPreferences[0].lastName").clear()
        self.driver.find_element(By.NAME, "tripPreferencesRequest.hotelTripPreferences.hotelRoomPreferences[0].lastName").send_keys("Bloggs")
        self.driver.find_element(By.XPATH, "//input[@name='email' and @type='email']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='email' and @type='email']").send_keys("buckeye.foobar@gmail.com")
        self.driver.find_element(By.NAME, "tripPreferencesRequest.hotelTripPreferences.hotelRoomPreferences[0].preferredPhoneNumber").clear()
        self.driver.find_element(By.NAME, "tripPreferencesRequest.hotelTripPreferences.hotelRoomPreferences[0].preferredPhoneNumber").send_keys("1111111111111111")
        self.driver.find_element(By.ID, "creditCardInput").clear()
        self.driver.find_element(By.ID, "creditCardInput").send_keys("1234567890123456")
        expiry_month_dropdown = self.driver.find_element(By.NAME, "expiration_month")
        expiry_month_select = Select(expiry_month_dropdown)
        expiry_month_select.select_by_value("7")
        expiry_year_dropdown = self.driver.find_element(By.NAME, "expiration_year")
        expiry_year_select = Select(expiry_year_dropdown)
        expiry_year_select.select_by_value("2026")
        self.driver.find_element(By.ID, "new_cc_security_code").clear()
        self.driver.find_element(By.ID, "new_cc_security_code").send_keys("123")
        self.driver.find_element(By.ID, "explicit-consent").click()
        self.driver.find_element(By.ID, "complete-booking").click()
