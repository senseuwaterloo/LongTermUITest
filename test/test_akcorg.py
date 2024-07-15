import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from browser_helper import switch_to_new_tab, calculate_dates_slash_format, scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestAkcOrg:
    
    # def test_akcorg_7933484c(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Breeds A-Z')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View All Breeds')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[2]/div[1]/h3[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[2]/div[2]/div[3]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[3]/div[1]/h3[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[3]/div[2]/div[3]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[5]/div[1]/h3[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='breed-filter']/div[5]/div[2]/div[9]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Submit')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='breed-type-card-']/a[1]/h3[1]").click()
    #
    # def test_akcorg_5e73dffe(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Products & Services')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Dog Groomer')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/svg[1]/use[1]").click()
    #     self.driver.find_element(By.ID, "react-select-2-option-4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]").send_keys("10005")
    #     self.driver.find_element(By.ID, "react-select-3-option-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/svg[1]/use[1]").click()
    #     self.driver.find_element(By.ID, "react-select-4-option-3").click()
    #     self.driver.find_element(By.XPATH, "//button[@name='' and @type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/a[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//button[@name='' and @type='button']").click()
    #
    # def test_akcorg_607dfa0d(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Boxer')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Breeds')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Bulldog')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Breeds')]").click()
    #
    # def test_akcorg_36d7dc8f(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Agility')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Events')]").click()
    #
    # def test_akcorg_5b1732fb(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[1]/div[1]/nav[1]/a[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "react-select-2-option-69").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "react-select-3-option-1").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]").send_keys("ALABAMA")
    #     self.driver.find_element(By.ID, "react-select-4-option-0").click()
    #     self.driver.find_element(By.XPATH, "//button[@name='' and @type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[2]/div[1]/form[1]/div[2]/p[1]/span[2]/svg[1]/use[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[5]/div[2]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[3]/div[3]/div[1]/div[1]/div[3]/div[1]/a[3]/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@name='' and @type='button']").click()
    #
    # def test_akcorg_dd3b12e6(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.ID, "homepage-hero-breed-search-selectized").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Golden Retriever')]").click()
    #
    # def test_akcorg_697f9915(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Obedience')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Events')]").click()
    #     self.driver.find_element(By.XPATH, "//strong[contains(.,'Search Events Calendar')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View Events')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='input--event-type']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='control-box--event-type']/div[2]/div[2]/div[2]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='control-box--event-type']/div[2]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='input--location']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='control-box--location']/div[2]/div[2]/div[3]/label[7]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='control-box--location']/div[2]/div[1]/button[3]").click()
    #     self.driver.find_element(By.ID, "default_widget").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='monthpicker_043290360658912985']/table[1]/tbody[1]/tr[2]/td[2]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='inputform']/div[3]/div[3]/button[1]").click()
    #
    # def test_akcorg_6b5cc19d(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Breeds A-Z')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dog-breeds']/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Afghan Hound')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Akita')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[3]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Azawakh')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Breeds')]").click()
    #
    # def test_akcorg_79450983(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Cardigan Welsh Corgi')]").click()
    #     self.driver.find_element(By.ID, "tab__breed-page__traits__social").click()
    #     self.driver.find_element(By.ID, "accordion-10").click()
    #
    # def test_akcorg_7b39d904(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See Upcoming Events')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Events Near You')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='input--event-type']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='event_type' and @value='HT' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='control-box--event-type']/div[2]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='input--location']/span[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='input--location']/span[1]").send_keys("TEXAS")
    #     self.driver.find_element(By.XPATH, "//div[@id='control-box--location']/div[2]/div[2]/div[4]/label[5]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='control-box--location']/div[2]/div[1]/button[3]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='inputform']/div[3]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='divCalendar']/table[1]/tbody[1]/tr[4]/td[6]/div[1]/a[1]").click()
    #     self.driver.find_element(By.ID, "addeventatc1").click()
    #     self.driver.find_element(By.ID, "addeventatc1-google").click()
    #
    # def test_akcorg_807a79ec(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Expert Advice')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='expert-advice']/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='dnt-landing']/div[1]/label[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cute')]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='dnt-landing']/div[2]/div[20]/label[1]").click()
    
    def test_akcorg_9d42f53a(self):
        # self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Event Search')]").click()
        switch_to_new_tab(self.driver)
        # there are two exactly the same element so has to find the desktop body
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//span[contains(text(),'Search near City')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//form[@id='locationName']/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//form[@id='locationName']/input[1]").send_keys("brighton")
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//button[@class='dropdown-item']//span[strong[text()='Brighton'] and contains(text(), 'AL')]").click()
        dropdown_element = self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//select[@name='radius']")
        select = Select(dropdown_element)
        select.select_by_value('100')
        start_date_str, end_date_str = calculate_dates_slash_format(14, 379)

        calendar_element = self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateStart' and @placeholder='MM/DD/YYYY']")
        scroll_to_element(self.driver, calendar_element)
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateStart' and @placeholder='MM/DD/YYYY']").click()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateStart' and @placeholder='MM/DD/YYYY']").clear()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateStart' and @placeholder='MM/DD/YYYY']").send_keys(start_date_str)
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateEnd' and @placeholder='MM/DD/YYYY']").click()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateEnd' and @placeholder='MM/DD/YYYY']").clear()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateEnd' and @placeholder='MM/DD/YYYY']").send_keys(end_date_str)

        # self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//label[@name='eventSetting' and .//p[normalize-space(text()[1])='Event' and normalize-space(text()[2])='Date']]").click()
        # need to scroll to a higher place since scroll to all us dog still can't show the element
        breed_element = self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//span[contains(text(),'Any AKC Recognized or FSS Breed')]")
        scroll_to_element(self.driver, breed_element)
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//span[contains(text(),'All-American Dogs')]").click()

        # need to scroll to a higher place since scroll to all us dog still can't show the Companion Events element
        conformation_events_element = self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//div[contains(text(),'Conformation Events')]")
        scroll_to_element(self.driver, conformation_events_element)
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//div[contains(text(),'Companion Events')]").click()

        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//span[contains(text(),'Agility (AG)')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//span[contains(text(),'Obedience (O/SO/PO/LO)')]").click()

        submit_button = self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[@value='RETRIEVE EVENTS' and @type='button']")
        scroll_to_element(self.driver, submit_button)
        submit_button.click()
    
    # def test_akcorg_ba537ab6(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Expert Advice')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Nutrition')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vitamins & Supplements')]").click()
    #
    # def test_akcorg_c7b0b259(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[1]/div[1]/nav[1]/a[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "react-select-2-option-5").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "react-select-3-option-1").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[4]/section[1]/div[2]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]").send_keys("Chicago")
    #     self.driver.find_element(By.ID, "react-select-4-option-0").click()
    #     self.driver.find_element(By.XPATH, "//button[@name='' and @type='button']").click()
    #
    # def test_akcorg_ce886520(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Judges Directory')]").click()
    #     self.driver.find_element(By.ID, "lastName").clear()
    #     self.driver.find_element(By.ID, "lastName").send_keys("Williams")
    #     self.driver.find_element(By.XPATH, "//option[@value='AK']").click()
    #     self.driver.find_element(By.ID, "submit_button").click()
    #
    # def test_akcorg_a02e8361(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Products & Services')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'AKC Veterinary Network')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for a Veterinarian')]").click()
    #     self.driver.find_element(By.ID, "zipCodeId").clear()
    #     self.driver.find_element(By.ID, "zipCodeId").send_keys("75228")
    #     self.driver.find_element(By.XPATH, "//lib-searchable-dropdown[@id='radiusSelect']/div[1]/angular2-multiselect[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//lib-searchable-dropdown[@id='radiusSelect']/div[1]/angular2-multiselect[1]/div[1]/div[2]/div[3]/div[3]/ul[1]/li[2]/label[1]").click()
    #     self.driver.find_element(By.ID, "agreeCheckId").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//td[@role='cell']").click()
    #
    # def test_akcorg_a138caa3(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[1]/div[1]/nav[1]/a[3]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Start Dog Registration Process')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[4]/div[1]/main[1]/form[1]/div[1]/div[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[4]/div[1]/main[1]/form[1]/div[1]/div[2]/div[2]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue To Registration')]").click()
    #
    # def test_akcorg_b5d06b36(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Breeds A-Z')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dog-breeds']/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Affenpinscher')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/div[2]/main[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Afghan Hound')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Breeds')]").click()
    #
    # def test_akcorg_ff1fb71d(self):
    #     # self.driver.get("https://www.akc.org/")
    #     self.driver.find_element(By.ID, "homepage-hero-breed-search-selectized").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Beagle')]").click()
    #     self.driver.find_element(By.ID, "tab__breed-page__traits__physical").click()
    #     self.driver.find_element(By.ID, "accordion-7").click()
    