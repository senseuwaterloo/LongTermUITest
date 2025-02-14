import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestEbay:
    def test_ebay_4a0bd619(self):
        # self.driver.get("https://ebay.com")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Collectibles')]").click()
        # above locator can't uniquely locate the target element
        self.driver.find_element(By.XPATH, "//div[@id='vl-flyout-nav']/ul/li[4]/a").click()

        # self.driver.find_element(By.ID, "s0-16-12-0-1[2]-0-0-27[0]-0-toggle-button").click()
        # dynamic id in above locator
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Antiques')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Furniture')]").click()
        # a change to span
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Furniture')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Chairs')]").click()
        # above locator can't uniquely locate the target element
        self.driver.find_element(By.XPATH, "//a[text()='Chairs']").click()

        # self.driver.find_element(By.XPATH, "//span[@id='nid-y88-1']/button[1]/span[1]").click()
        # # dynamic id in above locator
        self.driver.find_element(By.XPATH, "//button[@aria-label='Sort: Best Match']").click()

        # self.driver.find_element(By.XPATH, "//ul[@id='s0-27_1-9-0-1[0]-0-0-6-4-13-15-content-menu']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@class='fake-menu__items']/li[3]/a/span").click()

        # self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/button[1]").click()
        # directly use //span contains will lead to click intercept error
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'filter-button') and contains(., 'Condition')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/div[1]/ul[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[text()='Used']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'filter-button') and contains(., 'Style')]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/div[1]/ul[1]/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[text()='French']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[4]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'filter-button') and contains(., 'Material')]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[4]-flyout']/div[1]/ul[1]/li[11]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[text()='Oak']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'filter-button') and contains(., 'Time Period Manufactured')]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/div[1]/ul[1]/li[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//label[text()='Pre-1800']").click()
