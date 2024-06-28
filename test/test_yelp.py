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
class TestYelp:
    
    def test_yelp_96f184d8(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[3]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[4]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Shopping')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='BusinessAcceptsApplePay' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("CENTRAL NEW YARK")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Central New York, NY')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[3]/div[1]/div[1]/div[1]/span[1]").click()
    
    def test_yelp_5be61758(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("Cantonese food")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Cantonese Food')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("Chicago, IL")
        self.driver.find_element(By.XPATH, "//form[@id='header_find_form']/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/span[1]/span[1]/button[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/span[1]/div[1]/menu[1]/div[1]/div[2]/button[1]/div[1]/div[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[2]/span[1]").click()
    
    def test_yelp_4d42f600(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Auto Services')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Car Wash')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[3]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("San Francisco")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[3]/header[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/menu[1]/a[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/ul[1]/li[4]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[2]/div[4]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "collection-name").clear()
        self.driver.find_element(By.ID, "collection-name").send_keys("Car Wash")
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]").click()
    
    def test_yelp_50692ff0(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[2]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[4]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Gyms')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("DALLAS")
        self.driver.find_element(By.XPATH, "//span[contains(.,', TX')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='radio' and @name='Training environment' and @value='job_personal_training' and @type='radio' and @placeholder=' ']").click()
        self.driver.find_element(By.NAME, "Training type").click()
        self.driver.find_element(By.NAME, "Membership options").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[2]/div[1]").click()
    
    def test_yelp_da386775(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[2]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[3]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Parking')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("CALIFORNIA")
        self.driver.find_element(By.XPATH, "//span[contains(.,'California')]").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Limos')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='OffersMilitaryDiscount' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='WiFi.free' and @type='checkbox' and @placeholder=' ']").click()
    
    def test_yelp_b307117b(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("coffee shop")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Coffee Shop')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cafe de Nook')]").click()
    
    def test_yelp_c2e4800e(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_location").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("Greenville")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Greenville')]").click()
        self.driver.find_element(By.ID, "search_description").click()
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("McDonalds")
        self.driver.find_element(By.XPATH, "//form[@id='header_find_form']/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]/span[1]").click()
    
    def test_yelp_c64dcaa1(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("barbershop")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Barbershop')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See all')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/button[1]/span[1]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='BusinessParking.lot' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]/span[1]").click()
    
    def test_yelp_c987dd1d(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[3]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Thai')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("WESTMINSTER")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Westminster')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='RestaurantsTakeOut' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Thai')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See all')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='staff_fully_vaccinated' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='BusinessAcceptsApplePay' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[2]/div[1]/div[1]/div[1]/span[1]").click()
    
    def test_yelp_d9e9c178(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("spa")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Spa')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/span[1]/span[1]/button[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/span[1]/div[1]/menu[1]/div[1]/div[2]/button[1]/div[1]/div[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='on' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/span[1]/div[1]/menu[1]/div[2]/button[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[2]/div[1]/div[1]/div[1]/span[1]").click()
    
    def test_yelp_63e3020c(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[2]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[2]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Electricians')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("WESTMINSTER")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Westminster')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[2]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Fast-responding')]").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Open Now')]").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Request a Quote')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='radio' and @name='Job Type' and @value='job_electric_installation' and @type='radio' and @placeholder=' ']").click()
        self.driver.find_element(By.NAME, "Items").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/ul[1]/li[5]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]").click()
    
    def test_yelp_1b310ebc(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[2]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[4]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Dry Cleaning')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("new york city")
        self.driver.find_element(By.XPATH, "//span[contains(.,'New York, NY')]").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Virtual Consultations')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[2]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='job_ironing' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.NAME, "feature").click()
        self.driver.find_element(By.NAME, "feature").click()
    
    def test_yelp_f408cdf3(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_description").click()
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("Burgers")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Burgers')]").click()
        self.driver.find_element(By.ID, "search_location").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("44012")
        self.driver.find_element(By.XPATH, "//form[@id='header_find_form']/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[2]/div[1]/div[1]/div[1]/span[1]").click()
    
    def test_yelp_ea8737b0(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[2]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[2]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Locksmiths')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("SAN FRANSISCO")
        self.driver.find_element(By.XPATH, "//span[contains(.,'San Francisco, CA')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/label[1]/div[1]/div[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[3]/label[1]/div[1]/div[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[2]/div[1]/div[1]/div[1]/span[1]").click()
    
    def test_yelp_759d1c94(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_location").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("Concord")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Concord')]").click()
        self.driver.find_element(By.ID, "search_description").click()
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("mexican")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Mexican')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/ul[1]/li[15]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/span[1]").click()
    
    def test_yelp_7ce76343(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[3]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[4]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Phone Repair')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("houston")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Houston')]").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Fast-responding')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='radio' and @name='Jobs' and @value='job_data_recovery' and @type='radio' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[2]/div[1]/div[1]/div[1]/span[1]").click()
    
    def test_yelp_49372757(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_location").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("94115")
        self.driver.find_element(By.ID, "search_description").click()
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("electrician")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Electrician')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[3]/span[1]").click()
    
    def test_yelp_2e15efa0(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[2]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[2]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Movers')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("HONOLULU")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Honolulu')]").click()
        self.driver.find_element(By.NAME, "feature").click()
        self.driver.find_element(By.NAME, "feature").click()
        self.driver.find_element(By.XPATH, "//input[@role='radio' and @name='Job' and @value='job_moving_interstate' and @type='radio' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Virtual Consultations')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[2]/div[1]/div[1]/div[1]/span[1]").click()
    
    def test_yelp_84f19aba(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("cafe")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Cafe')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See all')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='OutdoorSeating' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='DogsAllowed' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]/span[1]").click()
    
    def test_yelp_8e200503(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[2]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[2]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("Texas City, Texas")
        self.driver.find_element(By.XPATH, "//button[@value='submit' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[5]/span[1]").click()
    
    def test_yelp_41b8202c(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_location").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("Oakland, CA")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Oakland, CA')]").click()
        self.driver.find_element(By.ID, "search_description").click()
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("Hot Dogs")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Hot Dogs')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[3]/span[1]").click()
    
    def test_yelp_4777d638(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[2]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Reservations')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("SAN FRANCISCO")
        self.driver.find_element(By.XPATH, "//span[contains(.,'San Francisco')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='category' and @value='cocktailbars' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='feature' and @value='OutdoorSeating' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[3]/div[1]/div[1]/div[1]/span[1]").click()
    
    def test_yelp_f738b393(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[3]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[2]/div[1]/a[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Landscaping')]").click()
        self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys("WEST HOLLYWOOD")
        self.driver.find_element(By.XPATH, "//span[contains(.,'West Hollywood')]").click()
        self.driver.find_element(By.NAME, "Element").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Fast-responding')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[3]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/ul[1]/li[5]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[6]/div[1]/div[1]/div[1]/div[2]/div[4]/button[1]/span[1]").click()
    
    def test_yelp_fd2e9403(self):
        # self.driver.get("https://yelp.com")
        self.driver.find_element(By.ID, "search_description").clear()
        self.driver.find_element(By.ID, "search_description").send_keys("thai restaurants")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Thai Restaurants')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See all')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='checkbox' and @name='category' and @value='vegan' and @type='checkbox' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-portal-container']/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]/span[1]").click()
    