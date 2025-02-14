import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_slash_format


@pytest.mark.usefixtures("setup_class")
class TestEnterprise:
    def test_enterprise_d5054276(self):
        # self.driver.get("https://enterprise.com")
        # time.sleep(10)
        self.driver.find_element(By.XPATH, "//nav[@id='primary-nav']/ul[1]/li[3]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='navContentLocations']/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "pickupLocationTextBox").clear()
        self.driver.find_element(By.ID, "pickupLocationTextBox").send_keys("02199")
        self.driver.find_element(By.XPATH, "//li[@id='location-US-02199-Boston']/a[1]/span[1]/span[1]").click()

        time.sleep(1)
        # somehow the following click actions is not performed but passed, tried to add 1-second sleep and issue is solved
        self.driver.find_element(By.ID, "continueButton").click()
        self.driver.find_element(By.ID, "1046329").click()
        self.driver.find_element(By.ID, "pickupCalendarFocusable").click()

        start_date_str, end_date_str = calculate_dates_slash_format(7, 9)
        # self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, f"//button[@data-test-id='{start_date_str}']").click()

        # self.driver.find_element(By.ID, "time-picker-1").clear()
        # self.driver.find_element(By.ID, "time-picker-1").select("11 00 AM")
        pick_up_time_dropdown = self.driver.find_element(By.XPATH, "//select[@data-dtm-tracking='dropdown|PICKUPtime|original']")
        pick_up_time_select = Select(pick_up_time_dropdown)
        pick_up_time_select.select_by_value('11:00 AM')

        self.driver.find_element(By.XPATH, "//button[@id='dropoffCalendarFocusable']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, f"//button[@data-test-id='{end_date_str}']").click()

        # self.driver.find_element(By.ID, "time-picker-2").clear()
        # self.driver.find_element(By.ID, "time-picker-2").select("1 00 PM")
        return_time_dropdown = self.driver.find_element(By.XPATH, "//select[@data-dtm-tracking='dropdown|RETURNtime|original']")
        return_time_select = Select(return_time_dropdown)
        return_time_select.select_by_value('1:00 PM')

        self.driver.find_element(By.ID, "continueButton").click()
        self.driver.find_element(By.XPATH, "//input[@value='300' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@value='2' and @type='checkbox']").click()
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div/section/ul/li[1]/div/div[1]/div[2]/div/div/div[2]/button").click()

        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[2]/section[1]/div[1]/div[5]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-code='GPS']//button[@aria-label='Add']").click()

        self.driver.find_element(By.XPATH, "//main[@id='main']/div[2]/div[1]/button[1]").click()
