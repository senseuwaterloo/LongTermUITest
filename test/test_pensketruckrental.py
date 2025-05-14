import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_day_month_format, scroll_down


@pytest.mark.usefixtures("driver_session")
class TestPensketruckrental:
    def test_pensketruckrental_d1c3d4d2(self):
        self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//div[@class='right-side']//a[contains(text(),'Locations')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Massachusetts')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Norwood')]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Seasons Rent')]").click()

        time.sleep(3)
        self.driver.find_element(By.ID, "returntoSB").click()

        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[contains(@id, 'sSidebar_Posts_')]//div[@class='quote_truck_size_select']/span[text()='Truck Size']").get_native_element())
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'sSidebar_Posts_')]//span[@data-truck-name='Cargo Van (Up to 1 Room)']").click()
        start_day, start_month, end_day, end_month = calculate_dates_day_month_format(14, 15)
        self.driver.find_element(By.ID, "mat-input-1").click()
        self.driver.find_element(By.XPATH, f"//div[contains(@class, 'month-container')]/month[./header/p[text()='{start_month}']]/div[1]/date[./div/span[text()='{start_day}']]").click()
        self.driver.find_element(By.XPATH, f"//div[contains(@class, 'month-container')]/month[./header/p[text()='{end_month}']]/div[1]/date[./div/span[text()='{end_day}']]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Continue ']").click()
        self.driver.find_element(By.ID, "submitbuttonSB").click()
