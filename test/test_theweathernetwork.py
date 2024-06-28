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
class TestTheweathernetwork:
    
    def test_theweathernetwork_208a2fd8(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.XPATH, "//nav[@id='main-nav']/div[1]/div[1]/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Severe Weather')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'US Alerts')]").click()
    
    def test_theweathernetwork_253b052a(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("vancouver")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Vancouver, British Columbia, Canada')]").click()
        self.driver.find_element(By.ID, "weather-link").click()
    
    def test_theweathernetwork_2cd6dc29(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.XPATH, "//nav[@id='main-nav']/div[1]/div[1]/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Severe Weather')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Canada Alerts')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[2]/div[1]/div[2]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[2]/div[1]/div[2]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Nova Scotia')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='all-index']/section[1]/ul[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Wind Warning for Victoria County')]").click()
    
    def test_theweathernetwork_445462dc(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.XPATH, "//div[@id='climate']/a[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/div[1]/div[1]/div[2]/a[1]/li[1]/span[1]/span[1]").click()
    
    def test_theweathernetwork_54edb54d(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("calgary, alberta")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Calgary, Alberta, Canada')]").click()
    
    def test_theweathernetwork_7ba05167(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.XPATH, "//nav[@id='main-nav']/div[1]/div[1]/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Maps & Roads')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Highway Conditions')]").click()
        self.driver.find_element(By.ID, "regiondropdownlist").clear()
        self.driver.find_element(By.ID, "regiondropdownlist").select("Vancouver")
    
    def test_theweathernetwork_8d7ac150(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.XPATH, "//nav[@id='main-nav']/div[1]/div[1]/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Forecasts & Reports')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Weekend')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Allenford')]").click()
    
    def test_theweathernetwork_947685ab(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("90028")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'West Hollywood, CA')]").click()
        self.driver.find_element(By.ID, "36-hour-forecast-link").click()
    
    def test_theweathernetwork_b707e935(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.XPATH, "//nav[@id='main-nav']/div[1]/div[1]/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Maps & Roads')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'UK Weather Warnings Map')]").click()
    
    def test_theweathernetwork_ceeac19a(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.XPATH, "//nav[@id='main-nav']/div[1]/div[1]/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Severe Weather')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Canada Alerts')]").click()
    
    def test_theweathernetwork_db6b218c(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("10019")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Manhattan, NY')]").click()
    
    def test_theweathernetwork_e1708851(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("10019")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Manhattan, NY')]").click()
        self.driver.find_element(By.ID, "weekend-forecast-link").click()
    
    def test_theweathernetwork_f7f87ceb(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("Miami, FL")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Miami, FL')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='add-saved-location']/div[1]/a[1]/span[1]").click()
    
    def test_theweathernetwork_0b5d3539(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("Vancouver")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Vancouver, British Columbia, Canada')]").click()
        self.driver.find_element(By.XPATH, "//label[@value='Show/Hide']").click()
    
    def test_theweathernetwork_11bdabf5(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.XPATH, "//nav[@id='main-nav']/div[1]/div[1]/div[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gallery')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Storm Hunters')]").click()
    
    def test_theweathernetwork_1ed326a4(self):
        # self.driver.get("https://theweathernetwork.com")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("Brooklyn")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Brooklyn, NY')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='historical-trend-link']/span[1]").click()
    