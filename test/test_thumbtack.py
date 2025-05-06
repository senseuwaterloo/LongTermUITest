import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestThumbtack:
    def test_thumbtack_5a55aaa5(self):
        self.driver.get("https://www.thumbtack.com/")

        self.driver.find_element(By.XPATH, "//input[@aria-label='Search on Thumbtack']").clear()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Search on Thumbtack']").send_keys("Phone or Tablet Repair")

        self.driver.find_element(By.NAME, "zip_code").clear()
        self.driver.find_element(By.NAME, "zip_code").send_keys("89116")

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Search' and @type='button' and text()='Search']").click()

        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[text()='iPad mini']").click()
        self.driver.find_element(By.XPATH, "//section//div[text()='Water damage']").click()

        self.driver.find_element(By.XPATH, "//div[@data-testid='pro-list-result-price-info']").click()

        self.driver.find_element(By.XPATH, "//div[@data-testid='request-flow-step--active']//button[@type='submit' and ./span[text()='Next']]").click()

        self.driver.find_element(By.XPATH, "//span[text()='My home, venue, etc.']").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='request-flow-step--active']//button[@type='submit' and ./span[text()='Next']]").click()

        self.driver.find_element(By.XPATH, "//span[text()='Flexible on timeline']").click()

        self.driver.find_element(By.XPATH, "//textarea[@data-test='request-flow-text-box']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@data-test='request-flow-text-box']").send_keys("not turning on")
        self.driver.find_element(By.XPATH, "//div[@data-testid='request-flow-step--active']//button[@type='submit' and ./span[text()='Next']]").click()

        self.driver.find_element(By.XPATH, "//input[@data-test='request-flow-text-box']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-test='request-flow-text-box']").send_keys("joe@joebloggs.com")
        self.driver.find_element(By.XPATH, "//div[@data-testid='request-flow-step--active']//button[@type='submit' and ./span[text()='Next']]").click()

        self.driver.find_element(By.XPATH, "//input[@data-test='request-flow-text-box' and @type='tel']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-test='request-flow-text-box' and @type='tel']").send_keys("1239990000")
        self.driver.find_element(By.XPATH, "//div[@data-testid='request-flow-step--active']//button[@type='button' and ./span[text()='Back']]").click()
