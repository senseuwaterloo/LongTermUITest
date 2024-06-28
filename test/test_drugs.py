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
class TestDrugs:
    
    def test_drugs_05fd73ba(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drugs A-Z')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'C')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Clonazepam')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'2,010 Reviews')]").click()
        self.driver.find_element(By.XPATH, "//button[@name='sort_reviews' and @value='most_helpful']").click()
    
    def test_drugs_65c2867e(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'More')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Natural products database')]").click()
    
    def test_drugs_6c2592e0(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Interactions Checker')]").click()
        self.driver.find_element(By.ID, "livesearch-interaction-basic").clear()
        self.driver.find_element(By.ID, "livesearch-interaction-basic").send_keys("viagra")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "livesearch-interaction").clear()
        self.driver.find_element(By.ID, "livesearch-interaction").send_keys("alcohol")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]/var[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Check Interactions')]").click()
    
    def test_drugs_6e046178(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/ul[1]/li[4]/a[1]/img[1]").click()
        self.driver.find_element(By.ID, "livesearch-sfx").clear()
        self.driver.find_element(By.ID, "livesearch-sfx").send_keys("Tamiflu")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]/var[1]/b[1]").click()
    
    def test_drugs_7d6b41a1(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'H')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Humira')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Dosage')]").click()
    
    def test_drugs_8e47b536(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.ID, "livesearch-main").clear()
        self.driver.find_element(By.ID, "livesearch-main").send_keys("anxiety")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]/var[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[2]/div[2]/div[1]/div[1]/a[1]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View all')]").click()
    
    def test_drugs_a62bf569(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/img[1]").click()
        self.driver.find_element(By.ID, "livesearch-interaction-basic").clear()
        self.driver.find_element(By.ID, "livesearch-interaction-basic").send_keys("melatonin")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]").click()
        self.driver.find_element(By.ID, "livesearch-interaction").clear()
        self.driver.find_element(By.ID, "livesearch-interaction").send_keys("Folate Forte")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Check Interactions')]").click()
    
    def test_drugs_ae287033(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Interactions Checker')]").click()
        self.driver.find_element(By.ID, "livesearch-interaction-basic").clear()
        self.driver.find_element(By.ID, "livesearch-interaction-basic").send_keys("Novolin N")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]/var[1]/b[1]").click()
        self.driver.find_element(By.ID, "livesearch-interaction").clear()
        self.driver.find_element(By.ID, "livesearch-interaction").send_keys("Novolin R")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]/var[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Check Interactions')]").click()
    
    def test_drugs_aeb455c0(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drugs A-Z')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'E')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Eulexin')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Check interactions')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Eulexin disease interactions')]").click()
    
    def test_drugs_b02b7643(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drugs A-Z')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'M')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Montelukast')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Side effects')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Montelukast drug interactions')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Claritin (loratadine)')]").click()
    
    def test_drugs_bb78798e(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/ul[1]/li[2]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Agree and Continue')]").click()
        self.driver.find_element(By.ID, "livesearch-imprint").clear()
        self.driver.find_element(By.ID, "livesearch-imprint").send_keys("894 5")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]").click()
        self.driver.find_element(By.ID, "color-select").clear()
        self.driver.find_element(By.ID, "color-select").select("Pink")
        self.driver.find_element(By.ID, "shape-select").clear()
        self.driver.find_element(By.ID, "shape-select").select("Oval")
        self.driver.find_element(By.XPATH, "//input[@value='Search' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View details')]").click()
    
    def test_drugs_c57526cc(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.ID, "livesearch-main").clear()
        self.driver.find_element(By.ID, "livesearch-main").send_keys("tylenol")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]/var[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Side Effects')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/a[1]").click()
    
    def test_drugs_cd4a2de1(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Drugs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'FDA Alerts')]").click()
    
    def test_drugs_d69769ba(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drugs A-Z')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'M')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Metformin')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Warnings')]").click()
    
    def test_drugs_e1dfd13b(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'More')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mobile apps')]").click()
    
    def test_drugs_e7cab3cb(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drugs A-Z')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'V')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Valtrex')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare alternatives')]").click()
    
    def test_drugs_b3963653(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/ul[1]/li[2]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Agree and Continue')]").click()
        self.driver.find_element(By.ID, "livesearch-imprint").clear()
        self.driver.find_element(By.ID, "livesearch-imprint").send_keys("123456")
        self.driver.find_element(By.ID, "color-select").clear()
        self.driver.find_element(By.ID, "color-select").select("White")
        self.driver.find_element(By.ID, "shape-select").clear()
        self.driver.find_element(By.ID, "shape-select").select("Round")
        self.driver.find_element(By.XPATH, "//input[@value='Search' and @type='submit']").click()
    
    def test_drugs_06e56c2c(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Pill Identifier')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Agree and Continue')]").click()
        self.driver.find_element(By.ID, "livesearch-imprint").clear()
        self.driver.find_element(By.ID, "livesearch-imprint").send_keys("M366")
        self.driver.find_element(By.XPATH, "//input[@value='Search' and @type='submit']").click()
    
    def test_drugs_1910f385(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/img[1]").click()
        self.driver.find_element(By.ID, "livesearch-interaction-basic").clear()
        self.driver.find_element(By.ID, "livesearch-interaction-basic").send_keys("ibuprofen")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]/var[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Check Interactions')]").click()
    
    def test_drugs_279cb741(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/ul[1]/li[4]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Adderall')]").click()
    
    def test_drugs_2854bdb8(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drugs A-Z')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'A')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Allegra')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Interactions')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Allegra drug interactions')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Allegra alcohol/food interactions')]").click()
    
    def test_drugs_4bd16a73(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.ID, "livesearch-main").clear()
        self.driver.find_element(By.ID, "livesearch-main").send_keys("Hypersomnia")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]/var[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[2]/div[2]/div[2]/div[1]/a[1]/h3[1]").click()
    
    def test_drugs_5d17dbe3(self):
        # self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.ID, "livesearch-main").clear()
        self.driver.find_element(By.ID, "livesearch-main").send_keys("Paracetamol")
        self.driver.find_element(By.XPATH, "//div[@id='ls-wrap']/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[2]/div[2]/div[1]/div[1]/a[1]/h3[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Side effects')]").click()
    