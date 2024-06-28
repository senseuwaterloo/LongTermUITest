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
class TestKoa:
    
    def test_koa_97219f72(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Deals')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Hot Deals')]").click()
        self.driver.find_element(By.ID, "input-find-hot-deals").clear()
        self.driver.find_element(By.ID, "input-find-hot-deals").send_keys("10019")
        self.driver.find_element(By.XPATH, "//div[@id='form-find-hot-deals']/div[2]/span[1]/button[1]/span[1]").click()
    
    def test_koa_3d731c1d(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.ID, "txtLocation").clear()
        self.driver.find_element(By.ID, "txtLocation").send_keys("Myrtle Beach")
        self.driver.find_element(By.ID, "checkInDate").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']/div[2]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'20')]").click()
        self.driver.find_element(By.ID, "checkOutDate").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'23')]").click()
        self.driver.find_element(By.ID, "filters").click()
        self.driver.find_element(By.ID, "chkHotTub").click()
        self.driver.find_element(By.ID, "btnAdvancedSearch").click()
    
    def test_koa_6de5b415(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.ID, "txtLocation").clear()
        self.driver.find_element(By.ID, "txtLocation").send_keys("Orlando")
        self.driver.find_element(By.XPATH, "//li[@id='ui-id-8']/b[1]").click()
        self.driver.find_element(By.ID, "checkInDate").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'29')]").click()
        self.driver.find_element(By.ID, "checkOutDate").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'30')]").click()
        self.driver.find_element(By.ID, "btnBasicSearch").click()
        self.driver.find_element(By.ID, "Adults").clear()
        self.driver.find_element(By.ID, "Adults").select("2")
        self.driver.find_element(By.ID, "btnApplyFilter").click()
    
    def test_koa_b2dd00ff(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Camping at KOA')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'KOA Holiday Campgrounds')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='brands']/div[2]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='brands']/div[2]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
    
    def test_koa_b4872f0e(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Campground')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find by State/Province')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'California')]").click()
    
    def test_koa_b7e501a4(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.XPATH, "//a[@id='filters']/i[1]").click()
        self.driver.find_element(By.ID, "chkRvSite").click()
        self.driver.find_element(By.ID, "txtLocation").clear()
        self.driver.find_element(By.ID, "txtLocation").send_keys("California")
        self.driver.find_element(By.ID, "btnAdvancedSearch").click()
    
    def test_koa_c7b0d1bc(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.ID, "txtLocation").clear()
        self.driver.find_element(By.ID, "txtLocation").send_keys("Lansing")
        self.driver.find_element(By.ID, "ui-id-6").click()
        self.driver.find_element(By.ID, "checkInDate").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']/div[2]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']/div[2]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'7')]").click()
        self.driver.find_element(By.ID, "checkOutDate").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'12')]").click()
        self.driver.find_element(By.ID, "btnBasicSearch").click()
    
    def test_koa_d3ca5294(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.ID, "txtLocation").clear()
        self.driver.find_element(By.ID, "txtLocation").send_keys("Phoenix")
        self.driver.find_element(By.ID, "checkInDate").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'9')]").click()
        self.driver.find_element(By.ID, "filters").click()
        self.driver.find_element(By.ID, "chkWiFi").click()
        self.driver.find_element(By.ID, "btnAdvancedSearch").click()
    
    def test_koa_a39f20a6(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Deals')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Hot Deals')]").click()
        self.driver.find_element(By.ID, "input-find-hot-deals").clear()
        self.driver.find_element(By.ID, "input-find-hot-deals").send_keys("10001")
        self.driver.find_element(By.XPATH, "//div[@id='form-find-hot-deals']/div[2]/span[1]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "input-radius").clear()
        self.driver.find_element(By.ID, "input-radius").select("500 Miles")
    
    def test_koa_a92a83ca(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.ID, "txtLocation").clear()
        self.driver.find_element(By.ID, "txtLocation").send_keys("Lave Hot Springs East KOA")
        self.driver.find_element(By.ID, "ui-id-3").click()
        self.driver.find_element(By.ID, "btnBasicSearch").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Photos')]").click()
    
    def test_koa_08a0c5cc(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Camping at KOA')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'KOA Resort Campgrounds')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='brands']/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='brands']/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "getDirections").click()
    
    def test_koa_117b1d5c(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rewards Program')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Purchase or Renew Now')]").click()
        self.driver.find_element(By.ID, "vkrPurchaseTypeRenew").click()
        self.driver.find_element(By.ID, "Step1_AccountNumber").clear()
        self.driver.find_element(By.ID, "Step1_AccountNumber").send_keys("1000000001")
        self.driver.find_element(By.ID, "Step1_PostalCode").clear()
        self.driver.find_element(By.ID, "Step1_PostalCode").send_keys("10023")
        self.driver.find_element(By.ID, "continueButton").click()
    
    def test_koa_39358d9c(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Deals')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'DISH Outdoors')]").click()
    
    def test_koa_4970cd99(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Campground')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trip Planner')]").click()
        self.driver.find_element(By.ID, "origin").clear()
        self.driver.find_element(By.ID, "origin").send_keys("Cheyenne")
        self.driver.find_element(By.ID, "destination").clear()
        self.driver.find_element(By.ID, "destination").send_keys("Helena")
        self.driver.find_element(By.ID, "btn-directions").click()
        self.driver.find_element(By.ID, "origin0").click()
        self.driver.find_element(By.ID, "destination0").click()
        self.driver.find_element(By.ID, "continueModalBtn").click()
    
    def test_koa_6d338fef(self):
        # self.driver.get("https://koa.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Ways To Stay')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Glamping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'glamping near you')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'California')]").click()
    