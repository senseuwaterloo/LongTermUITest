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
class TestSpothero:
    
    def test_spothero_4aa42fe7(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("bradley airport")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/select[1]").select("Price")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Book Now')]").click()
    
    def test_spothero_070e63b9(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/header[1]/div[1]/nav[1]/ul[1]/li[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Parking Guarantee')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Contact our Heroes')]").click()
    
    def test_spothero_2e78c6c2(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.ID, "tabs-2--tab-1").click()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("florida keys")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='Apr 7, 2023' and @type='text']").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'12')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[3]/button[1]").click()
    
    def test_spothero_009cc066(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.ID, "tabs-2--tab-1").click()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("Chicago")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/button[1]").click()
        self.driver.find_element(By.ID, "Checkbox-FilterItem-ev").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Show 10 Results')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").select("Sort by Price")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
    
    def test_spothero_04782cf5(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("New York City")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").select("Sort by Price")
    
    def test_spothero_0b59dd33(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.ID, "tabs-2--tab-2").click()
        self.driver.find_element(By.XPATH, "//input[@name='search' and @value='' and @type='search' and @placeholder='Airport Name, Code or City']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search' and @value='' and @type='search' and @placeholder='Airport Name, Code or City']").send_keys("Dallas Love Field")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
    
    def test_spothero_0fc98662(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("florida")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='Today' and @type='text' and @placeholder='Start Date']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[7]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/select[1]").select("5 00 PM")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/select[1]").select("6 00 PM")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[3]/button[1]").click()
    
    def test_spothero_1d173ebb(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.ID, "tabs-2--tab-1").click()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("New York")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='Mar 4, 2023' and @type='text']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[4]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[3]/button[1]").click()
    
    def test_spothero_3f0988e0(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("Barclays Center")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Select Event Date']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Philadelphia 76ers at Brooklyn Nets')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/button[1]").click()
        self.driver.find_element(By.ID, "Checkbox-FilterItem-wheelchair").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Show 18 Results')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/select[1]").select("10 00 AM")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/button[1]").click()
    
    def test_spothero_5f9182dc(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
        self.driver.find_element(By.ID, "tabs-6--tab-4").click()
    
    def test_spothero_6b627cbc(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("Times Square")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[4]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/button[1]").click()
        self.driver.find_element(By.ID, "Checkbox-FilterItem-wheelchair").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Show 12 Results')]").click()
    
    def test_spothero_749dfeeb(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("Smithsonian")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/button[1]").click()
        self.driver.find_element(By.ID, "Checkbox-FilterItem-ev").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Show 1 Results')]").click()
        self.driver.find_element(By.XPATH, "//input[@value='Today' and @type='text' and @placeholder='Start Date']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/select[1]").select("9 00 AM")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/select[1]").select("6 00 PM")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").select("Sort by Distance")
    
    def test_spothero_77be98ff(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("busch stadium")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Pittsburgh Pirates at St. Louis Cardinals')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/button[1]").click()
        self.driver.find_element(By.ID, "Checkbox-FilterItem-wheelchair").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Show 10 Results')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").select("Sort by Price")
    
    def test_spothero_839ad551(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("stripe, 5th avenue")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.ID, "tabs-1--tab-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/select[1]").select("Daytime Only Parking")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").select("Sort by Price")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h2[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[4]/div[6]/div[1]/button[1]").click()
    
    def test_spothero_87989b8e(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.ID, "tabs-2--tab-0").click()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("Atlanta International Airport")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[2]").click()
    
    def test_spothero_a2959cdb(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.ID, "tabs-2--tab-2").click()
        self.driver.find_element(By.XPATH, "//input[@name='search' and @value='' and @type='search' and @placeholder='Airport Name, Code or City']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search' and @value='' and @type='search' and @placeholder='Airport Name, Code or City']").send_keys("jfk")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='AirportDateRangePickerInputs-start' and @value='Today' and @type='text' and @placeholder='Select Parking Start Date']").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'18')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'20')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/select[1]").select("Shuttle Time")
    
    def test_spothero_b5de73d0(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("barclays center")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//p[contains(.,'Orlando Magic at Brooklyn Nets')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/select[1]").select("Sort by Distance")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/select[1]").select("3 00 PM")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/select[1]").select("5 00 PM")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[2]").click()
    
    def test_spothero_c9f65ae8(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rent My Parking Space')]").click()
        self.driver.find_element(By.ID, "first_name").clear()
        self.driver.find_element(By.ID, "first_name").send_keys("James")
        self.driver.find_element(By.ID, "last_name").clear()
        self.driver.find_element(By.ID, "last_name").send_keys("Smith")
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys("buckeye.foobar@gmail.com")
        self.driver.find_element(By.ID, "phone").clear()
        self.driver.find_element(By.ID, "phone").send_keys("8888888888")
        self.driver.find_element(By.ID, "00N3o0000090xBb").clear()
        self.driver.find_element(By.ID, "00N3o0000090xBb").select("Chicago")
        self.driver.find_element(By.ID, "00Ni000000GyvxJ").clear()
        self.driver.find_element(By.ID, "00Ni000000GyvxJ").send_keys("123rd st")
        self.driver.find_element(By.XPATH, "//input[@name='submit' and @value='' and @type='submit']").click()
    
    def test_spothero_e4f8a347(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View All Airports')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Reserve Now')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='AirportDateRangePickerInputs-start' and @value='Today' and @placeholder='Select Start Date']").click()
        self.driver.find_element(By.XPATH, "//div[@id='popover-body-6']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[4]/div[5]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='AirportDateRangePickerInputs-end' and @value='' and @placeholder='Select End Date']").click()
        self.driver.find_element(By.XPATH, "//div[@id='popover-body-6']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[5]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
    
    def test_spothero_bba6dd60(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/header[1]/div[1]/nav[1]/ul[1]/li[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'SpotHero for Business')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='getting-started']/div[1]/div[2]/div[1]/button[1]").click()
    
    def test_spothero_bf008019(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View All Stadiums')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Book Now')]").click()
        self.driver.find_element(By.ID, "tabs-1--tab-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-1--tabpanel-1']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-1--tabpanel-1']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/select[1]").select("5 00 PM")
        self.driver.find_element(By.XPATH, "//div[@id='tabs-1--tabpanel-1']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='tabs-1--tabpanel-1']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/select[1]").select("8 00 PM")
        self.driver.find_element(By.XPATH, "//div[@id='tabs-1--tabpanel-1']/button[1]").click()
    
    def test_spothero_40cd58cd(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.ID, "tabs-2--tab-1").click()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("madison square garden")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/select[1]").select("Daytime Only Parking")
        self.driver.find_element(By.XPATH, "//input[@value='Apr 8, 2023' and @type='text']").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'22')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[3]/button[1]").click()
    
    def test_spothero_45ae95ac(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.ID, "tabs-2--tab-1").click()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("New York University")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/button[1]").click()
        self.driver.find_element(By.ID, "Checkbox-FilterItem-valet").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Show 15 Results')]").click()
    
    def test_spothero_4ee7d5e1(self):
        # self.driver.get("https://spothero.com/")
        self.driver.find_element(By.ID, "tabs-2--tab-1").click()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search-input' and @value='' and @type='text' and @placeholder='Address, Place, City or Venue']").send_keys("street taco")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='Apr 7, 2023' and @type='text']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'6')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[3]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[4]/button[1]").click()
        self.driver.find_element(By.ID, "Checkbox-FilterItem-self-park").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Show 1 Results')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
    