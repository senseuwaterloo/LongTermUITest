import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestHealthgrades:
    def test_healthgrades_8aa9bddc(self):
        # self.driver.get("https://www.healthgrades.com/")
        # uiteststudy@gmail.com:Pass4Healthgrades2024!
        # self.driver.find_element(By.ID, "0.581095264485394-input-group").clear()
        # self.driver.find_element(By.ID, "0.581095264485394-input-group").send_keys("allergy")
        self.driver.find_element(By.ID, "homepage-search-input").clear()
        self.driver.find_element(By.ID, "homepage-search-input").send_keys("allergy")

        # self.driver.find_element(By.XPATH, "//form[@id='hero-search-bar']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "homepage-search-drawer-sugg-6").click()

        # self.driver.find_element(By.ID, "0.7644171572862428-input-group").clear()
        # self.driver.find_element(By.ID, "0.7644171572862428-input-group").send_keys("stamford")
        self.driver.find_element(By.ID, "synd-header-location-input").clear()
        self.driver.find_element(By.ID, "synd-header-location-input").send_keys("stamford")

        # self.driver.find_element(By.XPATH, "//div[@id='usearch-container']/main[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[contains(@id, 'synd-header-location-drawer-sugg-')]//span[contains(., 'Stamford,') and contains(., 'CT')]").click()

        self.driver.find_element(By.XPATH, "//button[@id='quick-filter--nearby']/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='standard-filter--rating']/span[1]").click()

        # self.driver.find_element(By.XPATH, "//form[@id='filter-bar']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-bar']/div[2]/div/div[1]/div[1]/div/div/button").click()

        self.driver.find_element(By.XPATH, "//form[@id='filter-bar']/div[1]/button[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='all-filters-modal']/section[1]/div[2]/div[1]/fieldset[3]/div[1]/div[1]/div[3]/label[1]/span[1]").click()
        # need to increase the distance to 100 to make sure there are schedules available
        self.driver.find_element(By.XPATH, "//label[@for='all-filters-distance-100']/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='all-filters-modal']/section[1]/div[2]/div[1]/fieldset[5]/div[1]/div[1]/div[4]/label[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//label[@for='all-filters-rating-5']/span[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='all-filters-modal']/section[1]/div[3]/button[2]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedule Now')]").click()
        schedule_now_btn = self.driver.find_element(By.XPATH, "//div[contains(@data-qa-target, 'pro-card-natural-')]//a[contains(text(),'Schedule Now')]")
        scroll_to_element(self.driver, schedule_now_btn)
        schedule_now_btn.click()
        # online appointment is disabled so skip the following steps
        # self.driver.find_element(By.ID, "input-9").click()
        # self.driver.find_element(By.XPATH, "//li[@role='button']").click()
        # self.driver.find_element(By.ID, "select_12").click()
        # self.driver.find_element(By.ID, "select_option_19").click()
        # self.driver.find_element(By.XPATH, "//li[contains(.,'11am')]").click()
        # self.driver.find_element(By.XPATH, "//span[contains(.,'Continue to Visit Details')]").click()
        # self.driver.find_element(By.XPATH, "//label[contains(.,'Me')]").click()
        # self.driver.find_element(By.XPATH, "//label[contains(.,'No')]").click()
        # self.driver.find_element(By.ID, "month").clear()
        # self.driver.find_element(By.ID, "month").send_keys("5")
        # self.driver.find_element(By.ID, "day").clear()
        # self.driver.find_element(By.ID, "day").send_keys("5")
        # self.driver.find_element(By.ID, "year").clear()
        # self.driver.find_element(By.ID, "year").send_keys("1995")
        # self.driver.find_element(By.ID, "comments").clear()
        # self.driver.find_element(By.ID, "comments").send_keys("none")
        # self.driver.find_element(By.XPATH, "//span[contains(.,'Continue to Contact Info')]").click()
    