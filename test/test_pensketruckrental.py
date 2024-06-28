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
class TestPensketruckrental:
    
    def test_pensketruckrental_d1c3d4d2(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Location')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Massachusetts')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Norwood')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Seasons Rent All')]").click()
        self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
        self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("NORWOOD")
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='appRoot']/section[1]/form[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='appRoot']/section[1]/form[1]/fieldset[2]/div[1]/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[18]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[19]/span[1]").click()
        self.driver.find_element(By.ID, "truck_size_select").clear()
        self.driver.find_element(By.ID, "truck_size_select").select("High Roof Cargo Van (Up to 1 Room)")
        self.driver.find_element(By.XPATH, "//div[@id='appRoot']/section[1]/form[1]/div[2]/div[1]/button[1]").click()
    
    def test_pensketruckrental_ed4fe7c1(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Commercial Rental')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Commercial Trucks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s_menu__commercial-items_0_0_28_0_0_1_2_0_2_0']/button[1]").click()
        self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
        self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("newark")
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quoteFormId']/fieldset[1]/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quoteFormId']/fieldset[2]/div[1]/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[13]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[15]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Select')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/section[1]/div[5]/div[1]/button[1]").click()
    
    def test_pensketruckrental_0ea84d8f(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Renting from Penske')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Plan Your Move')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Load')]").click()
    
    def test_pensketruckrental_31bd1b59(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
        self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("Detroit")
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]/span[1]").click()
        self.driver.find_element(By.ID, "drop_location_txtbox").clear()
        self.driver.find_element(By.ID, "drop_location_txtbox").send_keys("Cleveland")
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]/span[1]").click()
        self.driver.find_element(By.ID, "pickupdate").click()
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[18]/span[1]").click()
        self.driver.find_element(By.ID, "quote_truck_size_select").clear()
        self.driver.find_element(By.ID, "quote_truck_size_select").select("12 Foot Truck (1-2 Rooms)")
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    
    def test_pensketruckrental_4288a464(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Renting from Penske')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'How to Load a Moving Truck')]").click()
    
    def test_pensketruckrental_56cb11f2(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trucks')]").click()
        self.driver.find_element(By.ID, "view-comparison").click()
        self.driver.find_element(By.XPATH, "//div[@id='desktop-view-trucks']/table[2]/tbody[1]/tr[1]/td[4]/a[1]/strong[1]").click()
    
    def test_pensketruckrental_5abf54a3(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trucks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s_menu__main-items_0_0_19_0_0_1_2_0_1_1']/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
        self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("Oregon")
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.ID, "drop_location_txtbox").clear()
        self.driver.find_element(By.ID, "drop_location_txtbox").send_keys("Cleveland")
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    
    def test_pensketruckrental_6a414da4(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trucks')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Truck Wizard')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'+')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sPost_0_0_19_0_53_1_2_2_0']/div[1]/article[1]/div[1]/div[1]/div[1]/div[4]/div[1]/truckwizard-app[1]/room-items[1]/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/ul[1]/li[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'+')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Get a Quote')]").click()
    
    def test_pensketruckrental_7137b440(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
        self.driver.find_element(By.ID, "loc_input").click()
        self.driver.find_element(By.ID, "loc_input").clear()
        self.driver.find_element(By.ID, "loc_input").send_keys("Dallas")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Dallas')]").click()
        self.driver.find_element(By.ID, "dosearch").click()
    
    def test_pensketruckrental_9d57aa74(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Supplies & Services')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Self-Storage Rentals')]").click()
        self.driver.find_element(By.ID, "sparefoot-zip").clear()
        self.driver.find_element(By.ID, "sparefoot-zip").send_keys("02155")
        self.driver.find_element(By.ID, "sparefootSubmit").click()
        self.driver.find_element(By.XPATH, "//input[@name='sqft' and @value='100' and @type='radio']").click()
        self.driver.find_element(By.XPATH, "//input[@name='order' and @value='price' and @type='radio']").click()
        self.driver.find_element(By.XPATH, "//input[@name='amenities' and @value='twenty_four_hour_access' and @type='radio']").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-results']/table[1]/tbody[1]/tr[1]/td[2]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
    
    def test_pensketruckrental_bcf178b2(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trucks')]").click()
        self.driver.find_element(By.ID, "view-comparison").click()
    
    def test_pensketruckrental_c25e97d4(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Location')]").click()
        self.driver.find_element(By.ID, "loc_input").clear()
        self.driver.find_element(By.ID, "loc_input").send_keys("Seattle")
        self.driver.find_element(By.ID, "dosearch").click()
    
    def test_pensketruckrental_ef760dc5(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trucks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s_menu__main-items_0_0_19_0_0_1_2_0_0_1']/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
        self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("DAYTON")
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[2]/span[1]").click()
        self.driver.find_element(By.ID, "drop_location_txtbox").clear()
        self.driver.find_element(By.ID, "drop_location_txtbox").send_keys("TEXAS CITY")
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]/span[1]").click()
        self.driver.find_element(By.ID, "pickupdate").click()
        self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[34]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    
    def test_pensketruckrental_f0ae88cd(self):
        # self.driver.get("https://pensketruckrental.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
        self.driver.find_element(By.XPATH, "//section[@id='featured-jobs']/div[1]/article[1]/div[2]/div[1]/a[1]/div[1]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='main-search']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='btn-direct_stateDisambig']/h3[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New York (25)')]").click()
        self.driver.find_element(By.XPATH, "//button[@id='btn-direct_cityDisambig']/h3[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rochester, NY (5)')]").click()
        self.driver.find_element(By.XPATH, "//button[@id='btn-direct_sortOptions']/h3[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sort by Date')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='direct_listingDiv']/ul[2]/li[1]/h4[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply Now')]").click()
    