import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestBestbuy:
    def test_bestbuy_84c1847c(self):
        self.driver.get("https://www.bestbuy.com/?intl=nosplash")
        self.driver.find_element(By.ID, "gh-search-input").clear()

        self.driver.find_element(By.ID, "gh-search-input").send_keys("iPhone 15")
        self.driver.find_element(By.XPATH, "//div[@data-testid='SuggestedSearches']/div[1]/div[2]/div/div/ul/li/a").click()
        pre_owned_checkbox = self.driver.find_element(By.ID, "condition_facet-Pre-Owned-1")
        scroll_to_element(self.driver, pre_owned_checkbox)
        pre_owned_checkbox.click()

        self.driver.find_element(By.XPATH, "//div[@id='main-results']/ol/li[2]/div/div/div/div/div/div[3]/div[3]/div/div/div/div/div/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Go to Cart')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Check Trade-In Value')]").click()
        time.sleep(1)
        brand_dropdown_element = self.driver.find_element(By.ID, "brand")
        brand_select = Select(brand_dropdown_element)
        brand_select.select_by_value('Apple')
        time.sleep(1)
        model_dropdown_element = self.driver.find_element(By.ID, "modelFamily")
        model_select = Select(model_dropdown_element)
        model_select.select_by_value('Apple iPhone 14 Pro')
        time.sleep(1)
        color_dropdown_element = self.driver.find_element(By.ID, "color")
        color_select = Select(color_dropdown_element)
        color_select.select_by_value('Space Black')
        time.sleep(1)
        carrier_dropdown_element = self.driver.find_element(By.ID, "carrier")
        carrier_select = Select(carrier_dropdown_element)
        carrier_select.select_by_value('Verizon')
        time.sleep(1)
        memory_dropdown_element = self.driver.find_element(By.ID, "internalMemory")
        memory_select = Select(memory_dropdown_element)
        memory_select.select_by_value('256 gigabytes')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@data-testid='trade-in-search-form-search-button']").click()
        self.driver.find_element(By.XPATH, "//span[@data-testid='trade-in-condition-label-No']").click()
        self.driver.find_element(By.XPATH, "//span[@data-testid='trade-in-condition-label-Good']").click()

        self.driver.find_element(By.XPATH, "//span[contains(text(),'Add to Cart')]").click()
    