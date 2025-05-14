import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_without_space, switch_to_new_tab_and_close_old


@pytest.mark.usefixtures("driver_session")
class TestUnited:
    def test_united_fdf322bd(self):
        self.driver.get("https://www.united.com/en/us")

        self.driver.find_element(By.XPATH, "//button/span[text()='Book']").click()

        self.driver.find_element(By.XPATH, "//a[text()='Vacation packages']").click()
        switch_to_new_tab_and_close_old(self.driver)

        self.driver.find_element(By.XPATH, "//label[@for='Hotel + Flight + Car']").click()

        self.driver.find_element(By.ID, "Where from?").clear()
        self.driver.find_element(By.ID, "Where from?").send_keys("new york")

        self.driver.find_element(By.XPATH, "//div[@id='Where from?-dropdown']//div[@id='undefined-item-0']/div[1]/div[1]").click()

        self.driver.find_element(By.ID, "Where to?").clear()
        self.driver.find_element(By.ID, "Where to?").send_keys("las vegas")

        self.driver.find_element(By.XPATH, "//div[@id='Where to?-dropdown']//div[@id='undefined-item-0']/div[1]/div[1]").click()

        self.driver.find_element(By.XPATH, "//div[text()='Departing - Returning']").click()
        start_date_str, end_date_str = calculate_dates_without_space(14, 21)
        self.driver.find_element(By.XPATH, f"//div[@data-autobot-element-id='DATEPICKER_DAY_{start_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//div[@data-autobot-element-id='DATEPICKER_DAY_{end_date_str}']").click()

        self.driver.find_element(By.XPATH, "//div[text()='Start Saving']").click()
        switch_to_new_tab_and_close_old(self.driver)

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text()='1 Room, 2 Adults']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Select traveler information']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Increase Rooms']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Increase Adults']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Increase Adults']").click()

        time.sleep(20)
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[text()='Done']").get_native_element())
        self.driver.find_element(By.XPATH, "//div[text()='Update Search']").click()
        switch_to_new_tab_and_close_old(self.driver)

        self.driver.find_element(By.XPATH, "//div[text()='4 +']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Show 12 more']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@for, 'Amenities-CASINO-checkbox-')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='DROP_DOWN_FIELD_BOX']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Lowest Price']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'undefined listings')]/div[contains(@class, 'Listings__StyledWrapper')]/div[1]//button[@data-testid='price-choosen-button']").click()
        time.sleep(2)
