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
class TestYellowpages:
    
    def test_yellowpages_32174c75(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.XPATH, "//a[@title='Search Attorneys']").click()
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("west hollywood")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-location']/li[2]/a[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='search-form']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/a[1]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/label[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/h3[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[3]/div[3]/label[4]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/h3[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[2]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/button[1]").click()
        self.driver.find_element(By.ID, "js-sort-toggle").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Distance')]").click()
    
    def test_yellowpages_34c474ef(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "query").clear()
        self.driver.find_element(By.ID, "query").send_keys("hair salon")
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("San Diego")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-location']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='search-form']/button[1]/span[1]").click()
    
    def test_yellowpages_a0b55038(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("Chicago")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-location']/li[1]/a[1]/b[1]").click()
        self.driver.find_element(By.ID, "query").clear()
        self.driver.find_element(By.ID, "query").send_keys("Dentist")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-term']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Aspen Dental')]").click()
    
    def test_yellowpages_3fdbadc8(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "popular-cities").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Miami')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content-container']/section[2]/div[1]/nav[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[1]/div[3]/label[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/h3[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[3]/div[1]/label[6]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[3]/div[1]/label[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filter-and-sort']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rating')]").click()
    
    def test_yellowpages_834dda72(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Las Vegas')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content-container']/section[2]/div[1]/nav[1]/a[8]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/h3[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[2]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/h3[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[3]/div[2]/label[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/button[1]").click()
    
    def test_yellowpages_b50ce7bf(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='quick-search']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'BY ADDRESS')]").click()
        self.driver.find_element(By.ID, "street").clear()
        self.driver.find_element(By.ID, "street").send_keys("Nice st - 1234")
        self.driver.find_element(By.ID, "city").clear()
        self.driver.find_element(By.ID, "city").send_keys("Good")
        self.driver.find_element(By.XPATH, "//select[@name='state']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='state']").select("FL")
        self.driver.find_element(By.XPATH, "//input[@value='Search by Address' and @type='submit']").click()
    
    def test_yellowpages_c5a20fb8(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.XPATH, "//a[@title='Search Dentists']").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/a[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/h3[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[3]/div[1]/label[9]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/button[1]").click()
        self.driver.find_element(By.ID, "js-sort-toggle").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Distance')]").click()
    
    def test_yellowpages_cc5908a9(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "popular-cities").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cleveland')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for more')]").click()
    
    def test_yellowpages_01bede1e(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='quick-search']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'BY PHONE�')]").click()
        self.driver.find_element(By.ID, "phone").clear()
        self.driver.find_element(By.ID, "phone").send_keys("123456789")
        self.driver.find_element(By.XPATH, "//input[@value='Search by Phone' and @type='submit']").click()
    
    def test_yellowpages_229199b4(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "q-and-a").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Insurance')]").click()
        self.driver.find_element(By.ID, "ask-question").clear()
        self.driver.find_element(By.ID, "ask-question").send_keys("Health Insurance Top Up plans beneficial or not?")
        self.driver.find_element(By.XPATH, "//article[@id='app']/main[1]/article[1]/section[1]/div[1]/div[1]/div[1]/ul[1]/footer[1]/button[1]").click()
    
    def test_yellowpages_3b390b60(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "popular-cities").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Fresno')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content-container']/section[2]/div[1]/nav[1]/a[1]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/label[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/button[1]").click()
    
    def test_yellowpages_a3edc9c7(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='quick-search']/li[1]/a[1]").click()
        self.driver.find_element(By.ID, "first").clear()
        self.driver.find_element(By.ID, "first").send_keys("John")
        self.driver.find_element(By.ID, "last").clear()
        self.driver.find_element(By.ID, "last").send_keys("Smith")
        self.driver.find_element(By.ID, "city").clear()
        self.driver.find_element(By.ID, "city").send_keys("New York")
        self.driver.find_element(By.XPATH, "//input[@value='Search for Someone' and @type='submit']").click()
    
    def test_yellowpages_a6fc427d(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "popular-cities").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New York')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New York Coupons & Deals')]").click()
    
    def test_yellowpages_b3fbf029(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.XPATH, "//a[@title='Search Attorneys']").click()
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("Union City Nj")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Union City, NJ')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='search-form']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='lid-8754205']/div[1]/div[1]/div[2]/div[1]/h2[1]/a[1]/span[1]").click()
    
    def test_yellowpages_d0d6b0ed(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "popular-cities").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cleveland')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content-container']/section[2]/div[1]/nav[1]/a[5]/span[1]/img[1]").click()
        self.driver.find_element(By.ID, "goto-map-view").click()
    
    def test_yellowpages_e9c7496f(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("Stanford, CA")
        self.driver.find_element(By.ID, "query").clear()
        self.driver.find_element(By.ID, "query").send_keys("car accident lawyers")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-term']/li[1]/a[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filter-and-sort']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Distance')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='lid-562265928']/div[1]/div[1]").click()
    
    def test_yellowpages_95936f53(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.XPATH, "//a[@title='Search Restaurants']").click()
        self.driver.find_element(By.ID, "open24").click()
        self.driver.find_element(By.ID, "js-sort-toggle").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rating')]").click()
    
    def test_yellowpages_8b4e49e9(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "query").clear()
        self.driver.find_element(By.ID, "query").send_keys("beauty salons")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-term']/li[1]/a[1]/b[1]").click()
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("Seattle, WA")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-location']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-location']/li[1]/a[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='search-form']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/label[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/label[1]/span[1]").click()
    
    def test_yellowpages_91f56f3b(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.XPATH, "//a[@title='Search Veterinarians']").click()
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("hawaii")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-location']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//button[@value='Find' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/label[4]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/h3[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/button[1]").click()
    
    def test_yellowpages_4097c577(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "query").clear()
        self.driver.find_element(By.ID, "query").send_keys("pedicure salon")
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("New York")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-location']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//button[@value='Find' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='lid-462459927']/div[1]/div[1]/div[2]/div[1]/h2[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='main-header']/article[1]/div[1]/a[1]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//button[@value='Find' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='lid-467213009']/div[1]/div[1]/div[2]/div[1]/h2[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='main-header']/article[1]/div[1]/a[1]/svg[1]/use[1]").click()
    
    def test_yellowpages_40fbda9d(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "q-and-a").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Home Improvement Remodeling')]").click()
    
    def test_yellowpages_4baa4918(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-links']/a[2]").click()
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("new york")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-location']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='search-form']/button[1]/span[1]").click()
    
    def test_yellowpages_62806bef(self):
        # self.driver.get("https://www.yellowpages.com/")
        self.driver.find_element(By.ID, "popular-cities").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Columbus')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for more')]").click()
    