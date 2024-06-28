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
class TestViator:
    
    def test_viator_a4f3beb3(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/a[1]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='sort-dropdown']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-option']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='productName0']/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    
    def test_viator_3c10b271(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/a[1]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tours & Tickets')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ratingFilterOptions']/div[1]/div[1]/label[1]/label[1]").click()
    
    def test_viator_8308d10f(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("India")
        self.driver.find_element(By.XPATH, "//div[@id='react-select-homepageTypeaheadSearch-option-1']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@role='gridcell']").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[5]/div[6]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[2]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/circle[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='heading21913']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='collapseGroup21913']/div[1]/div[7]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='specialsFilterOptions']/div[3]/div[3]/label[1]/span[1]/label[1]").click()
        self.driver.find_element(By.ID, "displayed-sort").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-option']/span[1]").click()
    
    def test_viator_2e133e56(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("Dubai")
        self.driver.find_element(By.XPATH, "//div[@id='react-select-homepageTypeaheadSearch-option-1']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='heading21909']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='collapseGroup21909']/div[1]/div[15]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='durationFilterOptions']/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='durationFilterOptions']/div[1]/div[1]/div[2]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='timeOfDayFilterOptions']/div[1]/div[1]/div[3]/label[1]/div[1]").click()
    
    def test_viator_39937001(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tours & Tickets')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='specialsFilterOptions']/div[2]/label[1]/span[1]/label[1]").click()
    
    def test_viator_64779409(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("skiing")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[2]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/circle[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='sort-dropdown']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-option']/span[1]").click()
    
    def test_viator_7b7079f0(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").click()
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[5]/div[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[2]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/circle[1]").click()
    
    def test_viator_04ec089f(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("Montana")
        self.driver.find_element(By.XPATH, "//div[@id='react-select-homepageTypeaheadSearch-option-1']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@role='gridcell']").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[2]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/circle[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='heading21909']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='collapseGroup21909']/div[1]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='collapseGroup21909-11923']/div[1]/div[3]/div[1]").click()
        self.driver.find_element(By.ID, "displayed-sort").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-option']/span[1]").click()
    
    def test_viator_19847108(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("Paris")
        self.driver.find_element(By.XPATH, "//div[@id='react-select-homepageTypeaheadSearch-option-1']/button[1]/div[2]/div[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[6]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/circle[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='sort-dropdown']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-option']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='productName0']/div[1]/div[2]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[1]/div[4]/div[2]/div[3]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[1]/div[4]/div[2]/div[5]/div[2]/div[1]/div[13]/div[1]/div[3]/div[1]/div[4]/div[1]/button[1]").click()
    
    def test_viator_8e133f6c(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("Paris")
        self.driver.find_element(By.XPATH, "//div[@id='react-select-homepageTypeaheadSearch-option-1']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/circle[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='heading21911']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='collapseGroup21911']/div[1]/div[9]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='specialsFilterOptions']/div[2]/label[1]").click()
        self.driver.find_element(By.ID, "displayed-sort").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-option']/span[1]").click()
    
    def test_viator_9b6316ee(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("cancun")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/circle[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='global-nav-desktop-container']/div[1]/div[1]/div[5]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='global-nav-links-2-0']/div[1]/div[1]/a[1]/div[1]").click()
    
    def test_viator_298c854d(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("London")
        self.driver.find_element(By.XPATH, "//div[@id='react-select-homepageTypeaheadSearch-option-1']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/circle[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Unique Experiences')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='durationFilterOptions']/div[1]/div[1]/div[1]/label[1]/span[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ratingFilterOptions']/div[1]/div[2]/label[1]").click()
    
    def test_viator_f27bb47e(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/a[1]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Food & Drink')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Coffee & Tea')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='timeOfDayFilterOptions']/div[1]/div[1]/div[1]/label[1]/div[1]/label[1]").click()
    
    def test_viator_d6dd19a2(self):
        # self.driver.get("https://www.viator.com/")
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").clear()
        self.driver.find_element(By.ID, "react-select-homepageTypeaheadSearch-input").send_keys("Los Angeles")
        self.driver.find_element(By.XPATH, "//div[@id='react-select-homepageTypeaheadSearch-option-1']/button[1]/div[2]/div[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/svg[1]/circle[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Likely To Sell Out')]").click()
        self.driver.find_element(By.XPATH, "//span[@id='sort-dropdown']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-option']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Hollywood Sign Hiking Tour to Griffith Observatory')]").click()
    