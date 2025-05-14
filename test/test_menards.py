import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("driver_session")
class TestMenards:
    def test_menards_24de7f7d(self):
        self.driver.get("https://menards.com")

        self.driver.find_element(By.XPATH, "//button[@qubit-id='SelectStore']").click()

        self.driver.find_element(By.ID, "header-zip-input").clear()
        self.driver.find_element(By.ID, "header-zip-input").send_keys("60538")

        self.driver.find_element(By.XPATH, "//a[@qubit-id='StoreLocator']").click()

        if self.driver.find_element(By.XPATH, "//div[@id='emailBanner']/div[2]/button[1]"):
            self.driver.find_element(By.XPATH, "//div[@id='emailBanner']/div[2]/button[1]").click()

        self.driver.find_element(By.ID, "zip-input").clear()
        self.driver.find_element(By.ID, "zip-input").send_keys("60538")
        self.driver.find_element(By.XPATH, "//button[@id='zip-submit']/i[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='store-locator-results']/ul[1]/li[1]/div[2]/div[1]/button[1]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//nav//input[@name='search' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//nav//input[@name='search' and @type='text' and @placeholder='Search']").send_keys("Magtag electric dryer")

        self.driver.find_element(By.XPATH, "//nav//button[@data-at-id='searchSubmitBtn']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@for='inStockToday']").click()
        electric_dryer_link = self.driver.find_element(By.XPATH, "//label[@role='checkbox' and contains(text(), 'Electric Dryers')]")
        scroll_to_element(self.driver, electric_dryer_link)
        electric_dryer_link.click()

        self.driver.find_element(By.ID, "priceMin").clear()
        self.driver.find_element(By.ID, "priceMin").send_keys("0")
        self.driver.find_element(By.ID, "priceMax").clear()
        self.driver.find_element(By.ID, "priceMax").send_keys("1000")

        self.driver.find_element(By.XPATH, "//input[@value='GO' and @type='button']").click()
    