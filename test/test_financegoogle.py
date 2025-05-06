import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestFinanceGoogle:
    def test_financegoogle_d78d07bf(self):
        self.driver.get("https://www.google.com/finance/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
        self.driver.find_element(By.NAME, "identifier").click()
        self.driver.find_element(By.NAME, "identifier").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//button[contains(., 'Next') and @type='button']").click()
        self.driver.find_element(By.NAME, "Passwd").click()
        self.driver.find_element(By.NAME, "Passwd").send_keys("UITestStudy2024")
        self.driver.find_element(By.XPATH, "//button[contains(., 'Next') and @type='button']").click()

        self.driver.find_element(By.XPATH, "//span[text()='New portfolio']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Portfolio name']/ancestor::label//input").clear()
        self.driver.find_element(By.XPATH, "//span[text()='Portfolio name']/ancestor::label//input").send_keys("AI")

        self.driver.find_element(By.XPATH, "//button[contains(., 'Save') and @data-mdc-dialog-action='ok']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Add investments']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@value='Type an investment name or symbol']/following-sibling::input").clear()
        self.driver.find_element(By.XPATH, "//input[@value='Type an investment name or symbol']/following-sibling::input").send_keys("Artificial")

        self.driver.find_element(By.XPATH, "//div[@role='option' and @data-display-name='Artificial Intelligence Tech Solutns Inc']").click()

        self.driver.find_element(By.XPATH, "//button[@aria-label='Add one share']").click()

        self.driver.find_element(By.XPATH, "//button[contains(., 'Save') and @data-mdc-dialog-action='ok']").click()

        self.driver.find_element(By.XPATH, "//button[@aria-label='More menu options']/i").click()
        self.driver.find_element(By.XPATH, "//li[contains(., 'Delete') and @role='menuitem' and @aria-label='Delete']").click()
        self.driver.find_element(By.XPATH, "//button[contains(., 'Delete') and @data-mdc-dialog-action='ok']").click()
