import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestGamestop:
    def test_gamestop_2705de3e(self):
        # self.driver.get("https://gamestop.com")
        time.sleep(6)

        # self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[1]/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[contains(@data-menucontent, 'Page-IncludeHeaderMenu')]//a[span[text()='Consoles & Hardware']]/span[text()='chevron_right']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[contains(@data-menucontent, 'Page-IncludeHeaderMenu')]//a[@data-name='Xbox One']//span[@data-catname2='Xbox One' and @data-catname1='Consoles & Hardware']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Filter']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: Consoles']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[5]/div[2]/ul[1]/li[1]/a[1]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[8]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[8]/div[2]/ul[1]/li[2]/a[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[9]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[9]/div[2]/ul[1]/li[2]/a[1]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[11]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[11]/div[2]/ul[1]/li[1]/a[1]").click()

        # NEED TO Wait for a few seconds otherwise the filter conditions will not be properly clicked and applied otherwise the test will pass even though some options are not selected
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//label[contains(text(), ' Microsoft')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[contains(text(), ' Color')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//label[contains(text(), '	White')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[contains(text(), ' Condition')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//label[contains(text(), '  Pre-Owned')]").click()
        time.sleep(1)

        # self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Done') and @type='button']").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//button[@id='sortby-dropdown']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low To High')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/a[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']//div[@id='product-grid-tile-grid-item']/div[1]/a[1]").click()
