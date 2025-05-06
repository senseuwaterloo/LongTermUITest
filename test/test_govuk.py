import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestGovUk:
    def test_govuk_593f78ad(self):
        self.driver.get("https://www.gov.uk/")

        self.driver.find_element(By.XPATH, "//div[@id='wrapper']//input[contains(@id, 'search-main-') and @name='q']").clear()
        self.driver.find_element(By.XPATH, "//div[@id='wrapper']//input[contains(@id, 'search-main-') and @name='q']").send_keys("benefits")

        self.driver.find_element(By.XPATH, "//div[@id='wrapper']//button[@enterkeyhint='search']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Check benefits and financial support you can get')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(.,'Check what you can get')]").click()

        self.driver.find_element(By.XPATH, "//label[@for='response-0']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()

        self.driver.find_element(By.XPATH, "//label[@for='response-0']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()

        self.driver.find_element(By.XPATH, "//label[@for='response-2']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()

        self.driver.find_element(By.XPATH, "//label[@for='response-1']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()

        self.driver.find_element(By.XPATH, "//label[@for='response-1']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()

        self.driver.find_element(By.XPATH, "//label[@for='response-1']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
