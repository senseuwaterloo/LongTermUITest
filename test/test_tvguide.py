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
class TestTvguide:
    
    def test_tvguide_942666cb(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").send_keys("the price is right")
        self.driver.find_element(By.XPATH, "//li[@id='c-searchBox_autoSuggest__results-item--1']/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='1000172866']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Biography')]").click()
    
    def test_tvguide_4357a1ab(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").send_keys("The Wire")
        self.driver.find_element(By.XPATH, "//li[@id='c-searchBox_autoSuggest__results-item--0']/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='1030226010']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[2]/li[1]/span[1]/span[1]").click()
    
    def test_tvguide_7f90a191(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").send_keys("Smile")
        self.driver.find_element(By.XPATH, "//li[@id='c-searchBox_autoSuggest__results-item--0']/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='2030492747']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/a[1]/div[2]/svg[1]/use[1]").click()
    
    def test_tvguide_f9e88baa(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").send_keys("Avatar The Way of Water")
        self.driver.find_element(By.XPATH, "//li[@id='c-searchBox_autoSuggest__results-item--0']/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='2000185249']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[3]/div[1]").click()
    
    def test_tvguide_6f4e562e(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/a[2]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/section[1]/div[1]/section[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filtersSettings']/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/section[1]/div[2]/div[1]/div[1]/div[2]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/section[1]/div[2]/div[1]/div[2]/div[2]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/section[1]/div[2]/div[1]/div[3]/div[2]/span[1]/span[1]").click()
    
    def test_tvguide_789b7d2d(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").send_keys("Titanic")
        self.driver.find_element(By.XPATH, "//li[@id='c-searchBox_autoSuggest__results-item--0']/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cast & Crew')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='2000278278']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[2]/li[1]/span[1]").click()
    
    def test_tvguide_c9215395(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Recommendations')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Recommendations')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Winter Preview: New Shows Worth Watching')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='c-pageArticleSingle-winter-tv-preview-the-14-best-shows-to-watch']/div[1]/div[1]/div[2]/div[1]/div[1]/p[9]/a[8]/strong[1]").click()
    
    def test_tvguide_d0ce3db1(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").send_keys("Alien Worlds")
        self.driver.find_element(By.XPATH, "//li[@id='c-searchBox_autoSuggest__results-item--0']/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Seasons & Episodes')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='episode4']/div[1]/div[1]/span[1]").click()
    
    def test_tvguide_02e7bae3(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/section[1]/div[1]/section[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filtersSettings']/div[4]/div[1]/div[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filtersSettings']/div[1]/div[1]/div[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/section[1]/div[2]/div[1]/div[8]/div[2]/span[1]/span[1]").click()
    
    def test_tvguide_0dd0b532(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/a[4]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/section[1]/div[1]/section[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filtersSettings']/div[4]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filtersSettings']/div[5]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filtersSettings']/div[6]/div[1]/span[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]").click()
    
    def test_tvguide_9cc81f50(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Live TV')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search']").send_keys("99201")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/button[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/button[3]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    
    def test_tvguide_1b82bda7(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search TV Shows and Movies...']").send_keys("Ali Wong")
        self.driver.find_element(By.XPATH, "//li[@id='c-searchBox_autoSuggest__results-item--0']/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='2030256641']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a[1]").click()
    
    def test_tvguide_28d54466(self):
        # self.driver.get("https://tvguide.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/section[1]/div[1]/section[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filtersSettings']/div[4]/div[1]/div[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[3]/div[2]/main[1]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]").click()
    