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
class TestEventbrite:
    
    def test_eventbrite_453ebdd8(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//header[@id='global-header']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='global-header']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "menu-item-dropdown-385875").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Event Planning')]").click()
    
    def test_eventbrite_4b8fb0aa(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//header[@id='global-header']/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "search-autocomplete-input").clear()
        self.driver.find_element(By.ID, "search-autocomplete-input").send_keys("fishing")
        self.driver.find_element(By.ID, "search-autocomplete-input").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Price']/div[2]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Format']/div[1]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.ID, "locationPicker").click()
        self.driver.find_element(By.ID, "locationPicker").clear()
        self.driver.find_element(By.ID, "locationPicker").send_keys("chicago")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJ7cv00DwsDogRAMDACa2m4K8']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
    
    def test_eventbrite_105d3ad2(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[1]/h1[1]/div[1]/a[1]/div[1]").click()
        self.driver.find_element(By.ID, "browse-location-selector").clear()
        self.driver.find_element(By.ID, "browse-location-selector").send_keys("Chester, UK")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJafWcYtnBekgRn_jYjbNsYkk']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Date']/div[3]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/aside[1]/div[1]/div[2]/div[5]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Category']/div[13]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
    
    def test_eventbrite_c200352a(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.ID, "search-autocomplete-input").clear()
        self.driver.find_element(By.ID, "search-autocomplete-input").send_keys("food festival")
        self.driver.find_element(By.ID, "location-autocomplete").clear()
        self.driver.find_element(By.ID, "location-autocomplete").send_keys("colorado")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJt1YYm3QUQIcR_6eQSTGDVMc']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='edsModalContentChildren']/div[1]/main[1]/header[1]/div[1]/form[1]/div[1]/div[1]/div[1]/span[2]/span[1]/button[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Date']/div[3]/li[1]/label[1]/span[2]").click()
    
    def test_eventbrite_d075a906(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.ID, "locationPicker").click()
        self.driver.find_element(By.ID, "locationPicker").clear()
        self.driver.find_element(By.ID, "locationPicker").send_keys("san fransisco")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJIQBpAG2ahYAR_6128GcTUEo']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[1]/h1[1]/div[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/aside[1]/div[1]/div[2]/div[5]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Category']/div[9]/li[1]/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Date']/div[3]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Price']/div[1]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/aside[1]/div[1]/div[2]/div[6]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Format']/div[7]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
    
    def test_eventbrite_63c65d96(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//div[@id='panel0']/div[1]/div[1]/div[1]/a[4]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[6]/div[1]/section[1]/div[1]/div[1]/div[1]/a[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/aside[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/button[1]/div[1]").click()
    
    def test_eventbrite_ee22220c(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//header[@id='global-header']/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "search-autocomplete-input").clear()
        self.driver.find_element(By.ID, "search-autocomplete-input").send_keys("pet festival")
        self.driver.find_element(By.XPATH, "//div[@id='edsModalContentChildren']/div[1]/main[1]/header[1]/div[1]/form[1]/div[1]/div[1]/div[1]/span[2]/span[1]/button[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Format']/div[3]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Language']/div[1]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Price']/div[1]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.ID, "locationPicker").clear()
        self.driver.find_element(By.ID, "locationPicker").send_keys("portland")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJJ3SpfQsLlVQRkYXR9ua5Nhw']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Date']/div[4]/li[1]/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Date']/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[7]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Date']/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]/div[1]/div[2]").click()
        self.driver.find_element(By.ID, "eventbrite-widget-modal-trigger-559262147137").click()
        self.driver.find_element(By.ID, "ticket-quantity-selector-931865299").clear()
        self.driver.find_element(By.ID, "ticket-quantity-selector-931865299").select("2")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]").click()
    
    def test_eventbrite_fb7741f6(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//div[@id='panel0']/div[1]/div[1]/div[1]/a[8]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[1]/section[1]/div[2]/div[1]/span[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='this_weekend']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
    
    def test_eventbrite_63388e25(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//li[@id='tab4']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See more')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/aside[1]/div[1]/div[2]/div[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Price']/div[1]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/aside[1]/div[1]/div[2]/div[5]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Category']/div[9]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Format']/div[1]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Language']/div[1]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[2]/div[1]/span[1]/span[1]/button[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/section[1]/div[2]/button[1]").click()
    
    def test_eventbrite_6b54b029(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//header[@id='global-header']/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "search-autocomplete-input").clear()
        self.driver.find_element(By.ID, "search-autocomplete-input").send_keys("music")
        self.driver.find_element(By.ID, "location-autocomplete").clear()
        self.driver.find_element(By.ID, "location-autocomplete").send_keys("los angeles")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJE9on3F3HwoAR9AhGJW_fL-I']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='edsModalContentChildren']/div[1]/main[1]/header[1]/div[1]/form[1]/div[1]/div[1]/div[1]/span[2]/span[1]/button[1]/i[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/aside[1]/div[1]/div[1]/ul[1]/li[3]/button[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/aside[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    
    def test_eventbrite_ddee9314(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//div[@id='panel0']/div[1]/div[1]/div[1]/a[6]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.ID, "category-browse-location-autocomplete").clear()
        self.driver.find_element(By.ID, "category-browse-location-autocomplete").send_keys("LAS VEGAS")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJ0X31pIK3voARo3mz1ebVzDo']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[1]/section[1]/div[2]/div[1]/span[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='tomorrow']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[2]/section[1]/div[2]/div[1]/a[3]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[8]/section[1]/div[2]/div[1]/div[2]/a[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Price']/div[1]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/section[2]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/section[1]/div[2]/button[1]").click()
    
    def test_eventbrite_e9300d50(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//div[@id='panel0']/div[1]/div[1]/div[1]/a[4]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[1]/a[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/aside[1]/div[1]/div[2]/div[2]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/aside[1]/div[1]/div[2]/div[2]/div[1]/label[1]").click()
    
    def test_eventbrite_b5b56e9a(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'here')]").click()
        self.driver.find_element(By.ID, "filter_department_1_0_2").click()
        self.driver.find_element(By.ID, "filter_country_code_1_0_3").click()
        self.driver.find_element(By.ID, "filter_city_1_0_3").click()
        self.driver.find_element(By.ID, "link_job_title_1_0_0").click()
        self.driver.find_element(By.ID, "form_first_name_2_1_0").clear()
        self.driver.find_element(By.ID, "form_first_name_2_1_0").send_keys("James")
        self.driver.find_element(By.ID, "form_last_name_2_1_1").clear()
        self.driver.find_element(By.ID, "form_last_name_2_1_1").send_keys("Smith")
        self.driver.find_element(By.ID, "form_email_2_1_2").clear()
        self.driver.find_element(By.ID, "form_email_2_1_2").send_keys("buckeye.foobar@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@name='form_submission[fields_attributes][3][options_attributes][2][checked]' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@name='form_submission[fields_attributes][3][options_attributes][3][checked]' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@name='form_submission[fields_attributes][3][options_attributes][0][checked]' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//button[@id='form_submit_2_1']/span[1]").click()
    
    def test_eventbrite_cd8d723a(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//header[@id='global-header']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='global-header']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='j_id0:HelpCenterSiteTemplate:j_id2:j_id35:3:j_id42']/section[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[2]/a[1]").click()
    
    def test_eventbrite_2a45ede7(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.ID, "locationPicker").clear()
        self.driver.find_element(By.ID, "locationPicker").send_keys("New Orleans")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJZYIRslSkIIYRtNMiXuhbBts']/div[1]/button[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//li[@id='tab11']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel12']/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/aside[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[2]/div[2]/section[4]/section[1]/div[2]/ul[1]/li[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='edsModalContentChildren']/main[1]/section[2]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "reason").clear()
        self.driver.find_element(By.ID, "reason").select("Question about the event")
    
    def test_eventbrite_51221157(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//header[@id='global-header']/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "search-autocomplete-input").clear()
        self.driver.find_element(By.ID, "search-autocomplete-input").send_keys("music")
        self.driver.find_element(By.ID, "location-autocomplete").clear()
        self.driver.find_element(By.ID, "location-autocomplete").send_keys("ohio")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJwY5NtXrpNogRFtmfnDlkzeU']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='edsModalContentChildren']/div[1]/main[1]/header[1]/div[1]/form[1]/div[1]/div[1]/div[1]/span[2]/span[1]/button[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='View more Format']/div[4]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/section[1]/div[2]/button[1]").click()
    
    def test_eventbrite_74cb088a(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//div[@id='panel0']/div[1]/div[1]/div[1]/a[8]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.ID, "category-browse-location-autocomplete").clear()
        self.driver.find_element(By.ID, "category-browse-location-autocomplete").send_keys("San Francisco")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJIQBpAG2ahYAR_6128GcTUEo']/div[1]/button[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[1]/section[1]/div[2]/div[1]/span[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='pick-a-date']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "chevron-right-chunky_svg__eds-icon--chevron-right-chunky_svg").click()
        self.driver.find_element(By.ID, "chevron-right-chunky_svg__eds-icon--chevron-right-chunky_svg").click()
        self.driver.find_element(By.ID, "chevron-right-chunky_svg__eds-icon--chevron-right-chunky_svg").click()
        self.driver.find_element(By.ID, "chevron-right-chunky_svg__eds-icon--chevron-right-chunky_svg").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[6]/td[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[2]/section[1]/div[2]/div[1]/a[5]/div[1]/div[1]/img[1]").click()
    
    def test_eventbrite_7cd5a347(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//div[@id='panel0']/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[5]/section[1]/section[1]/ul[1]/li[2]/div[1]/div[1]/section[1]/div[1]/div[2]/button[1]").click()
    
    def test_eventbrite_8634bbc0(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//header[@id='global-header']/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "location-autocomplete").clear()
        self.driver.find_element(By.ID, "location-autocomplete").send_keys("Hackney")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJgUR35uUcdkgRkigWi7YDIO4']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "location-autocomplete").click()
        self.driver.find_element(By.ID, "location-autocomplete").clear()
        self.driver.find_element(By.ID, "location-autocomplete").send_keys("Hackney")
        self.driver.find_element(By.XPATH, "//li[@id='ChIJgUR35uUcdkgRkigWi7YDIO4']/div[1]/button[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.ID, "search-autocomplete-input").clear()
        self.driver.find_element(By.ID, "search-autocomplete-input").send_keys("Hackney Clothes Swap - Earth Day")
        self.driver.find_element(By.XPATH, "//div[@id='edsModalContentChildren']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]/div[1]/div[2]").click()
        self.driver.find_element(By.ID, "eventbrite-widget-modal-trigger-556529463607").click()
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        self.driver.find_element(By.ID, "buyer.N-first_name").clear()
        self.driver.find_element(By.ID, "buyer.N-first_name").send_keys("Joe")
        self.driver.find_element(By.ID, "buyer.N-last_name").clear()
        self.driver.find_element(By.ID, "buyer.N-last_name").send_keys("Bloggs")
        self.driver.find_element(By.ID, "buyer.N-email").clear()
        self.driver.find_element(By.ID, "buyer.N-email").send_keys("joe@bloggs.com")
    
    def test_eventbrite_920f240d(self):
        # self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//div[@id='panel0']/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='recent-85633041']/div[1]/button[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[1]/section[1]/div[2]/div[1]/span[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='this_weekend']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[2]/section[1]/div[2]/div[1]/a[3]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/main[1]/div[3]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[3]/span[1]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/main[1]/div[3]/div[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/article[1]/div[1]/div[3]/span[1]/span[1]/button[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/main[1]/div[3]/div[1]/section[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/article[1]/div[1]/div[3]/span[1]/span[1]/button[1]/i[1]/svg[1]").click()
    