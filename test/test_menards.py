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
class TestMenards:
    
    def test_menards_12cbd3a8(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.XPATH, "//button[@id='d60e7556-febe-4d59-8726-a659ea3e10c9']/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'My Lists')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View / Add List')]").click()
        self.driver.find_element(By.ID, "createButton").click()
    
    def test_menards_08840c76(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.XPATH, "//input[@name='search' and @type='text' and @placeholder='Enter SKU, Model # or Keyword']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search' and @type='text' and @placeholder='Enter SKU, Model # or Keyword']").send_keys("front load washing machine")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.ID, "priceMax").clear()
        self.driver.find_element(By.ID, "priceMax").send_keys("800")
        self.driver.find_element(By.XPATH, "//input[@value='GO' and @type='button']").click()
        self.driver.find_element(By.ID, "actionButton1541489389106").click()
    
    def test_menards_7b99ca15(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.XPATH, "//input[@name='search' and @type='text' and @placeholder='Enter SKU, Model # or Keyword']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search' and @type='text' and @placeholder='Enter SKU, Model # or Keyword']").send_keys("swivel vacuum")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/header[1]/div[2]/div[2]/nav[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.ID, "priceMax").clear()
        self.driver.find_element(By.ID, "priceMax").send_keys("150")
        self.driver.find_element(By.XPATH, "//input[@value='GO' and @type='button']").click()
        self.driver.find_element(By.ID, "actionButton1642874264860848").click()
    
    def test_menards_a4a06039(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.ID, "56bf2da9-4496-42d0-af4b-b4cc10f748db").click()
        self.driver.find_element(By.ID, "header-zip-input").clear()
        self.driver.find_element(By.ID, "header-zip-input").send_keys("82718")
        self.driver.find_element(By.XPATH, "//button[@id='header-zip-submit']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Make My Store')]").click()
        self.driver.find_element(By.ID, "530857d0-c7e7-4094-99a5-833572dc3084").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View All Flyers')]").click()
    
    def test_menards_a690af04(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.ID, "549951c0-3ff4-456e-b9ff-c9dde716aac2").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'My Lists')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='myListsIntroduction']/div[1]/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.ID, "addNewListButton").click()
        self.driver.find_element(By.ID, "title").clear()
        self.driver.find_element(By.ID, "title").send_keys("Bathroom Remodeling")
        self.driver.find_element(By.ID, "createButton").click()
    
    def test_menards_1bd729e8(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.XPATH, "//button[@id='1793d71e-a228-44b0-8035-d19b2f6b0d45']/svg[1]").click()
        self.driver.find_element(By.ID, "7918").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Painting Tools')]").click()
        self.driver.find_element(By.ID, "12ab7254-b634-4962-a072-5673cc68d760").clear()
        self.driver.find_element(By.ID, "12ab7254-b634-4962-a072-5673cc68d760").send_keys("44240")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//label[@role='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='spec_producttype_facetfacetsBody']/div[1]/div[4]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='brandname_facetfacetsBody']/div[1]/div[4]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='1444452036915']/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]").click()
        self.driver.find_element(By.ID, "addToListSelect").clear()
        self.driver.find_element(By.ID, "addToListSelect").select("Wish List")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View Your List')]").click()
    
    def test_menards_e224beac(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.ID, "9fc6bb1a-1d0a-47a6-9031-647a41ba94ba").click()
        self.driver.find_element(By.ID, "6290").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Smart Home')]").click()
        self.driver.find_element(By.ID, "image-0e393b7b-eb5a-4b00-8f30-4f71b9d729f4").click()
        self.driver.find_element(By.XPATH, "//div[@id='categoryhierarchy_facetfacetsBody']/div[1]/div[3]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='spec_producttype_facetfacetsBody']/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='sortByDropdownButton']/strong[1]").click()
        self.driver.find_element(By.ID, "sortBy1").click()
        self.driver.find_element(By.ID, "actionButton1557729340401").click()
        self.driver.find_element(By.ID, "viewCartBtn").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='shippingOption192162226']/div[2]/label[1]").click()
    
    def test_menards_4775a0e3(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.ID, "27460a97-812f-4fb9-a6a9-75ef436eed9e").click()
        self.driver.find_element(By.ID, "header-zip-input").clear()
        self.driver.find_element(By.ID, "header-zip-input").send_keys("59901")
        self.driver.find_element(By.XPATH, "//button[@id='header-zip-submit']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Make My Store')]").click()
        self.driver.find_element(By.ID, "cd30bc3f-89f8-4419-a2c3-af80207066e5").click()
        self.driver.find_element(By.ID, "19741").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Grocery')]").click()
        self.driver.find_element(By.ID, "image-b33bd789-f72e-451a-b7a5-b79456aacd91").click()
        self.driver.find_element(By.XPATH, "//div[@id='facetMenu']/div[1]/div[1]/div[1]/div[2]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='spec_producttype_facetfacetsBody']/div[1]/div[3]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='1444431274734']/div[1]/div[1]/div[7]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='1444431274734']/div[1]/div[1]/div[7]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='1444431274734']/div[1]/div[1]/div[7]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='1444431274734']/div[1]/div[1]/div[7]/button[2]/svg[1]").click()
        self.driver.find_element(By.ID, "actionButton1444431274734").click()
        self.driver.find_element(By.ID, "viewCartBtn").click()
    
    def test_menards_78e346d2(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.ID, "ee0f078e-d798-4e26-9aee-82f5f8906c33").click()
        self.driver.find_element(By.ID, "orderNumber").clear()
        self.driver.find_element(By.ID, "orderNumber").send_keys("456481897")
        self.driver.find_element(By.ID, "secondaryInput").clear()
        self.driver.find_element(By.ID, "secondaryInput").send_keys("898-448-6474")
        self.driver.find_element(By.ID, "trackerSearchButton").click()
    
    def test_menards_9e44c63b(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.ID, "fd18ad38-ccf6-48e0-9128-53925fefe209").click()
        self.driver.find_element(By.ID, "image-75fe0033-d866-4fab-8fc7-676cd2cc77d9").click()
        self.driver.find_element(By.XPATH, "//input[@type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Monty")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/form[1]/div[2]/div[1]/span[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/form[1]/div[2]/div[1]/span[1]/input[1]").send_keys("Lue")
        self.driver.find_element(By.ID, "house-num").clear()
        self.driver.find_element(By.ID, "house-num").send_keys("4847")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/form[1]/div[3]/div[2]/span[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/form[1]/div[3]/div[2]/span[1]/input[1]").send_keys("10019")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/form[1]/div[4]/div[1]/button[1]").click()
    
    def test_menards_24de7f7d(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.XPATH, "//svg[@role='presentation']").click()
        self.driver.find_element(By.XPATH, "//button[@id='679bbee9-5f2c-4469-a6cf-f76711ccb188']/span[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.ID, "header-zip-input").clear()
        self.driver.find_element(By.ID, "header-zip-input").send_keys("60538")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Store Locator')]").click()
        self.driver.find_element(By.ID, "zip-input").clear()
        self.driver.find_element(By.ID, "zip-input").send_keys("60538")
        self.driver.find_element(By.XPATH, "//button[@id='zip-submit']/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-locator-results']/ul[1]/li[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='search' and @type='text' and @placeholder='Enter SKU, Model # or Keyword']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search' and @type='text' and @placeholder='Enter SKU, Model # or Keyword']").send_keys("Magtag electric dryer")
        self.driver.find_element(By.XPATH, "//div[@id='5593']/div[2]/form[1]/button[1]/small[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='spec_capacity_facetfacetsBody']/div[1]/div[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='spec_capacity_facetfacetsBody']/div[1]/div[3]/div[1]/label[1]").click()
        self.driver.find_element(By.ID, "headerpriceFacets").click()
        self.driver.find_element(By.XPATH, "//div[@id='pricefacets']/button[1]/span[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.ID, "priceMin").clear()
        self.driver.find_element(By.ID, "priceMin").send_keys("0")
        self.driver.find_element(By.ID, "priceMax").clear()
        self.driver.find_element(By.ID, "priceMax").send_keys("1000")
        self.driver.find_element(By.XPATH, "//input[@value='GO' and @type='button']").click()
    
    def test_menards_3d7f4f43(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.XPATH, "//a[@id='4799bca2-ca9c-4ec1-b284-38be0c831ebf']/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='gcTypeVariations']/div[1]/label[1]/div[1]").click()
        self.driver.find_element(By.ID, "amount").clear()
        self.driver.find_element(By.ID, "amount").send_keys("50")
        self.driver.find_element(By.XPATH, "//div[@id='gcItemDetails']/div[7]/div[1]/div[2]/div[8]/button[1]").click()
        self.driver.find_element(By.ID, "mcom-image-621298c7-8abd-4e5a-ab92-8688a6ea59d2").click()
        self.driver.find_element(By.ID, "gcTo").clear()
        self.driver.find_element(By.ID, "gcTo").send_keys("John")
        self.driver.find_element(By.ID, "gcFrom").clear()
        self.driver.find_element(By.ID, "gcFrom").send_keys("James")
        self.driver.find_element(By.ID, "gcMessage").clear()
        self.driver.find_element(By.ID, "gcMessage").send_keys("Congrats on your new home.")
        self.driver.find_element(By.ID, "addToCartButton").click()
        self.driver.find_element(By.XPATH, "//form[@id='frm']/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
    
    def test_menards_40bf7303(self):
        # self.driver.get("https://menards.com")
        self.driver.find_element(By.XPATH, "//button[@id='ad78aa1c-f637-478a-9131-c5c9f343d4dd']/svg[1]").click()
        self.driver.find_element(By.ID, "7200").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Kitchen Sinks')]").click()
        self.driver.find_element(By.ID, "image-3f3a514a-3fb3-4f1a-b1e3-220c6cc754cb").click()
        self.driver.find_element(By.XPATH, "//div[@id='shippingoptions_facetfacetsBody']/div[1]/div[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='spec_sinkmaterial_facetfacetsBody']/div[1]/div[5]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='spec_bowlconfiguration_facetfacetsBody']/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='spec_overallwidth_facetfacetsBody']/div[1]/div[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='sortByDropdownButton']/strong[1]").click()
        self.driver.find_element(By.ID, "sortBy1").click()
        self.driver.find_element(By.XPATH, "//span[@id='compareLabel60890701931']/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='compareLabel3149259783593504']/span[1]/span[1]").click()
        self.driver.find_element(By.ID, "compare").click()
    