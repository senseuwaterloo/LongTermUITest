import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestCoinmarketcap:
    def test_coinmarketcap_5f0c4ebf(self):
        self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/ul/li[5]/button").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[5]/div/div/div[2]/div[1]/div[1]/button").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[5]/div/div/div[2]/div[1]/div[2]/div[2]/button").click()

        self.driver.find_element(By.XPATH, "//label[@id='mineable']/span").click()

        time.sleep(1)

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[5]/div/div/div[2]/div[1]/div[2]/button").click()

        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$0']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$0']").send_keys("100000000")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$999,999,999,999']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$999,999,999,999']").send_keys("1000000000")

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[5]/div/div/div[2]/div/div[3]/div[2]/div/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[5]/div/div/div[2]/div[1]/div[4]/button").click()

        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='-100%']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='-100%']").send_keys("0")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='1,000%']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='1,000%']").send_keys("100")

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[5]/div/div/div[2]/div/div[5]/div[2]/div/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[5]/div/div/div[2]/div[1]/div[5]/button").click()

        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$0']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$0']").send_keys("10000000")

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[5]/div/div/div[2]/div/div[6]/div[2]/div/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[5]/div/div/div[2]/div[2]/button[1]").click()
