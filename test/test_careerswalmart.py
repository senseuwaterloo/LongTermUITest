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
class TestCareersWalmart:
    
    def test_careerswalmart_051a421d(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Career Areas')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sam’s Club Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='type-accordion']/div[1]/div[3]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rate-accordion']/div[1]/div[2]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='department-accordion']/div[1]/div[5]/h6[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='subfilter-00000159-7574-d286-a3f9-7ff45f640000']/div[14]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("DALLAS")
        self.driver.find_element(By.XPATH, "//ul[@id='search-location-list']/li[8]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Member Specialist-Unlocked Potential/Internship')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    
    def test_careerswalmart_0da913af(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Silicon Valley')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='brand-accordion']/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='type-accordion']/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rate-accordion']/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='department-accordion']/div[1]/div[5]/h6[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='subfilter-00000159-7574-d286-a3f9-7ff45f640000']/div[3]/label[1]").click()
        self.driver.find_element(By.XPATH, "//label[@role='button' and @title='Job Post Date']").click()
    
    def test_careerswalmart_0e923eac(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Career Areas')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cybersecurity')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='type-accordion']/div[1]/div[1]/label[1]").click()
    
    def test_careerswalmart_119c9160(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Career Areas')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Walmart Store Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='brand-accordion']/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("NEW ALBANY")
        self.driver.find_element(By.XPATH, "//ul[@id='search-location-list']/li[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='type-accordion']/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rate-accordion']/div[1]/div[2]/label[1]").click()
        self.driver.find_element(By.XPATH, "//label[@role='button' and @title='Job Post Date']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Fuel Station')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    
    def test_careerswalmart_290508bc(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//span[@role='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='categories']/div[5]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("ohio")
        self.driver.find_element(By.XPATH, "//ul[@id='search-location-list']/li[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//label[@role='button' and @title='Job Post Date']").click()
        self.driver.find_element(By.XPATH, "//div[@id='type-accordion']/div[1]/div[3]/label[1]").click()
    
    def test_careerswalmart_3068d843(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Career Areas')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drivers & Transportation')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("TRUCK DRIVER")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'truck driver gordonsville va')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Yard Truck and City Driver')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    
    def test_careerswalmart_3cbbbbaa(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Students')]").click()
        self.driver.find_element(By.XPATH, "//h3[contains(.,'Graduate and MBA internships')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See all opportunities')]").click()
    
    def test_careerswalmart_40e0550f(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//h4[contains(.,'Sam’s Club Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
    
    def test_careerswalmart_42eac105(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("software engineer")
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("Atlanta")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_careerswalmart_7ffd9e73(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//span[@role='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='categories']/div[2]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "search").click()
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("support services")
        self.driver.find_element(By.ID, "location").click()
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("Bentonville")
        self.driver.find_element(By.XPATH, "//ul[@id='search-location-list']/li[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_careerswalmart_04dd477b(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Military')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Search Careers')]").click()
        self.driver.find_element(By.XPATH, "//h4[contains(.,'Sam’s Club Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='type-accordion']/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rate-accordion']/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='department-accordion']/div[1]/div[5]/h6[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='subfilter-00000159-7574-d286-a3f9-7ff45f640000']/div[5]/label[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='search-results']/li[1]/div[1]/h4[1]").click()
    
    def test_careerswalmart_982c89fb(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//h4[contains(.,'Walmart Store Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        self.driver.find_element(By.XPATH, "//label[@role='button' and @title='Job Post Date']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/label[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='type-accordion']/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Auto Care Center')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    
    def test_careerswalmart_ac674082(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("nurses")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_careerswalmart_b0a7510a(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Silicon Valley')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rate-accordion']/div[1]/div[2]/label[1]").click()
    
    def test_careerswalmart_d78cd44d(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Career Areas')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Walmart Health')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='type-accordion']/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//label[@role='button' and @title='Job Post Date']").click()
    
    def test_careerswalmart_d9fead04(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Culture')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Diversity & Inclusion')]").click()
        self.driver.find_element(By.XPATH, "//img[@alt='African American Business Resource Group Logo']").click()
    
    def test_careerswalmart_eb669668(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Students')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'See all roles')]").click()
        self.driver.find_element(By.XPATH, "//label[@role='button' and @title='Job Post Date']").click()
    
    def test_careerswalmart_edaae9f6(self):
        # self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Career Areas')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sam’s Club Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='department-accordion']/div[1]/div[3]/h6[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='subfilter-00000159-758d-d286-a3f9-7fad37a00000']/div[1]/label[1]").click()
    