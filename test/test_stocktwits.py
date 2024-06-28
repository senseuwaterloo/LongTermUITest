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
class TestStocktwits:
    
    def test_stocktwits_283385b4(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("@pedrob")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='@pedrob' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/span[1]").click()
    
    def test_stocktwits_2d1ea58e(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rankings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-tabs-21']/div[1]/div[1]/div[12]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-tabs-21']/div[1]/div[1]/div[18]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-tabs-21']/div[1]/div[1]/div[24]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-tabs-21']/div[1]/div[1]/div[30]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-tabs-21']/div[1]/div[1]/div[36]").click()
    
    def test_stocktwits_0bae14d0(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").click()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("@WarrenBuffett")
        self.driver.find_element(By.XPATH, "//div[@id='app-main-header']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
    
    def test_stocktwits_0f8930ab(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").click()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("AMZN")
        self.driver.find_element(By.XPATH, "//div[@id='app-main-header']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").click()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("GOOG")
        self.driver.find_element(By.XPATH, "//div[@id='app-main-header']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
    
    def test_stocktwits_6e99bca6(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rankings')]").click()
        self.driver.find_element(By.XPATH, "//li[@id='react-tabs-28']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'SPY')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='symbol-page-hero-tabs']/div[5]/div[1]/a[1]/h2[1]").click()
    
    def test_stocktwits_845241b5(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rooms')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Click Here.')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Create a Room')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='slug' and @value='' and @type='text' and @placeholder='room_name']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='slug' and @value='' and @type='text' and @placeholder='room_name']").send_keys("AI_Stocks")
        self.driver.find_element(By.XPATH, "//main[@id='Main']/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//select[@name='topics[0]']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='topics[0]']").select("Technology")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_stocktwits_8a8b5502(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").click()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("AAPL")
        self.driver.find_element(By.XPATH, "//div[@id='app-main-header']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
    
    def test_stocktwits_8bdd06e7(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rooms')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Click Here.')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='Main']/div[1]/div[2]/article[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
    
    def test_stocktwits_90fc1791(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").click()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("TSLA")
        self.driver.find_element(By.XPATH, "//div[@id='app-main-header']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'6m')]").click()
    
    def test_stocktwits_94ac9003(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("tesla")
        self.driver.find_element(By.XPATH, "//div[@id='app-main-header']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-tabs-11']/div[1]/form[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='react-tabs-11']/div[1]/form[1]/div[1]/select[1]").select("Price")
        self.driver.find_element(By.XPATH, "//div[@id='react-tabs-11']/div[1]/form[1]/div[2]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='react-tabs-11']/div[1]/form[1]/div[2]/select[1]").select("Is Below")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter a value']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter a value']").send_keys("300")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_stocktwits_2e6d3e61(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Earnings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/article[1]/div[2]/div[1]/header[1]/nav[1]/a[2]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/article[1]/div[2]/div[1]/header[1]/div[2]/div[1]/div[4]/div[2]/div[1]").click()
    
    def test_stocktwits_3a66f429(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rankings')]").click()
        self.driver.find_element(By.XPATH, "//li[@id='react-tabs-38']/div[1]/span[1]").click()
    
    def test_stocktwits_5a026c85(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("AMC")
        self.driver.find_element(By.XPATH, "//div[@id='app-main-header']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]").click()
    
    def test_stocktwits_1dce8510(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("btc")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='btc' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='react-tabs-150']/div[1]/span[1]").click()
    
    def test_stocktwits_98c3b106(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rankings')]").click()
        self.driver.find_element(By.XPATH, "//li[@id='react-tabs-56']/div[1]").click()
    
    def test_stocktwits_ac06c0bc(self):
        # self.driver.get("https://stocktwits.com/")
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='desktopSearch' and @value='' and @type='text' and @placeholder='Search Companies, Crypto, NFTs and @usernames']").send_keys("BUD")
        self.driver.find_element(By.XPATH, "//div[@id='app-main-header']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Layout']/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]/span[1]").click()
    