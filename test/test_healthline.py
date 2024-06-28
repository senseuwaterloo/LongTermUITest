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
class TestHealthline:
    
    def test_healthline_79ed44d6(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[2]/ul[1]/li[1]/div[1]/a[1]/span[1]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Healthy Eating')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-host']/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[4]/div[6]/div[1]/div[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'30 High Protein Snacks That Are Healthy and Portable')]").click()
        self.driver.find_element(By.XPATH, "//a[@title='Print this page']").click()
    
    def test_healthline_81035475(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Diet')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[5]/ul[1]/div[1]/div[2]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[5]/ul[1]/div[2]/div[2]/div[3]/button[1]").click()
    
    def test_healthline_95359e31(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//form[@id='healthline-search-form']/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='q1' and @value='' and @placeholder='Search Healthline']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='q1' and @value='' and @placeholder='Search Healthline']").send_keys("Vivitrol")
        self.driver.find_element(By.XPATH, "//form[@id='healthline-search-form']/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/div[3]/div[3]/div[1]/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Dosage')]").click()
    
    def test_healthline_ad8a4699(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='nav-panel-flyout-wrapper']/div[1]/div[2]/ul[1]/li[4]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Transform: Future of Health - The Therapeutic Benefits of Psychedelics')]").click()
    
    def test_healthline_d5cd0664(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gut Health')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='email' and @value='' and @type='email' and @placeholder='Enter your email']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='email' and @value='' and @type='email' and @placeholder='Enter your email']").send_keys("buck19915@gmail.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/form[1]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]").click()
    
    def test_healthline_eb222205(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Newsletters')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/form[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/label[1]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/form[1]/div[2]/div[1]/div[1]/div[1]/div[7]/div[1]/div[2]/label[1]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/form[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[2]/label[1]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/form[1]/div[2]/div[1]/div[1]/div[1]/div[18]/div[1]/div[2]/label[1]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/form[1]/div[2]/div[1]/div[1]/div[1]/div[20]/div[1]/div[2]/label[1]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='email' and @value='' and @type='email' and @placeholder='Enter your email']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='email' and @value='' and @type='email' and @placeholder='Enter your email']").send_keys("buckeye.foobar@gmail.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/form[1]/div[2]/div[1]/section[1]/div[1]/div[1]/button[1]/span[1]").click()
    
    def test_healthline_f14c55fc(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//button[@role='menuitem' and @type='button']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Breast Cancer')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Treatments')]").click()
    
    def test_healthline_60e959e8(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Healthy Snacks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
    
    def test_healthline_6585d751(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Bipolar Disorder')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Causes and risk factors')]").click()
    
    def test_healthline_66c89053(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mindful Eating')]").click()
    
    def test_healthline_6daf6bb2(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//button[@role='menuitem' and @type='button']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Acid Reflux')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-host']/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Treatment options')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Yes')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-host']/div[1]/div[1]/div[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-host']/div[1]/div[1]/div[1]/button[1]").click()
    
    def test_healthline_77979435(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Weight Management')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'CONTINUE')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[6]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[7]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[2]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[5]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Read More')]").click()
    
    def test_healthline_21d3931e(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Diet')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
    
    def test_healthline_2b4b55d9(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='nav-panel-flyout-wrapper']/div[1]/div[2]/ul[1]/li[2]/div[1]/div[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'CBD')]").click()
    
    def test_healthline_c44c645d(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Type 2 Diabetes')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Type 2 Diabetes: Vitamin D May Slightly Lower Risk for People with…')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Yes')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modal-host']/div[1]/div[1]/div[1]/div[1]/button[2]").click()
    
    def test_healthline_373a92f6(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//form[@id='healthline-search-form']/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='q1' and @value='' and @placeholder='Search Healthline']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='q1' and @value='' and @placeholder='Search Healthline']").send_keys("vegan diet")
        self.driver.find_element(By.XPATH, "//form[@id='healthline-search-form']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/div[3]/div[1]/div[1]/a[1]/span[1]/em[3]").click()
    
    def test_healthline_51a2f042(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drugs A-Z')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Amoxicillin')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Side effects')]").click()
    
    def test_healthline_52acfc8d(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Healthy Snacks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/ul[1]/a[2]").click()
    
    def test_healthline_579091c0(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[2]/ul[1]/li[2]/div[1]/a[1]/span[1]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sleep Disorders')]").click()
    
    def test_healthline_5891bf55(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'IBD')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Treatments')]").click()
    
    def test_healthline_0d91fb81(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Diet')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/ul[1]/a[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='unselected']/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='enabled']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='preferences-d']/div[2]/div[4]/div[1]/div[1]/label[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='preferences-d']/div[2]/div[4]/div[1]/div[1]/label[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='preferences-d']/div[2]/div[4]/div[1]/div[1]/label[6]/span[1]").click()
        self.driver.find_element(By.ID, "emailInput").clear()
        self.driver.find_element(By.ID, "emailInput").send_keys("buckeye.foobar@gmail.com")
        self.driver.find_element(By.ID, "submit").click()
    
    def test_healthline_161b687a(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Acid Reflux')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Symptoms')]").click()
    
    def test_healthline_1760bd6e(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Primary Care')]").click()
        self.driver.find_element(By.ID, "where").clear()
        self.driver.find_element(By.ID, "where").send_keys("Milwaukee")
        self.driver.find_element(By.XPATH, "/html/body[1]/ps-providersearchbaralternative[1]/div[1]/form[1]/div[3]/div[2]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Search')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Filters')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rating: High to Low')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Filters')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/ps-providerresultswithmap[1]/main[1]/ps-providerfilterscontrol-fc[1]/form[1]/div[2]/div[1]/div[4]/ps-providerfilters[1]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/ul[1]/li[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/ps-providerresultswithmap[1]/main[1]/ps-providerfilterscontrol-fc[1]/form[1]/div[2]/div[1]/div[4]/ps-providerfilters[2]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/ul[1]/li[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/ps-providerresultswithmap[1]/main[1]/ps-providerfilterscontrol-fc[1]/form[1]/div[2]/div[1]/div[4]/ps-providerfilters[4]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/ul[1]/li[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/ps-providerresultswithmap[1]/main[1]/ps-providerfilterscontrol-fc[1]/form[1]/div[2]/div[1]/div[4]/ps-providerfilters[6]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/ul[1]/li[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Show')]").click()
        self.driver.find_element(By.XPATH, "//button[@id='sortToggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rating: High to Low')]").click()
    