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
class TestRottentomatoes:
    
    def test_rottentomatoes_79d9203e(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tv shows')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View All')]").click()
    
    def test_rottentomatoes_0b2c1886(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Movies')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Certified fresh movies')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[2]/template[1]/div[1]/rt-icon[1]/template[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[28]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
    
    def test_rottentomatoes_117c1176(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search movies, TV, actors, more...']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search movies, TV, actors, more...']").send_keys("scream")
        self.driver.find_element(By.XPATH, "//rt-header[@id='header-main']/search-algolia[1]/search-algolia-results[1]/search-algolia-results-category[1]/ul[1]/li[1]/a[1]/search-algolia-results-item[1]/template[1]/div[1]/div[1]/p[2]").click()
        self.driver.find_element(By.XPATH, "//section[@id='cast-and-crew']/div[1]/div[1]/div[4]/div[1]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'In the Heights')]").click()
    
    def test_rottentomatoes_60e7ffd3(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'News')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View All')]").click()
    
    def test_rottentomatoes_867dc9d1(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Movies')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trailers')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View all')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[5]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[2]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
    
    def test_rottentomatoes_86afd67c(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tv shows')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/bubbles-overflow-container[1]/where-to-watch-bubble[3]/template[1]/div[1]/affiliate-icon[1]/template[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[6]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-radio-group[1]/select-label[6]/span[1]").click()
    
    def test_rottentomatoes_b2c18588(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Movies')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//dropdown-option[@value='movies_at_home']").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[12]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-radio-group[1]/select-label[2]/span[1]").click()
    
    def test_rottentomatoes_18a581b9(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Movies')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Coming soon to theaters')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[2]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
    
    def test_rottentomatoes_1ed913ba(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Movies')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//dropdown-option[@value='movies_coming_soon']").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[3]/template[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[4]/template[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
    
    def test_rottentomatoes_f86b0a14(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Movies')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[5]/template[1]/div[1]/rt-icon[1]/template[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[1]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[1]/template[1]/div[1]/rt-icon[1]/template[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-radio-group[1]/select-label[6]/select-radio[1]/template[1]/div[1]").click()
    
    def test_rottentomatoes_30d5f7dc(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Movies')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[1]/template[1]/div[1]/rt-icon[1]/template[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-radio-group[1]/select-label[6]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[6]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[3]/template[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
    
    def test_rottentomatoes_1203a016(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tv shows')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[2]/template[1]/div[1]/rt-icon[1]/template[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[4]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[1]/template[1]/div[1]/rt-icon[1]/template[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-radio-group[1]/select-label[2]/select-radio[1]/template[1]/div[1]").click()
    
    def test_rottentomatoes_160fc162(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tv shows')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/bubbles-overflow-container[1]/where-to-watch-bubble[10]/template[1]/div[1]/affiliate-icon[1]/template[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[1]/template[1]/div[1]/rt-icon[1]/template[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-radio-group[1]/select-label[2]/select-radio[1]/template[1]/div[1]").click()
    
    def test_rottentomatoes_d1942a73(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Movies')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Netflix streaming')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[2]/template[1]/div[1]/rt-icon[1]/template[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[6]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[3]/div[1]/div[1]/a[4]/tile-dynamic[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//button[@value='+' and @type='button']").click()
    
    def test_rottentomatoes_5092fad7(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search movies, TV, actors, more...']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search movies, TV, actors, more...']").send_keys("Tom Hanks")
        self.driver.find_element(By.XPATH, "//rt-header[@id='header-main']/search-algolia[1]/search-algolia-results[1]/search-algolia-results-category[2]/ul[1]/li[1]/a[1]/search-algolia-results-item[1]/template[1]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'My Life in Ruins (2009)')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Top Critics (49)')]").click()
    
    def test_rottentomatoes_5fb9730d(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search movies, TV, actors, more...']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search movies, TV, actors, more...']").send_keys("George Clooney")
        self.driver.find_element(By.XPATH, "//rt-header[@id='header-main']/search-algolia[1]/search-algolia-results[1]/search-algolia-results-category[2]/ul[1]/li[1]/a[1]/search-algolia-results-item[1]/template[1]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/article[1]/section[4]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[5]/button[1]").click()
    
    def test_rottentomatoes_d4d4a01e(self):
        # self.driver.get("https://rottentomatoes.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tv shows')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-radio-group[1]/select-label[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[1]/template[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[1]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[5]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[1]/select-checkbox[1]/template[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
    