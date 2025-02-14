import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_down


@pytest.mark.usefixtures("setup_class")
class TestExtraspace:
    def test_extraspace_8fb3e11e(self):
        # self.driver.get("https://extraspace.com")
        # logic changed
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").send_keys("colorado springs")

        # self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @data-qa='navbar-search-button']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/div/main/div[3]/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/div/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/label[1]").click()

        # the cookie window will intercept the click of this checkbox, and the close button of the cookie window is in a shadow dom... need to scroll to an element below it...
        # scroll_to_element(self.driver, self.driver.find_element(By.XPATH, "//label[text()='RV Parking']"))
        # need to scroll down for a specific distance since scroll to element is not working
        scroll_down(self.driver, 500)
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted:
        time.sleep(2)
        enclosed_driver_up_checkbox = self.driver.find_element(By.XPATH, "//label[text()='Enclosed Drive-Up']")
        enclosed_driver_up_checkbox.click()

        # self.driver.find_element(By.XPATH, "//label[text()='Outdoor Covered']").click()
        # self.driver.find_element(By.XPATH, "//label[text()='Outdoor Uncovered']").click()
        # self.driver.find_element(By.XPATH, "//label[text()='RV Parking']").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/div/main/div[3]/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/div/div/div/div[2]/div[3]/a").click()
        self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/div/div/a/div[1]/img").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
        # self.driver.find_element(By.ID, "1").click()
        # self.driver.find_element(By.ID, "2").click()
        # self.driver.find_element(By.ID, "3").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.ID, "searchButton").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[5]").click()
        # self.driver.find_element(By.ID, "4").click()
        # self.driver.find_element(By.ID, "0").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-2']/div[1]/div[1]/div[1]/ul[1]/li[2]").click()
