import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestFinanceGoogle:
    def test_financegoogle_d78d07bf(self):
        # uiteststudy@gmail.com:UITestStudy2024
        # self.driver.get("https://www.google.com/finance/")
        # add extra login steps
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
        self.driver.find_element(By.NAME, "identifier").click()
        self.driver.find_element(By.NAME, "identifier").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//button[contains(., 'Next') and @type='button']").click()
        self.driver.find_element(By.NAME, "Passwd").click()
        self.driver.find_element(By.NAME, "Passwd").send_keys("UITestStudy2024")
        self.driver.find_element(By.XPATH, "//button[contains(., 'Next') and @type='button']").click()

        # self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/div[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[5]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='New portfolio']").click()

        # self.driver.find_element(By.ID, "c236").clear()
        # self.driver.find_element(By.ID, "c236").send_keys("AI")
        # very dynamic id and attributes, use neighbor text
        # selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable, click too fast need to wait for a few seconds
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Portfolio name']/ancestor::label//input").clear()
        self.driver.find_element(By.XPATH, "//span[text()='Portfolio name']/ancestor::label//input").send_keys("AI")

        # self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(., 'Save') and @data-mdc-dialog-action='ok']").click()

        # self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/c-wiz[1]/div[2]/div[1]/div[2]/div[1]/div[1]/c-wiz[1]/div[1]/div[1]/div[1]/div[1]/div[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Add investments']").click()

        # self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        # self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("Artificial")
        # selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable, click too fast need to wait for a few seconds
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@value='Type an investment name or symbol']/following-sibling::input").clear()
        self.driver.find_element(By.XPATH, "//input[@value='Type an investment name or symbol']/following-sibling::input").send_keys("Artificial")

        # self.driver.find_element(By.XPATH, "//div[@id='nngdp8850']/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@role='option' and @data-display-name='Artificial Intelligence Tech Solutns Inc']").click()

        # self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/i[1]").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Add one share']").click()

        # self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(., 'Save') and @data-mdc-dialog-action='ok']").click()

        # delete the data for next test run
        self.driver.find_element(By.XPATH, "//button[@aria-label='More menu options']/i").click()
        self.driver.find_element(By.XPATH, "//li[contains(., 'Delete') and @role='menuitem' and @aria-label='Delete']").click()
        self.driver.find_element(By.XPATH, "//button[contains(., 'Delete') and @data-mdc-dialog-action='ok']").click()
