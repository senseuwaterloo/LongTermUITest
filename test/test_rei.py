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
class TestRei:
    
    def test_rei_826e2b3e(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//input[@role='searchbox' and @name='q' and @type='text' and @placeholder='Search for great gear & clothing' and @title='search input field']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='searchbox' and @name='q' and @type='text' and @placeholder='Search for great gear & clothing' and @title='search input field']").send_keys("Yaktrax traction cleats")
        self.driver.find_element(By.XPATH, "//button[@id='search-button']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-size']/div[1]/ul[1]/li[3]/span[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-results']/ul[1]/li[1]/a[2]/h2[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-color-size-component']/div[2]/fieldset[1]/div[1]/div[1]/button[2]").click()
        self.driver.find_element(By.ID, "add-to-cart-button").click()
    
    def test_rei_5099fc8a(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//header[@id='headerWrapper']/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='app']/div[1]/section[1]/div[1]/div[2]/div[2]/button[1]").click()
    
    def test_rei_615b59c3(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[15]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='app']/div[1]/section[1]/div[2]/div[1]/section[2]/button[28]/img[1]").click()
        self.driver.find_element(By.ID, "cdr-id-93bf8a").click()
        self.driver.find_element(By.ID, "cdr-id-93bf8a").clear()
        self.driver.find_element(By.ID, "cdr-id-93bf8a").send_keys("James Smith")
        self.driver.find_element(By.ID, "cdr-id-f12ccb").clear()
        self.driver.find_element(By.ID, "cdr-id-f12ccb").send_keys("James Smith")
        self.driver.find_element(By.ID, "cdr-id-48a1c4").clear()
        self.driver.find_element(By.ID, "cdr-id-48a1c4").send_keys("100")
        self.driver.find_element(By.ID, "cdr-id-7e2f2f").clear()
        self.driver.find_element(By.ID, "cdr-id-7e2f2f").send_keys("abc@abc.com")
        self.driver.find_element(By.ID, "cdr-id-a5497d").clear()
        self.driver.find_element(By.ID, "cdr-id-a5497d").send_keys("abc@abc.com")
        self.driver.find_element(By.ID, "cdr-id-f20cf1").clear()
        self.driver.find_element(By.ID, "cdr-id-f20cf1").send_keys("Best Wishes")
        self.driver.find_element(By.XPATH, "//main[@id='app']/div[1]/section[1]/div[2]/form[1]/div[1]/section[2]/div[9]/button[2]").click()
    
    def test_rei_c59043d8(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//header[@id='headerWrapper']/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "2").clear()
        self.driver.find_element(By.ID, "2").select("Cycling")
        self.driver.find_element(By.ID, "7").clear()
        self.driver.find_element(By.ID, "7").send_keys("new york city")
        self.driver.find_element(By.XPATH, "//div[@id='page-content']/section[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-content']/section[1]/div[1]/div[1]/div[1]/form[1]/div[4]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mountain Biking (2)')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='er-results']/div[1]/article[2]/div[2]/div[1]/h2[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Details & sign up')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='app']/section[3]/div[2]/form[1]/button[1]").click()
        self.driver.find_element(By.ID, "192").clear()
        self.driver.find_element(By.ID, "192").send_keys("Joe")
        self.driver.find_element(By.ID, "194").clear()
        self.driver.find_element(By.ID, "194").send_keys("Bloggs")
        self.driver.find_element(By.ID, "196").clear()
        self.driver.find_element(By.ID, "196").send_keys("joe@joebloggs.com")
        self.driver.find_element(By.ID, "198").clear()
        self.driver.find_element(By.ID, "198").send_keys("1111111111")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]/section[1]/aside[1]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "347").clear()
        self.driver.find_element(By.ID, "347").send_keys("June")
        self.driver.find_element(By.ID, "349").clear()
        self.driver.find_element(By.ID, "349").send_keys("Bloggs")
        self.driver.find_element(By.ID, "349").clear()
        self.driver.find_element(By.ID, "349").send_keys("2222222222")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]/section[1]/article[1]/div[2]/section[1]/section[1]/form[3]/fieldset[1]/div[1]/div[2]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]/section[1]/article[1]/div[2]/section[1]/section[1]/form[3]/fieldset[2]/div[1]/div[2]/label[1]").click()
        self.driver.find_element(By.ID, "366").clear()
        self.driver.find_element(By.ID, "366").send_keys("6")
        self.driver.find_element(By.ID, "368").clear()
        self.driver.find_element(By.ID, "368").send_keys("0")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]/section[1]/aside[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]/section[1]/article[1]/div[2]/section[1]/section[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]/section[1]/article[1]/div[2]/section[1]/section[1]/div[2]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]/section[1]/article[1]/div[2]/section[1]/section[1]/div[3]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]/section[1]/aside[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]").click()
    
    def test_rei_09675529(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//header[@id='headerWrapper']/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trade in by mail')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='q' and @value='' and @type='text' and @placeholder='Search by brand, description, or item']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='q' and @value='' and @type='text' and @placeholder='Search by brand, description, or item']").send_keys("Nemo Front Porch 2P Tent")
        self.driver.find_element(By.XPATH, "//div[@id='REI']/main[1]/div[1]/section[2]/div[1]/div[1]/form[1]/button[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='REI']/main[1]/div[1]/section[3]/article[1]/div[2]/ol[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Complete trade-in')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='REI']/main[1]/div[1]/section[2]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "firstName").clear()
        self.driver.find_element(By.ID, "firstName").send_keys("Joe")
        self.driver.find_element(By.ID, "lastName").clear()
        self.driver.find_element(By.ID, "lastName").send_keys("Bloggs")
        self.driver.find_element(By.ID, "memberNumber").clear()
        self.driver.find_element(By.ID, "memberNumber").send_keys("123456789")
        self.driver.find_element(By.XPATH, "//div[@id='REI']/main[1]/div[1]/main[1]/section[1]/div[1]/div[1]/button[1]").click()
    
    def test_rei_0ff1648e(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\"Women's\")]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-size']/div[1]/ul[1]/li[3]/span[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-features']/div[1]/ul[1]/li[1]/span[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[@name='4-to-5']").click()
    
    def test_rei_7a40f4c8(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Hiking Footwear')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-features']/div[1]/ul[1]/li[1]/span[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[@name='3-to-5']").click()
    
    def test_rei_54e0d420(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[5]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Paddle Boards')]").click()
        self.driver.find_element(By.ID, "image-205254-0").click()
        self.driver.find_element(By.ID, "add-to-cart-button").click()
        self.driver.find_element(By.ID, "atc-modal-btn-checkout").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//button[@title='Continue with this address']").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_rei_8aae9804(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Camping Tents')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-sleeping_capacity']/div[1]/ul[1]/li[5]/span[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//select[@value='relevance']").clear()
        self.driver.find_element(By.XPATH, "//select[@value='relevance']").select("Price  Low - High")
    
    def test_rei_932c0ec6(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Stoves, Grills & Fuel')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-features']/div[1]/ul[1]/li[2]/span[1]/a[1]").click()
    
    def test_rei_ad0369b6(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[13]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[13]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Climbing')]").click()
        self.driver.find_element(By.XPATH, "//select[@value='relevance']").clear()
        self.driver.find_element(By.XPATH, "//select[@value='relevance']").select("Price  Low - High")
        self.driver.find_element(By.ID, "image-208063-0").click()
        self.driver.find_element(By.ID, "add-to-cart-button").click()
        self.driver.find_element(By.ID, "atc-modal-btn-checkout").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").click()
    
    def test_rei_8865ca64(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop Services')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a bike shop near you')]").click()
        self.driver.find_element(By.ID, "13").clear()
        self.driver.find_element(By.ID, "13").send_keys("10013")
        self.driver.find_element(By.XPATH, "//section[@id='locations']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See services menu')]").click()
    
    def test_rei_d4298ee7(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Hammocks')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Camping Hammocks')]").click()
        self.driver.find_element(By.XPATH, "//select[@value='relevance']").clear()
        self.driver.find_element(By.XPATH, "//select[@value='relevance']").select("Price  Low - High")
    
    def test_rei_2eaf60d5(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//header[@id='headerWrapper']/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\"Women's\")]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Running Shoes')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='REI']/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[2]/section[3]/fieldset[1]/article[1]/label[1]").click()
        self.driver.find_element(By.ID, "sort-by").clear()
        self.driver.find_element(By.ID, "sort-by").select("Price  Low - High")
        self.driver.find_element(By.XPATH, "//div[@id='REI']/main[1]/div[1]/section[1]/article[1]/div[2]/ol[1]/li[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.ID, "5").click()
        self.driver.find_element(By.ID, "GRADE_A").click()
        self.driver.find_element(By.XPATH, "//div[@id='REI']/main[1]/div[1]/div[1]/article[1]/section[1]/div[6]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Confirm Membership to Checkout')]").click()
        self.driver.find_element(By.ID, "firstName").clear()
        self.driver.find_element(By.ID, "firstName").send_keys("Joe")
        self.driver.find_element(By.ID, "lastName").clear()
        self.driver.find_element(By.ID, "lastName").send_keys("Bloggs")
        self.driver.find_element(By.ID, "memberNumber").clear()
        self.driver.find_element(By.ID, "memberNumber").send_keys("123456789")
        self.driver.find_element(By.XPATH, "//div[@id='REI']/main[1]/div[1]/main[1]/section[1]/div[1]/div[1]/button[1]").click()
    
    def test_rei_486bdb13(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//input[@role='searchbox' and @name='q' and @type='text' and @placeholder='Search for great gear & clothing' and @title='search input field']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='searchbox' and @name='q' and @type='text' and @placeholder='Search for great gear & clothing' and @title='search input field']").send_keys("gobites uno spork")
        self.driver.find_element(By.XPATH, "//button[@id='search-button']/svg[1]").click()
        self.driver.find_element(By.ID, "image-131279-0").click()
        self.driver.find_element(By.XPATH, "//button[@name='109389' and @type='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[3]/div[3]/form[1]/fieldset[1]/div[1]/div[3]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-fulfillment-details']/button[1]").click()
        self.driver.find_element(By.ID, "cdr-id-36a0b7").clear()
        self.driver.find_element(By.ID, "cdr-id-36a0b7").send_keys("Seattle, WA")
        self.driver.find_element(By.XPATH, "//div[@id='page-body']/div[6]/div[1]/div[3]/div[1]/section[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='store-results-list']/li[1]/div[4]/button[1]").click()
        self.driver.find_element(By.ID, "atc-modal-btn-checkout").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").click()
        self.driver.find_element(By.XPATH, "//button[@title='Continue with this address']").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.ID, "credit_card_id").clear()
        self.driver.find_element(By.ID, "credit_card_id").send_keys("123456789")
        self.driver.find_element(By.ID, "expr_month").clear()
        self.driver.find_element(By.ID, "expr_month").send_keys("01")
        self.driver.find_element(By.ID, "expr_year").clear()
        self.driver.find_element(By.ID, "expr_year").select("2024")
        self.driver.find_element(By.ID, "security_code").clear()
        self.driver.find_element(By.ID, "security_code").send_keys("123")
    
    def test_rei_70b3ef5b(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[3]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop all climbing gear')]").click()
        self.driver.find_element(By.XPATH, "//select[@value='relevance']").clear()
        self.driver.find_element(By.XPATH, "//select[@value='relevance']").select("Price  High - Low")
    
    def test_rei_af6655c8(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//header[@id='headerWrapper']/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[7]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "2").clear()
        self.driver.find_element(By.ID, "2").select("Climbing")
        self.driver.find_element(By.ID, "7").clear()
        self.driver.find_element(By.ID, "7").send_keys("90028")
        self.driver.find_element(By.ID, "15").clear()
        self.driver.find_element(By.ID, "15").select("Within 50 miles")
        self.driver.find_element(By.XPATH, "//div[@id='page-content']/section[1]/div[1]/div[1]/div[1]/form[1]/div[4]/button[1]").click()
    
    def test_rei_4e3cc9e2(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[9]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Travel Backpacks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-best_use']/div[1]/ul[1]/li[2]/span[1]/a[1]").click()
    
    def test_rei_d6c1c4f5(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//footer[@id='page-footer']/div[2]/div[3]/div[2]/div[1]/a[1]").click()
        self.driver.find_element(By.ID, "4").clear()
        self.driver.find_element(By.ID, "4").send_keys("37863")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/section[1]/div[1]/div[2]/article[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See rentals menu')]").click()
        self.driver.find_element(By.ID, "category-item-cycling-gear-6").click()
    
    def test_rei_1bf4f465(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='secondary-nav']/div[2]/div[1]/ul[1]/li[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='mm-camping-and-hiking-hiking-backpacks']/li[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-gear_capacity_l_range']/div[1]/ul[1]/li[3]/span[1]/a[1]").click()
    
    def test_rei_277a776a(self):
        # self.driver.get("https://www.rei.com/")
        self.driver.find_element(By.XPATH, "//input[@role='searchbox' and @name='q' and @type='text' and @placeholder='Search for great gear & clothing' and @title='search input field']").click()
        self.driver.find_element(By.XPATH, "//input[@role='searchbox' and @name='q' and @type='text' and @placeholder='Search for great gear & clothing' and @title='search input field']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='searchbox' and @name='q' and @type='text' and @placeholder='Search for great gear & clothing' and @title='search input field']").send_keys("Kayaks")
        self.driver.find_element(By.XPATH, "//li[@id='autosuggest-result-0']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Whitewater Kayaks')]").click()
    