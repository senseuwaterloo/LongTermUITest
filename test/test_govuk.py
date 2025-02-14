import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestGovUk:
    def test_govuk_593f78ad(self):
        # self.driver.get("https://www.gov.uk/")
        # self.driver.find_element(By.ID, "search-main-6ddf766d").clear()
        # self.driver.find_element(By.ID, "search-main-6ddf766d").send_keys("benefits")
        self.driver.find_element(By.XPATH, "//div[@id='wrapper']//input[contains(@id, 'search-main-') and @name='q']").clear()
        self.driver.find_element(By.XPATH, "//div[@id='wrapper']//input[contains(@id, 'search-main-') and @name='q']").send_keys("benefits")

        # self.driver.find_element(By.XPATH, "//main[@id='content']/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='wrapper']//button[@enterkeyhint='search']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Check benefits and financial support you can get')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Check what you can get')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(.,'Check what you can get')]").click()

        # somehow wait for the radio button to be clickable will timeout and therefore we wait for the label
        # self.driver.find_element(By.ID, "response-0").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-0']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
        # self.driver.find_element(By.ID, "response-0").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-0']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
        # self.driver.find_element(By.ID, "response-2").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-2']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
        # self.driver.find_element(By.ID, "response-1").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-1']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
        # self.driver.find_element(By.ID, "response-1").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-1']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
        # self.driver.find_element(By.ID, "response-1").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-1']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
