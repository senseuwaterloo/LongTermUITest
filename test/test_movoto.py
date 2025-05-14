import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import switch_to_new_tab


@pytest.mark.usefixtures("driver_session")
class TestMovoto:
    def test_movoto_d6fe3275(self):
        self.driver.get("https://movoto.com")

        self.driver.find_element(By.XPATH, "//a[@role='button' and text()='Sign In']").click()
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("Pass4Movoto!")
        self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Continue with Email']").click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH, "//a[@class='dialog-close' and @comp='mvtHotleadForm']") is not None:
            self.driver.find_element(By.XPATH, "//a[@class='dialog-close' and @comp='mvtHotleadForm']").click()

        self.driver.find_element(By.XPATH, "//button[text()='Buy']").click()
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, ".mvt-searchbox__input > input").clear()
        self.driver.find_element(By.CSS_SELECTOR, ".mvt-searchbox__input > input").send_keys("Huntsville, AL")

        time.sleep(2)

        time.sleep(2)
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.XPATH, "//button[@role='button' and @aria-label='Search']/i[@title='Search']").get_native_element())

        time.sleep(3)

        self.driver.find_element(By.ID, "btnFilter").click()

        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[1]/input").click()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[1]/input").clear()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[1]/input").send_keys("150000")
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[2]/input").click()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[2]/input").clear()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[2]/input").send_keys("300000")

        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/div/label[5]").click()

        self.driver.find_element(By.XPATH, "//div[@id='container']/div[5]/div[3]/button[2]").click()

        self.driver.find_element(By.XPATH, "//div[@comp='searchSort']/button[1]").click()

        self.driver.find_element(By.XPATH, "//a[@role='button' and ./span[text()='Price Low']]").click()

        self.driver.find_element(By.XPATH, "//div[@comp='searchGrid']/div[1]/div[1]/div[2]/div[1]").click()
        switch_to_new_tab(self.driver)

        self.driver.find_element(By.XPATH, "//section[@id='openHousePanel']/div[1]/ul[1]/li[1]/a[1]/span[1]").click()

        self.driver.find_element(By.XPATH, "//div[@class='dialog-body']//div[@class='mvt-shifter-list' and @data-role='scroller']/div[3]/button[@class='btn-canlendar' and ./span[3]]").click()
