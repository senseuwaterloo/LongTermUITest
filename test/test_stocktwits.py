import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestStocktwits:
    def test_stocktwits_94ac9003(self):
        # self.driver.get("https://stocktwits.com/")
        # uiteststudy@gmail.com:Pass4Stockwits!
        # add extra steps to login
        self.driver.find_element(By.XPATH, "//a[text()='Log in to existing account']").click()
        self.driver.find_element(By.NAME, "login").clear()
        self.driver.find_element(By.NAME, "login").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("Pass4Stockwits!")
        self.driver.find_element(By.XPATH, "//button[@data-testid='log-in-submit']").click()

        # self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("tesla")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search stocks, crypto, and people']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search stocks, crypto, and people']").send_keys("tesla")

        # self.driver.find_element(By.XPATH, "//div[@id='app-main-header']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        # new xpath: //div[@id="app-main-header"]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[1]
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'Item_itemDescriptionTitle') and ./span[text()='TSLA']]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Alerts ']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='react-tabs-11']/div[1]/form[1]/div[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='react-tabs-11']/div[1]/form[1]/div[1]/select[1]").select("Price")
        # self.driver.find_element(By.XPATH, "//div[@id='react-tabs-11']/div[1]/form[1]/div[2]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='react-tabs-11']/div[1]/form[1]/div[2]/select[1]").select("Is Below")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Enter a value']").clear()
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Enter a value']").send_keys("300")
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        signal_dropdown = self.driver.find_element(By.XPATH, "//select[@data-testid='signal']")
        signal_select = Select(signal_dropdown)
        signal_select.select_by_value("PRICE")
        condition_dropdown = self.driver.find_element(By.XPATH, "//select[@data-testid='condition']")
        condition_select = Select(condition_dropdown)
        condition_select.select_by_value("IS_BELOW")
        self.driver.find_element(By.XPATH, "//input[@data-testid='valueSelector']").send_keys("300")

        self.driver.find_element(By.XPATH, "//button[text()='Save Alert']").click()

        # delete alert for next test run
        self.driver.find_element(By.XPATH, "//h2[@data-testid='manage']").click()
        self.driver.find_element(By.XPATH, "//div[./div/span[text()='TSLA']]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Yes, Delete Alert']").click()
        # wait for the delete operation to finish
        time.sleep(2)
