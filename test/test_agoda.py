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
class TestAgoda:
    
    def test_agoda_4e065fe4(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Phuket Hotels')]").click()
        self.driver.find_element(By.XPATH, "//span[@role='button' and @data-selenium='calendar-next-month-button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[2]/div[5]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[1]/div[4]/ul[1]/li[5]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-bar']/div[1]/a[3]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-bar']/div[1]/a[3]/div[2]/ul[1]/li[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[2]/div[2]/ul[1]/li[2]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[6]/div[2]/ul[1]/li[3]/span[1]/span[1]/span[1]").click()
    
    def test_agoda_c0a27903(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.XPATH, "//header[@id='page-header']/section[1]/div[1]/nav[1]/div[2]/div[1]/ul[1]/li[5]/div[1]/div[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[1]/div[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[1]/div[1]").send_keys("New Delhi")
        self.driver.find_element(By.XPATH, "//li[@data-selenium='autosuggest-item']").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[3]/div[6]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/button[1]/span[1]").click()
    
    def test_agoda_c614be5b(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.XPATH, "//li[@id='tab-flight-tab']/svg[1]/path[1]").click()
        self.driver.find_element(By.ID, "flight-origin-search-input").clear()
        self.driver.find_element(By.ID, "flight-origin-search-input").send_keys("Belo Horizonte")
        self.driver.find_element(By.XPATH, "//span[@data-selenium='suggestion-text']").click()
        self.driver.find_element(By.ID, "flight-destination-search-input").clear()
        self.driver.find_element(By.ID, "flight-destination-search-input").send_keys("Buenos Aires")
        self.driver.find_element(By.XPATH, "//span[@data-selenium='suggestion-text']").click()
        self.driver.find_element(By.XPATH, "//div[@id='dateSelector-departure']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[5]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabpanel-flight-tab']/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabpanel-flight-tab']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
    
    def test_agoda_fca09c13(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.ID, "textInput").clear()
        self.driver.find_element(By.ID, "textInput").send_keys("Tokyo")
        self.driver.find_element(By.XPATH, "//li[@role='option' and @data-selenium='autosuggest-item']").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[3]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[5]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[3]/div[2]/div[3]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-bar']/div[1]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//h3[@data-selenium='hotel-name']").click()
    
    def test_agoda_fe6b5531(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.XPATH, "//li[@id='tab-flight-tab']/svg[1]").click()
        self.driver.find_element(By.ID, "flight-origin-search-input").clear()
        self.driver.find_element(By.ID, "flight-origin-search-input").send_keys("London")
        self.driver.find_element(By.XPATH, "//span[@data-selenium='suggestion-text']").click()
        self.driver.find_element(By.ID, "flight-destination-search-input").clear()
        self.driver.find_element(By.ID, "flight-destination-search-input").send_keys("New York")
        self.driver.find_element(By.XPATH, "//span[@data-selenium='suggestion-text']").click()
        self.driver.find_element(By.XPATH, "//div[@id='dateSelector-departure']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabpanel-flight-tab']/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='agoda-spa']/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Cheapest first')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='agoda-spa']/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='agoda-spa']/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[4]/button[1]/div[1]").click()
    
    def test_agoda_7a698566(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.ID, "textInput").clear()
        self.driver.find_element(By.ID, "textInput").send_keys("Tokyo")
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[5]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[7]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[3]/div[2]/div[3]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='4,450' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='4,450' and @type='text']").send_keys("500")
    
    def test_agoda_8c5ccffa(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.XPATH, "//header[@id='page-header']/section[1]/div[1]/nav[1]/div[2]/div[1]/ul[1]/li[4]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='LTO' and @type='checkbox']").click()
    
    def test_agoda_9a5aa299(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.ID, "textInput").clear()
        self.driver.find_element(By.ID, "textInput").send_keys("mumbai")
        self.driver.find_element(By.XPATH, "//span[@data-selenium='suggestion-text-highlight']").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[3]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-box']/div[1]/div[1]/div[1]/div[3]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-box']/div[1]/div[1]/div[1]/div[3]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-bar']/div[1]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[1]/div[4]/ul[1]/li[1]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[5]/div[2]/ul[1]/li[2]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[2]/div[2]/ul[1]/li[1]/span[1]/span[1]/span[1]").click()
    
    def test_agoda_e3486ac5(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.ID, "textInput").clear()
        self.driver.find_element(By.ID, "textInput").send_keys("bali")
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[6]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[1]/div[2]/div[3]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[2]/div[2]/div[3]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//select[@data-selenium='dropdownInput']").clear()
        self.driver.find_element(By.XPATH, "//select[@data-selenium='dropdownInput']").select("3")
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[2]/div[2]/div[3]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[2]/ul[1]/div[2]/li[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[2]/ul[1]/div[2]/li[1]/div[1]/select[1]").select("5")
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[2]/div[2]/div[3]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[2]/ul[1]/div[3]/li[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[2]/ul[1]/div[3]/li[1]/div[1]/select[1]").select("8")
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[2]/div[2]/div[3]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[2]/ul[1]/div[4]/li[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[2]/ul[1]/div[4]/li[1]/div[1]/select[1]").select("12")
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[1]/div[4]/ul[1]/li[5]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[3]/div[2]/ul[1]/li[6]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[11]/div[2]/ul[1]/li[4]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[9]/div[2]/ul[1]/li[1]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-bar']/div[1]/a[2]/span[1]").click()
    
    def test_agoda_fbe9f625(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.XPATH, "//li[@id='tab-flight-tab']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabpanel-flight-tab']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.ID, "flight-origin-search-input").clear()
        self.driver.find_element(By.ID, "flight-origin-search-input").send_keys("MUMBAI")
        self.driver.find_element(By.XPATH, "//div[@id='autocompleteSearch-origin']/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[1]/span[2]").click()
        self.driver.find_element(By.ID, "flight-destination-search-input").clear()
        self.driver.find_element(By.ID, "flight-destination-search-input").send_keys("NEW DELHI")
        self.driver.find_element(By.XPATH, "//div[@id='autocompleteSearch-destination']/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dateSelector-departure']/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dateSelector-departure']/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dateSelector-departure']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[4]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dateSelector-return']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[4]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabpanel-flight-tab']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='agoda-spa']/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[9]/div[1]/label[1]/span[1]").click()
    
    def test_agoda_4596152e(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.XPATH, "//a[@id='footer-faqs']/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='helpcenter-page']/section[1]/section[2]/div[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//h5[@id='htlcxl2-heading']/svg[1]").click()
    
    def test_agoda_49c60777(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.XPATH, "//header[@id='page-header']/section[1]/div[1]/nav[1]/div[2]/div[1]/ul[1]/li[7]/div[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Car rentals')]").click()
        self.driver.find_element(By.ID, "puSearchInput").clear()
        self.driver.find_element(By.ID, "puSearchInput").send_keys("Houston")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Houston, US')]").click()
        self.driver.find_element(By.ID, "formsubmit").click()
        self.driver.find_element(By.XPATH, "//div[@id='car_cat_scroll_carousel']/ul[1]/li[1]/button[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[6]/div[1]/div[3]/div[5]/div[2]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Select Car')]").click()
    
    def test_agoda_1b17b79c(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.ID, "textInput").clear()
        self.driver.find_element(By.ID, "textInput").send_keys("seattle")
        self.driver.find_element(By.XPATH, "//li[@role='option' and @data-selenium='autosuggest-item']").click()
        self.driver.find_element(By.XPATH, "//span[@role='button' and @data-selenium='calendar-next-month-button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[4]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]/div[4]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[2]/div[2]/ul[1]/li[3]/span[1]/span[2]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-bar']/div[1]/a[2]/span[1]").click()
    
    def test_agoda_1fefdb27(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.XPATH, "//li[@id='tab-activities-tab']/svg[1]/path[1]").click()
        self.driver.find_element(By.ID, "activities-search-input").clear()
        self.driver.find_element(By.ID, "activities-search-input").send_keys("Phuket")
        self.driver.find_element(By.XPATH, "//div[@id='autocompleteSearch']/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabpanel-activities-tab']/div[2]/button[1]/div[1]").click()
    
    def test_agoda_04d45cb8(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.XPATH, "//li[@id='tab-activities-tab']/svg[1]/path[1]").click()
        self.driver.find_element(By.ID, "activities-search-input").clear()
        self.driver.find_element(By.ID, "activities-search-input").send_keys("Miami")
        self.driver.find_element(By.XPATH, "//div[@id='autocompleteSearch']/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-selenium='searchButton']").click()
        self.driver.find_element(By.XPATH, "//main[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[11]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[11]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/label[2]/div[1]/div[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//input[@role='radio' and @name='sort' and @value='Price_Ascending' and @type='radio']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[11]/div[1]/div[3]/div[1]/button[2]").click()
    
    def test_agoda_1684f224(self):
        # self.driver.get("https://agoda.com")
        self.driver.find_element(By.ID, "textInput").clear()
        self.driver.find_element(By.ID, "textInput").send_keys("HOLLYWOOD")
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/ul[1]/li[3]/ul[1]/li[1]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[7]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[2]/div[2]/div[3]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='occupancy-box']/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[2]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='0' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='0' and @type='text']").send_keys("150")
        self.driver.find_element(By.XPATH, "//input[@value='3,570' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='3,570' and @type='text']").send_keys("200")
        self.driver.find_element(By.XPATH, "//div[@id='SideBarLocationFilters']/div[1]/div[4]/ul[1]/li[5]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-bar']/div[1]/a[3]/div[1]/svg[1]").click()
    