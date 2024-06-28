import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.mark.usefixtures("setup_class")
class TestAirbnb:
    
    def test_airbnb_4fa7cab9(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Anywhere')]").click()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").click()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").clear()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").send_keys("New York")
        self.driver.find_element(By.XPATH, "//div[@id='bigsearch-query-location-suggestion-0']/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel--tabs--0']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel--tabs--0']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stepper-adults']/button[2]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stepper-adults']/button[2]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[3]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='site-content']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/picture[1]/source[1]/source[1]/source[1]/source[1]/img[1]").click()
    
    def test_airbnb_cdf4d2ec(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Anywhere')]").click()
        self.driver.find_element(By.XPATH, "//button[@id='search-block-tab-EXPERIENCES']/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").clear()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").send_keys("portugal")
        self.driver.find_element(By.XPATH, "//div[@id='bigsearch-query-location-suggestion-0']/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stepper-adults']/button[2]/span[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stepper-children']/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[3]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='menuItemButton-host_language']/button[1]/span[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterItem-host_language-checkbox-experience_languages-1']/label[1]/div[1]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.ID, "filter-panel-save-button").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-menu-chip-group']/div[2]/div[1]/div[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterItem-experience_time_of_day-checkbox-experience_time_of_day-morning']/label[1]/div[1]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.ID, "filter-panel-save-button").click()
        self.driver.find_element(By.XPATH, "//div[@id='menuItemButton-toggleItem-taxonomy_quick_filter-Sports-Sports']/button[1]/span[1]/div[1]/span[1]").click()
    
    def test_airbnb_012446b3(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//div[@id='menuItemButton-toggleItem-ghost-platform-quick-filters-Cooking-Cooking']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='menuItemButton-date_picker']/button[1]/span[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-menu-chip-group']/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/section[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-menu-chip-group']/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[1]").click()
        self.driver.find_element(By.ID, "filter-panel-save-button").click()
        self.driver.find_element(By.XPATH, "//div[@id='menuItemButton-experience_group_size']/button[1]/span[1]/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "4-10 guests").click()
        self.driver.find_element(By.ID, "filter-panel-save-button").click()
    
    def test_airbnb_d070774f(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//div[@id='categoryScroller']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/label[3]/div[1]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Filters')]").click()
        self.driver.find_element(By.ID, "price_filter_min").clear()
        self.driver.find_element(By.ID, "price_filter_min").send_keys("200")
        self.driver.find_element(By.ID, "price_filter_max").clear()
        self.driver.find_element(By.ID, "price_filter_max").send_keys("400")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Show 664 stays')]").click()
    
    def test_airbnb_0b2f241e(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//div[@id='categoryScroller']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/label[5]/div[1]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Anywhere')]").click()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").clear()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").send_keys("India")
        self.driver.find_element(By.XPATH, "//div[@id='bigsearch-query-location-suggestion-1']/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[2]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "price_filter_max").click()
        self.driver.find_element(By.ID, "price_filter_max").clear()
        self.driver.find_element(By.ID, "price_filter_max").send_keys("99")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Show 1,000+ stays')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='site-content']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/picture[1]/source[1]/source[1]/source[1]/img[1]").click()
    
    def test_airbnb_102c50a4(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//div[@id='categoryScroller']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/label[1]/div[1]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "price_filter_max").clear()
        self.driver.find_element(By.ID, "price_filter_max").send_keys("500")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Show 684 stays')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='site-content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.ID, "name-list-input-save-to-list-modal").clear()
        self.driver.find_element(By.ID, "name-list-input-save-to-list-modal").send_keys("Togo")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Create')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='site-content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='loading-row-title']/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='site-content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='loading']/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    
    def test_airbnb_1267fbd8(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//div[@id='categoryScroller']/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]/span[1]/svg[1]/g[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='categoryScroller']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/label[13]/div[1]/span[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Any week')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel--tabs--0']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel--tabs--0']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[4]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stepper-adults']/button[2]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stepper-pets']/button[2]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stepper-pets']/button[2]/span[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[3]/button[1]/span[1]/span[1]").click()
    
    def test_airbnb_181e8206(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Anywhere')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='locationInspirationsSectionID']/div[1]/div[3]/div[1]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel--tabs--0']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel--tabs--0']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[7]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[2]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='categoryScroller']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/label[3]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "price_filter_max").clear()
        self.driver.find_element(By.ID, "price_filter_max").send_keys("1000")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Show 673 stays')]").click()
    
    def test_airbnb_a52774d2(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//div[@id='categoryScroller']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/label[4]/div[1]/span[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Anywhere')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='locationInspirationsSectionID']/div[1]/div[2]/div[1]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Any week')]").click()
        self.driver.find_element(By.ID, "tab--tabs--2").click()
        self.driver.find_element(By.ID, "flexible_trip_lengths-one_month").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stepper-adults']/button[2]/span[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stepper-adults']/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stepper-adults']/button[2]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[3]/button[1]/span[1]/span[1]").click()
    
    def test_airbnb_58394242(self):
        # self.driver.get("https://www.airbnb.com/")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Anywhere')]").click()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").clear()
        self.driver.find_element(By.ID, "bigsearch-query-location-input").send_keys("belo horizonte")
        self.driver.find_element(By.XPATH, "//div[@id='bigsearch-query-location-suggestion-0']/div[2]/div[1]").click()
        self.driver.find_element(By.ID, "tab--tabs--2").click()
        self.driver.find_element(By.ID, "flexible_trip_lengths-weekend_trip").click()
        self.driver.find_element(By.XPATH, "//div[@id='flexible_trip_dates-may']/button[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-tabpanel']/div[1]/div[5]/div[1]/div[2]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Filters')]").click()
        self.driver.find_element(By.ID, "price_filter_max").clear()
        self.driver.find_element(By.ID, "price_filter_max").send_keys("100")
        self.driver.find_element(By.ID, "filterItem--6576909515349354093-checkbox-room_types-Shared_room-row-title").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Show 71 stays')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='site-content']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]/path[1]").click()
    