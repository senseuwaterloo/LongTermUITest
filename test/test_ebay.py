import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestEbay:
    def test_ebay_4a0bd619(self):
        self.driver.get("https://ebay.com")

        self.driver.find_element(By.XPATH, "//div[@id='vl-flyout-nav']/ul/li[4]/a").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Antiques')]").click()

        self.driver.find_element(By.XPATH, "//span[contains(text(),'Furniture')]").click()

        self.driver.find_element(By.XPATH, "//a[text()='Chairs']").click()

        self.driver.find_element(By.XPATH, "//button[@aria-label='Sort: Best Match']").click()

        self.driver.find_element(By.XPATH, "//ul[@class='fake-menu__items']/li[3]/a/span").click()

        self.driver.find_element(By.XPATH, "//button[contains(@class, 'filter-button') and contains(., 'Condition')]").click()

        self.driver.find_element(By.XPATH, "//label[text()='Used']").click()

        self.driver.find_element(By.XPATH, "//button[contains(@class, 'filter-button') and contains(., 'Style')]").click()

        self.driver.find_element(By.XPATH, "//label[text()='French']").click()

        self.driver.find_element(By.XPATH, "//button[contains(@class, 'filter-button') and contains(., 'Material')]").click()

        self.driver.find_element(By.XPATH, "//label[text()='Oak']").click()

        self.driver.find_element(By.XPATH, "//button[contains(@class, 'filter-button') and contains(., 'Time Period Manufactured')]").click()

        self.driver.find_element(By.XPATH, "//label[text()='Pre-1800']").click()
