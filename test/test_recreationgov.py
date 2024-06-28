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
class TestRecreationGov:
    
    def test_recreationgov_a3cacfe8(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.XPATH, "//button[@id='tabs-button-3']/div[1]").click()
        self.driver.find_element(By.ID, "hero-permits-input").clear()
        self.driver.find_element(By.ID, "hero-permits-input").send_keys("Brooks Camp")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-permits-input-section-0-item-0']/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.ID, "date-picker").clear()
        self.driver.find_element(By.ID, "date-picker").send_keys("05/22/2023")
        self.driver.find_element(By.XPATH, "//div[@id='page-content']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='guest-counter-QuotaUsageByMemberDaily']/span[1]").click()
        self.driver.find_element(By.ID, "guest-counter-QuotaUsageByMemberDaily-number-field-People").clear()
        self.driver.find_element(By.ID, "guest-counter-QuotaUsageByMemberDaily-number-field-People").send_keys("4")
        self.driver.find_element(By.XPATH, "//div[@id='guest-counter-QuotaUsageByMemberDaily-popup']/div[1]/div[2]/div[1]/button[1]").click()
    
    def test_recreationgov_a8e59039(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.XPATH, "//div[@id='page-content']/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "map-filter-input").clear()
        self.driver.find_element(By.ID, "map-filter-input").send_keys("Yosemite")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Yosemite National Park')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[5]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[2]/tr[1]/td[4]/ul[1]/div[1]/div[1]/button[2]/span[1]/svg[1]").click()
        self.driver.find_element(By.ID, "holder-zip-code-1").clear()
        self.driver.find_element(By.ID, "holder-zip-code-1").send_keys("94587")
        self.driver.find_element(By.ID, "start-date-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='container-start-date-1']/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[6]/td[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "vehicle-license-1").clear()
        self.driver.find_element(By.ID, "vehicle-license-1").send_keys("12345")
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[7]/section[1]/div[3]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[8]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
    
    def test_recreationgov_3960e140(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-0']/div[2]/div[1]/div[4]/button[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "search-filters-search-input").clear()
        self.driver.find_element(By.ID, "search-filters-search-input").send_keys("tennessee")
        self.driver.find_element(By.ID, "search-filters-search-input").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-autowhatever-what']/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-what-section-1-item-0']/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "occupants").clear()
        self.driver.find_element(By.ID, "occupants").send_keys("20")
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[3]/div[2]/div[14]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
    
    def test_recreationgov_502a9d95(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.ID, "hero-search-input").clear()
        self.driver.find_element(By.ID, "hero-search-input").send_keys("Albion Basin")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-search-input-section-0-item-0']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sticky-table-wrap']/div[1]/div[4]/div[1]/button[2]").click()
    
    def test_recreationgov_63be6edd(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.ID, "hero-search-input").clear()
        self.driver.find_element(By.ID, "hero-search-input").send_keys("Arizona")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-search-input-section-1-item-0']/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[2]/div[7]/div[1]/div[5]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "testhook-apply").click()
    
    def test_recreationgov_79f72a57(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.XPATH, "//button[@id='tabs-button-3']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-3']/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "search-filters-search-input").clear()
        self.driver.find_element(By.ID, "search-filters-search-input").send_keys("Bryce Canyon National Park")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-what-section-0-item-1']/div[1]/div[2]/span[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
    
    def test_recreationgov_81c87171(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.ID, "hero-search-input").clear()
        self.driver.find_element(By.ID, "hero-search-input").send_keys("Allecy Creek Camp")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-search-input-section-0-item-0']/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sticky-table-wrap']/div[1]/div[4]/div[1]/button[2]").click()
    
    def test_recreationgov_986bfa5e(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.ID, "hero-camping-search-input").clear()
        self.driver.find_element(By.ID, "hero-camping-search-input").send_keys("Illinois")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-camping-search-input-section-1-item-0']/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='homepage-search-options']/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='homepage-search-options']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='homepage-search-options-popup']/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "startDate").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-1']/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[7]").click()
        self.driver.find_element(By.ID, "endDate").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-1']/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.ID, "endDate").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-1']/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-1']/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "search-sort-dropdown").clear()
        self.driver.find_element(By.ID, "search-sort-dropdown").select("Price")
        self.driver.find_element(By.ID, "search-sort-dropdown").clear()
        self.driver.find_element(By.ID, "search-sort-dropdown").select("Available")
    
    def test_recreationgov_a2c9ea94(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.ID, "hero-search-input").clear()
        self.driver.find_element(By.ID, "hero-search-input").send_keys("New York")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-search-input-section-1-item-0']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "testhook-apply").click()
        self.driver.find_element(By.ID, "search-sort-dropdown").clear()
        self.driver.find_element(By.ID, "search-sort-dropdown").select("Mobile Coverage")
    
    def test_recreationgov_d2528fed(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.XPATH, "//button[@id='tabs-button-2']/div[1]").click()
        self.driver.find_element(By.ID, "hero-tickets-search-input").clear()
        self.driver.find_element(By.ID, "hero-tickets-search-input").send_keys("Washington")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-tickets-search-input-section-1-item-1']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-2']/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "startDate").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[5]/td[4]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[9]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[2]/div[2]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "testhook-apply").click()
        self.driver.find_element(By.ID, "search-sort-dropdown").clear()
        self.driver.find_element(By.ID, "search-sort-dropdown").select("Available")
    
    def test_recreationgov_d5602fc7(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-0']/div[2]/div[1]/div[3]/button[1]/div[1]/div[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[2]/div[2]/div[1]/div[9]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "search-sort-dropdown").clear()
        self.driver.find_element(By.ID, "search-sort-dropdown").select("Price")
        self.driver.find_element(By.XPATH, "//div[@id='rec-card-233396_permit']/div[1]/a[1]/div[2]/h2[1]").click()
    
    def test_recreationgov_de69733d(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-0']/div[2]/div[1]/div[4]/button[1]/div[1]/div[1]/h2[1]").click()
        self.driver.find_element(By.ID, "search-filters-search-input").clear()
        self.driver.find_element(By.ID, "search-filters-search-input").send_keys("nashville")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-what-section-1-item-0']/div[1]/div[2]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[3]/div[2]/div[10]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
    
    def test_recreationgov_e677b812(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.ID, "hero-search-input").clear()
        self.driver.find_element(By.ID, "hero-search-input").send_keys("Alpine Ridge")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-search-input-section-0-item-0']/div[1]/div[2]/span[3]").click()
        self.driver.find_element(By.XPATH, "//button[@id='tabs-button-4']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rating-review-inventory-review-section']/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "reviews-sort").clear()
        self.driver.find_element(By.ID, "reviews-sort").select("Sort by  Most Helpful")
    
    def test_recreationgov_e719ca92(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.XPATH, "//button[@id='tabs-button-1']/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='homepage-search-options']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='homepage-search-options-popup']/div[1]/div[1]/div[1]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='homepage-search-options-popup']/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-content']/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "hero-camping-search-input").clear()
        self.driver.find_element(By.ID, "hero-camping-search-input").send_keys("Kansas")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-camping-search-input-section-1-item-0']/div[1]").click()
        self.driver.find_element(By.ID, "startDate").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-1']/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-1']/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-1']/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "search-sort-dropdown").clear()
        self.driver.find_element(By.ID, "search-sort-dropdown").select("Rating")
    
    def test_recreationgov_fafc3874(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.ID, "hero-search-input").clear()
        self.driver.find_element(By.ID, "hero-search-input").send_keys("Brooken Cove")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-search-input-section-0-item-0']/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='tabs-button-4']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rating-review-inventory-review-section']/div[1]/div[2]/div[2]/div[1]/button[1]").click()
    
    def test_recreationgov_fd600e18(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.ID, "hero-search-input").clear()
        self.driver.find_element(By.ID, "hero-search-input").send_keys("Alley Spring")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-search-input-section-0-item-0']/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//button[@id='tabs-button-2']/div[1]").click()
    
    def test_recreationgov_c72c2a37(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-0']/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[2]/div[2]/div[1]/div[4]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[2]/div[6]/div[1]/div[4]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
    
    def test_recreationgov_c7f38343(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.ID, "hero-search-input").clear()
        self.driver.find_element(By.ID, "hero-search-input").send_keys("Oregon")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-search-input-section-1-item-1']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[5]/div[2]/div[15]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[5]/div[2]/div[5]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "testhook-apply").click()
    
    def test_recreationgov_cde403e5(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.XPATH, "//div[@id='page-content']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-content']/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/svg[1]/g[1]/path[2]").click()
    
    def test_recreationgov_cee31d7c(self):
        # self.driver.get("https://www.recreation.gov/")
        self.driver.find_element(By.ID, "hero-search-input").clear()
        self.driver.find_element(By.ID, "hero-search-input").send_keys("campsites")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-search-input-section-0-item-4']/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.ID, "campground-start-date-calendar").clear()
        self.driver.find_element(By.ID, "campground-start-date-calendar").send_keys("May 22, 2023")
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-0']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[2]/div[1]").click()
        self.driver.find_element(By.ID, "campground-end-date-calendar").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-0']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[4]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sticky-table-wrap']/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='legend-icon-dropdown-popup']/div[1]/div[1]/div[1]/section[1]/div[4]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='legend-icon-dropdown-popup']/div[1]/div[1]/div[1]/section[1]/div[11]/div[1]/div[4]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='legend-icon-dropdown-popup']/div[1]/div[2]/div[1]/button[1]").click()
    