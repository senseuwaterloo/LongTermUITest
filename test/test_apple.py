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
class TestApple:
    
    def test_apple_01815816(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'MacBook Air')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='compare-table-notebooks']/div[1]/div[17]/p[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tech Specs')]").click()
    
    def test_apple_d5b1ca5f(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Displays')]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='chapternav']/div[1]/ul[1]/li[2]/a[1]/figure[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Buy')]").click()
        self.driver.find_element(By.XPATH, "//label[@id='08e89070-d891-11ed-97b1-312990d59d44_label']/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[@id='097f5230-d891-11ed-97b1-312990d59d44_label']/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[@id='097fc761-d891-11ed-97b1-312990d59d44_label']/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@name='add-to-cart' and @value='add-to-cart' and @type='submit' and @title='Add to Bag']").click()
    
    def test_apple_2fc80069(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[5]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='chapternav']/div[1]/ul[1]/li[7]/a[1]/figure[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[4]/div[3]/div[2]/div[2]/a[1]/span[1]").click()
    
    def test_apple_74992300(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[10]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[6]/div[3]/div[2]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Track the status of an existing repair')]").click()
    
    def test_apple_2a8ae104(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[3]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop iPad')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='shelf-1_section']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/img[1]").click()
    
    def test_apple_d743815d(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[10]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[6]/div[2]/div[5]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Find My AirPods')]").click()
    
    def test_apple_fd2494f3(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Order Status')]").click()
        self.driver.find_element(By.ID, "signIn.orderLookUp.orderNumber").clear()
        self.driver.find_element(By.ID, "signIn.orderLookUp.orderNumber").send_keys("24124124091")
        self.driver.find_element(By.ID, "signIn.orderLookUp.emailAddress").clear()
        self.driver.find_element(By.ID, "signIn.orderLookUp.emailAddress").send_keys("boobear@gmail.com")
        self.driver.find_element(By.XPATH, "//button[@id='signIn.orderLookUp.guestUserOrderLookUp']/span[1]/span[1]/span[1]").click()
    
    def test_apple_3b6385ea(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Store')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search by location, ZIP, or store name']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search by location, ZIP, or store name']").send_keys("90028")
        self.driver.find_element(By.XPATH, "//ul[@id='store-search-suggestions']/li[1]/a[1]/span[1]/span[1]").click()
    
    def test_apple_6c0a3b1e(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[9]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel-1aeca1e0-bced-11ed-9ebd-0d1feadbe04c-0']/ul[1]/li[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='2d047010-bced-11ed-95f2-d14365e67dcb-gallery-item-0']/div[3]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    
    def test_apple_a10e6232(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[3]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Buy')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//label[@id='6290c2b0-d962-11ed-ac04-ad7e008cbb80_label']/span[2]/span[2]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[@id='629110d0-d962-11ed-ac04-ad7e008cbb80_label']/span[1]/span[1]/span[1]/div[1]").click()
        self.driver.find_element(By.ID, "62f15941-d962-11ed-ac04-ad7e008cbb80").click()
        self.driver.find_element(By.ID, "6e493fb0-d962-11ed-ac04-ad7e008cbb80").clear()
        self.driver.find_element(By.ID, "6e493fb0-d962-11ed-ac04-ad7e008cbb80").send_keys("Hello World")
        self.driver.find_element(By.XPATH, "//div[@id='portal']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='acc_pencil_first']/button[2]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='acc_adapter']/button[2]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='acc_magic_keyboard']/button[2]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[2]/div[2]/div[1]/div[8]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/fieldset[1]/div[1]/div[2]/label[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[@id='6324c550-d962-11ed-ac04-ad7e008cbb80_label']/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[@id='applecareplus_noapplecare_label']/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[2]/div[2]/div[1]/div[12]/div[1]/div[5]/div[1]/div[1]/span[1]/form[1]/div[1]/span[1]/button[1]/span[1]").click()
    
    def test_apple_ccee2694(self):
        # self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find one near you')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search by location, ZIP, or store name']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search by location, ZIP, or store name']").send_keys("60540")
        self.driver.find_element(By.XPATH, "//ul[@id='store-search-suggestions']/li[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='gallery-item-0']/a[1]/div[2]/div[1]/address[1]").click()
    