import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_day_month_format, scroll_down


@pytest.mark.usefixtures("setup_class")
class TestPensketruckrental:
    def test_pensketruckrental_d1c3d4d2(self):
        # self.driver.get("https://pensketruckrental.com")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='right-side']//a[contains(text(),'Locations')]").click()

        # redundant action in the new web page
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Location')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Massachusetts')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Norwood')]").click()
        # self.driver.find_element(By.XPATH, "//div[@class='big-container no-map']//a[contains(text(),'Norwood')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'All Seasons Rent All')]").click()
        # page is still loading and lead to selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted:
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Seasons Rent')]").click()

        # self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
        # self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("NORWOOD")
        # self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[2]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='appRoot']/section[1]/form[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='appRoot']/section[1]/form[1]/fieldset[2]/div[1]/div[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[18]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[19]/span[1]").click()
        # self.driver.find_element(By.ID, "truck_size_select").clear()
        # self.driver.find_element(By.ID, "truck_size_select").select("High Roof Cargo Van (Up to 1 Room)")
        # self.driver.find_element(By.XPATH, "//div[@id='appRoot']/section[1]/form[1]/div[2]/div[1]/button[1]").click()

        # page is still loading and lead to selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted:
        time.sleep(3)
        self.driver.find_element(By.ID, "returntoSB").click()
        # somehow dropdown will not expand with typical click method. Try click with JS
        # self.driver.find_element(By.XPATH, "//div[contains(@id, 'sSidebar_Posts_')]//div[@class='quote_truck_size_select']/span[text()='Truck Size']").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[contains(@id, 'sSidebar_Posts_')]//div[@class='quote_truck_size_select']/span[text()='Truck Size']").get_native_element())
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'sSidebar_Posts_')]//span[@data-truck-name='Cargo Van (Up to 1 Room)']").click()
        start_day, start_month, end_day, end_month = calculate_dates_day_month_format(14, 15)
        self.driver.find_element(By.ID, "mat-input-1").click()
        self.driver.find_element(By.XPATH, f"//div[contains(@class, 'month-container')]/month[./header/p[text()='{start_month}']]/div[1]/date[./div/span[text()='{start_day}']]").click()
        self.driver.find_element(By.XPATH, f"//div[contains(@class, 'month-container')]/month[./header/p[text()='{end_month}']]/div[1]/date[./div/span[text()='{end_day}']]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Continue ']").click()
        self.driver.find_element(By.ID, "submitbuttonSB").click()
