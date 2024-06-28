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
class TestTesla:
    
    def test_tesla_7ac28815(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View Inventory')]").click()
        self.driver.find_element(By.ID, "4e9e4cdf-85a1-44f5-afa8-e151a695bd71_used").click()
        self.driver.find_element(By.ID, "TRIM:PAWD").click()
    
    def test_tesla_642ac4f9(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='tesla-hero-3693']/div[2]/div[1]/section[1]/div[1]/section[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "0682e73f-fc27-41d3-9616-21c1c4ec8a9f_used").click()
        self.driver.find_element(By.XPATH, "//div[@id='iso-container']/div[1]/div[1]/aside[1]/form[1]/div[1]/div[6]/fieldset[1]/div[1]/div[6]/label[1]/svg[1]/image[1]").click()
    
    def test_tesla_0fb1c90e(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[1]/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedule a virtual consultation')]").click()
        self.driver.find_element(By.ID, "8d14b3a2-20ea-4da3-a5e0-e51e25f0bcb1").clear()
        self.driver.find_element(By.ID, "8d14b3a2-20ea-4da3-a5e0-e51e25f0bcb1").send_keys("James")
        self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[1]/div[1]/aside[1]/form[1]/div[1]/div[2]/div[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[1]/div[1]/aside[1]/form[1]/div[1]/div[2]/div[1]").send_keys("Smith")
        self.driver.find_element(By.ID, "address-search").clear()
        self.driver.find_element(By.ID, "address-search").send_keys("123st rd")
        self.driver.find_element(By.ID, "921e1cc2-1aa2-43ab-8771-4e2b02b7b334").clear()
        self.driver.find_element(By.ID, "921e1cc2-1aa2-43ab-8771-4e2b02b7b334").send_keys("abc@abc.com")
        self.driver.find_element(By.ID, "10").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_tesla_3b7cead3(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[1]/li[7]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='tesla-hero-1355']/div[2]/div[1]/section[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "landing-page-installationAddress").clear()
        self.driver.find_element(By.ID, "landing-page-installationAddress").send_keys("7528 East Mechanic Ave. Fargo, ND 58102")
        self.driver.find_element(By.ID, "landing-page-installationAddress").click()
        self.driver.find_element(By.ID, "homeSqFt").clear()
        self.driver.find_element(By.ID, "homeSqFt").send_keys("200")
        self.driver.find_element(By.ID, "homeStories").clear()
        self.driver.find_element(By.ID, "homeStories").select("Two-Story")
        self.driver.find_element(By.XPATH, "//div[@id='powerwall-landing-page']/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "landing-page-next-btn").click()
        self.driver.find_element(By.ID, "without-incentives").click()
    
    def test_tesla_4985e844(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='tesla-carousel-v2-4043']/section[1]/div[1]/section[1]/section[1]/section[2]/div[1]/section[1]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='iso-container']/div[1]/div[1]/aside[1]/form[1]/div[1]/div[7]/fieldset[1]/div[1]/div[5]/label[1]/svg[1]/image[1]").click()
        self.driver.find_element(By.ID, "filter_lbl").clear()
        self.driver.find_element(By.ID, "filter_lbl").select("Price   low to high")
        self.driver.find_element(By.ID, "8adaa05a-0617-45b0-b429-f5d73e565764").clear()
        self.driver.find_element(By.ID, "8adaa05a-0617-45b0-b429-f5d73e565764").send_keys("94043")
    
    def test_tesla_851ed4e6(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[2]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tds-global-menu']/dialog[1]/section[1]/ol[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[5]/button[3]").click()
    
    def test_tesla_8e7b05d4(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[2]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tds-global-menu']/dialog[1]/section[1]/ol[1]/li[9]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='tesla-gallery-advanced-389']/div[1]/section[1]/div[2]/section[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='' and @value='' and @type='text' and @placeholder='Enter location']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='' and @value='' and @type='text' and @placeholder='Enter location']").send_keys("London")
        self.driver.find_element(By.XPATH, "//ul[@id='autocomplete']/li[3]").click()
    
    def test_tesla_9cd20dc6(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='tesla-hero-3693']/div[2]/div[1]/section[1]/div[1]/section[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='iso-container']/div[1]/div[1]/aside[1]/form[1]/div[1]/div[7]/fieldset[1]/div[1]/div[3]/label[1]/svg[1]/image[1]").click()
        self.driver.find_element(By.ID, "WHEELS:NINETEEN").click()
        self.driver.find_element(By.ID, "0783102c-18aa-45c8-9769-690231ca1408").clear()
        self.driver.find_element(By.ID, "0783102c-18aa-45c8-9769-690231ca1408").send_keys("60602")
        self.driver.find_element(By.ID, "d654b8ce-9626-4dda-8f14-9a7f845ca315").clear()
        self.driver.find_element(By.ID, "d654b8ce-9626-4dda-8f14-9a7f845ca315").select("50 miles")
    
    def test_tesla_cdbd410d(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[2]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop Now')]").click()
        self.driver.find_element(By.ID, "model-x.best-sellers").click()
    
    def test_tesla_e12f51f6(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[2]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Lifestyle')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='category--lifestyle--giftcards']/ul[1]/li[1]/div[1]/div[1]/a[1]/img[1]").click()
        self.driver.find_element(By.ID, "2854c256-6d5b-47ee-99f0-c214ace2ab97").clear()
        self.driver.find_element(By.ID, "2854c256-6d5b-47ee-99f0-c214ace2ab97").send_keys("April May")
        self.driver.find_element(By.ID, "5763900a-2092-4707-8bd6-931c456beff6").clear()
        self.driver.find_element(By.ID, "5763900a-2092-4707-8bd6-931c456beff6").send_keys("april.may@gmail.com")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_tesla_e2142cde(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='tesla-hero-3693']/div[2]/div[1]/section[1]/div[1]/section[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "37933305-0aef-468f-a5d8-3ec4eacee214").clear()
        self.driver.find_element(By.ID, "37933305-0aef-468f-a5d8-3ec4eacee214").send_keys("10001")
        self.driver.find_element(By.ID, "79a86eac-4f3e-4317-b0f3-3b6a86dd242d").clear()
        self.driver.find_element(By.ID, "79a86eac-4f3e-4317-b0f3-3b6a86dd242d").select("200 miles")
    
    def test_tesla_e6bdb364(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[1]/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='tesla-hero-1124']/div[2]/div[1]/section[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-selection']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='help-me-choose-roof-info']/div[2]/div[1]/button[2]").click()
    
    def test_tesla_fdc94e3a(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//div[@id='block-tesla-frontend-content']/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[5]/button[4]").click()
        self.driver.find_element(By.ID, "edit-lastname-td").clear()
        self.driver.find_element(By.ID, "edit-lastname-td").send_keys("Adams")
        self.driver.find_element(By.ID, "edit-firstname-td").clear()
        self.driver.find_element(By.ID, "edit-firstname-td").send_keys("Roy")
        self.driver.find_element(By.ID, "edit-phonenumber-td").clear()
        self.driver.find_element(By.ID, "edit-phonenumber-td").send_keys("123-999-0000")
        self.driver.find_element(By.ID, "edit-usermail-td").clear()
        self.driver.find_element(By.ID, "edit-usermail-td").send_keys("RA@gmail.com")
        self.driver.find_element(By.ID, "edit-zipcode-td").clear()
        self.driver.find_element(By.ID, "edit-zipcode-td").send_keys("90001")
        self.driver.find_element(By.ID, "edit-submit-td-ajax0").click()
    
    def test_tesla_71638c81(self):
        # self.driver.get("https://tesla.com")
        self.driver.find_element(By.XPATH, "//header[@id='tds-site-header']/ol[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='tesla-hero-3728']/div[2]/div[1]/section[1]/div[1]/section[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[5]/fieldset[1]/div[1]/div[1]/div[1]/div[3]/div[1]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "DeliveryPostalCode").clear()
        self.driver.find_element(By.ID, "DeliveryPostalCode").send_keys("10001")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    