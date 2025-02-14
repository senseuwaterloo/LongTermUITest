import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestAccuweather:
    def test_accuweather_8cfafcc6(self):
        # self.driver.get("https://www.accuweather.com/")
        # TODO

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/svg[1]").click()
        # can't find svg with xpath
        self.driver.find_element(By.CSS_SELECTOR, "body > div > div[class*='page-hero hero-'] > div[class*='basic-header'] > div.header-outer > div > div > svg.hamburger-button.icon-hamburger").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Health & Activities')]").click()

        # self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("salt lake city")
        # placeholder changed
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Address, City or Zip Code']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Address, City or Zip Code']").send_keys("salt lake city")

        # self.driver.find_element(By.XPATH, "//div[contains(.,'Salt Lake City, UT, US')]").click()
        # added <p> inside <div>
        self.driver.find_element(By.XPATH, "//div[p[@class='search-bar-result__long-name' and text()='Salt Lake City, UT US']]").click()

        self.driver.find_element(By.XPATH, "//span[contains(.,'Health & Activities')]").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[3]/a[5]/div[2]").click()
        # avoid using fragile absolute xpath
        self.driver.find_element(By.XPATH, "//div[contains(.,'Migraine')]").click()
    