import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("driver_session")
class TestUdemy:
    def test_udemy_949e33a5(self):
        self.driver.get("https://www.udemy.com/")

        self.driver.find_element(By.NAME, "q").clear()
        self.driver.find_element(By.NAME, "q").send_keys("home workout")

        self.driver.find_element(By.NAME, "q").send_keys(Keys.RETURN)

        self.driver.find_element(By.XPATH, "//span[text()='Video Duration']").click()
        self.driver.find_element(By.XPATH, "//label[text()='0-1 Hour']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Topic']").click()
        self.driver.find_element(By.XPATH, "//label[text()='Weight Loss']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Level']").click()
        self.driver.find_element(By.XPATH, "//label[text()='Beginner']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Subtitles']").click()
        self.driver.find_element(By.XPATH, "//div[./div[1]/h3/button/span[text()='Subtitles']]//label[text()='English']").click()

        time.sleep(2)
        sort_dropdown = self.driver.find_element(By.NAME, "sort")
        sort_select = Select(sort_dropdown)
        sort_select.select_by_value("newest")
        time.sleep(1)
