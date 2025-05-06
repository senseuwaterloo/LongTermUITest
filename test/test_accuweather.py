import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestAccuweather:
    def test_accuweather_8cfafcc6(self):
        self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//*[@id='privacy-policy-banner']/div/div").click()
        self.driver.find_element(By.CSS_SELECTOR, "body > div > div[class*='page-hero hero-'] > div[class*='basic-header'] > div.header-outer > div > div > svg.hamburger-button.icon-hamburger").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Health & Activities')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Address, City or Zip Code']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Address, City or Zip Code']").send_keys("salt lake city")
        self.driver.find_element(By.XPATH, "//div[p[@class='search-bar-result__long-name' and text()='Salt Lake City, UT US']]").click()

        self.driver.find_element(By.XPATH, "//span[contains(.,'Health & Activities')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Migraine')]").click()
    