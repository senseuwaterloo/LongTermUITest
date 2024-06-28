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
class TestNpsGov:
    
    def test_npsgov_0db002f6(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.XPATH, "//button[@id='GlobalNav-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Passes')]").click()
        self.driver.find_element(By.ID, "https://store.usgs.gov/pass|").click()
        self.driver.find_element(By.XPATH, "//div[@id='block-uswds-usgs-store-content']/article[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='block-uswds-usgs-store-content']/article[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='block-uswds-usgs-store-content']/article[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='block-uswds-usgs-store-content']/article[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[4]/span[1]/button[1]").click()
    
    def test_npsgov_2a831fb6(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.ID, "anch_6").click()
        self.driver.find_element(By.ID, "anch_63").click()
        self.driver.find_element(By.ID, "form-park").clear()
        self.driver.find_element(By.ID, "form-park").select("Colorado")
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Activity']").click()
        self.driver.find_element(By.XPATH, "//input[@value='23' and @type='checkbox']").click()
        self.driver.find_element(By.ID, "FacetedSearch-submitButton").click()
    
    def test_npsgov_4132002e(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.XPATH, "//button[@id='GlobalNav-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='CollapsibleForm']/div[3]/span[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='Living History' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='DatePicker']/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]/i[1]").click()
    
    def test_npsgov_612653f8(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.XPATH, "//div[@id='HERO']/nav[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "anch_17").click()
        self.driver.find_element(By.ID, "anch_37").click()
    
    def test_npsgov_6eeaa528(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.XPATH, "//div[@id='HERO']/nav[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "anch_12").click()
        self.driver.find_element(By.ID, "anch_25").click()
    
    def test_npsgov_6fd2a5e9(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.ID, "anch_6").click()
        self.driver.find_element(By.ID, "anch_63").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Topic']").click()
        self.driver.find_element(By.XPATH, "//input[@value='38' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='CS_CCF_5275265_5084463']/div[2]/div[1]/div[3]/span[1]/div[1]/div[1]/button[44]/span[1]/input[1]").click()
        self.driver.find_element(By.ID, "FacetedSearch-submitButton").click()
    
    def test_npsgov_7b5b2188(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.ID, "GlobalNav-toggle").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Volunteer')]").click()
        self.driver.find_element(By.ID, "anch_5").click()
        self.driver.find_element(By.ID, "anch_6").click()
    
    def test_npsgov_7bdf34b4(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.ID, "anch_6").click()
        self.driver.find_element(By.ID, "FindAParkName").clear()
        self.driver.find_element(By.ID, "FindAParkName").send_keys("Alagnak")
        self.driver.find_element(By.ID, "FindAParkName__option--0").click()
        self.driver.find_element(By.XPATH, "//a[@id='anch_9']/svg[1]/use[1]").click()
    
    def test_npsgov_83ada6a6(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.XPATH, "//button[@id='GlobalNav-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Photos & Multimedia')]").click()
        self.driver.find_element(By.ID, "https://npgallery.nps.gov/|").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[1]/div[1]/div[3]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[4]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[1]/div[1]/div[4]/button[1]/span[1]").click()
    
    def test_npsgov_8d7a29cf(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.XPATH, "//button[@id='GlobalNav-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Events')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='CollapsibleForm']/div[2]/span[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='IL' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='CollapsibleForm']/div[3]/span[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='CollapsibleForm']/div[3]/span[1]/div[1]/div[1]/button[4]/span[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='CollapsibleForm2']/button[1]").click()
    
    def test_npsgov_bef473f1(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.XPATH, "//div[@id='HERO']/nav[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "anch_8").click()
        self.driver.find_element(By.ID, "anch_113").click()
        self.driver.find_element(By.ID, "CP___PAGEID=6776794,kenai-mountains-turnagain-arm-national-heritage-area.htm,30224|").click()
    
    def test_npsgov_c2a17420(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.ID, "anch_6").click()
        self.driver.find_element(By.ID, "FindAParkName").clear()
        self.driver.find_element(By.ID, "FindAParkName").send_keys("Canyon de Chelly")
        self.driver.find_element(By.ID, "FindAParkName__option--0").click()
        self.driver.find_element(By.XPATH, "//a[@id='anch_11']/svg[1]/use[1]").click()
    
    def test_npsgov_f863168b(self):
        # self.driver.get("https://nps.gov")
        self.driver.find_element(By.ID, "anch_6").click()
        self.driver.find_element(By.ID, "anch_63").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Activity']").click()
        self.driver.find_element(By.XPATH, "//input[@value='82' and @type='checkbox']").click()
        self.driver.find_element(By.ID, "FacetedSearch-submitButton").click()
    