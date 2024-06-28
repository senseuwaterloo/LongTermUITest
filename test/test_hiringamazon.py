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
class TestHiringAmazon:
    
    def test_hiringamazon_183fec0a(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore Benefits →')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find out more')]").click()
    
    def test_hiringamazon_40e4a02d(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search jobs near you')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[3]/div[1]").click()
        self.driver.find_element(By.ID, "zipcode-nav-filter").clear()
        self.driver.find_element(By.ID, "zipcode-nav-filter").send_keys("Lincoln nebraska")
        self.driver.find_element(By.ID, "0").click()
        self.driver.find_element(By.XPATH, "//button[@id='downshift-14-toggle-button']/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='downshift-14-item-6']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.ID, "filterPanelShowFiltersButton").click()
        self.driver.find_element(By.XPATH, "//div[@id='pageRouter']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]").click()
    
    def test_hiringamazon_45b9f4d0(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search jobs near you')]").click()
        self.driver.find_element(By.ID, "zipcode-nav-guide").clear()
        self.driver.find_element(By.ID, "zipcode-nav-guide").send_keys("44278")
        self.driver.find_element(By.ID, "0").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='downshift-110-toggle-button']/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='downshift-110-item-1']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[3]/div[1]").click()
    
    def test_hiringamazon_511a7a5a(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore Available Shifts →')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search Night Shift Jobs')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Night')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Next')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[3]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[3]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search Night Shifts')]").click()
    
    def test_hiringamazon_58ea2569(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs by Location')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[23]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Omaha Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Here are some more jobs that you might be interested in.')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hvh-vanity-url']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pageRouter']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pageRouter']/div[1]/div[1]/div[1]/div[3]/button[2]/div[1]").click()
    
    def test_hiringamazon_73a9575b(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//div[@role='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[5]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='desktopFilter_job_type_filter']/div[1]/div[1]/fieldset[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-results-box']/div[2]/div[1]/div[1]/div[2]/content[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/fieldset[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-results-box']/div[2]/div[1]/div[1]/div[2]/content[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "recent").click()
        self.driver.find_element(By.XPATH, "//div[@id='desktopFilter_normalized_country_code']/div[1]/div[1]/div[1]/div[2]/fieldset[1]/div[1]/button[1]/div[1]").click()
    
    def test_hiringamazon_785bdcfa(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/header[1]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn More')]").click()
    
    def test_hiringamazon_e7984ab4(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/header[1]/div[1]/div[1]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Delivery Station Jobs Near You')]").click()
        self.driver.find_element(By.ID, "zipcode-nav-search").clear()
        self.driver.find_element(By.ID, "zipcode-nav-search").send_keys("capitol hill wa")
        self.driver.find_element(By.ID, "0").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-modal-body']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pageRouter']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pageRouter']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]").click()
    
    def test_hiringamazon_ea3e8b42(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/header[1]/div[1]/div[1]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[5]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='desktopFilter_job_type_filter']/div[1]/div[1]/fieldset[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='desktopFilter_normalized_country_code']/div[1]/div[1]/div[1]/div[2]/fieldset[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='desktopFilter_normalized_city_name']/div[1]/div[1]/div[1]/div[2]/fieldset[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='desktopFilter_category_filter']/div[1]/div[1]/fieldset[1]/div[1]/button[2]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-results-box']/div[2]/div[1]/div[1]/div[2]/content[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/h3[1]").click()
        self.driver.find_element(By.ID, "apply-button").click()
    
    def test_hiringamazon_fe9f532e(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//img[@alt='Person working in a delivery station']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Delivery Station Jobs Near You')]").click()
        self.driver.find_element(By.ID, "zipcode-nav-search").clear()
        self.driver.find_element(By.ID, "zipcode-nav-search").send_keys("windsor")
        self.driver.find_element(By.ID, "0").click()
        self.driver.find_element(By.XPATH, "//div[@id='pageRouter']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pageRouter']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pageRouter']/div[1]/div[1]/div[1]/div[3]/button[2]").click()
    
    def test_hiringamazon_7980ddca(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/header[1]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply with an Amazon Delivery Service Partner')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Accept All')]").click()
        self.driver.find_element(By.ID, "state_code").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'CA')]").click()
        self.driver.find_element(By.ID, "distance").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'100mi')]").click()
        self.driver.find_element(By.ID, "minPayDropdown").click()
        self.driver.find_element(By.ID, "minPay").clear()
        self.driver.find_element(By.ID, "minPay").send_keys("22")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Update')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
    
    def test_hiringamazon_7b56daf2(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//div[@role='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply with an Amazon Delivery Service Partner')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Accept All')]").click()
        self.driver.find_element(By.ID, "address").clear()
        self.driver.find_element(By.ID, "address").send_keys("Grand Rapids")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Grand Rapids, MI')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        self.driver.find_element(By.ID, "application_form_first_name").clear()
        self.driver.find_element(By.ID, "application_form_first_name").send_keys("Nelson")
        self.driver.find_element(By.ID, "application_form_last_name").clear()
        self.driver.find_element(By.ID, "application_form_last_name").send_keys("Freeman")
        self.driver.find_element(By.ID, "application_form_email").clear()
        self.driver.find_element(By.ID, "application_form_email").send_keys("Nelsonfree@gmail.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/article[1]/div[1]/form[1]/div[1]/fieldset[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/article[1]/div[1]/form[1]/div[1]/fieldset[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/article[1]/div[1]/form[1]/div[1]/fieldset[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/article[1]/div[1]/form[1]/div[1]/fieldset[2]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "applicationFormSubmitButton").click()
    
    def test_hiringamazon_85ba991f(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs by Location')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Wisconsin')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Madison Jobs')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hvh-vanity-url']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pageRouter']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pageRouter']/div[1]/div[1]/div[1]/div[3]/button[2]").click()
    
    def test_hiringamazon_8b2b5af2(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/header[1]/div[1]/div[1]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[5]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[1]/div[1]/div[1]/nav[1]/div[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='locations.index.continents.north_america']/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='822ab203-edb9-45da-8daa-96babc380756']/a[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='desktopFilter_job_type_filter']/div[1]/div[1]/fieldset[1]/div[1]/button[1]/div[1]").click()
    
    def test_hiringamazon_9570dbac(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//strong[contains(.,'Amazon Pharmacy')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/header[1]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[5]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='desktopFilter_job_type_filter']/div[1]/div[1]/fieldset[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-results-box']/div[2]/div[1]/div[1]/div[2]/content[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "recent").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-results-box']/div[2]/div[1]/div[1]/div[2]/content[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/h3[1]").click()
    
    def test_hiringamazon_a56cca7c(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//img[@title='']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Fulfillment Center Jobs Near You')]").click()
        self.driver.find_element(By.ID, "jobAlertSignupEmailInput").clear()
        self.driver.find_element(By.ID, "jobAlertSignupEmailInput").send_keys("abc@abc.com")
        self.driver.find_element(By.XPATH, "//button[@id='jobAlertSignupButton']/div[1]").click()
    
    def test_hiringamazon_e786f18b(self):
        # self.driver.get("https://hiring.amazon.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Military →')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn more ➜')]").click()
        self.driver.find_element(By.XPATH, "//strong[contains(.,'Learn how to get started')]").click()
    