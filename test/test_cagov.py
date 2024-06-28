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
class TestCaGov:
    
    def test_cagov_6ab62146(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply for Food Stamps')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='launch-apply-for-food-stamps']/span[2]").click()
        self.driver.find_element(By.XPATH, "//button[@id='lift-ux-id-f350ae04cbec434090810ef664694b75']/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='lift-ux-id-45278c4b81bf4cba8032d70e361fd853']/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='lift-ux-id-21e17d855bac418c9ca61c3c3b957dc4']/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='lift-ux-id-ded1ebe75585462da99cd37ee776e14c']/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.ID, "text1").clear()
        self.driver.find_element(By.ID, "text1").send_keys("Jane")
        self.driver.find_element(By.ID, "text3").clear()
        self.driver.find_element(By.ID, "text3").send_keys("Martin")
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.ID, "disability0").click()
        self.driver.find_element(By.ID, "deaf1").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.ID, "CollegeStudentE_radio_button_1").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.ID, "label_1").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.ID, "addressLine1").clear()
        self.driver.find_element(By.ID, "addressLine1").send_keys("123 Main street")
        self.driver.find_element(By.ID, "city").clear()
        self.driver.find_element(By.ID, "city").send_keys("Los Angeles")
        self.driver.find_element(By.ID, "county").clear()
        self.driver.find_element(By.ID, "county").select("Alameda")
        self.driver.find_element(By.ID, "zip5").clear()
        self.driver.find_element(By.ID, "zip5").send_keys("90001")
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
    
    def test_cagov_6fe6fa2a(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[7]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Look Up a Bill or Law')]").click()
        self.driver.find_element(By.ID, "launch-look-up-a-bill-or-law").click()
        self.driver.find_element(By.ID, "search_bill_num").clear()
        self.driver.find_element(By.ID, "search_bill_num").send_keys("AB1548")
        self.driver.find_element(By.ID, "home_search_bills_button").click()
    
    def test_cagov_72346d21(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[7]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Register to Vote')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='launch-register-to-vote']/span[2]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_cagov_7437b124(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//div[@id='askGroup']/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Agency Profile')]").click()
    
    def test_cagov_12b7d4be(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-content']/main[1]/article[1]/div[3]/div[1]/div[1]/div[1]/div[3]/a[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='MSOZoneCell_WebPartWPQ5']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]").click()
    
    def test_cagov_1b4901e9(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[7]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Look Up My Representatives')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='launch-look-up-my-representatives']/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-content-normal']/ul[1]/li[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'State Senate')]").click()
        self.driver.find_element(By.ID, "street").clear()
        self.driver.find_element(By.ID, "street").send_keys("2043 E Lewis Ave")
        self.driver.find_element(By.ID, "city").clear()
        self.driver.find_element(By.ID, "city").send_keys("Fresno")
        self.driver.find_element(By.ID, "ZIP").clear()
        self.driver.find_element(By.ID, "ZIP").send_keys("93701")
        self.driver.find_element(By.ID, "locate_label").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Senator  Anna Caballero')]").click()
    
    def test_cagov_2083a376(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply for a Cal Grant')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='launch-apply-for-a-cal-grant']/span[2]").click()
        self.driver.find_element(By.ID, "accordion-heading-0-0").click()
    
    def test_cagov_34e2c645(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply for Birth Certificate')]").click()
    
    def test_cagov_4b60a0fc(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Department of Motor Vehicles')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='website-department-of-motor-vehicles']/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\"Driver's License & ID Cards\")]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Driver’s Licenses')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Licensing Fees')]").click()
    
    def test_cagov_83e54729(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply for Birth Certificate')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='launch-apply-for-birth-certificate']/span[2]").click()
    
    def test_cagov_99d08027(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[7]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Register to Vote')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\"Los Angeles County - Registrar-Recorder/County Clerk's Administrative Office\")]").click()
    
    def test_cagov_a9c12e1b(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply for Sellers Permit')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='launch-apply-for-sellers-permit']/span[2]").click()
        self.driver.find_element(By.ID, "ui-collapse-000").click()
    
    def test_cagov_f464396e(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.ID, "q").clear()
        self.driver.find_element(By.ID, "q").send_keys("minimum wage rate")
        self.driver.find_element(By.XPATH, "//form[@id='Search']/button[1]/span[1]").click()
    
    def test_cagov_f806cdff(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Your Local School')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='launch-find-your-local-school']/span[2]").click()
        self.driver.find_element(By.ID, "AllSearchField").clear()
        self.driver.find_element(By.ID, "AllSearchField").send_keys("San Jose")
        self.driver.find_element(By.ID, "SimSearchButton").click()
    
    def test_cagov_ff1de5de(self):
        # self.driver.get("https://ca.gov")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'File for Unemployment')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='launch-file-for-unemployment']/span[2]").click()
    