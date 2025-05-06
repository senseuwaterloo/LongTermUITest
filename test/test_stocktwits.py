import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestStocktwits:
    def test_stocktwits_94ac9003(self):
        self.driver.get("https://stocktwits.com/")

        self.driver.find_element(By.XPATH, "//a[text()='Log in to existing account']").click()
        self.driver.find_element(By.NAME, "login").clear()
        self.driver.find_element(By.NAME, "login").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("Pass4Stockwits!")
        self.driver.find_element(By.XPATH, "//button[@data-testid='log-in-submit']").click()

        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search stocks, crypto, and people']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search stocks, crypto, and people']").send_keys("tesla")

        self.driver.find_element(By.XPATH, "//div[contains(@class, 'Item_itemDescriptionTitle') and ./span[text()='TSLA']]").click()

        self.driver.find_element(By.XPATH, "//span[text()='Alerts ']").click()

        signal_dropdown = self.driver.find_element(By.XPATH, "//select[@data-testid='signal']")
        signal_select = Select(signal_dropdown)
        signal_select.select_by_value("PRICE")
        condition_dropdown = self.driver.find_element(By.XPATH, "//select[@data-testid='condition']")
        condition_select = Select(condition_dropdown)
        condition_select.select_by_value("IS_BELOW")
        self.driver.find_element(By.XPATH, "//input[@data-testid='valueSelector']").send_keys("300")

        self.driver.find_element(By.XPATH, "//button[text()='Save Alert']").click()

        self.driver.find_element(By.XPATH, "//h2[@data-testid='manage']").click()
        self.driver.find_element(By.XPATH, "//div[./div/span[text()='TSLA']]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Yes, Delete Alert']").click()
        time.sleep(2)
