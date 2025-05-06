import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestCabelas:
    def test_cabelas_3f62b47b(self):
        self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "departmentButton_3074457345616967316").click()
        self.driver.find_element(By.ID, "moreLink_3074457345616967316_3074457345616967320").click()
        self.driver.find_element(By.XPATH, "//label[@for='Ice Fishing']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Power']").click()
        self.driver.find_element(By.XPATH, "//label[@for='Medium Light']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Length']").click()
        self.driver.find_element(By.XPATH, "//label[@for='32\"']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Price']").click()
        self.driver.find_element(By.XPATH, "//label[@for='Less than $100']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Average Ratings']").click()
        self.driver.find_element(By.XPATH, "//span[@aria-label='4 stars out of undefined reviews']").click()

        first_candidate = self.driver.find_element(By.XPATH, "//div[@id='main']/div/div/div[1]/div[1]/a/div/img")
        scroll_to_element(self.driver, first_candidate)
        first_candidate.click()
