import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates, switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestRyanair:
    def test_ryanair_edf748d4(self):
        # self.driver.get("http://ryanair.com/")

        # self.driver.find_element(By.XPATH, "/html/body[1]/hp-app-root[1]/hp-home-container[1]/hp-home[1]/hp-search-widget-container[1]/hp-search-widget[1]/div[1]/hp-search-widget-tabs-container[1]/button[3]/hp-search-widget-tab[1]").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='hotels']").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/hp-app-root[1]/hp-home-container[1]/hp-home[1]/hp-search-widget-container[1]/hp-search-widget[1]/div[1]/hp-lazy-room-search-widget[1]/hp-app-room-search-widget[1]/hp-room-search-widget-container[1]/hp-room-search-widget[1]/div[1]/hp-room-search-widget-controls-container[1]/hp-room-search-widget-controls[1]/div[1]/hp-input-button[1]/div[1]/div[1]").clear()
        # self.driver.find_element(By.XPATH, "/html/body[1]/hp-app-root[1]/hp-home-container[1]/hp-home[1]/hp-search-widget-container[1]/hp-search-widget[1]/div[1]/hp-lazy-room-search-widget[1]/hp-app-room-search-widget[1]/hp-room-search-widget-container[1]/hp-room-search-widget[1]/div[1]/hp-room-search-widget-controls-container[1]/hp-room-search-widget-controls[1]/div[1]/hp-input-button[1]/div[1]/div[1]").send_keys("jakarta")
        # self.driver.find_element(By.XPATH, "/html/body[1]/hp-app-root[1]/hp-home-container[1]/hp-home[1]/hp-search-widget-container[1]/hp-search-widget[1]/div[1]/hp-lazy-room-search-widget[1]/hp-app-room-search-widget[1]/hp-room-search-widget-container[1]/hp-room-search-widget[1]/div[1]/hp-room-search-widget-controls-container[1]/hp-room-search-widget-controls[1]/div[1]/hp-input-button[1]").clear()
        # self.driver.find_element(By.XPATH, "/html/body[1]/hp-app-root[1]/hp-home-container[1]/hp-home[1]/hp-search-widget-container[1]/hp-search-widget[1]/div[1]/hp-lazy-room-search-widget[1]/hp-app-room-search-widget[1]/hp-room-search-widget-container[1]/hp-room-search-widget[1]/div[1]/hp-room-search-widget-controls-container[1]/hp-room-search-widget-controls[1]/div[1]/hp-input-button[1]").send_keys("jakarta")
        # self.driver.find_element(By.XPATH, "//ry-tooltip[@id='ry-tooltip-8']/div[2]/hp-lazy-room-search-controls-tooltips[1]/hp-app-room-search-controls-tooltips[1]/hp-room-search-controls-tooltips-container[1]/hp-room-search-controls-tooltips[1]/hp-room-search-locations-properties-container[1]/hp-room-search-locations-properties[1]/div[1]/hp-room-search-location-item[1]/div[1]").click()
        self.driver.find_element(By.ID, "input-button__locations-or-properties").clear()
        self.driver.find_element(By.ID, "input-button__locations-or-properties").send_keys("Jakarta")
        self.driver.find_element(By.XPATH, "//div[@class='tooltip-inner']//div[text()='Jakarta, Special Capital Region of Jakarta']").click()

        # self.driver.find_element(By.XPATH, "//div[contains(.,'Choose date')]").click()
        # self.driver.find_element(By.XPATH, "//ry-tooltip[@id='ry-tooltip-9']/div[2]/hp-lazy-room-search-controls-tooltips[1]/hp-app-room-search-controls-tooltips[1]/hp-room-search-controls-tooltips-container[1]/hp-room-search-controls-tooltips[1]/hp-room-search-datepicker-container[1]/fsw-datepicker[1]/ry-datepicker-desktop[1]/month-toggle[1]/div[1]/div[2]/div[1]/div[3]/div[2]").click()
        # self.driver.find_element(By.XPATH, "//ry-tooltip[@id='ry-tooltip-9']/div[2]/hp-lazy-room-search-controls-tooltips[1]/hp-app-room-search-controls-tooltips[1]/hp-room-search-controls-tooltips-container[1]/hp-room-search-controls-tooltips[1]/hp-room-search-datepicker-container[1]/fsw-datepicker[1]/ry-datepicker-desktop[1]/div[1]/calendar[1]/calendar-body[1]/div[2]/div[10]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//ry-tooltip[@id='ry-tooltip-10']/div[2]/hp-lazy-room-search-controls-tooltips[1]/hp-app-room-search-controls-tooltips[1]/hp-room-search-controls-tooltips-container[1]/hp-room-search-controls-tooltips[1]/hp-room-search-datepicker-container[1]/fsw-datepicker[1]/ry-datepicker-desktop[1]/div[1]/calendar[1]/calendar-body[1]/div[2]/div[19]/div[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/hp-app-root[1]/hp-home-container[1]/hp-home[1]/hp-search-widget-container[1]/hp-search-widget[1]/div[1]/hp-lazy-room-search-widget[1]/hp-app-room-search-widget[1]/hp-room-search-widget-container[1]/hp-room-search-widget[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.CSS_SELECTOR, "hp-input-button[uniqueid='check-in']").click()
        start_date_str, end_date_str = calculate_dates(14, 17)
        self.driver.find_element(By.XPATH, f"//div[@class='tooltip-inner']//div[@data-id='{start_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//div[@class='tooltip-inner']//div[@data-id='{end_date_str}']").click()
        self.driver.find_element(By.XPATH, "//button[@data-ref='rooms-search-widget__cta']").click()

        # handle the cookie popup again
        # self.driver.find_element(By.XPATH, "//div[@id='cookie-popup-with-overlay']/div[1]/div[3]/button[2]").click()
        if self.driver.find_element(By.ID, "onetrust-accept-btn-handler") is not None:
            # wait for the cookie popup to be stable otherwise will have: selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted
            time.sleep(2)
            self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Lowest price')]").click()
        sort_by_dropdown = self.driver.find_element(By.ID, "sort-filter-dropdown-sort")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_value("PRICE_LOW_TO_HIGH")

        # wait for a few seconds to let the result to be refreshed otherwise will click on a wrong result item
        time.sleep(2)

        # self.driver.find_element(By.XPATH, "//button[contains(.,'Choose room')]").click()
        self.driver.find_element(By.XPATH, "//div[@data-stid='property-listing-results']/div[1]//a[@data-stid='open-hotel-information']").click()
        switch_to_new_tab(self.driver)

        # self.driver.find_element(By.XPATH, "//button[contains(.,'Book now')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-stid='sticky-button']").click()
        self.driver.find_element(By.XPATH, "//button[@data-stid='submit-hotel-reserve']").click()
        self.driver.find_element(By.XPATH, "//button[@data-stid='submit-hotel-reserve' and @type='submit' and ./span[text()='Pay now']]").click()


        # self.driver.find_element(By.XPATH, "//input[@name='firstName' and @type='text']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='firstName' and @type='text']").send_keys("Joe")
        # self.driver.find_element(By.XPATH, "//input[@name='firstSurname' and @type='text']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='firstSurname' and @type='text']").send_keys("Bloggs")
        # self.driver.find_element(By.ID, "email").clear()
        # self.driver.find_element(By.ID, "email").send_keys("buckeye.foobar@gmail.com")
        # self.driver.find_element(By.ID, "confirmEmail").clear()
        # self.driver.find_element(By.ID, "confirmEmail").send_keys("buckeye.foobar@gmail.com")
        # self.driver.find_element(By.XPATH, "//input[@name='phone' and @type='tel']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='phone' and @type='tel']").send_keys("1111111111111111")
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
