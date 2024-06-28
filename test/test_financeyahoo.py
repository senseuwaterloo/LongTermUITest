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
class TestFinanceYahoo:
    
    def test_financeyahoo_b5e55e9f(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Markets')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Currencies')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'EURUSD=X')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='quote-nav']/ul[1]/li[4]/a[1]/span[1]").click()
    
    def test_financeyahoo_c3e1b4ad(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("Microsoft corporation")
        self.driver.find_element(By.XPATH, "//button[@id='header-desktop-search-button']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='quote-header-info']/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]").click()
    
    def test_financeyahoo_c47cc903(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("NVIDIA Corporation")
        self.driver.find_element(By.XPATH, "//form[@id='header-search-form']/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='myLightboxContainer']/section[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Col1-3-Summary-Proxy']/section[1]/div[1]/div[1]/div[3]/a[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='summaryPressStream-0-Stream']/ul[1]/li[1]/div[1]/div[1]/div[2]/h3[1]/a[1]/u[1]").click()
    
    def test_financeyahoo_c4a26624(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("microsoft")
        self.driver.find_element(By.XPATH, "//form[@id='header-search-form']/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='quote-nav']/ul[1]/li[4]/a[1]/span[1]").click()
    
    def test_financeyahoo_9f780eb0(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("tesla")
        self.driver.find_element(By.XPATH, "//form[@id='header-search-form']/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='quote-nav']/ul[1]/li[6]/a[1]/span[1]").click()
    
    def test_financeyahoo_a76119c9(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Watchlists')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Col1-0-ExploreCuratedWatchlists-Proxy']/div[1]/section[4]/header[1]/p[1]/span[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Col1-0-ExploreCuratedWatchlists-Proxy']/div[1]/section[4]/div[1]/div[1]/ul[1]/li[7]/div[1]/a[1]/header[1]/section[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Col1-0-WatchlistDetail-Proxy']/div[1]/div[2]/section[1]/footer[1]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-menu']/ul[1]/li[2]/a[1]/div[1]").click()
    
    def test_financeyahoo_afe67cf4(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Crypto')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'BTC-USD')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='quote-nav']/ul[1]/li[2]/a[1]/span[1]").click()
    
    def test_financeyahoo_b2fd70cb(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'My Portfolio')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Col1-0-Portfolios-Proxy']/main[1]/header[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='myLightboxContainer']/section[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Portfolio Name']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Portfolio Name']").send_keys("Tech")
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @title='Submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='myLightboxContainer']/div[1]/button[2]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='myLightboxContainer']/div[1]/div[10]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Lead-3-Portfolios-Proxy']/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='VZ, AAPL, TSLA']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='VZ, AAPL, TSLA']").send_keys("Microsoft")
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-menu']/div[3]/form[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[2]/span[2]/svg[1]").click()
    
    def test_financeyahoo_095e35d4(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("Dogecoin")
        self.driver.find_element(By.XPATH, "//button[@id='header-desktop-search-button']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='interactive-2col-qsp-m']/ul[1]/li[4]/button[1]").click()
    
    def test_financeyahoo_0e56e2a4(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'S&P 500')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='interactive-2col-qsp-m']/ul[1]/li[7]/button[1]").click()
    
    def test_financeyahoo_12cfbc8c(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("btc")
        self.driver.find_element(By.ID, "header-desktop-search-button").click()
        self.driver.find_element(By.XPATH, "//div[@id='quote-nav']/ul[1]/li[4]/a[1]/span[1]").click()
    
    def test_financeyahoo_1793dd8c(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Dow 30')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='quote-nav']/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='chart-toolbar']/div[1]/span[1]/div[1]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-menu']/div[3]/div[1]/div[2]/ul[1]/li[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='chart-toolbar']/div[1]/span[1]/div[2]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    
    def test_financeyahoo_21a0b1bf(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("Most Active Penny Stocks")
        self.driver.find_element(By.XPATH, "//form[@id='header-search-form']/div[2]/div[1]/div[1]/ul[3]/li[2]/div[2]/h5[1]").click()
    
    def test_financeyahoo_2e946bdf(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Yahoo Finance Plus')]").click()
        self.driver.find_element(By.XPATH, "//section[@id='comparison-table']/div[1]").click()
    
    def test_financeyahoo_34e0bf85(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("apple")
        self.driver.find_element(By.XPATH, "//form[@id='header-search-form']/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='myLightboxContainer']/section[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='quote-header-info']/div[2]/div[3]/a[1]/span[1]/span[1]").click()
    
    def test_financeyahoo_659b04d5(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Watchlists')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Col1-0-ExploreCuratedWatchlists-Proxy']/div[1]/section[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/header[1]/section[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Col1-0-WatchlistDetail-Proxy']/div[1]/div[2]/section[1]/footer[1]/button[1]/span[1]").click()
    
    def test_financeyahoo_77663082(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Markets')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Calendars')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Lead-4-CalNav-Proxy']/div[1]/ul[1]/li[4]/a[1]/span[1]").click()
    
    def test_financeyahoo_f4333d7a(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Screeners')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Equity Screener')]").click()
        self.driver.find_element(By.XPATH, "//button[@title='Mid Cap']").click()
        self.driver.find_element(By.XPATH, "//div[@id='screener-criteria']/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-menu']/div[1]/div[2]/ul[1]/li[6]/label[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-menu']/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='screener-criteria']/div[2]/div[1]/div[3]/button[1]/span[1]/span[1]").click()
    
    def test_financeyahoo_05d98f5e(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("Bitcoin")
        self.driver.find_element(By.XPATH, "//form[@id='header-search-form']/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='quoteNewsStream-0-Stream']/ul[1]/li[1]/div[1]/div[1]/div[2]/h3[1]/a[1]/u[1]").click()
    
    def test_financeyahoo_7aa219f8(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("Apple")
        self.driver.find_element(By.XPATH, "//form[@id='header-search-form']/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]").click()
    
    def test_financeyahoo_86f12dc0(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("gold")
        self.driver.find_element(By.ID, "header-desktop-search-button").click()
        self.driver.find_element(By.XPATH, "//div[@id='quote-header-info']/div[2]/div[2]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-menu']/ul[1]/li[3]/button[1]/svg[1]").click()
    
    def test_financeyahoo_97cd7138(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("taxes")
        self.driver.find_element(By.XPATH, "//form[@id='header-search-form']/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]").click()
        self.driver.find_element(By.ID, "tab-2").click()
    
    def test_financeyahoo_9f590239(self):
        # self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.ID, "yfin-usr-qry").clear()
        self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("tesla")
        self.driver.find_element(By.XPATH, "//form[@id='header-search-form']/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='quote-nav']/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@title='Hiring Trends']").click()
    