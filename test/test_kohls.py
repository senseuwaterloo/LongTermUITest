import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestKohls:
    def test_kohls_aab91310(self):
        self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("mens hiking shoes")
        self.driver.find_element(By.XPATH, "//input[@name='submit-search' and @value='' and @type='submit']").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'root_panel')]/div[10]/div[1]").click()

        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[1]/a[1]/span[1]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[2]/a[1]/span[1]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[3]/a[1]/span[1]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'panel')]/div[6]/div[1]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ul[@id='Size']/li[10]/a[1]/span[1]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(@id, 'sbSelector_')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Percent Off')]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ul[@id='productsContainer']/li[1]/div[1]").click()
