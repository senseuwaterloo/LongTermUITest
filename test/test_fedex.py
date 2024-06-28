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
class TestFedex:
    
    def test_fedex_9c62f688(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.ID, "trackingnumber").clear()
        self.driver.find_element(By.ID, "trackingnumber").send_keys("3023858502")
        self.driver.find_element(By.ID, "btnSingleTrack").click()
    
    def test_fedex_9db512af(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Shipping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shipping Rates & Delivery Times')]").click()
        self.driver.find_element(By.ID, "fromGoogleAddress").click()
        self.driver.find_element(By.ID, "fromGoogleAddress").clear()
        self.driver.find_element(By.ID, "fromGoogleAddress").send_keys("Texas")
        self.driver.find_element(By.XPATH, "//ul[@id='e2eGoogleAddressSuggestionList']/li[1]/span[1]").click()
        self.driver.find_element(By.ID, "toGoogleAddress").clear()
        self.driver.find_element(By.ID, "toGoogleAddress").send_keys("New York")
        self.driver.find_element(By.XPATH, "//ul[@id='e2eGoogleAddressSuggestionList']/li[1]/span[1]").click()
        self.driver.find_element(By.ID, "package-details__weight-0").clear()
        self.driver.find_element(By.ID, "package-details__weight-0").send_keys("4")
        self.driver.find_element(By.ID, "e2ePackageDetailsSubmitButtonRates").click()
    
    def test_fedex_9e03f99a(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Shipping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Freight')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Track Freight')]").click()
        self.driver.find_element(By.ID, "tab-list-item-tab_panel_3").click()
        self.driver.find_element(By.ID, "tracking_number_0_1662431322510").clear()
        self.driver.find_element(By.ID, "tracking_number_0_1662431322510").send_keys("3345654345")
        self.driver.find_element(By.ID, "tbrDestCntry").clear()
        self.driver.find_element(By.ID, "tbrDestCntry").select("UNITED STATES")
        self.driver.find_element(By.XPATH, "//div[@id='tab_panel_3']/app-track-by-reference[1]/div[1]/div[3]/trk-shared-form-input[1]/div[1]/label[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='tab_panel_3']/app-track-by-reference[1]/div[1]/div[3]/trk-shared-form-input[1]/div[1]/label[1]").send_keys("344565432")
        self.driver.find_element(By.XPATH, "//div[@id='tab_panel_3']/app-track-by-reference[1]/div[1]/div[4]/div[1]/trk-shared-form-input[1]/div[1]/label[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='tab_panel_3']/app-track-by-reference[1]/div[1]/div[4]/div[1]/trk-shared-form-input[1]/div[1]/label[1]").send_keys("44912")
        self.driver.find_element(By.XPATH, "//div[@id='tab_panel_3']/app-track-by-reference[1]/div[1]/div[4]/div[2]/trk-shared-date-picker[1]/div[1]/button[1]/span[1]/trk-shared-icon[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//mat-calendar[@id='mat-datepicker-1']/div[1]/mat-month-view[1]/table[1]/tbody[1]/tr[5]/td[6]/div[1]").click()
        self.driver.find_element(By.ID, "track").click()
    
    def test_fedex_4271fa7e(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//li[@id='cubeThreePar']/button[1]/svg[1]").click()
        self.driver.find_element(By.ID, "DirectorySearchInput").clear()
        self.driver.find_element(By.ID, "DirectorySearchInput").send_keys("90028")
        self.driver.find_element(By.XPATH, "//ul[@id='results']/li[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='js-locator']/div[3]/div[2]/div[1]/div[2]/input[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='js-yl-007QM']/article[1]/div[1]/h3[1]/span[1]").click()
    
    def test_fedex_45e1d59f(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//li[@id='cubeThreePar']/button[1]/svg[1]").click()
        self.driver.find_element(By.ID, "DirectorySearchInput").clear()
        self.driver.find_element(By.ID, "DirectorySearchInput").send_keys("10019")
        self.driver.find_element(By.XPATH, "//ul[@id='results']/li[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='js-locator']/div[3]/div[2]/div[1]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='fdxType-filters-label']/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='staffed' and @value='on' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//button[@id='js-form-submit']/span[1]").click()
    
    def test_fedex_4d3f660a(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Design & Print')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Browse Services')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn More')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='config-accordion']/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='config-accordion']/div[2]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='config-accordion']/div[5]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='config-accordion']/div[6]/ul[1]/li[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='config-accordion']/div[7]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='config-accordion']/div[8]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='config-accordion']/div[9]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='config-accordion']/div[10]/ul[1]/li[2]").click()
    
    def test_fedex_27620cc4(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Shipping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shipping Rates & Delivery Times')]").click()
        self.driver.find_element(By.ID, "fromGoogleAddress").clear()
        self.driver.find_element(By.ID, "fromGoogleAddress").send_keys("New York")
        self.driver.find_element(By.XPATH, "//li[@role='option']").click()
        self.driver.find_element(By.ID, "toGoogleAddress").clear()
        self.driver.find_element(By.ID, "toGoogleAddress").send_keys("London")
        self.driver.find_element(By.XPATH, "//ul[@id='e2eGoogleAddressSuggestionList']/li[1]/span[1]").click()
        self.driver.find_element(By.ID, "package-details__package-type").clear()
        self.driver.find_element(By.ID, "package-details__package-type").select("FedEx Medium Box")
        self.driver.find_element(By.ID, "package-details__quantity-0").clear()
        self.driver.find_element(By.ID, "package-details__quantity-0").select("2")
        self.driver.find_element(By.ID, "package-details__weight-0").clear()
        self.driver.find_element(By.ID, "package-details__weight-0").send_keys("25")
        self.driver.find_element(By.ID, "packageShipDate").clear()
        self.driver.find_element(By.ID, "packageShipDate").select("Tuesday, March 28, 2023")
        self.driver.find_element(By.ID, "e2ePackageDetailsSubmitButtonRates").click()
    
    def test_fedex_b677741c(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Central & South America')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'English')]").click()
    
    def test_fedex_ba68208c(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//li[@id='cubeOnePar']/button[1]").click()
        self.driver.find_element(By.ID, "fromGoogleAddress").clear()
        self.driver.find_element(By.ID, "fromGoogleAddress").send_keys("Miami, FL")
        self.driver.find_element(By.XPATH, "//ul[@id='e2eGoogleAddressSuggestionList']/li[1]/span[1]/strong[1]").click()
        self.driver.find_element(By.ID, "toGoogleAddress").clear()
        self.driver.find_element(By.ID, "toGoogleAddress").send_keys("San Francisco, CA")
        self.driver.find_element(By.XPATH, "//ul[@id='e2eGoogleAddressSuggestionList']/li[1]/span[1]/strong[1]").click()
        self.driver.find_element(By.ID, "package-details__weight-0").clear()
        self.driver.find_element(By.ID, "package-details__weight-0").send_keys("10")
        self.driver.find_element(By.ID, "e2ePackageDetailsSubmitButtonRates").click()
    
    def test_fedex_c8426127(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Shipping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Packing & Shipping Supplies')]").click()
        self.driver.find_element(By.XPATH, "//img[@alt='alt=\"\"']").click()
    
    def test_fedex_f9d02b1b(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Locations')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drop Off a Package')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Drop Off location')]").click()
        self.driver.find_element(By.ID, "DirectorySearchInput").clear()
        self.driver.find_element(By.ID, "DirectorySearchInput").send_keys("49103")
        self.driver.find_element(By.XPATH, "//li[@role='option']").click()
        self.driver.find_element(By.XPATH, "//li[@id='js-yl-SBNDH']/article[1]/div[1]/h3[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]").click()
    
    def test_fedex_fb498b54(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Design & Print')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore Print, Products & Design')]").click()
        self.driver.find_element(By.XPATH, "//img[@title='Backlit Poster Sign']").click()
        self.driver.find_element(By.XPATH, "//div[@id='config-accordion']/div[3]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='config-accordion']/div[4]/ul[1]/li[4]").click()
    
    def test_fedex_14d29c07(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Shipping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedule & Manage Pickups')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'One-time pickup')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'pickup request')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[10]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/label[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='submit' and @value='Continue  >>' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//select[@name='questionCd9' and @title='Answer is required.']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='questionCd9' and @title='Answer is required.']").select("Today")
        self.driver.find_element(By.XPATH, "//select[@name='questionCd10' and @title='Answer is required.']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='questionCd10' and @title='Answer is required.']").select("No")
        self.driver.find_element(By.XPATH, "//select[@name='questionCd11' and @title='Answer is required.']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='questionCd11' and @title='Answer is required.']").select("No")
        self.driver.find_element(By.ID, "CCType").clear()
        self.driver.find_element(By.ID, "CCType").select("MasterCard")
        self.driver.find_element(By.ID, "creditCardNumber").clear()
        self.driver.find_element(By.ID, "creditCardNumber").send_keys("4564456745689874")
        self.driver.find_element(By.ID, "creditCardIDNumber").clear()
        self.driver.find_element(By.ID, "creditCardIDNumber").send_keys("265")
        self.driver.find_element(By.ID, "monthExpiry").clear()
        self.driver.find_element(By.ID, "monthExpiry").select("01")
        self.driver.find_element(By.ID, "yearExpiry").clear()
        self.driver.find_element(By.ID, "yearExpiry").select("26")
        self.driver.find_element(By.ID, "Complete").click()
    
    def test_fedex_1a9de745(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View Jobs')]").click()
        self.driver.find_element(By.ID, "location-search").click()
        self.driver.find_element(By.ID, "location-search").clear()
        self.driver.find_element(By.ID, "location-search").send_keys("United States")
        self.driver.find_element(By.XPATH, "//mat-option[@id='mat-option-241']/span[1]/span[1]").click()
    
    def test_fedex_1f339e44(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'SHIP TO HOMES')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See pickup options')]").click()
    
    def test_fedex_27437134(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Shipping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shipping Rates & Delivery Times')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'LTL Rates')]").click()
        self.driver.find_element(By.ID, "fromAddress").clear()
        self.driver.find_element(By.ID, "fromAddress").send_keys("Chicago")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]").click()
        self.driver.find_element(By.ID, "toAddress").clear()
        self.driver.find_element(By.ID, "toAddress").send_keys("Kansas")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]").click()
        self.driver.find_element(By.ID, "uomData_0").clear()
        self.driver.find_element(By.ID, "uomData_0").select("Carton")
        self.driver.find_element(By.ID, "weight_0").clear()
        self.driver.find_element(By.ID, "weight_0").send_keys("5000")
        self.driver.find_element(By.ID, "classData_0").clear()
        self.driver.find_element(By.ID, "classData_0").select("50.0")
        self.driver.find_element(By.ID, "number_0").clear()
        self.driver.find_element(By.ID, "number_0").send_keys("2")
        self.driver.find_element(By.ID, "declaredValue").clear()
        self.driver.find_element(By.ID, "declaredValue").send_keys("20000")
        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form[1]/fieldset[1]/div[1]/div[2]/div[3]/app-addtional-services[1]/form[1]/div[5]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form[1]/fieldset[1]/div[1]/div[2]/div[3]/app-addtional-services[1]/form[1]/div[5]/div[1]/div[1]/div[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form[1]/fieldset[1]/div[1]/div[2]/div[3]/app-addtional-services[1]/form[1]/div[5]/div[1]/div[2]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form[1]/fieldset[1]/div[1]/div[2]/div[3]/app-addtional-services[1]/form[1]/div[5]/div[1]/div[2]/div[2]/div[4]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form[1]/fieldset[1]/div[1]/div[2]/div[3]/app-addtional-services[1]/form[1]/div[5]/div[1]/div[3]/div[1]/button[1]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form[1]/fieldset[1]/div[1]/div[2]/div[3]/app-addtional-services[1]/form[1]/div[5]/div[1]/div[3]/div[2]/div[5]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
    
    def test_fedex_042bde97(self):
        # self.driver.get("https://www.fedex.com/en-us/home.html")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Shipping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shipping Rates & Delivery Times')]").click()
        self.driver.find_element(By.ID, "fromGoogleAddress").clear()
        self.driver.find_element(By.ID, "fromGoogleAddress").send_keys("10019")
        self.driver.find_element(By.XPATH, "//ul[@id='e2eGoogleAddressSuggestionList']/li[1]/span[1]/strong[1]").click()
        self.driver.find_element(By.ID, "toGoogleAddress").clear()
        self.driver.find_element(By.ID, "toGoogleAddress").send_keys("90028")
        self.driver.find_element(By.XPATH, "//li[@role='option']").click()
        self.driver.find_element(By.ID, "package-details__weight-0").clear()
        self.driver.find_element(By.ID, "package-details__weight-0").send_keys("3")
        self.driver.find_element(By.ID, "e2ePackageDetailsSubmitButtonRates").click()
        self.driver.find_element(By.XPATH, "//button[@id='toggle-3-0']/fdx-icon[1]/svg[1]").click()
    