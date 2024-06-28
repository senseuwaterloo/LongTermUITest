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
class TestAmazon:
    
    def test_amazon_1140f858(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.XPATH, "//a[@id='nav-hamburger-menu']/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hmenu-content']/ul[1]/li[29]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hmenu-content']/ul[1]/ul[2]/li[7]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All gift cards')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s-refinements']/div[2]/ul[1]/li[12]/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_format_browse-bin/2740966011']/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_36/2661614011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[15]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.ID, "gc-order-form-quantity").clear()
        self.driver.find_element(By.ID, "gc-order-form-quantity").send_keys("2")
        self.driver.find_element(By.ID, "gc-buy-box-atc").click()
    
    def test_amazon_e3143d13(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("wireless headphones")
        self.driver.find_element(By.XPATH, "//div[@role='button']").click()
        self.driver.find_element(By.ID, "high-price").clear()
        self.driver.find_element(By.ID, "high-price").send_keys("100")
        self.driver.find_element(By.XPATH, "//span[@id='a-autoid-1']/span[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_feature_two_browse-bin/23746030011']/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "add-to-cart-button").click()
    
    def test_amazon_1c6bfd10(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.XPATH, "//a[@id='nav-hamburger-menu']/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hmenu-content']/ul[1]/li[12]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Kindle Books')]").click()
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("roman empire history")
        self.driver.find_element(By.ID, "nav-search-submit-button").click()
        self.driver.find_element(By.XPATH, "//li[@id='n/154606011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_feature_nine_browse-bin/3291437011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_date/1249101011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='a-autoid-18-announce']/span[2]").click()
        self.driver.find_element(By.ID, "s-result-sort-select_4").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.ID, "add-to-wishlist-button-submit").click()
        self.driver.find_element(By.XPATH, "//span[@id='wl-redesigned-create-list']/span[1]/span[1]/input[1]").click()
    
    def test_amazon_581da9fe(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("mens black running shoes")
        self.driver.find_element(By.ID, "nav-search-submit-button").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_72/2661618011']/span[1]/a[1]/section[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='size_name_10']/span[1]/input[1]").click()
        self.driver.find_element(By.ID, "add-to-cart-button").click()
    
    def test_amazon_5f2c3149(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("dog food")
        self.driver.find_element(By.XPATH, "//div[@id='nav-flyout-searchAjax']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_feature_eleven_browse-bin/6514407011']/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_72/2661618011']/span[1]/a[1]/section[1]/i[1]").click()
        self.driver.find_element(By.ID, "a-autoid-10-announce").click()
        self.driver.find_element(By.ID, "s-result-sort-select_1").click()
    
    def test_amazon_dc636898(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Amazon Basics')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='nav-area']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/nav[1]/ul[1]/li[2]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='nav-area']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/nav[1]/ul[1]/li[2]/div[1]/ul[1]/li[5]/a[1]").click()
        self.driver.find_element(By.ID, "a-autoid-0-announce").click()
    
    def test_amazon_04b8b406(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Google Play")
        self.driver.find_element(By.XPATH, "//div[@role='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.ID, "gc-mini-picker-amount-4").click()
        self.driver.find_element(By.ID, "gc-order-form-recipients").clear()
        self.driver.find_element(By.ID, "gc-order-form-recipients").send_keys("abc@abc.com")
        self.driver.find_element(By.ID, "gc-buy-box-atc").click()
    
    def test_amazon_61563837(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.XPATH, "//a[@id='nav-hamburger-menu']/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hmenu-content']/ul[1]/li[22]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hmenu-content']/ul[1]/ul[1]/li[3]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drives & Storage')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s-refinements']/div[1]/ul[1]/li[5]/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='a-autoid-0-announce']/span[1]").click()
        self.driver.find_element(By.ID, "s-result-sort-select_1").click()
    
    def test_amazon_6fd2fbb1(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("smartwatch")
        self.driver.find_element(By.XPATH, "//div[@id='nav-flyout-searchAjax']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_feature_thirty_browse-bin/82343553011']/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.ID, "add-to-cart-button").click()
    
    def test_amazon_862faed7(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("surge protector")
        self.driver.find_element(By.XPATH, "//div[@id='nav-flyout-searchAjax']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='n/761520']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_feature_ten_browse-bin/17854131011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_36/1253503011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_72/1248879011']/span[1]/a[1]/section[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_condition-type/2224371011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='a-autoid-14-announce']/span[2]").click()
        self.driver.find_element(By.ID, "s-result-sort-select_1").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.ID, "a-autoid-4-announce").click()
        self.driver.find_element(By.ID, "quantity_1").click()
        self.driver.find_element(By.ID, "add-to-cart-button").click()
    
    def test_amazon_884a375b(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("dog bed 30 inches")
        self.driver.find_element(By.ID, "nav-search-submit-button").click()
        self.driver.find_element(By.XPATH, "/html").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_feature_browse-bin/23940584011']/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/div[1]/img[1]").click()
    
    def test_amazon_d64cbfc6(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("COMFORTER")
        self.driver.find_element(By.ID, "nav-search-submit-button").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_89/Amazon Basics']/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_size_browse-bin/362280011']/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_72/1248915011']/span[1]/a[1]/section[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_36/1253525011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='a-autoid-9-announce']/span[2]").click()
        self.driver.find_element(By.ID, "s-result-sort-select_1").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/h2[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='2' and @value='' and @type='submit']").click()
        self.driver.find_element(By.ID, "add-to-cart-button").click()
    
    def test_amazon_f754d919(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.XPATH, "//a[@id='nav-hamburger-menu']/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hmenu-content']/ul[1]/li[21]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Video Games')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s-refinements']/div[13]/ul[1]/li[2]/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='n/229575']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='n/318813011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='n/402052011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='a-autoid-0-announce']/span[2]").click()
        self.driver.find_element(By.ID, "s-result-sort-select_1").click()
    
    def test_amazon_fc21339a(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "nav-hamburger-menu").click()
        self.driver.find_element(By.XPATH, "//div[@id='hmenu-content']/ul[1]/li[29]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hmenu-content']/ul[1]/li[27]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Amazon Pharmacy')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='checkprices']/div[1]/div[3]/div[2]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='checkprices']/div[1]/div[3]/div[2]/div[1]/label[1]/span[1]").send_keys("Metformin 1000mg")
        self.driver.find_element(By.XPATH, "//div[@id='checkprices']/div[1]/div[3]/div[2]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/a[1]/div[1]/img[1]").click()
    
    def test_amazon_e62bcf45(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Sam Harris")
        self.driver.find_element(By.XPATH, "//div[@id='nav-flyout-searchAjax']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_72/1250221011']/span[1]/a[1]/section[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_feature_browse-bin/2656022011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/h2[1]").click()
    
    def test_amazon_f57e6c0a(self):
        # self.driver.get("https://amazon.com")
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("toilet paper")
        self.driver.find_element(By.ID, "nav-search-submit-button").click()
        self.driver.find_element(By.XPATH, "//span[@id='a-autoid-0-announce']/span[2]").click()
        self.driver.find_element(By.ID, "s-result-sort-select_1").click()
        self.driver.find_element(By.ID, "a-autoid-69-announce").click()
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("laundry detergent")
        self.driver.find_element(By.ID, "nav-search-submit-button").click()
        self.driver.find_element(By.XPATH, "//span[@id='a-autoid-7-announce']/span[2]").click()
        self.driver.find_element(By.ID, "s-result-sort-select_1").click()
        self.driver.find_element(By.ID, "a-autoid-74-announce").click()
    