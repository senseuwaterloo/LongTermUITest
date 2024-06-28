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
class TestCourseraOrg:
    
    def test_courseraorg_5991ba25(self):
        # self.driver.get("https://coursera.org")
        self.driver.find_element(By.ID, "student-link").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Resources')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//img[@alt='Career Readiness: Secrets to delivering better graduate career outcomes']").click()
        self.driver.find_element(By.ID, "question_first_name").clear()
        self.driver.find_element(By.ID, "question_first_name").send_keys("Johnn")
        self.driver.find_element(By.ID, "question_last_name").clear()
        self.driver.find_element(By.ID, "question_last_name").send_keys("Doe")
        self.driver.find_element(By.ID, "question_email").clear()
        self.driver.find_element(By.ID, "question_email").send_keys("johndoe@gmail.com")
        self.driver.find_element(By.ID, "question_confirm_email").clear()
        self.driver.find_element(By.ID, "question_confirm_email").send_keys("johndoe@gmail.com")
        self.driver.find_element(By.ID, "question_job_title").clear()
        self.driver.find_element(By.ID, "question_job_title").send_keys("Accounting")
        self.driver.find_element(By.ID, "custom_question_0").clear()
        self.driver.find_element(By.ID, "custom_question_0").send_keys("UAI")
        self.driver.find_element(By.ID, "btnSubmit").click()
    
    def test_courseraorg_733d1e8f(self):
        # self.driver.get("https://coursera.org")
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").send_keys("Psychology")
        self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/button[2]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='coursera-onboarding-profile-form']/div[1]/div[3]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "cds-react-aria-84").click()
    
    def test_courseraorg_d27a6164(self):
        # self.driver.get("https://coursera.org")
        self.driver.find_element(By.XPATH, "//div[@id='MegamenuWrapperDiv']/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='learning_paths~menu-item']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Data Analyst')]").click()
        self.driver.find_element(By.ID, "cds-react-aria-55").click()
        self.driver.find_element(By.ID, "cds-react-aria-71").click()
        self.driver.find_element(By.ID, "cds-react-aria-163").click()
        self.driver.find_element(By.ID, "cds-react-aria-97").click()
    
    def test_courseraorg_228fc81a(self):
        # self.driver.get("https://coursera.org")
        self.driver.find_element(By.ID, "student-link").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Resources')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]").click()
        self.driver.find_element(By.ID, "FirstName").clear()
        self.driver.find_element(By.ID, "FirstName").send_keys("John")
        self.driver.find_element(By.ID, "LastName").clear()
        self.driver.find_element(By.ID, "LastName").send_keys("Doe")
        self.driver.find_element(By.ID, "Title").clear()
        self.driver.find_element(By.ID, "Title").send_keys("Accounting")
        self.driver.find_element(By.ID, "Email").clear()
        self.driver.find_element(By.ID, "Email").send_keys("Johndoe@gmail.com")
        self.driver.find_element(By.ID, "Phone").clear()
        self.driver.find_element(By.ID, "Phone").send_keys("234567890")
        self.driver.find_element(By.ID, "Company").clear()
        self.driver.find_element(By.ID, "Company").send_keys("University of Michigan")
        self.driver.find_element(By.ID, "Primary_Discipline__c").clear()
        self.driver.find_element(By.ID, "Primary_Discipline__c").select("Accounting")
        self.driver.find_element(By.ID, "Country").clear()
        self.driver.find_element(By.ID, "Country").select("United States")
        self.driver.find_element(By.ID, "State").clear()
        self.driver.find_element(By.ID, "State").select("MI")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_courseraorg_2776878c(self):
        # self.driver.get("https://coursera.org")
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").send_keys("deeeplearning")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-1-item-0']/div[1]/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.ID, "cds-react-aria-44").click()
        self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/a[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]/div[1]/span[1]").click()
    
    def test_courseraorg_2bc717a1(self):
        # self.driver.get("https://coursera.org")
        self.driver.find_element(By.XPATH, "//div[@id='MegamenuWrapperDiv']/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='free~menu-item']/span[1]").click()
        self.driver.find_element(By.ID, "cds-react-aria-20-label-text").click()
        self.driver.find_element(By.ID, "cds-react-aria-30").click()
        self.driver.find_element(By.ID, "cds-react-aria-42").click()
        self.driver.find_element(By.ID, "cds-react-aria-52").click()
    
    def test_courseraorg_0a060d81(self):
        # self.driver.get("https://coursera.org")
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").send_keys("university of london")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']/div[1]/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='nav-title~1']/span[1]").click()
    
    def test_courseraorg_0cc44161(self):
        # self.driver.get("https://coursera.org")
        self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='certificates~menu-item']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/div[3]/div[1]/section[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h1[1]").click()
    
    def test_courseraorg_efa508bf(self):
        # self.driver.get("https://coursera.org")
        self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='free~menu-item']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "cds-react-aria-95").click()
        self.driver.find_element(By.XPATH, "//div[@id='cds-react-aria-85']/div[3]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
    