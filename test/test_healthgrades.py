import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("driver_session")
class TestHealthgrades:
    def test_healthgrades_8aa9bddc(self):
        self.driver.get("https://www.healthgrades.com/")

        self.driver.find_element(By.ID, "homepage-search-input").clear()
        self.driver.find_element(By.ID, "homepage-search-input").send_keys("allergy")

        self.driver.find_element(By.ID, "homepage-search-drawer-sugg-6").click()

        self.driver.find_element(By.ID, "synd-header-location-input").clear()
        self.driver.find_element(By.ID, "synd-header-location-input").send_keys("stamford")

        self.driver.find_element(By.XPATH, "//li[contains(@id, 'synd-header-location-drawer-sugg-')]//span[contains(., 'Stamford,') and contains(., 'CT')]").click()

        self.driver.find_element(By.XPATH, "//button[@id='quick-filter--nearby']/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='standard-filter--rating']/span[1]").click()

        self.driver.find_element(By.XPATH, "//form[@id='filter-bar']/div[2]/div/div[1]/div[1]/div/div/button").click()

        self.driver.find_element(By.XPATH, "//form[@id='filter-bar']/div[1]/button[1]/span[1]").click()

        self.driver.find_element(By.XPATH, "//label[@for='all-filters-distance-100']/span[1]").click()

        self.driver.find_element(By.XPATH, "//label[@for='all-filters-rating-5']/span[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='all-filters-modal']/section[1]/div[3]/button[2]").click()

        schedule_now_btn = self.driver.find_element(By.XPATH, "//div[contains(@data-qa-target, 'pro-card-natural-')]//a[contains(text(),'Schedule Now')]")
        scroll_to_element(self.driver, schedule_now_btn)
        schedule_now_btn.click()
    