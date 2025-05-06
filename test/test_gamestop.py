import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestGamestop:
    def test_gamestop_2705de3e(self):
        self.driver.get("https://gamestop.com")
        time.sleep(6)

        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[1]/button").click()

        self.driver.find_element(By.XPATH, "//nav[contains(@data-menucontent, 'Page-IncludeHeaderMenu')]//a[span[text()='Consoles & Hardware']]/span[text()='chevron_right']").click()

        self.driver.find_element(By.XPATH, "//nav[contains(@data-menucontent, 'Page-IncludeHeaderMenu')]//a[@data-name='Xbox One']//span[@data-catname2='Xbox One' and @data-catname1='Consoles & Hardware']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Filter']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: Consoles']").click()

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

        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Done') and @type='button']").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//button[@id='sortby-dropdown']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low To High')]").click()

        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']//div[@id='product-grid-tile-grid-item']/div[1]/a[1]").click()
