import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestTheweathernetwork:
    def test_theweathernetwork_7ba05167(self):
        self.driver.get("https://theweathernetwork.com")

        self.driver.find_element(By.ID, "InputField").clear()
        self.driver.find_element(By.ID, "InputField").send_keys("Vancouver")

        self.driver.find_element(By.XPATH, "//div[@data-testid='search-result-item']/div[text()='Vancouver, British Columbia']").click()

        time.sleep(5)
        self.driver.find_element(By.XPATH, "//nav[@data-testid='header-navigation-bar']/a[2]").click()

        self.driver.find_element(By.XPATH, "//button[@title='Highway Conditions']").click()
