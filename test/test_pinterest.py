import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestPinterest:
    def test_pinterest_70cb365b(self):
        self.driver.get("https://pinterest.com")

        self.driver.find_element(By.XPATH, "//div[@data-test-id='simple-login-button']/button").click()
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys("Pass4Pinterest2024!")
        self.driver.find_element(By.XPATH, "//div[@data-test-id='registerFormSubmitButton']/button").click()

        self.driver.find_element(By.NAME, "searchBoxInput").clear()
        self.driver.find_element(By.NAME, "searchBoxInput").send_keys("christian quotes")

        time.sleep(2)
        self.driver.find_element(By.NAME, "searchBoxInput").send_keys(Keys.RETURN)

        self.driver.back()

        self.driver.find_element(By.XPATH, "//div[@data-test-id='max-width-container']/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='closeup-action-bar-button']//button[@aria-label='More options']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()

        self.driver.back()

        self.driver.find_element(By.XPATH, "//div[@data-test-id='max-width-container']/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='closeup-action-bar-button']//button[@aria-label='More options']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()

        self.driver.back()

        self.driver.find_element(By.XPATH, "//div[@data-test-id='max-width-container']/div[1]/div[1]/div[3]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='closeup-action-bar-button']//button[@aria-label='More options']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()

        self.driver.back()

        self.driver.find_element(By.XPATH, "//div[@data-test-id='max-width-container']/div[1]/div[1]/div[4]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='closeup-action-bar-button']//button[@aria-label='More options']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()

        self.driver.back()

        self.driver.find_element(By.XPATH, "//div[@data-test-id='max-width-container']/div[1]/div[1]/div[5]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='closeup-action-bar-button']//button[@aria-label='More options']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()
