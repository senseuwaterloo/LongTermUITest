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
class TestWebmd:
    
    def test_webmd_84f8cbd9(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Doctor')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @type='text' and @placeholder='Search doctors, conditions, or procedures']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @type='text' and @placeholder='Search doctors, conditions, or procedures']").send_keys("migrain")
        self.driver.find_element(By.XPATH, "//li[@id='webmd-typeahead-5531-item-1']/div[1]/strong[1]").click()
        self.driver.find_element(By.ID, "searchlocation_desktop").clear()
        self.driver.find_element(By.ID, "searchlocation_desktop").send_keys("philadelphia")
        self.driver.find_element(By.XPATH, "//li[@id='webmd-typeahead-5401-item-0']/div[1]/strong[1]").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-110").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-110']/div[1]/div[1]/div[1]/label[1]/span[2]/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-90").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-90']/div[1]/div[2]/div[1]/div[1]/div[1]/label[2]/span[1]").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-135").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-135']/div[1]/label[4]/span[2]").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-75").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-75']/div[1]/div[3]/div[1]/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Jonathan H Indik MD')]").click()
    
    def test_webmd_89a03889(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-2").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Pill Identifier')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='Enter Pill Imprint']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='Enter Pill Imprint']").send_keys("123")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Select']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[1]/div[1]/ul[1]/div[11]/div[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ContentPane14']/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Round')]").click()
    
    def test_webmd_92a49fdb(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-6").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Best Hospitals')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cardiology')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Portland')]").click()
        self.driver.find_element(By.XPATH, "//span[@type='primary']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'PHYSICIANS AT THIS HOSPITAL')]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Select Specialty']").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Child Neurology')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Dr. Robert Jason Coryell, MD')]").click()
    
    def test_webmd_b3f27ec6(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Doctor')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[5]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Botox (Botulinum toxin)')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rhode Island')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Bristol')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/main[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-186").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-186']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Add a First Preferred Date']").click()
        self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[4]/div[5]").click()
        self.driver.find_element(By.XPATH, "//input[@name='first_name' and @value='' and @placeholder='First Name']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='first_name' and @value='' and @placeholder='First Name']").send_keys("James")
        self.driver.find_element(By.XPATH, "//input[@name='last_name' and @value='' and @placeholder='Last Name']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='last_name' and @value='' and @placeholder='Last Name']").send_keys("Smith")
        self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/select[1]").select("1990")
        self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/select[1]").select("June")
        self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[4]/div[4]").click()
        self.driver.find_element(By.XPATH, "//input[@name='phone' and @value='' and @placeholder='(555) 555-5555']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='phone' and @value='' and @placeholder='(555) 555-5555']").send_keys("456546546")
        self.driver.find_element(By.XPATH, "//input[@name='email' and @value='' and @placeholder='email@example.com']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='email' and @value='' and @placeholder='email@example.com']").send_keys("buckeye.foobar@gmail.com")
        self.driver.find_element(By.XPATH, "//textarea[@name='visit_reason' and @placeholder='']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@name='visit_reason' and @placeholder='']").send_keys("Consultation")
    
    def test_webmd_b41de74c(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-6").click()
        self.driver.find_element(By.ID, "vn-link-hdr-site-6").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Newsletters')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Family &')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='adserved-ddg']/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ContentPane30']/div[1]/section[1]/div[1]/ul[1]/li[4]/a[1]/div[2]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='x53']/a[1]/h4[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ContentPane31']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/span[11]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ContentPane31']/div[1]/div[1]/div[3]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='active']/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ContentPane31']/div[1]/div[1]/div[3]/div[1]/div[4]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ContentPane31']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]").click()
    
    def test_webmd_c0ecc025(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-1").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Depression')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Diagnosis')]").click()
    
    def test_webmd_c920a7d2(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Family &')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\"Children's Vaccines\")]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Vaccine Schedule')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'What Is a Vaccination Schedule?')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Types of Vaccines')]").click()
    
    def test_webmd_ce41fd2f(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Health')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sleep Disorders')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='adserved-ddg']/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ContentPane31']/section[2]/ul[1]/li[7]/a[1]/div[1]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Circadian Rhythm Sleep Disorders')]").click()
    
    def test_webmd_e046373c(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-2").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Supplements')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Chromium')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Interactions')]").click()
    
    def test_webmd_05e827ee(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-2").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drugs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drugs &')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drug Comparison Tool')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tramadol Oral vs. Dilaudid Oral')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Prices')]").click()
    
    def test_webmd_0c874738(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Doctor')]").click()
        self.driver.find_element(By.XPATH, "//div[@role='tab']").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-19']/div[1]/ul[1]/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Audiology')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Michigan')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Jackson')]").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-240").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-240']/div[1]/div[2]/div[1]/label[1]/span[2]/div[1]/span[2]").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-75").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-75']/div[1]/div[3]/div[1]/label[1]/span[2]").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-90").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-90']/div[1]/div[2]/div[1]/div[1]/div[1]/label[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[3]/div[1]/a[1]/h2[1]").click()
    
    def test_webmd_4c57385a(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-3").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Birth Control')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Types')]").click()
    
    def test_webmd_5d51089f(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Doctor')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @type='text' and @placeholder='Search doctors, conditions, or procedures']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @type='text' and @placeholder='Search doctors, conditions, or procedures']").send_keys("Stomach Pain")
        self.driver.find_element(By.XPATH, "//ul[@id='webmd-typeahead-3020']/li[1]/a[1]/strong[1]").click()
        self.driver.find_element(By.ID, "searchlocation_desktop").clear()
        self.driver.find_element(By.ID, "searchlocation_desktop").send_keys("San Antonio")
        self.driver.find_element(By.XPATH, "//li[@id='webmd-typeahead-8323-item-0']/div[1]/strong[1]").click()
    
    def test_webmd_61acfbd7(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='vn-menu-hdr-site-1']/ul[1]/li[28]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\"Children's Conditions A-Z\")]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Clubfoot')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Treatment')]").click()
    
    def test_webmd_67ae570b(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-2").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drugs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search Medications by Condition')]").click()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='Enter condition to search medication']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='Enter condition to search medication']").send_keys("herpes zoster")
        self.driver.find_element(By.XPATH, "//div[@id='ContentPane15']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='Enter condition to search medication']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'herpes zoster')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Reviews')]").click()
    
    def test_webmd_68893ec2(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Doctor')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-22']/div[1]/ul[1]/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'K')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Kidney Stone Surgery')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/main[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Nephrology')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Texas')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Austin')]").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-301").click()
        self.driver.find_element(By.XPATH, "//div[@role='slider']").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-306").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-306']/div[1]/div[1]/div[1]/label[1]/span[2]/div[1]").click()
        self.driver.find_element(By.ID, "webmd-collapse-head-75").click()
        self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-75']/div[1]/div[3]/div[1]/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[3]/div[1]/a[1]/h2[1]").click()
    
    def test_webmd_2192cca2(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-1").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Allergies')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Food Allergies')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tests for Food Allergies')]").click()
    
    def test_webmd_21c2203c(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Symptom Checker')]").click()
        self.driver.find_element(By.ID, "age").clear()
        self.driver.find_element(By.ID, "age").send_keys("30")
        self.driver.find_element(By.XPATH, "//button[@id='female']/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Continue Button']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Type your main symptom here' and @title='']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Type your main symptom here' and @title='']").send_keys("toothache")
        self.driver.find_element(By.XPATH, "//ul[@id='resultContainer']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ContentPane30']/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]").click()
    
    def test_webmd_47e4f80b(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.ID, "vn-link-hdr-site-2").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Interaction Checker')]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter two or more drugs' and @title='']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter two or more drugs' and @title='']").send_keys("Ibuprofen")
        self.driver.find_element(By.XPATH, "//ul[@id='resultContainer']/li[1]/a[1]/span[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter two or more drugs' and @title='']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter two or more drugs' and @title='']").send_keys("Aspirin")
        self.driver.find_element(By.XPATH, "//ul[@id='resultContainer']/li[1]/a[1]/span[1]").click()
    
    def test_webmd_4835a052(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//div[@id='vn-links']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @name='query' and @value='' and @type='text' and @placeholder='Search WebMD']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @name='query' and @value='' and @type='text' and @placeholder='Search WebMD']").send_keys("sleep apnea symptoms")
        self.driver.find_element(By.XPATH, "//li[@id='webmd-typeahead-item-0']/span[1]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Symptoms of Sleep Apnea')]").click()
    