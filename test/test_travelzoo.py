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
class TestTravelzoo:
    
    def test_travelzoo_984775e2(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").clear()
        self.driver.find_element(By.ID, "what-field-1").send_keys("disney")
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.XPATH, "//button[@id='refine-search-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='catfilter-container']/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[10]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='2960703']/div[1]/a[1]/div[1]/h2[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'CONTINUE')]").click()
    
    def test_travelzoo_a55e347d(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.ID, "ui-id-53").click()
        self.driver.find_element(By.ID, "where-field-1").clear()
        self.driver.find_element(By.ID, "where-field-1").send_keys("chicago")
        self.driver.find_element(By.ID, "ui-id-144").click()
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.ID, "ui-id-56").click()
        self.driver.find_element(By.ID, "refine-search-toggle").click()
        self.driver.find_element(By.XPATH, "//div[@id='catfilter-container']/div[1]/div[1]/div[1]/div[1]/div[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()
        self.driver.find_element(By.ID, "when-field-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-id-6']/ul[1]/li[5]").click()
        self.driver.find_element(By.ID, "search-button-1").click()
    
    def test_travelzoo_3592a015(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.XPATH, "//body[@id='bodyTop']/nav[1]/div[2]/div[3]/ul[1]/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='chunk-0']/div[1]/ul[2]/li[3]/a[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//button[@id='refine-search-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[14]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[8]/button[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='3022059']/div[1]/a[1]/div[1]/div[2]/img[1]").click()
    
    def test_travelzoo_1570a4b7(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.ID, "ui-id-36").click()
        self.driver.find_element(By.ID, "where-field-1").click()
        self.driver.find_element(By.ID, "where-field-1").clear()
        self.driver.find_element(By.ID, "where-field-1").send_keys("Alaska")
        self.driver.find_element(By.ID, "ui-id-68").click()
        self.driver.find_element(By.XPATH, "//button[@id='refine-search-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[12]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()
    
    def test_travelzoo_aeace1e7(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.XPATH, "//body[@id='bodyTop']/nav[1]/div[2]/div[3]/ul[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='chunk-0']/div[1]/ul[2]/li[5]/a[1]/h3[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='refine-search-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[8]/button[1]").click()
    
    def test_travelzoo_afa1f70c(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.XPATH, "//body[@id='bodyTop']/nav[1]/div[2]/div[3]/ul[1]/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "where-field-1").click()
        self.driver.find_element(By.ID, "ui-id-41").click()
        self.driver.find_element(By.ID, "when-field-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-id-5']/ul[1]/li[5]").click()
        self.driver.find_element(By.ID, "search-button-1").click()
        self.driver.find_element(By.ID, "refine-search-toggle").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[4]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()
    
    def test_travelzoo_b770af80(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.ID, "ui-id-66").click()
        self.driver.find_element(By.ID, "ui-id-81").click()
        self.driver.find_element(By.ID, "when-field-1").click()
        self.driver.find_element(By.ID, "ui-id-6").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-id-7']/ul[1]/li[5]").click()
        self.driver.find_element(By.ID, "guests-field-1").clear()
        self.driver.find_element(By.ID, "guests-field-1").select("1 Guest")
        self.driver.find_element(By.ID, "search-button-1").click()
        self.driver.find_element(By.ID, "refine-search-toggle").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[21]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[25]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[15]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[3]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='51574']/div[1]/a[1]/div[1]/h2[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'CHECK DATES')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'$189')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'$259')]").click()
        self.driver.find_element(By.ID, "btnContinueToRoomRates").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-id-21']/div[4]/div[1]/div[3]/div[2]/div[1]/div[2]/button[1]/h3[1]").click()
    
    def test_travelzoo_4a9a05f8(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.ID, "ui-id-39").click()
        self.driver.find_element(By.ID, "where-field-1").clear()
        self.driver.find_element(By.ID, "where-field-1").send_keys("mexico")
        self.driver.find_element(By.ID, "ui-id-90").click()
        self.driver.find_element(By.ID, "when-field-1").click()
        self.driver.find_element(By.ID, "ui-id-6").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-id-7']/ul[1]/li[5]").click()
        self.driver.find_element(By.XPATH, "//button[@id='refine-search-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()
    
    def test_travelzoo_4e44e7b6(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.XPATH, "//body[@id='bodyTop']/nav[1]/div[2]/div[3]/ul[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='chunk-0']/div[1]/ul[2]/li[4]/a[1]/h3[1]/span[1]").click()
        self.driver.find_element(By.ID, "refine-search-toggle").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[8]/button[1]").click()
    
    def test_travelzoo_0633c328(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.ID, "ui-id-59").click()
        self.driver.find_element(By.ID, "ui-id-62").click()
        self.driver.find_element(By.ID, "when-field-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-id-5']/ul[1]/li[4]").click()
        self.driver.find_element(By.ID, "search-button-1").click()
    
    def test_travelzoo_1ba150cb(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.ID, "ui-id-38").click()
        self.driver.find_element(By.ID, "where-field-1").clear()
        self.driver.find_element(By.ID, "where-field-1").send_keys("las vegas")
        self.driver.find_element(By.ID, "ui-id-98").click()
        self.driver.find_element(By.ID, "when-field-1").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'17')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'20')]").click()
        self.driver.find_element(By.ID, "guests-field-1").clear()
        self.driver.find_element(By.ID, "guests-field-1").select("4 Guests")
        self.driver.find_element(By.ID, "search-button-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='btnAlert-bottom']/div[2]/button[1]").click()
    
    def test_travelzoo_1c1af35c(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.XPATH, "//body[@id='bodyTop']/nav[1]/div[2]/div[3]/ul[1]/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='chunk-0']/div[1]/ul[2]/li[3]/a[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//button[@id='refine-search-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[8]/button[1]").click()
    
    def test_travelzoo_33964bc4(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.ID, "ui-id-47").click()
        self.driver.find_element(By.ID, "ui-id-57").click()
        self.driver.find_element(By.ID, "when-field-1").click()
        self.driver.find_element(By.ID, "ui-id-7").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-id-8']/ul[1]/li[12]").click()
        self.driver.find_element(By.XPATH, "//button[@id='refine-search-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='maplist-toggle']/span[1]/span[2]").click()
    
    def test_travelzoo_c5cc7e71(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").clear()
        self.driver.find_element(By.ID, "what-field-1").send_keys("Hotels")
        self.driver.find_element(By.ID, "ui-id-47").click()
        self.driver.find_element(By.ID, "where-field-1").clear()
        self.driver.find_element(By.ID, "where-field-1").send_keys("Mexico")
        self.driver.find_element(By.ID, "ui-id-74").click()
        self.driver.find_element(By.ID, "search-button-1").click()
    
    def test_travelzoo_c8990751(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.ID, "ui-id-41").click()
        self.driver.find_element(By.ID, "where-field-1").click()
        self.driver.find_element(By.ID, "where-field-1").clear()
        self.driver.find_element(By.ID, "where-field-1").send_keys("Europe")
        self.driver.find_element(By.ID, "ui-id-141").click()
        self.driver.find_element(By.ID, "when-field-1").click()
        self.driver.find_element(By.ID, "ui-id-6").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-id-7']/ul[1]/li[7]").click()
        self.driver.find_element(By.ID, "search-button-1").click()
        self.driver.find_element(By.ID, "refine-search-toggle").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[13]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()
    
    def test_travelzoo_c95ac388(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "where-field-1").clear()
        self.driver.find_element(By.ID, "where-field-1").send_keys("New York City")
        self.driver.find_element(By.ID, "ui-id-160").click()
        self.driver.find_element(By.ID, "when-field-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-id-5']/ul[1]/li[4]").click()
        self.driver.find_element(By.ID, "search-button-1").click()
    
    def test_travelzoo_d9c160e7(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.XPATH, "//body[@id='bodyTop']/nav[1]/div[2]/div[3]/ul[1]/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='chunk-0']/div[1]/ul[2]/li[3]/a[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//button[@id='refine-search-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[26]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[8]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Go to Aspire Down Under site']").click()
    
    def test_travelzoo_50c13c64(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()
        self.driver.find_element(By.ID, "ui-id-37").click()
        self.driver.find_element(By.ID, "where-field-1").click()
        self.driver.find_element(By.ID, "where-field-1").clear()
        self.driver.find_element(By.ID, "where-field-1").send_keys("Spain")
        self.driver.find_element(By.ID, "ui-id-92").click()
        self.driver.find_element(By.ID, "when-field-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-id-5']/ul[1]/li[5]").click()
        self.driver.find_element(By.ID, "search-button-1").click()
        self.driver.find_element(By.XPATH, "//button[@id='refine-search-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[19]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()
    
    def test_travelzoo_604c4377(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "where-field-1").clear()
        self.driver.find_element(By.ID, "where-field-1").send_keys("Fiji")
        self.driver.find_element(By.ID, "ui-id-33").click()
        self.driver.find_element(By.ID, "refine-search-toggle").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='3021166']/div[1]/a[1]/div[2]/h2[1]/span[1]").click()
    