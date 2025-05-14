import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_full_month_name


@pytest.mark.usefixtures("driver_session")
class TestUsMegabus:
    def test_usmegabus_54d60a7c(self):
        self.driver.get("https://us.megabus.com")

        if self.driver.find_element(By.XPATH, "//button[text()='Decline Offer']") is not None:
            self.driver.find_element(By.XPATH, "//button[text()='Decline Offer']").click()

        self.driver.find_element(By.ID, "startingAt").clear()
        self.driver.find_element(By.ID, "startingAt").send_keys("albany")

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[./input[@id='startingAt']]//div[@title='Enter a town or city']/div[1]/div[2]").click()

        self.driver.find_element(By.ID, "goingTo").clear()
        self.driver.find_element(By.ID, "goingTo").send_keys("New York")

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[./input[@id='goingTo']]//div[@title='Enter a town or city']/div[1]/div[2]").click()

        time.sleep(2)
        self.driver.find_element(By.ID, "mat-input-0").click()

        start_date_str, end_date_str = calculate_dates_full_month_name(7, 14)
        if self.driver.find_element(By.XPATH, f"//td[@aria-label='{start_date_str}']") is None:
            self.driver.find_element(By.XPATH, "//button[@aria-label='Next month']").click()

        self.driver.find_element(By.XPATH, f"//td[@aria-label='{start_date_str}']").click()

        self.driver.find_element(By.ID, "mat-input-1").click()

        if self.driver.find_element(By.XPATH, f"//td[@aria-label='{end_date_str}']") is None:
            self.driver.find_element(By.XPATH, "//button[@aria-label='Next month']").click()

        self.driver.find_element(By.XPATH, f"//td[@aria-label='{end_date_str}']").click()

        self.driver.find_element(By.ID, "totalPassengers").clear()
        self.driver.find_element(By.ID, "totalPassengers").send_keys("3")
        self.driver.find_element(By.ID, "findTickets").click()
