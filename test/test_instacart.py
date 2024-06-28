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
class TestInstacart:
    
    def test_instacart_00199892(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//div[@id='use-cases']/a[5]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Grocery')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[2]/div[2]/div[2]/div[1]/div[1]/a[1]/div[1]/span[1]/svg[1]").click()
    
    def test_instacart_51fce1f7(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/header[1]/div[2]/nav[1]/div[1]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='departments']/a[13]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[5]/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[1]/p[1]").click()
    
    def test_instacart_844f8d77(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/header[1]/div[2]/nav[1]/div[1]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/header[1]/div[1]/div[1]/div[1]/div[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='more-ways-to-shop']/a[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[2]/div[2]/ul[1]/li[7]/div[1]/a[1]/div[2]/span[1]").click()
    
    def test_instacart_8f6374b0(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/ul[1]/li[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[3]/ul[1]/li[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[3]/ul[1]/li[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[3]/ul[1]/li[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/button[2]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/ul[1]/li[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[3]/ul[1]/li[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[3]/ul[2]/li[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/ul[1]/li[1]/ul[1]/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-694']/div[1]/div[1]/footer[1]/button[1]/span[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Delivery-address-chooser']/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-1332-confirm']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Delivery-time-chooser']/div[4]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Delivery options']/li[1]/div[1]/div[1]/div[1]/span[1]/span[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_instacart_945ac29d(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//img[@role='presentation']").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search Kroger...']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search Kroger...']").send_keys("bananas")
        self.driver.find_element(By.XPATH, "//li[@id='group-0-option-0']/a[1]/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "id-815").click()
        self.driver.find_element(By.ID, "id-814-priceAsc").click()
    
    def test_instacart_96fb7e5d(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").send_keys("Gingerbread cakes")
        self.driver.find_element(By.XPATH, "//li[@id='group-0-option-0']/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[1]/span[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[5]/div[1]/button[1]/span[1]").click()
    
    def test_instacart_10b2af14(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div[1]/span[1]/button[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-2611']/nav[1]/ul[1]/div[4]/li[3]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Create a list')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-2638']/div[2]/div[2]/div[1]/button[1]/div[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-2639']/div[2]/div[32]/a[1]/span[2]/span[1]/span[1]").click()
        self.driver.find_element(By.ID, "title").clear()
        self.driver.find_element(By.ID, "title").send_keys("Walgreens")
        self.driver.find_element(By.XPATH, "//div[@id='id-2643']/div[2]/div[1]/div[1]/div[6]/ul[1]/div[1]/li[5]/button[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-2643']/div[2]/div[1]/div[1]/div[7]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/ul[1]/li[8]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[5]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[5]/div[1]/div[2]/div[1]/div[2]/ul[1]/div[2]/li[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[2]/div[2]/div[2]/div[1]/div[1]/div[6]/div[2]/button[1]/span[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='on' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-2822']/div[2]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/div[4]/li[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[2]/div[2]/div[2]/div[1]/div[1]/div[6]/div[2]/button[1]/span[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='on' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-2924']/div[2]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View More')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[2]/ul[1]/li[14]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[2]/div[2]/div[2]/div[1]/div[1]/div[6]/div[2]/button[1]/span[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='on' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-3109']/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/ul[1]/li[8]/ul[1]/li[8]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[2]/ul[1]/li[23]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[2]/div[2]/div[2]/div[1]/div[1]/div[6]/div[2]/button[1]/span[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='on' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-3274']/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/div[1]/ul[1]/li[4]/a[1]/span[2]").click()
    
    def test_instacart_bbfed209(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div[1]/span[1]/button[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='id-209']/nav[1]/ul[1]/div[2]/li[5]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-views-container']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[8]/a[1]/span[2]").click()
    
    def test_instacart_d0ac6860(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").send_keys("organic strawberries")
        self.driver.find_element(By.XPATH, "//li[@id='group-0-option-0']/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/span[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div[1]/a[2]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").send_keys("organic strawberries")
        self.driver.find_element(By.XPATH, "//li[@id='group-0-option-0']/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/span[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div[2]/a[2]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").send_keys("organic strawberries")
        self.driver.find_element(By.XPATH, "//li[@id='group-0-option-0']/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/span[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div[2]/a[2]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").send_keys("organic strawberries")
        self.driver.find_element(By.XPATH, "//li[@id='group-0-option-0']/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/span[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[1]/div[2]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[2]/div[2]/div[2]/div[1]/div[1]/div[6]/button[2]/span[1]").click()
    
    def test_instacart_14a4e19d(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/div[1]/ul[1]/li[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/ul[1]/div[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[8]/div[1]/div[2]/div[1]/div[2]/ul[1]/div[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View More')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
    
    def test_instacart_15a0ffe5(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div[1]/div[2]/div[1]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.ID, "streetAddress").clear()
        self.driver.find_element(By.ID, "streetAddress").send_keys("2983 Marietta Street")
        self.driver.find_element(By.XPATH, "//div[@id='id-4']/div[2]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/address[1]/span[1]").click()
        self.driver.find_element(By.ID, "apartmentNumber").clear()
        self.driver.find_element(By.ID, "apartmentNumber").send_keys("2")
        self.driver.find_element(By.ID, "businessName").clear()
        self.driver.find_element(By.ID, "businessName").send_keys("Buck")
        self.driver.find_element(By.XPATH, "//div[@id='id-4']/div[2]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
    
    def test_instacart_277bdab6(self):
        # self.driver.get("https://instacart.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search products, stores, and recipes']").send_keys("dog treats")
        self.driver.find_element(By.XPATH, "//li[@id='group-0-option-0']/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[3]/span[1]").click()
        self.driver.find_element(By.ID, "id-313").click()
        self.driver.find_element(By.ID, "id-312-priceAsc").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[3]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[12]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[16]/ul[1]/li[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/span[1]").click()
    