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
class TestUmichEdu:
    
    def test_umichedu_f2cfae2c(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Giving')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='giving']/div[2]/div[2]/div[4]/div[1]/ul[1]/li[7]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Academics')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'U-M Dearborn')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Ways to Give')]").click()
    
    def test_umichedu_1060037c(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Academics')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='academics']/div[2]/div[2]/div[8]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "filter").clear()
        self.driver.find_element(By.ID, "filter").send_keys("summer internship")
        self.driver.find_element(By.XPATH, "//button[@id='searchIcon']/i[1]").click()
        self.driver.find_element(By.ID, "opportunity-type-checkboxes7").click()
        self.driver.find_element(By.ID, "location-checkboxes1").click()
    
    def test_umichedu_174dfd52(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Academics')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='academics']/div[2]/div[2]/div[7]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "edit-field-calendar-type-target-id-2").click()
        self.driver.find_element(By.ID, "edit-field-term-target-id").clear()
        self.driver.find_element(By.ID, "edit-field-term-target-id").select("Fall 2024")
        self.driver.find_element(By.ID, "edit-submit-calendars").click()
    
    def test_umichedu_2ecaefad(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Prospective Students')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='prospective-students']/div[2]/div[2]/div[3]/div[1]/ul[1]/li[3]/a[1]").click()
        self.driver.find_element(By.ID, "edit-academic-year").clear()
        self.driver.find_element(By.ID, "edit-academic-year").select("2022-2023")
        self.driver.find_element(By.ID, "edit-college-school").clear()
        self.driver.find_element(By.ID, "edit-college-school").select("College of Engineering")
        self.driver.find_element(By.ID, "edit-full-half-term").clear()
        self.driver.find_element(By.ID, "edit-full-half-term").select("Full Term")
        self.driver.find_element(By.ID, "edit-level-of-study").clear()
        self.driver.find_element(By.ID, "edit-level-of-study").select("Graduate")
        self.driver.find_element(By.ID, "edit-submit-tuition-fees-relationship").click()
    
    def test_umichedu_369a4134(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Prospective Students')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='prospective-students']/div[2]/div[2]/div[1]/div[1]/ul[1]/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Register for a tour for prospective first-year students')]").click()
        self.driver.find_element(By.XPATH, "//a[@title='Next']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'3')]").click()
    
    def test_umichedu_424a9b25(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Health & Medicine')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='health-medicine']/div[2]/div[2]/div[3]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='home-content']/div[3]/div[1]/div[1]/div[2]/a[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Undergraduate Information Session (First-Year Entry)')]").click()
    
    def test_umichedu_5a05fede(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Academics')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='academics']/div[2]/div[2]/div[7]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='None selected']").click()
        self.driver.find_element(By.XPATH, "//div[@id='divSearchForm']/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='None selected']").click()
        self.driver.find_element(By.XPATH, "//input[@value='100' and @type='checkbox']").click()
        self.driver.find_element(By.ID, "contentMain_btnSearch").click()
        self.driver.find_element(By.XPATH, "//div[@id='contentMain_panelResults']/div[4]/div[1]/div[1]/div[1]/a[1]/font[1]").click()
    
    def test_umichedu_5bd34d11(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Students')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tuition & Fees')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[3]/div[2]/article[1]/div[1]/div[2]/section[1]/a[1]/div[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[3]/div[2]/article[1]/div[1]/div[2]/section[1]/a[1]/div[1]/h2[1]").click()
    
    def test_umichedu_77e17464(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Academics')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='academics']/div[2]/div[2]/div[3]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "edit-field-school-college-target-id-13").click()
        self.driver.find_element(By.ID, "edit-field-school-college-target-id-16").click()
        self.driver.find_element(By.ID, "edit-submit-node").click()
    
    def test_umichedu_87108e28(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Athletics')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='athletics']/div[2]/div[2]/div[1]/div[1]/ul[1]/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='schedule-view-default']/div[1]/section[1]/ul[1]/li[1]/button[1]").click()
    
    def test_umichedu_8d77fb93(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Athletics')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='athletics']/div[2]/div[2]/div[4]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='navbar-collapse-1']/ul[1]/li[1]/a[1]/span[1]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Soccer')]").click()
    
    def test_umichedu_bcfeed8e(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Life at Michigan')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='life-at-michigan']/div[2]/div[2]/div[1]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Events')]").click()
        self.driver.find_element(By.ID, "start-date").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'5')]").click()
        self.driver.find_element(By.ID, "end-date").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'12')]").click()
        self.driver.find_element(By.XPATH, "//section[@id='content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Workshop / Seminar')]").click()
        self.driver.find_element(By.ID, "7").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Museum of Art')]").click()
    
    def test_umichedu_c33de9e1(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Life at Michigan')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='life-at-michigan']/div[2]/div[2]/div[1]/div[1]/ul[1]/li[7]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='menu-item-446']/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='post-352']/div[1]/table[1]/tbody[1]/tr[2]/td[3]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='post-317']/div[1]/div[2]/button[2]").click()
    
    def test_umichedu_c4dc5da3(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.ID, "quick-links-action-button").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Academic Calendar')]").click()
        self.driver.find_element(By.ID, "edit-field-calendar-type-target-id-2").click()
        self.driver.find_element(By.ID, "edit-field-term-target-id").clear()
        self.driver.find_element(By.ID, "edit-field-term-target-id").select("Fall 2024")
        self.driver.find_element(By.ID, "edit-submit-calendars").click()
    
    def test_umichedu_c76f5aac(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Current Students')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-students']/div[2]/div[2]/div[2]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "edit-college-school").clear()
        self.driver.find_element(By.ID, "edit-college-school").select("College of Pharmacy")
        self.driver.find_element(By.ID, "edit-level-of-study").clear()
        self.driver.find_element(By.ID, "edit-level-of-study").select("Undergraduate")
        self.driver.find_element(By.ID, "edit-submit-tuition-fees-relationship").click()
    
    def test_umichedu_e5414fb8(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Campus Life')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[3]/div[2]/div[3]/div[2]/section[1]/a[2]/div[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='mainbody']/div[2]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[92]/div[1]/div[5]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Inside Athletics')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Youth Camps')]").click()
    