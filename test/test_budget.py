import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_budget_dates


@pytest.mark.usefixtures("setup_class")
class TestBudget:
    def test_budget_c759aa6c(self):
        # self.driver.get("https://www.budget.com/en/home")
        # uiteststudy@gmail.com:UITestStudy2024!
        # self.driver.find_element(By.ID, "res-login-profile").click()
        # self.driver.find_element(By.ID, "username").click()
        # self.driver.find_element(By.ID, "username").send_keys("uiteststudy@gmail.com")
        # self.driver.find_element(By.ID, "password").click()
        # self.driver.find_element(By.ID, "password").send_keys("UITestStudy2024!")
        # self.driver.find_element(By.ID, "res-login-profile").click()
        self.driver.find_element(By.ID, "PicLoc_value").clear()
        self.driver.find_element(By.ID, "PicLoc_value").send_keys("Chicago O'hare Intl Airport, ORD")
        self.driver.find_element(By.XPATH, "//span[contains(text(),\"Chicago O'Hare Intl Airport\")]").click()
        (start_date_year, start_date_month_adjusted, start_date_day), (end_date_year, end_date_month_adjusted, end_date_day) = calculate_budget_dates(7, 14)
        # time.sleep(2)
        self.driver.find_element(By.ID, "from").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, f"//td[@data-year='{start_date_year}' and @data-month='{start_date_month_adjusted}']//a[text()='{start_date_day}']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "to").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, f"//td[@data-year='{end_date_year}' and @data-month='{end_date_month_adjusted}']//a[text()='{end_date_day}']").click()
        # time.sleep(2)
        self.driver.find_element(By.ID, "res-home-vehicle-type").click()
        self.driver.find_element(By.XPATH, "//form[@id='selectCar']//img[@alt='SUVs & Wagons']").click()
        self.driver.find_element(By.ID, "res-home-select-car").click()
        self.driver.find_element(By.ID, "res-vehicles-sort").click()
        self.driver.find_element(By.XPATH, "//a[contains(.,'Price (Low to High)')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(.,'Add Offer Code')]").click()
        self.driver.find_element(By.XPATH, "//a[@ng-click='vm.applyCoupon()' and text()='Update']").click()
        # time.sleep(1)
        # self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[1]/div/div/div[2]/div[1]/section[3]/div[1]/div[2]/div/section/div[1]/div/div[2]/div[2]/div[2]/a").click()
    