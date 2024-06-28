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
class TestCabelas:
    
    def test_cabelas_181e41bd(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "departmentButton_3074457345616967277").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Guns')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[3]/div[2]/ul[1]/li[4]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[4]/div[2]/ul[1]/li[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[9]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[9]/div[2]/ul[1]/li[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[9]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div[2]/div[4]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/div[1]/div[1]/a[1]/div[1]/img[1]").click()
    
    def test_cabelas_b3baca22(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "departmentButton_3074457345616967316").click()
        self.driver.find_element(By.ID, "subcategoryLink_3074457345616967316_3074457345616967320_3074457345616968337").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[13]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[13]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
    
    def test_cabelas_66d49483(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "departmentButton_3074457345616967290").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Boating Center')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'SHOP ALL BOATS')]").click()
        self.driver.find_element(By.ID, "zipInput").clear()
        self.driver.find_element(By.ID, "zipInput").send_keys("52554")
        self.driver.find_element(By.XPATH, "//input[@value='GO' and @type='submit']").click()
        self.driver.find_element(By.ID, "new").click()
        self.driver.find_element(By.ID, "BoatClassCodeList-accordion-label").click()
        self.driver.find_element(By.ID, "aluminum+fish+boats").click()
        self.driver.find_element(By.ID, "sort-selection").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Lowest Price')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='results-grid']/div[1]/a[1]/div[1]/div[1]/div[2]/div[1]/p[3]").click()
    
    def test_cabelas_9334211a(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Outdoor Rec')]").click()
        self.driver.find_element(By.ID, "subcategoryLink_3074457345616975315_3074457345616967300_3074457345616968653").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[5]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[5]/div[2]/ul[1]/li[2]/div[1]").click()
    
    def test_cabelas_619ba95b(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "departmentButton_3074457345616967301").click()
        self.driver.find_element(By.ID, "moreLink_3074457345616967301_3074457345616967313").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[5]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[5]/div[2]/ul[1]/li[3]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]").click()
        self.driver.find_element(By.ID, "productPageAdd2Cart").click()
    
    def test_cabelas_373dec75(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "departmentButton_3074457345616967837").click()
        self.driver.find_element(By.ID, "subcategoryLink_3074457345616967837_3074457345616967276_3074457345616968393").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[6]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[6]/div[2]/ul[1]/li[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div[2]/div[4]").click()
    
    def test_cabelas_3f62b47b(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "departmentButton_3074457345616967316").click()
        self.driver.find_element(By.ID, "moreLink_3074457345616967316_3074457345616967320").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[3]/div[2]/ul[1]/li[7]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[7]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[7]/div[2]/ul[1]/li[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[8]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[8]/div[2]/ul[1]/li[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[9]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[9]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div[2]/div[4]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[2]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[10]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[10]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]").click()
    
    def test_cabelas_9f76268f(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "departmentButton_3074457345616967837").click()
        self.driver.find_element(By.ID, "subcategoryLink_3074457345616967837_3074457345616967268_3074457345616967275").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/ul[1]/li[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[4]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[3]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
    
    def test_cabelas_a4397261(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "SimpleSearchForm_SearchTerm").clear()
        self.driver.find_element(By.ID, "SimpleSearchForm_SearchTerm").send_keys("black sleeping bag")
        self.driver.find_element(By.XPATH, "//form[@id='searchBox']/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "high_price_input").clear()
        self.driver.find_element(By.ID, "high_price_input").send_keys("40")
        self.driver.find_element(By.ID, "low_price_input").clear()
        self.driver.find_element(By.ID, "low_price_input").send_keys("0")
        self.driver.find_element(By.ID, "price_range_go").click()
    
    def test_cabelas_afb693cd(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Bargain Cave')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\"Men's Shoes & Boots\")]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[3]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[4]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[9]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[9]/div[2]/ul[1]/li[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[14]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[14]/div[2]/ul[1]/li[2]/div[1]/label[1]").click()
    
    def test_cabelas_e9a5ab90(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Registry')]").click()
        self.driver.find_element(By.XPATH, "//html[@id='index-page']/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "txtFindName").clear()
        self.driver.find_element(By.ID, "txtFindName").send_keys("Carla")
        self.driver.find_element(By.ID, "txtLastName").clear()
        self.driver.find_element(By.ID, "txtLastName").send_keys("Cahill")
        self.driver.find_element(By.XPATH, "//html[@id='index-page']/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pnlSearchResult']/div[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "linkDontHavePassword").click()
        self.driver.find_element(By.ID, "txtVisitorFirstName").clear()
        self.driver.find_element(By.ID, "txtVisitorFirstName").send_keys("Michael Cahill")
        self.driver.find_element(By.ID, "txtVisitorEmail").clear()
        self.driver.find_element(By.ID, "txtVisitorEmail").send_keys("cahillm@gmail.com")
        self.driver.find_element(By.ID, "btnVisitorPasswordRequest").click()
    
    def test_cabelas_ee9e993b(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "departmentButton_3074457345616967316").click()
        self.driver.find_element(By.ID, "categoryLink_3074457345616967316_3074457345616967319").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Power Assisted Reels')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
    
    def test_cabelas_eebf3f55(self):
        # self.driver.get("https://cabelas.com")
        self.driver.find_element(By.ID, "departmentButton_3074457345616967882").click()
        self.driver.find_element(By.ID, "subcategoryLink_3074457345616967882_3074457345616967884_3074457345616968425").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[5]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[5]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[6]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[6]/div[2]/ul[1]/li[6]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[1]/div[2]/ul[1]/li[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[4]/div[2]/ul[1]/li[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[11]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[11]/div[2]/ul[1]/li[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div[2]/div[4]").click()
    