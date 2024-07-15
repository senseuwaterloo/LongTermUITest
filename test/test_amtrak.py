import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element, switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestAmtrak:
    
    # def test_amtrak_8dcf6423(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Destinations')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='primary-nav']/nav[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/a[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View Details')]").click()
    #
    # def test_amtrak_845fbfa9(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Experience')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='primary-nav']/nav[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/a[4]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Onboard Dining')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Café')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[1]/div[3]/article[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/span[1]").click()
    #
    # def test_amtrak_b60cf528(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Auto Train')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/station-search[1]/button[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='option']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/station-search[1]/button[1]/div[1]/div[2]/div[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "mat-input-1").clear()
    #     self.driver.find_element(By.ID, "mat-input-1").send_keys("Chicago")
    #     self.driver.find_element(By.XPATH, "//div[@role='option']").click()
    #     self.driver.find_element(By.ID, "mat-input-2").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[2]/div[1]/ngb-datepicker-month[1]/div[5]/div[7]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[3]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[2]/div[1]/ngb-datepicker-month[1]/div[6]/div[7]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[3]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[3]/div[1]/div[1]/app-traveler[1]/am-dropdown[1]/div[1]/div[1]/button[1]/img[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[3]/div[1]/div[1]/app-traveler[1]/am-dropdown[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/am-counter[1]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[3]/button[1]").click()
    #
    # def test_amtrak_4ff37796(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='primary-nav']/nav[1]/ul[1]/li[4]/btn-train-schedule[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='top_nav_wrapper']/train-schedule[1]/div[1]/div[1]/train-schedule-form[1]/div[1]/form[1]/div[1]/span[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='am-simple-dropdown__0']/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='am-dropdown__options--instance-0']/div[7]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='top_nav_wrapper']/train-schedule[1]/div[1]/div[1]/train-schedule-form[1]/div[1]/form[1]/div[3]/button[2]").click()
    #     self.driver.find_element(By.ID, "mat-select-value-1").click()
    #     self.driver.find_element(By.XPATH, "//mat-option[@id='mat-option-3']/span[1]").click()
    #
    # def test_amtrak_e6789e88(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Auto Train')]").click()
    #     self.driver.find_element(By.ID, "mat-input-2").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Next month']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[1]/ngb-datepicker-navigation[1]/div[6]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[2]/div[2]/ngb-datepicker-month[1]/div[3]/div[7]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[3]/button[2]").click()
    #     self.driver.find_element(By.ID, "am-check-0").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[4]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[3]/button[1]").click()
    #     self.driver.find_element(By.ID, "firstName").clear()
    #     self.driver.find_element(By.ID, "firstName").send_keys("Mayank")
    #     self.driver.find_element(By.ID, "lastName").clear()
    #     self.driver.find_element(By.ID, "lastName").send_keys("Raheja")
    #     self.driver.find_element(By.ID, "am-check-1").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/modal-container[1]/div[2]/div[1]/app-pwd-questionnaire[1]/div[2]/div[2]/div[1]/pwd-basic-info[1]/div[1]/section[1]/div[2]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//card-radio-button[@id='am-radio-directive-0']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//card-radio-button[@id='am-radio-directive-3']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'SAVE')]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'SAVE AND CONTINUE')]").click()
    #     self.driver.find_element(By.XPATH, "//mat-checkbox[@id='mat-checkbox-2']/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'SAVE AND CONTINUE')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/div[6]/search-results[1]/div[1]/div[1]/div[2]/div[1]/app-search-results-journey-leg[1]/div[1]/div[1]/div[2]/div[1]/div[1]/search-results-leg[1]/div[1]/div[2]/div[1]/button[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='collapseManual']/div[1]/div[1]/div[1]/div[1]/fare-family-container[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/accomodation-pill[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.ID, "add-to-cart-btn").click()
    #
    # def test_amtrak_9b125b87(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Experience')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='primary-nav']/nav[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/a[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Passenger ID, Safety & Security')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn more')]").click()
    #
    # def test_amtrak_66a5b212(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Destinations')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='primary-nav']/nav[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/a[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Amtrak National Route Map (PDF, 3MB)')]").click()
    #
    # def test_amtrak_8cb94647(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.ID, "mat-input-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='option']").click()
    #     self.driver.find_element(By.ID, "mat-input-1").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='option']").click()
    #     self.driver.find_element(By.ID, "mat-input-2").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[2]/div[1]/ngb-datepicker-month[1]/div[5]/div[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[3]/div[1]/div[1]/app-traveler[1]/am-dropdown[1]/div[1]/div[1]/button[1]/img[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[3]/div[1]/div[1]/app-traveler[1]/am-dropdown[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/am-counter[1]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[3]/div[1]/div[1]/app-traveler[1]/am-dropdown[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[10]/div[3]/button[1]").click()
    #     self.driver.find_element(By.ID, "am-check-0").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[3]/button[1]").click()
    #
    # def test_amtrak_f0f8088f(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[@id='ff_tabbar_mytrip']/span[2]").click()
    #     self.driver.find_element(By.ID, "res-number").clear()
    #     self.driver.find_element(By.ID, "res-number").send_keys("123456")
    #     self.driver.find_element(By.XPATH, "//div[@id='am-simple-dropdown__0']/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='am-dropdown__options--instance-0']/div[3]").click()
    #     self.driver.find_element(By.ID, "mat-input-6").clear()
    #     self.driver.find_element(By.ID, "mat-input-6").send_keys("Smith")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Find Trip')]").click()
    #
    # def test_amtrak_f355cfcf(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'DEALS')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='primary-nav']/nav[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[1]/div[2]/div[1]/div[2]/article[1]/form[1]/div[2]/section[1]/article[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[1]/div[2]/div[1]/div[2]/article[1]/form[1]/div[2]/section[1]/article[1]/div[1]/ul[1]/li[3]/label[1]/span[1]").click()
    #
    # def test_amtrak_3cb44998(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.ID, "mat-input-0").clear()
    #     self.driver.find_element(By.ID, "mat-input-0").send_keys("New York")
    #     self.driver.find_element(By.XPATH, "//div[@id='autocomplete__0']/div[1]/div[1]/div[1]/div[3]").click()
    #     self.driver.find_element(By.ID, "mat-input-1").clear()
    #     self.driver.find_element(By.ID, "mat-input-1").send_keys("Washington")
    #     self.driver.find_element(By.XPATH, "//div[@role='option']").click()
    #     self.driver.find_element(By.ID, "mat-input-2").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[2]/div[1]/ngb-datepicker-month[1]/div[5]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/div[6]/search-results[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/am-dropdown[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//mat-radio-button[@id='mat-radio-3']/label[1]/span[2]").click()
    #
    # def test_amtrak_41cd71cb(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'DEALS')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='primary-nav']/nav[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/a[3]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[1]/div[2]/div[3]/div[1]/article[1]/div[1]/a[1]/picture[1]/div[1]/source[1]/source[1]/source[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(@href, 'link://#')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ylg-ms__listings-details']/div[1]/div[1]/div[4]/div[1]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ylg-ms__listings-details']/div[1]/div[1]/div[4]/div[1]/div[1]/button[3]").click()
    #
    # def test_amtrak_4498c83b(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.ID, "mat-input-0").clear()
    #     self.driver.find_element(By.ID, "mat-input-0").send_keys("new york")
    #     self.driver.find_element(By.XPATH, "//div[@id='autocomplete__0']/div[1]/div[1]/div[1]/div[3]").click()
    #     self.driver.find_element(By.ID, "mat-input-1").clear()
    #     self.driver.find_element(By.ID, "mat-input-1").send_keys("washington")
    #     self.driver.find_element(By.XPATH, "//div[@role='option']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[1]/ngb-datepicker-navigation[1]/div[6]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[2]/div[2]/ngb-datepicker-month[1]/div[2]/div[5]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[3]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/div[6]/search-results[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/am-dropdown[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "am-checkbox-directive-3").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='class-of-service-filters']/mat-selection-list[1]/li[3]/mat-list-option[1]/div[1]/mat-pseudo-checkbox[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/div[6]/search-results[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/am-dropdown[1]/div[1]/div[2]/div[1]/div[2]/app-search-sort-filter[1]/div[2]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/div[6]/search-results[1]/div[1]/div[1]/div[2]/div[1]/app-search-results-journey-leg[1]/div[1]/div[1]/div[2]/div[1]/div[1]/search-results-leg[1]/div[1]/div[2]/div[1]/button[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "add-to-cart-btn").click()
    #
    # def test_amtrak_2089ee5c(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'DEALS')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='primary-nav']/nav[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[1]/div[2]/div[1]/div[2]/article[1]/form[1]/div[2]/section[1]/article[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[1]/div[2]/div[1]/div[2]/article[1]/form[1]/div[2]/section[1]/article[1]/div[1]/ul[1]/li[3]/label[1]/span[1]").click()
    #
    # def test_amtrak_240952bd(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='primary-nav']/nav[1]/ul[1]/li[4]/btn-train-schedule[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "fromScheduleField").clear()
    #     self.driver.find_element(By.ID, "fromScheduleField").send_keys("chicago")
    #     self.driver.find_element(By.XPATH, "//div[@id='autocomplete__2']/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "mat-input-6").clear()
    #     self.driver.find_element(By.ID, "mat-input-6").send_keys("los angeles")
    #     self.driver.find_element(By.XPATH, "//div[@id='autocomplete__3']/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "mat-input-7").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='top_nav_wrapper']/train-schedule[1]/div[1]/div[1]/train-schedule-form[1]/div[1]/form[1]/div[3]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[2]/div[1]/ngb-datepicker-month[1]/div[5]/div[7]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='top_nav_wrapper']/train-schedule[1]/div[1]/div[1]/train-schedule-form[1]/div[1]/form[1]/div[4]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//img[@role='presentation']").click()
    #     self.driver.find_element(By.XPATH, "//mat-checkbox[@id='mat-checkbox-1']/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/div[3]/schedule-results[1]/div[1]/div[1]/div[1]/div[2]/am-dropdown[1]/div[1]/div[2]/div[1]/div[2]/app-schedule-sort-filter[1]/div[2]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/div[3]/schedule-results[1]/div[1]/div[2]/div[1]/div[1]/div[2]/app-schedule-print-pdf[1]/div[1]/trip-details[1]/div[1]/div[1]/am-dropdown[1]/div[1]/div[1]/button[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/div[3]/schedule-results[1]/div[1]/div[2]/div[1]/div[1]/div[2]/app-schedule-print-pdf[1]/div[1]/trip-details[1]/div[1]/div[1]/am-dropdown[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]").click()
    #
    # def test_amtrak_06ed65ba(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Destinations')]").click()
    #     self.driver.find_element(By.XPATH, "//g[@id='west']/polygon[1]").click()
    #     self.driver.find_element(By.XPATH, "//label[@id='progressBtn2']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'The Empire Builder')]").click()
    #     self.driver.find_element(By.XPATH, "//label[@id='progressBtn1']/span[1]").click()
    #
    # def test_amtrak_0b70e49b(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='q' and @type='text' and @placeholder='Search by Keyword']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='q' and @type='text' and @placeholder='Search by Keyword']").send_keys("Conductor")
    #     self.driver.find_element(By.XPATH, "//input[@name='locationsearch' and @type='text' and @placeholder='Search by Location']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='locationsearch' and @type='text' and @placeholder='Search by Location']").send_keys("New Yok")
    #     self.driver.find_element(By.XPATH, "//input[@value='Search Jobs' and @type='submit']").click()
    #     self.driver.find_element(By.ID, "searchfilter-submit").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'PASSENGER CONDUCTOR TRAINEE - 90344628 - New York, NY')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply now »')]").click()
    #
    # def test_amtrak_1d9c6a43(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.ID, "mat-input-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='option']").click()
    #     self.driver.find_element(By.ID, "mat-input-1").clear()
    #     self.driver.find_element(By.ID, "mat-input-1").send_keys("was")
    #     self.driver.find_element(By.XPATH, "//div[@role='option']").click()
    #     self.driver.find_element(By.ID, "mat-input-2").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[2]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[2]/div[2]/ngb-datepicker-month[1]/div[4]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[2]/div[3]/button[1]").click()
    
    def test_amtrak_b910229f(self):
        # self.driver.get("https://amtrak.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'DEALS') and @data-automation-id='sitePrimarySubnav']").click()
        self.driver.find_element(By.XPATH, "//a[@data-automation-id='VACATIONS & RAIL TOURS']").click()
        all_destinations_element = self.driver.find_element(By.XPATH, "//a[@data-automation-id='See all destinations']")
        scroll_to_element(self.driver, all_destinations_element)
        all_destinations_element.click()
        self.driver.find_element(By.XPATH, "//a[text()='AmtrakVacations.com']").click()
        switch_to_new_tab(self.driver, "https://amtrak.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Travel Styles')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Cross Country Journeys')]").click()

        second_trip_details = self.driver.find_element(By.XPATH, "//*[@id='ylg-ms__listings-search']/div/div/div[3]/div[1]/div/div/div/div[3]/a")
        scroll_to_element(self.driver, second_trip_details)
        second_trip_details.click()
        # //*[@id="ylg-ms__listings-search"]/div/div/div[3]/div[2]/div/div/div/div[3]/a

        instant_quote = self.driver.find_element(By.XPATH, "//*[@id='tour-details-container__actions']/div[2]/button[1]")
        scroll_to_element(self.driver, instant_quote)
        instant_quote.click()
        # always select the first day of next month
        self.driver.find_element(By.XPATH, "//*[@id='ylg-ms__listings-details']/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[4]/div/img").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='days-cell']//span[text()='1']").click()

        self.driver.find_element(By.XPATH, "//*[@id='ylg-ms__listings-details']/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div/button").click()
        leaving_from = self.driver.find_element(By.ID, "edit-add-additional-departure-city")
        scroll_to_element(self.driver, leaving_from)
        leaving_from.send_keys("Chicago")

        pre_post_rail = self.driver.find_element(By.XPATH, "//*[@id='edit-need-pre-post-rail']/div[2]/label")
        scroll_to_element(self.driver, pre_post_rail)
        pre_post_rail.click()

        deluxe_bedroom = self.driver.find_element(By.ID, "edit-private-bedroom")
        scroll_to_element(self.driver, deluxe_bedroom)
        deluxe_bedroom.click()

        adult_num = self.driver.find_element(By.ID, "edit-adults-num")
        scroll_to_element(self.driver, adult_num)
        adult_num.clear()
        adult_num.send_keys("2")

        about_trip = self.driver.find_element(By.XPATH, "//textarea[@data-drupal-selector='edit-about-your-trip']")
        scroll_to_element(self.driver, about_trip)
        about_trip.clear()
        about_trip.send_keys("Wedding Anniversary")

        next_step = self.driver.find_element(By.ID, "edit-actions-wizard-next")
        scroll_to_element(self.driver, next_step)
        next_step.click()
        # new form will scroll up so need to wait for a few seconds to avoid selenium.common.exceptions.ElementClickInterceptedException:
        # Message: element click intercepted: Element is not clickable at point
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-first-name']").click()
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-first-name']").send_keys("John")
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-last-name']").click()
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-last-name']").send_keys("Mark")
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-email-address']").click()
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-email-address']").send_keys("Johnmark@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-phone-number']").click()
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-phone-number']").send_keys("234567890")
        self.driver.find_element(By.XPATH, "//div[@data-drupal-selector='edit-travel-advisor-select']/div[1]/div[1]/label").click()

        submit_button = self.driver.find_element(By.XPATH, "//div[@data-drupal-selector='edit-actions']/div[2]/input")
        scroll_to_element(self.driver, submit_button)
        submit_button.click()
    
    # def test_amtrak_8df744ef(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='purchaseTicket']/div[1]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'EXPLORE MULTI-RIDE PASSES')]").click()
    #     self.driver.find_element(By.ID, "mat-input-0").clear()
    #     self.driver.find_element(By.ID, "mat-input-0").send_keys("WASHINGTON")
    #     self.driver.find_element(By.XPATH, "//div[@role='option']").click()
    #     self.driver.find_element(By.ID, "mat-input-1").clear()
    #     self.driver.find_element(By.ID, "mat-input-1").send_keys("NEW YORK")
    #     self.driver.find_element(By.XPATH, "//div[@id='autocomplete__1']/div[1]/div[1]/div[1]/div[3]").click()
    #     self.driver.find_element(By.ID, "mat-input-2").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[1]/div[3]/div[2]/am-farefinder-dates[1]/div[2]/div[2]/am-datepicker-standalone[1]/div[1]/ngb-datepicker[1]/div[2]/div[2]/ngb-datepicker-month[1]/div[3]/div[4]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[1]/div[3]/div[2]/am-farefinder-dates[1]/div[2]/div[3]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[2]/div[1]/div[1]/div[1]/amt-md-farefinder[1]/div[2]/div[1]/div[1]/div[4]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/div[5]/mr-search-results[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]/div[1]/span[1]").click()
    #
    # def test_amtrak_2b562465(self):
    #     # self.driver.get("https://amtrak.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'DEALS')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='primary-nav']/nav[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/a[4]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[9]/div[1]/picture[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'EXPLORE MULTI-RIDE PASSES')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='page-content']/section[2]/div[5]/div[2]/div[3]/article[1]/article[1]/label[1]").click()
    