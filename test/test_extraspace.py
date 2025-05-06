import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_down


@pytest.mark.usefixtures("setup_class")
class TestExtraspace:
    def test_extraspace_8fb3e11e(self):
        self.driver.get("https://extraspace.com")

        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").send_keys("colorado springs")

        self.driver.find_element(By.XPATH, "//button[@type='button' and @data-qa='navbar-search-button']").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/div/main/div[3]/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/div/button").click()

        scroll_down(self.driver, 500)
        time.sleep(2)
        enclosed_driver_up_checkbox = self.driver.find_element(By.XPATH, "//label[text()='Enclosed Drive-Up']")
        enclosed_driver_up_checkbox.click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/div/main/div[3]/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/div/div/div/div[2]/div[3]/a").click()
        self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/div/div/a/div[1]/img").click()
