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
class TestStubhub:
    
    def test_stubhub_d9e70643(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Help Center')]").click()
        self.driver.find_element(By.XPATH, "//h3[contains(.,'Where are my tickets?')]").click()
        self.driver.find_element(By.ID, "61000276824").click()
    
    def test_stubhub_dd3ef13f(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("KEVIN HART")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("BRISBANE")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[2]/div[1]/div[2]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[5]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[2]/a[1]/button[1]").click()
    
    def test_stubhub_e27fee2b(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("Blackpink")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[8]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
    
    def test_stubhub_3b1340a5(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/span[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    
    def test_stubhub_613e8978(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View All')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Celine Dion')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[10]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[4]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[7]/div[1]/div[2]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[2]/a[1]/button[1]").click()
    
    def test_stubhub_662af945(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("TAYLOR SWIFT")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("LAS VEGAS")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[2]/div[1]/div[2]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[2]/a[1]/button[1]").click()
    
    def test_stubhub_6f79871b(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/div[3]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("Austin")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/div[4]/div[1]/div[2]/div[2]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("NOFX")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/button[1]").click()
    
    def test_stubhub_77ed39d9(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/button[1]").click()
    
    def test_stubhub_7a9212a8(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/div[3]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("Boston")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/div[4]/div[1]/div[2]/div[2]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("NHL")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
    
    def test_stubhub_7eefb724(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("Adele")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[2]/a[1]/button[1]").click()
    
    def test_stubhub_8eb3f652(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("Bad Bunny")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]").click()
    
    def test_stubhub_abf2e88a(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("Los Angeles Lakers")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
    
    def test_stubhub_d4c8f4ae(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("Harry Styles")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[22]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[27]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/select[1]").select("4")
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[2]/div[1]/div[4]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/label[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
    
    def test_stubhub_1567bfa7(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("MIAMI HEAT")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("NEW YOK")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[2]/div[1]/div[2]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[3]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[6]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[10]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//select[@name='quantity-select']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='quantity-select']").select("6 tickets")
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[2]/a[1]/button[1]").click()
    
    def test_stubhub_18c81087(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Occasion')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Birthday')]").click()
        self.driver.find_element(By.ID, "card_b2c_2020_birthday1_virtual").click()
        self.driver.find_element(By.ID, "btnChooseNext2").click()
        self.driver.find_element(By.XPATH, "//div[@id='mainContent']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "btnPersonalizeForme").click()
        self.driver.find_element(By.ID, "btnPersonalizeNext2").click()
    
    def test_stubhub_1da50745(self):
        # self.driver.get("https://stubhub.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Top Cities')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/a[8]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='theatre']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/img[1]").click()
    