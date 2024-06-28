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
class TestAmctheatres:
    
    def test_amctheatres_925a2307(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Check Gift Card Balance')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='number' and @value='' and @type='number' and @placeholder='Gift Card Number']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='number' and @value='' and @type='number' and @placeholder='Gift Card Number']").send_keys("87654321")
        self.driver.find_element(By.XPATH, "//input[@name='pin' and @value='' and @type='number' and @placeholder='Gift Card Pin']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='pin' and @value='' and @type='number' and @placeholder='Gift Card Pin']").send_keys("9753")
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]").click()
    
    def test_amctheatres_2cdee3d3(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[17]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Get Tickets')]").click()
        self.driver.find_element(By.ID, "showtimes-theatre-filter").clear()
        self.driver.find_element(By.ID, "showtimes-theatre-filter").select("Change Location...")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").send_keys("90028")
        self.driver.find_element(By.ID, "icon_search").click()
    
    def test_amctheatres_330d5618(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Food & Drinks')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore Menu')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View Full Menu')]").click()
    
    def test_amctheatres_36ab5d78(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Our Theatres')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Theatre')]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").send_keys("10001")
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[2]/a[1]/span[1]").click()
    
    def test_amctheatres_66d12284(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Food & Drinks')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Order Food & Drinks')]").click()
        self.driver.find_element(By.ID, "showtimes-theatre-filter").clear()
        self.driver.find_element(By.ID, "showtimes-theatre-filter").select("AMC Grove City 14")
        self.driver.find_element(By.XPATH, "//div[@id='modal-body']/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='concessions-categories']/div[3]/button[1]/picture[1]/source[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='concessions-categories']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Add to Order')]").click()
    
    def test_amctheatres_6b831239(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'On Demand')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Now Trending')]").click()
    
    def test_amctheatres_779cec8e(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Our Theatres')]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").send_keys("10001")
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/i[1]/svg[1]").click()
    
    def test_amctheatres_90557510(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See A Movie')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Coming Soon')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[1]/label[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[1]/label[1]/select[1]").select("AMC Artisan Films")
    
    def test_amctheatres_cfaa49bd(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Our Theatres')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Theatre')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Wichita')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ShowtimesScroll']/main[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Get Tickets')]").click()
    
    def test_amctheatres_05e1f2bd(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Check Balance')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='number' and @value='' and @type='number' and @placeholder='Gift Card Number']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='number' and @value='' and @type='number' and @placeholder='Gift Card Number']").send_keys("1000000000000000")
        self.driver.find_element(By.XPATH, "//input[@name='pin' and @value='' and @type='number' and @placeholder='Gift Card Pin']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='pin' and @value='' and @type='number' and @placeholder='Gift Card Pin']").send_keys("1222")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_amctheatres_130b1cd5(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'On Demand')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'On Sale Now')]").click()
        self.driver.find_element(By.ID, "RG9kUHJvZHVjdDo4MDQyNDE=").click()
        self.driver.find_element(By.ID, "vod-cta-Rent").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]").click()
    
    def test_amctheatres_22509b64(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Food & Drinks')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore Menu')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View Full Menu')]").click()
    
    def test_amctheatres_29f47ddb(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.ID, "showtimes-theatre-filter").clear()
        self.driver.find_element(By.ID, "showtimes-theatre-filter").select("AMC Grove City 14")
        self.driver.find_element(By.ID, "showtimes-movie-title-filter").clear()
        self.driver.find_element(By.ID, "showtimes-movie-title-filter").select("65")
        self.driver.find_element(By.ID, "showtimes-date-filter").clear()
        self.driver.find_element(By.ID, "showtimes-date-filter").select("Tue, Mar 28")
        self.driver.find_element(By.ID, "showtimes-466-65-digital-7:30pm").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[10]/ul[1]/li[8]/svg[1]/g[3]/text[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[10]/ul[1]/li[9]/svg[1]/g[3]/text[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[10]/ul[1]/li[10]/svg[1]/g[3]/text[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[10]/ul[1]/li[11]/svg[1]/g[3]/text[1]").click()
        self.driver.find_element(By.ID, "icon_arrow-left").click()
    
    def test_amctheatres_f8428085(self):
        # self.driver.get("https://amctheatres.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'On Demand')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Releases')]").click()
    