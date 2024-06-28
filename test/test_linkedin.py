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
class TestLinkedin:
    
    def test_linkedin_20bc1709(self):
        # self.driver.get("https://www.linkedin.com/")
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").send_keys("Bioinformatician")
        self.driver.find_element(By.XPATH, "//div[@id='basic-result-x8t5c']/div[1]/span[1]/span[1]/strong[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-reusables__filters-bar']/ul[1]/li[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='ember518']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='artdeco-hoverable-artdeco-gen-61']/div[1]/div[1]/form[1]/fieldset[1]/div[1]/ul[1]/li[3]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='ember709']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-reusables__filters-bar']/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "ember981").click()
        self.driver.find_element(By.XPATH, "//button[@id='ember974']/li-icon[1]/svg[1]/path[1]").click()
    
    def test_linkedin_2cc60ed7(self):
        # self.driver.get("https://www.linkedin.com/")
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").send_keys("Calico Life Science")
        self.driver.find_element(By.XPATH, "//div[@id='basic-result-15yz3e']/div[1]/span[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Calico Life Sciences')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ember1377']/div[2]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='ember1643']/span[1]").click()
        self.driver.find_element(By.ID, "ember1667").click()
        self.driver.find_element(By.XPATH, "//button[@id='ember1766']/span[1]/div[1]/span[1]").click()
    
    def test_linkedin_a8637b2a(self):
        # self.driver.get("https://www.linkedin.com/")
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").send_keys("Data Entry")
        self.driver.find_element(By.XPATH, "//div[@id='basic-result-gy9m1']/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.ID, "ember3701").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/section[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "ember3714").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/section[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/span[1]").click()
    
    def test_linkedin_d18531ce(self):
        # self.driver.get("https://www.linkedin.com/")
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").click()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").send_keys("Customer support")
        self.driver.find_element(By.XPATH, "//div[@id='basic-result-q2q46']/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.ID, "jobs-search-box-location-id-ember2657").clear()
        self.driver.find_element(By.ID, "jobs-search-box-location-id-ember2657").send_keys("New York")
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    
    def test_linkedin_f9e3d54d(self):
        # self.driver.get("https://www.linkedin.com/")
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").click()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").send_keys("Linkedin learning")
        self.driver.find_element(By.XPATH, "//div[@id='basic-result-hfnqk']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'LinkedIn Learning')]").click()
        self.driver.find_element(By.XPATH, "//button[@id='ember2339']/span[1]").click()
    