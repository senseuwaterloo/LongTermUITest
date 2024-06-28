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
class TestMovoto:
    
    def test_movoto_bf74a5de(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Rent']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys("Anchorage Alaska")
        self.driver.find_element(By.XPATH, "//div[@id='textboxGeo']/div[2]/div[1]/a[1]/div[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='price']/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div[1]/div[1]/div[3]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div[1]/div[1]/div[3]/div[1]/input[1]").send_keys("800")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]").click()
    
    def test_movoto_c4bcdbc6(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Buy']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys("hanover pensylvania")
        self.driver.find_element(By.XPATH, "//div[@id='textboxGeo']/div[2]/div[1]/a[1]/div[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/div[1]/button[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='houseStates']/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[2]").click()
    
    def test_movoto_d5603064(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Buy']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys("11001")
        self.driver.find_element(By.XPATH, "//div[@id='textboxGeo']/div[2]/div[1]/a[1]/div[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='btnFilter']/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'$350K - $550K')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'1')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'1')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='houseStates']/div[1]/div[1]/label[6]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'10 Mi')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='38 Meadowood Ln, Brookville, NY 11545']").click()
    
    def test_movoto_d6fe3275(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Buy']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys("huntsville")
        self.driver.find_element(By.XPATH, "//div[@id='textboxGeo']/div[2]/div[1]/a[1]/div[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='btnFilter']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'$150K - $200K')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/div[1]/button[4]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='openHousePanel']/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/a[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'9:00 am')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/button[1]").click()
    
    def test_movoto_885e81a4(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Buy']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Homes for Sale Near Me')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='bed-bath']/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'2')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='price']/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div[1]/div[1]/div[3]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div[1]/div[1]/div[3]/div[1]/input[1]").send_keys("700000")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='searchList']/section[1]/div[1]/div[2]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low')]").click()
    
    def test_movoto_8bd80e0a(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Homeowner']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Home Repair & Service Providers')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[3]/div[1]/ul[1]/li[1]/a[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//input[@name='zipcode' and @type='text' and @placeholder='Zip Code']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='zipcode' and @type='text' and @placeholder='Zip Code']").send_keys("21012")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.ID, "sorting-select").clear()
        self.driver.find_element(By.ID, "sorting-select").select("Rating")
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    
    def test_movoto_96170ab8(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Agent']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Movoto Agents')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn More')]").click()
    
    def test_movoto_e8f8228b(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Homeowner']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Home Repair & Service Providers')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[3]/div[1]/ul[1]/li[1]/a[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    
    def test_movoto_ebea3aa1(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Buy']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys("anchorage")
        self.driver.find_element(By.XPATH, "//div[@id='textboxGeo']/div[2]/div[1]/a[1]/div[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='bed-bath']/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'3')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'3')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='btnFilter']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='houseStates']/div[1]/div[1]/label[7]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='5467 Sandhill Loop, Anchorage, AK 99502']").click()
    
    def test_movoto_eebe96f3(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Buy']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Homes for Sale Near Me')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='bed-bath']/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'3')]").click()
        self.driver.find_element(By.ID, "btnFilter").click()
        self.driver.find_element(By.XPATH, "//div[@id='houseStates']/div[1]/div[1]/label[3]/i[1]").click()
        self.driver.find_element(By.ID, "applyButton").click()
        self.driver.find_element(By.XPATH, "//div[@id='searchList']/div[2]/div[1]/div[2]/div[2]/a[1]/i[1]").click()
    
    def test_movoto_fa1114fd(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Agent']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Meet an Agent')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn More')]").click()
    
    def test_movoto_05c48a32(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys("Yorkville, IL")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Type')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Bed / Bath')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'2')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'1')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'$100K - $200K')]").click()
    
    def test_movoto_09d8499c(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Buy']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Homes for Sale Near Me')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='price']/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div[1]/div[1]/div[3]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div[1]/div[1]/div[3]/div[1]/input[1]").send_keys("500000")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[1]/div[1]").click()
    
    def test_movoto_10cf036a(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Mortgage']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Calculate Payments')]").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='ZIP Code']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='ZIP Code']").send_keys("60510")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]").send_keys("$450,800")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]").send_keys("30%")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[5]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[5]/div[1]/div[1]/select[1]").select("20 Years Fixed")
    
    def test_movoto_20efa1e6(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Mortgage']").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[2]/div[1]/div[2]/div[1]/div[1]/a[2]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[2]/div[1]/div[2]/div[1]/div[1]/a[2]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Savings')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='zipcode' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='zipcode' and @type='text']").send_keys("08816")
        self.driver.find_element(By.XPATH, "//input[@type='tel']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("475000")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/input[1]").send_keys("250000")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/select[1]").select("700-719 (Good)")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Show more options')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/form[1]/div[9]/div[1]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/form[1]/div[9]/div[1]/div[1]/div[1]/select[1]").select("None")
    
    def test_movoto_86fff327(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Mortgage']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Calculate Payments')]").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='ZIP Code']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='ZIP Code']").send_keys("93727")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]").send_keys("472450")
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]").send_keys("6")
        self.driver.find_element(By.XPATH, "//input[@type='tel']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("25000")
    
    def test_movoto_87abbab1(self):
        # self.driver.get("https://movoto.com")
        self.driver.find_element(By.XPATH, "//button[@title='Rent']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys("10001")
        self.driver.find_element(By.XPATH, "//div[@id='textboxGeo']/div[2]/div[1]/a[1]/div[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='btnFilter']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'2')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'2')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'2')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='houseStates']/div[1]/div[1]/label[6]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'30 Mi')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]/i[1]").click()
    