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
class TestAkcOrg:
    
    def test_akcorg_7933484c(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Breeds A-Z')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View All Breeds')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[2]/div[1]/h3[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[2]/div[2]/div[3]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[3]/div[1]/h3[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[3]/div[2]/div[3]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[5]/div[1]/h3[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[5]/div[2]/div[9]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Submit')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='breed-type-card-']/a[1]/h3[1]").click()
    
    def test_akcorg_5e73dffe(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Products & Services')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Dog Groomer')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/svg[1]/use[1]").click()
        self.driver.find_element(By.ID, "react-select-2-option-4").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]").send_keys("10005")
        self.driver.find_element(By.ID, "react-select-3-option-0").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/svg[1]/use[1]").click()
        self.driver.find_element(By.ID, "react-select-4-option-3").click()
        self.driver.find_element(By.XPATH, "//button[@name='' and @type='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/a[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//button[@name='' and @type='button']").click()
    
    def test_akcorg_607dfa0d(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Boxer')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Breeds')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Bulldog')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Breeds')]").click()
    
    def test_akcorg_36d7dc8f(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Agility')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Events')]").click()
    
    def test_akcorg_5b1732fb(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[1]/div[1]/nav[1]/a[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "react-select-2-option-69").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "react-select-3-option-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]").send_keys("ALABAMA")
        self.driver.find_element(By.ID, "react-select-4-option-0").click()
        self.driver.find_element(By.XPATH, "//button[@name='' and @type='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[2]/div[1]/form[1]/div[2]/p[1]/span[2]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[5]/div[2]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[3]/div[3]/div[1]/div[1]/div[3]/div[1]/a[3]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@name='' and @type='button']").click()
    
    def test_akcorg_dd3b12e6(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.ID, "homepage-hero-breed-search-selectized").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Golden Retriever')]").click()
    
    def test_akcorg_697f9915(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Obedience')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Events')]").click()
        self.driver.find_element(By.XPATH, "//strong[contains(.,'Search Events Calendar')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View Events')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='input--event-type']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='control-box--event-type']/div[2]/div[2]/div[2]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='control-box--event-type']/div[2]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='input--location']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='control-box--location']/div[2]/div[2]/div[3]/label[7]").click()
        self.driver.find_element(By.XPATH, "//div[@id='control-box--location']/div[2]/div[1]/button[3]").click()
        self.driver.find_element(By.ID, "default_widget").click()
        self.driver.find_element(By.XPATH, "//div[@id='monthpicker_043290360658912985']/table[1]/tbody[1]/tr[2]/td[2]").click()
        self.driver.find_element(By.XPATH, "//form[@id='inputform']/div[3]/div[3]/button[1]").click()
    
    def test_akcorg_6b5cc19d(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Breeds A-Z')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dog-breeds']/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Afghan Hound')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Akita')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[3]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Azawakh')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Breeds')]").click()
    
    def test_akcorg_79450983(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Cardigan Welsh Corgi')]").click()
        self.driver.find_element(By.ID, "tab__breed-page__traits__social").click()
        self.driver.find_element(By.ID, "accordion-10").click()
    
    def test_akcorg_7b39d904(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See Upcoming Events')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Events Near You')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='input--event-type']/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='event_type' and @value='HT' and @type='radio']").click()
        self.driver.find_element(By.XPATH, "//div[@id='control-box--event-type']/div[2]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='input--location']/span[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='input--location']/span[1]").send_keys("TEXAS")
        self.driver.find_element(By.XPATH, "//div[@id='control-box--location']/div[2]/div[2]/div[4]/label[5]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='control-box--location']/div[2]/div[1]/button[3]").click()
        self.driver.find_element(By.XPATH, "//form[@id='inputform']/div[3]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='divCalendar']/table[1]/tbody[1]/tr[4]/td[6]/div[1]/a[1]").click()
        self.driver.find_element(By.ID, "addeventatc1").click()
        self.driver.find_element(By.ID, "addeventatc1-google").click()
    
    def test_akcorg_807a79ec(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Expert Advice')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='expert-advice']/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dnt-landing']/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cute')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dnt-landing']/div[2]/div[20]/label[1]").click()
    
    def test_akcorg_9d42f53a(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Event Search')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Search near City')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='locationName']/input[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='locationName']/input[1]").send_keys("brighton")
        self.driver.find_element(By.XPATH, "//form[@id='locationName']/typeahead-container[1]/button[5]/span[1]").click()
        self.driver.find_element(By.NAME, "radius").clear()
        self.driver.find_element(By.NAME, "radius").select("100 Miles")
        self.driver.find_element(By.XPATH, "//date-selection[@id='location']/div[1]/div[2]/date-picker[1]/div[1]/div[1]/div[1]/div[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[9]/div[1]/div[2]/table[1]/thead[1]/tr[1]/th[2]/select[1]").clear()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[9]/div[1]/div[2]/table[1]/thead[1]/tr[1]/th[2]/select[1]").select("May")
        self.driver.find_element(By.XPATH, "//td[contains(.,'15')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[9]/div[3]/div[2]/table[1]/thead[1]/tr[1]/th[2]/select[1]").clear()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[9]/div[3]/div[2]/table[1]/thead[1]/tr[1]/th[2]/select[1]").select("May")
        self.driver.find_element(By.XPATH, "//td[contains(.,'30')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/app-root[1]/main[1]/div[2]/search[1]/div[1]/div[2]/div[1]/breed-options[1]/div[1]/div[3]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='competition']/comp-type[1]/div[1]/div[1]/div[1]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='competition']/comp-type[1]/div[1]/div[1]/div[1]/div[4]/div[1]/ul[1]/li[1]/fancy-checkbox[1]/label[1]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='competition']/comp-type[1]/div[1]/div[1]/div[1]/div[4]/div[1]/ul[1]/li[2]/fancy-checkbox[1]/label[1]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='RETRIEVE EVENTS' and @type='button']").click()
    
    def test_akcorg_ba537ab6(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Expert Advice')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Nutrition')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Vitamins & Supplements')]").click()
    
    def test_akcorg_c7b0b259(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[1]/div[1]/nav[1]/a[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "react-select-2-option-5").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "react-select-3-option-1").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]").send_keys("Chicago")
        self.driver.find_element(By.ID, "react-select-4-option-0").click()
        self.driver.find_element(By.XPATH, "//button[@name='' and @type='button']").click()
    
    def test_akcorg_ce886520(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Judges Directory')]").click()
        self.driver.find_element(By.ID, "lastName").clear()
        self.driver.find_element(By.ID, "lastName").send_keys("Williams")
        self.driver.find_element(By.XPATH, "//option[@value='AK']").click()
        self.driver.find_element(By.ID, "submit_button").click()
    
    def test_akcorg_a02e8361(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Products & Services')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'AKC Veterinary Network')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for a Veterinarian')]").click()
        self.driver.find_element(By.ID, "zipCodeId").clear()
        self.driver.find_element(By.ID, "zipCodeId").send_keys("75228")
        self.driver.find_element(By.XPATH, "//lib-searchable-dropdown[@id='radiusSelect']/div[1]/angular2-multiselect[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//lib-searchable-dropdown[@id='radiusSelect']/div[1]/angular2-multiselect[1]/div[1]/div[2]/div[3]/div[3]/ul[1]/li[2]/label[1]").click()
        self.driver.find_element(By.ID, "agreeCheckId").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
        self.driver.find_element(By.XPATH, "//td[@role='cell']").click()
    
    def test_akcorg_a138caa3(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[1]/div[1]/nav[1]/a[3]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Start Dog Registration Process')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[4]/div[1]/main[1]/form[1]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[4]/div[1]/main[1]/form[1]/div[1]/div[2]/div[2]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue To Registration')]").click()
    
    def test_akcorg_b5d06b36(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Breeds A-Z')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dog-breeds']/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Affenpinscher')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Afghan Hound')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Breeds')]").click()
    
    def test_akcorg_ff1fb71d(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.ID, "homepage-hero-breed-search-selectized").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Beagle')]").click()
        self.driver.find_element(By.ID, "tab__breed-page__traits__physical").click()
        self.driver.find_element(By.ID, "accordion-7").click()
    