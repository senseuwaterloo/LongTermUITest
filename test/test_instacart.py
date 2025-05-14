import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import switch_to_new_tab_and_return_old


@pytest.mark.usefixtures("driver_session")
class TestInstacart:
    def test_instacart_10b2af14(self):
        self.driver.get("https://instacart.com")

        self.driver.find_element(By.XPATH, "//button[@data-testid='auth-buttons-login']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Continue with Google']").click()
        original_window = switch_to_new_tab_and_return_old(self.driver)
        self.driver.find_element(By.NAME, "identifier").clear()
        self.driver.find_element(By.NAME, "identifier").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
        self.driver.find_element(By.NAME, "Passwd").clear()
        self.driver.find_element(By.NAME, "Passwd").send_keys("UITestStudy2024")
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
        self.driver.switch_to.window(original_window)
        self.driver.find_element(By.XPATH, "//span[text()='No thanks']").click()

        self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div/div/span/button").click()

        self.driver.find_element(By.XPATH, "//span[text()='Your lists']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Create a list')]").click()

        self.driver.find_element(By.XPATH, "//div[text()='Choose a store (Required)']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Walgreens']").click()

        self.driver.find_element(By.ID, "title").clear()
        self.driver.find_element(By.ID, "title").send_keys("Walgreens")

        self.driver.find_element(By.XPATH, "//div[text()='Add a cover photo to your list']/following-sibling::div//ul//img").click()

        self.driver.find_element(By.XPATH, "//button[@data-testid='list-sticky-footer-cta-mobile']").click()

        self.driver.find_element(By.XPATH, "//button[@data-testid='item-search-bar-button']").click()

        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//input[@id='search-bar-input']").clear()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//input[@id='search-bar-input']").send_keys("personal care")
        self.driver.find_element(By.ID, "group-0-option-1").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//ul[1]/li[1]/div[1]/div[1]//div[@aria-label='select item']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//ul[1]/li[2]/div[1]/div[1]//div[@aria-label='select item']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//ul[1]/li[3]/div[1]/div[1]//div[@aria-label='select item']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//ul[1]/li[4]/div[1]/div[1]//div[@aria-label='select item']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Done']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Done editing list']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='optionIcon' and @aria-label='edit list']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='deleteButton']").click()

        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Delete this list and all its items?']]//span[text()='Delete list']").click()

        time.sleep(2)
