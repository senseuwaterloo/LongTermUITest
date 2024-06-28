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
class TestMbta:
    
    def test_mbta_aecaba3f(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[2]/a[1]/span[2]").click()
        self.driver.find_element(By.ID, "from").clear()
        self.driver.find_element(By.ID, "from").send_keys("Boston Logan Airport")
        self.driver.find_element(By.XPATH, "//a[@id='hit-location-0']/span[2]").click()
        self.driver.find_element(By.ID, "to").clear()
        self.driver.find_element(By.ID, "to").send_keys("south station")
        self.driver.find_element(By.XPATH, "//div[@id='option-18404316']/a[1]").click()
        self.driver.find_element(By.ID, "trip-plan__submit").click()
        self.driver.find_element(By.XPATH, "//div[@id='accordion']/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trip-plan-options-section']/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trip-plan-options-section']/div[1]/div[1]/div[2]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trip-plan-options-section']/div[1]/div[1]/div[4]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_mbta_c094948f(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View MBTA job openings')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='action-filter']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-flyout-content']/div[2]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-flyout-content']/div[2]/div[1]/div[1]/ul[1]/li[27]/div[1]/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-flyout-content']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-flyout-content']/div[2]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[@id='category-100000-label']/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-flyout-content']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-flyout-content']/div[1]/button[3]").click()
        self.driver.find_element(By.XPATH, "//a[@id='action-sort-by']/span[1]").click()
        self.driver.find_element(By.XPATH, "//label[@id='posting-data-desc-label']/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Safety Lead Investigator - Heavy Rail')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='job-flyout-content']/div[1]/div[1]/div[2]/button[1]").click()
    
    def test_mbta_a5c7b71c(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Fares')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='fares']/div[1]/div[6]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedule an appointment')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='mainContainer']/div[1]/form[1]/div[5]/div[1]/ul[1]/li[4]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='mainContainer']/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@title='Selected date - Times available']").click()
        self.driver.find_element(By.XPATH, "//div[@id='mainContainer']/div[1]/form[1]/div[6]/div[2]/div[1]/div[1]/ul[1]/li[6]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Name *']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Name *']").send_keys("James Smith")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='email' and @placeholder='Email *']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='email' and @placeholder='Email *']").send_keys("james.smith@gmail.com")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_mbta_0f9382d3(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//div[@id='schedules-content']/div[2]/a[4]").click()
        self.driver.find_element(By.ID, "search-route--ferry__input").clear()
        self.driver.find_element(By.ID, "search-route--ferry__input").send_keys("East Boston Ferry")
        self.driver.find_element(By.XPATH, "//div[@id='option-52940476']/a[1]/span[3]/em[3]").click()
        self.driver.find_element(By.ID, "schedule-&-maps-tab").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-schedule-direction-root']/div[1]/form[1]/div[2]/label[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//aside[@id='modal-cover']/div[1]/div[1]/div[2]/div[1]").click()
    
    def test_mbta_e2adf8f1(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[2]/a[2]/div[1]/span[2]").click()
        self.driver.find_element(By.ID, "search-transit-near-me__input").clear()
        self.driver.find_element(By.ID, "search-transit-near-me__input").send_keys("South Station")
        self.driver.find_element(By.ID, "hit-location-0").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@role='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='route-pattern_7-1-0']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-schedule-direction-root']/div[4]/ol[1]/li[1]/section[1]/footer[1]/button[1]").click()
    
    def test_mbta_edbac1c3(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//div[@id='schedules-content']/div[1]/a[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/div[1]/span[2]").click()
        self.driver.find_element(By.ID, "alerts-tab").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Planned Service Alerts')]").click()
    
    def test_mbta_fa2828c5(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.ID, "search-header-desktop__input").clear()
        self.driver.find_element(By.ID, "search-header-desktop__input").send_keys("oak grove station")
        self.driver.find_element(By.XPATH, "//button[@id='search-header-desktop__input-go-btn']/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-results-container']/div[3]/div[2]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='route-card-list']/div[1]/div[2]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-schedule-direction-root']/div[3]/ol[1]/li[1]/section[1]/footer[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//aside[@id='modal-cover']/div[1]/div[1]/div[1]/form[1]/div[2]/label[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//aside[@id='modal-cover']/div[1]/div[1]/div[1]/form[1]/div[2]/label[1]/div[1]/select[1]").select("SOUTHBOUND Forest Hills")
        self.driver.find_element(By.XPATH, "//div[@role='button']").click()
    
    def test_mbta_fd0e4520(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[2]/a[1]/span[2]").click()
        self.driver.find_element(By.ID, "from").clear()
        self.driver.find_element(By.ID, "from").send_keys("brain")
        self.driver.find_element(By.XPATH, "//div[@id='option-83946893']/a[1]/span[3]/em[1]").click()
        self.driver.find_element(By.ID, "to").clear()
        self.driver.find_element(By.ID, "to").send_keys("boston")
        self.driver.find_element(By.XPATH, "//a[@id='hit-location-0']/span[2]").click()
        self.driver.find_element(By.ID, "trip-plan__submit").click()
        self.driver.find_element(By.XPATH, "//div[@id='accordion']/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//label[@id='plan-date-label']/div[1]").click()
        self.driver.find_element(By.ID, "cell14-plan-date-input").click()
        self.driver.find_element(By.ID, "plan_date_time_hour").clear()
        self.driver.find_element(By.ID, "plan_date_time_hour").send_keys("12")
        self.driver.find_element(By.ID, "plan_date_time_minute").clear()
        self.driver.find_element(By.ID, "plan_date_time_minute").send_keys("00")
        self.driver.find_element(By.ID, "plan_date_time_am_pm").clear()
        self.driver.find_element(By.ID, "plan_date_time_am_pm").select("PM")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.ID, "itinerary-1-fare-calculator-title").click()
    
    def test_mbta_059327ab(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//div[@id='schedules-content']/div[2]/a[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[1]/div[3]/a[3]/div[1]/span[2]").click()
        self.driver.find_element(By.ID, "schedules-&-maps-tab").click()
    
    def test_mbta_644b7bed(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Transit')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='transit']/div[1]/div[2]/a[4]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[1]/div[3]/a[3]/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "schedule-&-maps-tab").click()
        self.driver.find_element(By.XPATH, "//h3[@id='header-connections']/div[1]").click()
        self.driver.find_element(By.XPATH, "//h3[@id='header-fares']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel-pdfs']/a[1]").click()
    
    def test_mbta_8f41d9db(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sign up for job posting alerts')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='categories-cards-container']/div[2]/div[3]/div[6]/div[1]/label[1]/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "subscribe-cards").click()
        self.driver.find_element(By.ID, "first-name").clear()
        self.driver.find_element(By.ID, "first-name").send_keys("James")
        self.driver.find_element(By.ID, "last-name").clear()
        self.driver.find_element(By.ID, "last-name").send_keys("Smith")
        self.driver.find_element(By.ID, "email-address").clear()
        self.driver.find_element(By.ID, "email-address").send_keys("abc@abc.com")
        self.driver.find_element(By.XPATH, "//button[@id='submit']/span[1]/span[1]").click()
    
    def test_mbta_9223ed29(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Fares')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='fares']/div[1]/div[4]/a[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn more about reduced fares')]").click()
    
    def test_mbta_14be9a2b(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//div[@id='schedules-content']/div[1]/a[1]").click()
        self.driver.find_element(By.ID, "search-route--commuter_rail__input").clear()
        self.driver.find_element(By.ID, "search-route--commuter_rail__input").send_keys("Oyster Bay")
        self.driver.find_element(By.XPATH, "//a[@id='hit-location-0']/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]").click()
    
    def test_mbta_408cc1bd(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[2]/a[1]/span[2]").click()
        self.driver.find_element(By.ID, "from").clear()
        self.driver.find_element(By.ID, "from").send_keys("Boston Logan Airport")
        self.driver.find_element(By.ID, "hit-location-0").click()
        self.driver.find_element(By.ID, "to").clear()
        self.driver.find_element(By.ID, "to").send_keys("North Station")
        self.driver.find_element(By.XPATH, "//div[@id='option-73425136']/a[1]/span[3]/em[2]").click()
        self.driver.find_element(By.ID, "trip-plan__submit").click()
    
    def test_mbta_41ff100f(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Transit')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='transit']/div[1]/div[2]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/div[1]/span[2]").click()
    
    def test_mbta_4ff347e6(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[3]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='alerts-content']/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[9]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Current Alerts')]").click()
    
    def test_mbta_504c0c6b(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Transit')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='transit']/div[1]/div[4]/a[4]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Parking Lots')]").click()
        self.driver.find_element(By.ID, "cms-10661-title").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gloucester')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Plan a trip from this station')]").click()
        self.driver.find_element(By.ID, "to").clear()
        self.driver.find_element(By.ID, "to").send_keys("NORTH PLYMOUTH")
        self.driver.find_element(By.XPATH, "//a[@id='hit-location-0']/span[2]/em[2]").click()
        self.driver.find_element(By.ID, "trip-plan-departure-title").click()
        self.driver.find_element(By.XPATH, "//label[@id='plan-date-label']/div[1]").click()
        self.driver.find_element(By.ID, "cell28-plan-date-input").click()
        self.driver.find_element(By.ID, "plan_date_time_hour").clear()
        self.driver.find_element(By.ID, "plan_date_time_hour").send_keys("2")
        self.driver.find_element(By.ID, "plan_date_time_minute").clear()
        self.driver.find_element(By.ID, "plan_date_time_minute").send_keys("30")
        self.driver.find_element(By.ID, "plan_date_time_am_pm").clear()
        self.driver.find_element(By.ID, "plan_date_time_am_pm").select("PM")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.ID, "itinerary-1-title").click()
    
    def test_mbta_cc174cb2(self):
        # self.driver.get("https://mbta.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Fares')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='fares']/div[1]/div[2]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trip-plan__container--from']/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='trip-plan__container--from']/input[1]").send_keys("south station")
        self.driver.find_element(By.XPATH, "//div[@id='option-96136452']/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trip-plan__container--to']/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='trip-plan__container--to']/input[1]").send_keys("north station")
        self.driver.find_element(By.XPATH, "//div[@id='option-5870339']/a[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='planner-form']/div[3]/button[1]").click()
    