import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestKohls:
    def test_kohls_aab91310(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("mens hiking shoes")
        self.driver.find_element(By.XPATH, "//input[@name='submit-search' and @value='' and @type='submit']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='root_panel454250']/div[10]/div[1]").click()
        # there is a layout change that will coincide with the below action and as a result the list will not expand, so need some sleep
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'root_panel')]/div[10]/div[1]").click()

        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[1]/a[1]/span[1]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        # need some time to refresh the page every time a checkbox is clicked therefore we need some sleep here
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[2]/a[1]/span[1]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        # need some time to refresh the page every time a checkbox is clicked therefore we need some sleep here
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[3]/a[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='panel454323']/div[6]/div[1]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        # need some time to refresh the page every time a checkbox is clicked therefore we need some sleep here
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'panel')]/div[6]/div[1]").click()

        # self.driver.find_element(By.XPATH, "//ul[@id='Size']/li[11]/a[1]/span[1]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        # need some time to refresh the page every time a checkbox is clicked therefore we need some sleep here. Otherwise, no stale element will be thrown. Please refer to the screenshots and logs
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ul[@id='Size']/li[10]/a[1]/span[1]").click()

        # self.driver.find_element(By.ID, "sbSelector_19359954").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        # need some time to refresh the page every time a checkbox is clicked therefore we need some sleep here. Otherwise, no stale element will be thrown. Please refer to the screenshots and logs
        # why there is a time that in the page it looks like the size 9 is also selected while in the followup pages it is not selected?
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(@id, 'sbSelector_')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Percent Off')]").click()

        # self.driver.find_element(By.XPATH, "//img[@title=\"Eddie Bauer Canyon Men's Waterproof Hiking Shoes\"]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        # need some time to refresh the page every time a checkbox is clicked therefore we need some sleep here
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ul[@id='productsContainer']/li[1]/div[1]").click()
