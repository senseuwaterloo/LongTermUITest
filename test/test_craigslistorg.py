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
class TestCraigslistOrg:
    
    def test_craigslistorg_5038548a(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//ul[@id='hhh0']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='min_bedrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='min_bedrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").send_keys("2")
        self.driver.find_element(By.XPATH, "//input[@name='min_bathrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='min_bathrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").send_keys("2")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='max']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='max']").send_keys("4000")
        self.driver.find_element(By.XPATH, "//span[contains(.,'apply')]").click()
    
    def test_craigslistorg_58159b38(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='search craigslist']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='search craigslist']").send_keys("solar panel installer")
        self.driver.find_element(By.XPATH, "//div[@id='leftbar']/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//input[@name='bundleDuplicates' and @value='1' and @type='checkbox']").click()
    
    def test_craigslistorg_583edc7a(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//div[@id='sss']/h3[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='search for sale']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='search for sale']").send_keys("couch")
        self.driver.find_element(By.XPATH, "//div[contains(.,'couch')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-toolbars-1']/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'﹩→ $$$')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[3]/div[2]/div[2]/label[1]").click()
    
    def test_craigslistorg_668f8097(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='search craigslist']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='search craigslist']").send_keys("piano lessons")
        self.driver.find_element(By.XPATH, "//div[@id='leftbar']/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-toolbars-1']/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'map')]").click()
    
    def test_craigslistorg_7109646c(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/header[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'indianapolis')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/header[1]/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/header[1]/div[1]/div[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'apartments / housing for rent')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'housing')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-toolbars-1']/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'﹩→ $$$')]").click()
    
    def test_craigslistorg_85d6921e(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//ul[@id='ccc1']/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='hasPic' and @value='1' and @type='checkbox']").click()
    
    def test_craigslistorg_9c4a64e6(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//div[@id='rightbar']/ul[1]/li[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'new york')]").click()
        self.driver.find_element(By.XPATH, "//b[contains(.,'new york city')]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='jjj0']/li[31]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[3]/div[2]/div[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'full-time')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[3]/div[4]/button[3]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'►📖✍ REMOTE COPY STRATEGIST / EDITOR / MANAGER 📝✐◄')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'PLEASE CLICK HERE TO APPLY')]").click()
    
    def test_craigslistorg_bc2387b2(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='search craigslist']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='search craigslist']").send_keys("a doll's house")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='search craigslist']").click()
        self.driver.find_element(By.XPATH, "//input[@type='tel' and @placeholder='miles']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='tel' and @placeholder='miles']").send_keys("50")
        self.driver.find_element(By.XPATH, "//input[@name='postal' and @type='tel' and @placeholder='from zip']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='postal' and @type='tel' and @placeholder='from zip']").send_keys("10001")
        self.driver.find_element(By.XPATH, "//input[@name='postedToday' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'March 29 2pm Dolls House')]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button']").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'show address')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'copy')]").click()
    
    def test_craigslistorg_bfcbf289(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//ul[@id='hhh0']/li[10]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='pets_dog' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@name='airconditioning' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[3]/div[2]/div[11]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "_21").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[3]/div[4]/button[3]").click()
    
    def test_craigslistorg_e23459fd(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='search craigslist']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='search craigslist']").send_keys("washing machine")
        self.driver.find_element(By.XPATH, "//div[@id='leftbar']/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//input[@name='postedToday' and @value='1' and @type='checkbox']").click()
    
    def test_craigslistorg_e7e02515(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//div[@id='sss']/h3[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='search for sale']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='search for sale']").send_keys("iphone X")
        self.driver.find_element(By.XPATH, "//div[contains(.,'iphone x')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'condition')]").click()
        self.driver.find_element(By.ID, "_43").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='max']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='max']").send_keys("400")
        self.driver.find_element(By.XPATH, "//span[contains(.,'apply')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='srchType' and @value='T' and @type='checkbox']").click()
    
    def test_craigslistorg_ee9cd8da(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//div[@id='jjj']/h3[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='search jobs']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='search jobs']").send_keys("cashier")
        self.driver.find_element(By.XPATH, "//div[contains(.,'cashier')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'employment type')]").click()
        self.driver.find_element(By.ID, "_6").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[3]/div[4]/button[3]").click()
    
    def test_craigslistorg_ff8f6003(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'phoenix')]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='sss1']/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//td[contains(.,'31')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-toolbars-1']/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'list')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'CYBER GARAGE SALE VINTAGE AND NEW TOYS LEGO STAR WARS HOT WHEELS N MOR')]").click()
        self.driver.find_element(By.ID, "printme").click()
    
    def test_craigslistorg_0e48ad89(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'austin')]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='hhh0']/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='tel' and @placeholder='miles']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='tel' and @placeholder='miles']").send_keys("10")
        self.driver.find_element(By.XPATH, "//input[@name='postal' and @type='tel' and @placeholder='from zip']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='postal' and @type='tel' and @placeholder='from zip']").send_keys("78563")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='min']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='min']").send_keys("50")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='max']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='max']").send_keys("150")
        self.driver.find_element(By.XPATH, "//input[@name='airconditioning' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[3]/div[4]/button[3]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'10x10 CC ~  WOW!!!  Affordable!!')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'show contact info')]").click()
    
    def test_craigslistorg_0f4b58c0(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//div[@id='bbb']/h3[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='search services']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='search services']").send_keys("babysitter")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[1]/button[1]/span[1]").click()
    
    def test_craigslistorg_120be24d(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//ul[@id='sss0']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-toolbars-1']/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'oldest')]").click()
    
    def test_craigslistorg_2c79a395(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//ul[@id='hhh0']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='search apartments / housing for rent']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='search apartments / housing for rent']").send_keys("laundry")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='srchType' and @value='T' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@name='min_bedrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='min_bedrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").send_keys("2")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[3]").click()
    
    def test_craigslistorg_3154d1c8(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//div[@id='rightbar']/ul[1]/li[3]/h5[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'new york')]").click()
        self.driver.find_element(By.XPATH, "//b[contains(.,'new york city')]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='hhh0']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='hasPic' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-toolbars-1']/div[1]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'gallery')]").click()
        self.driver.find_element(By.XPATH, "//select[@name='availabilityMode']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='availabilityMode']").select("within 30 days")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[3]/div[2]/div[7]/label[9]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/main[1]/form[1]/div[3]/div[2]/div[7]/label[3]").click()
        self.driver.find_element(By.XPATH, "//input[@name='min_bedrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='min_bedrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").send_keys("1")
        self.driver.find_element(By.XPATH, "//input[@name='min_bathrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='min_bathrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").send_keys("1")
        self.driver.find_element(By.XPATH, "//span[contains(.,'apply')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'parking')]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'attached garage')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'apply')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Brooklyn LUXURY building 25th FLOOR, AMENITIES, GREAT LOCATION')]").click()
        self.driver.find_element(By.ID, "printme").click()
    
    def test_craigslistorg_0471dcf7(self):
        # self.driver.get("https://craigslist.org")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'chicago')]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='sss1']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='crypto_currency_ok' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'apply')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='bundleDuplicates' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-toolbars-1']/div[5]/button[1]/span[2]").click()
    