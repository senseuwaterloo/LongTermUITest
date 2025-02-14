import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestUltimateGuitar:
    def test_ultimateguitar_61d28a34(self):
        # self.driver.get("https://www.ultimate-guitar.com/")
        # NO Change
        # self.driver.find_element(By.XPATH, "//span[contains(.,'Tabs')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Tabs']").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Beginner')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Beginner']").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Drop C')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Drop C']").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Rock')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Rock']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Tab')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Tab']").click()

        # self.driver.find_element(By.XPATH, "//div[contains(.,\"Today's most popular\")]").click()
        self.driver.find_element(By.XPATH, "//div[text()=\"Today's most popular\"]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Most popular of all time')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Most popular of all time']").click()
        time.sleep(1)
