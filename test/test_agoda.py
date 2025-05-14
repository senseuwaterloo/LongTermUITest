import time
import pytest
from selenium.webdriver.common.by import By
from browser_helper import calculate_dates, switch_to_new_tab_and_close_old

@pytest.mark.usefixtures('driver_session')
class TestAgoda:

    def test_agoda_e3486ac5(self):
        self.driver.get('https://agoda.com')
        self.driver.find_element(By.XPATH, "//li[@id='tab-home']/div[1]/div[1]").click()
        self.driver.find_element(By.ID, 'textInput').clear()
        self.driver.find_element(By.ID, 'textInput').send_keys('bali')
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[1]/div[2]/span[1]").click()
        (start_date_str, end_date_str) = calculate_dates(20, 24)
        self.driver.find_element(By.CSS_SELECTOR, f"span[data-selenium-date='{start_date_str}']").click()
        self.driver.find_element(By.CSS_SELECTOR, f"span[data-selenium-date='{end_date_str}']").click()
        self.driver.find_element(By.XPATH, "//button[@data-selenium='plus' and @data-element-name='occupancy-selector-panel-adult']").click()
        self.driver.find_element(By.XPATH, "//button[@data-selenium='plus' and @data-element-name='occupancy-selector-panel-children']").click()
        self.driver.find_element(By.XPATH, "//button[@data-selenium='plus' and @data-element-name='occupancy-selector-panel-children']").click()
        self.driver.find_element(By.XPATH, "//button[@data-element-name='occ-child-age-dropdown'][.//p[contains(text(),'Age of Child 1')]]").click()
        self.driver.find_element(By.XPATH, "//span[@data-testid='title' and text()='5 years old']").click()
        self.driver.find_element(By.XPATH, "//button[@data-element-name='occ-child-age-dropdown'][.//p[contains(text(),'Age of Child 2')]]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[@data-testid='title' and text()='12 years old']").click()
        self.driver.find_element(By.XPATH, "//*[@data-selenium='occupancyBox']").click()
        self.driver.find_element(By.XPATH, "//button[@data-selenium='searchButton']").click()
        switch_to_new_tab_and_close_old(self.driver)
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Homestay') and @data-selenium='filter-item-text']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Balcony/terrace') and @data-selenium='filter-item-text']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Breakfast included')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Double') and @data-selenium='filter-item-text']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@data-element-name='search-sort-price']").click()