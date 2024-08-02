import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_down


@pytest.mark.usefixtures("setup_class")
class TestKbb:
    
    # def test_kbb_5535f398(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/a[1]/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='second-years']/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='second-years']/select[1]").select("2015")
    #     self.driver.find_element(By.XPATH, "//div[@id='intent-content']/div[1]/div[1]/label[2]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Sort By']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Sort By']").select("Price  Low to High")
    #
    # def test_kbb_68c320f1(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='superheroSection']/div[1]/div[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[41]/a[1]/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='']").select("2004")
    #     self.driver.find_element(By.XPATH, "//div[@id='second-years']/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='second-years']/select[1]").select("2012")
    #     self.driver.find_element(By.XPATH, "//div[@id='intent-content']/div[1]/div[1]/label[2]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='intent-content']/div[1]/div[1]/label[1]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Sort By']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Sort By']").select("Price  High to Low")
    #
    # def test_kbb_6b215dbb(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cars for Sale')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mountNode']/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/span[1]/span[2]").click()
    #     self.driver.find_element(By.NAME, "zip").clear()
    #     self.driver.find_element(By.NAME, "zip").send_keys("42701")
    #     self.driver.find_element(By.NAME, "searchRadius").clear()
    #     self.driver.find_element(By.NAME, "searchRadius").select("10 Miles")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Submit')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/label[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='ae-accordion-filter-desc-2']/h4[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[2]/div[1]/div[1]/div[1]/label[4]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[17]/div[2]/div[1]/div[1]/div[1]/label[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='675324097']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mountNode']/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[3]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "date2066937087").click()
    #     self.driver.find_element(By.XPATH, "//button[@value='17']").click()
    #     self.driver.find_element(By.ID, "time1755361").clear()
    #     self.driver.find_element(By.ID, "time1755361").select("9 00am")
    #     self.driver.find_element(By.ID, "firstName1246366233").click()
    #     self.driver.find_element(By.ID, "firstName1246366233").clear()
    #     self.driver.find_element(By.ID, "firstName1246366233").send_keys("James")
    #     self.driver.find_element(By.ID, "lastName").clear()
    #     self.driver.find_element(By.ID, "lastName").send_keys("Smith")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    # def test_kbb_3d77584f(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//button[@id='homepage-bycity-links-button-3']/div[1]/div[1]/svg[1]/g[2]/polyline[1]").click()
    #     self.driver.find_element(By.ID, "seo-link-cars-for-sale-near-tampa-fl-4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/label[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='ae-accordion-filter-desc-1']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/label[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='ae-accordion-filter-desc-4']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[11]/div[2]/div[1]/div[1]/div[1]/label[8]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[14]/div[2]/div[1]/div[1]/div[1]/label[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='ae-accordion-filter-desc-6']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[13]/div[2]/div[1]/div[1]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "149138475").clear()
    #     self.driver.find_element(By.ID, "149138475").select("Price - Lowest")
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "firstName1246366233").clear()
    #     self.driver.find_element(By.ID, "firstName1246366233").send_keys("James")
    #     self.driver.find_element(By.ID, "lastName").clear()
    #     self.driver.find_element(By.ID, "lastName").send_keys("Smith")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Send Email')]").click()
    #
    # def test_kbb_a67318a4(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[3]/a[1]/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='intent-content']/div[1]/div[1]/label[2]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='']").select("2010")
    #     self.driver.find_element(By.XPATH, "//button[@id='fsrFocusFirst']/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='second-years']/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='second-years']/select[1]").select("2010")
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Sort By']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Sort By']").select("Price  Low to High")
    #     self.driver.find_element(By.XPATH, "//div[@id='vehicle_card_2']/div[1]/div[2]/label[1]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='vehicle_card_3']/div[1]/div[2]/label[1]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='vehicle_card_0']/div[1]/div[2]/label[1]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='vehicle_card_1']/div[1]/div[2]/label[1]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='compare_sticky_btn']/span[1]").click()
    #
    # def test_kbb_ca049641(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cars for Sale')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cars for Sale')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='ae-accordion-filter-desc-3']/h4[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/label[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='ae-accordion-filter-desc-4']/h4[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[10]/div[2]/div[1]/div[1]/div[1]/label[4]/div[1]").click()
    #     self.driver.find_element(By.ID, "149138475").clear()
    #     self.driver.find_element(By.ID, "149138475").select("Price - Lowest")
    #     self.driver.find_element(By.XPATH, "//div[@id='677043562']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]").click()
    
    def test_kbb_d3a4e6c3(self):
        # self.driver.get("https://kbb.com")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Car Values')]").click()
        self.driver.find_element(By.XPATH, "//div/a[contains(text(),'Car Values')]").click()

        # add extra step to handle popup
        time.sleep(3)
        if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']"):
            self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        scroll_down(self.driver, 500)

        # self.driver.find_element(By.XPATH, "//a[contains(text(),\"My Car's Value\")]").click()
        self.driver.find_element(By.XPATH, "//div[text()=\"My Car's Value\"]").click()

        # the following step is redundant
        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[2]/div[1]/div[1]/div[1]").click()

        # self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").clear()
        # self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").select("2016")
        # self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").clear()
        # self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").select("Toyota")
        # self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").clear()
        # self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").select("Camry")
        # self.driver.find_element(By.XPATH, "//input[@value='' and @type='tel' and @placeholder=' ']").clear()
        # self.driver.find_element(By.XPATH, "//input[@value='' and @type='tel' and @placeholder=' ']").send_keys("40000")
        year_dropdown = self.driver.find_element(By.XPATH, "//select[@aria-label='Year' and @placeholder='Year' and not(.//option[@value='2027'])]")
        year_select = Select(year_dropdown)
        year_select.select_by_visible_text('2016')
        make_dropdown = self.driver.find_element(By.XPATH, "//select[@aria-label='Make' and @placeholder='Make' and .//option[@value='Acura']]")
        make_select = Select(make_dropdown)
        make_select.select_by_value('Toyota')
        model_dropdown = self.driver.find_element(By.XPATH, "//select[@aria-label='Model' and @placeholder='Model' and .//option[@value='Camry']]")
        model_select = Select(model_dropdown)
        model_select.select_by_value('Camry')
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'mileage') and @type='tel']").clear()
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'mileage') and @type='tel']").send_keys("40000")

        # extra steps to input postal code
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'zipcode') and @type='tel' and ./ancestor::label[1]/preceding-sibling::label]").clear()
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'zipcode') and @type='tel' and ./ancestor::label[1]/preceding-sibling::label]").send_keys("07055")

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='vehicle_picker_submit_button' and not(@disabled)]").click()

        # add extra step to handle popup
        time.sleep(3)
        if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']"):
            self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        scroll_down(self.driver, 500)

        self.driver.find_element(By.XPATH, "//div[@id='box-style']/div[4]/label[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()

        # add extra step to handle popup
        # time.sleep(3)
        # if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']"):
        #     self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        scroll_down(self.driver, 500)

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Select Your Options']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/div[1]").click()
        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//img[@alt='Black image']").click()

        # add extra step
        self.driver.find_element(By.XPATH, "//div[text()='Selling my car']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//button[@data-lean-auto='optionsNextButton']").click()

        # add extra step to handle popup
        # time.sleep(3)
        # if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']"):
        #     self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        # scroll_down(self.driver, 500)

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/label[2]/span[3]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-lean-auto='next-btn']").click()

        # add extra step to handle popup
        # time.sleep(3)
        # if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']"):
        #     self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        scroll_down(self.driver, 500)

        # self.driver.find_element(By.XPATH, "//div[@id='BodyDivFlex']/div[2]/div[1]/ol[1]/li[1]/div[1]").click()
        # self.driver.find_element(By.ID, "license-plate-entry").clear()
        # self.driver.find_element(By.ID, "license-plate-entry").send_keys("AZXA46")
        # self.driver.find_element(By.ID, "state-entry").clear()
        # self.driver.find_element(By.ID, "state-entry").select("AZ")
        # self.driver.find_element(By.XPATH, "//div[@id='BodyDivFlex']/div[2]/div[1]/div[3]/div[3]/button[1]").click()
        # page logic changed
        self.driver.find_element(By.XPATH, "//div[text()='Has repairable cosmetic defects and mechanical problems']").click()
        self.driver.find_element(By.XPATH, "//button[@data-lean-auto='conditionNextButton']").click()
    
    # def test_kbb_e2f8b054(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cars for Sale')]").click()
    #     self.driver.find_element(By.ID, "2225141853").clear()
    #     self.driver.find_element(By.ID, "2225141853").send_keys("07055")
    #     self.driver.find_element(By.ID, "2281868035").clear()
    #     self.driver.find_element(By.ID, "2281868035").select("100 Miles")
    #     self.driver.find_element(By.ID, "614960940").clear()
    #     self.driver.find_element(By.ID, "614960940").select("2018")
    #     self.driver.find_element(By.ID, "2152820002").clear()
    #     self.driver.find_element(By.ID, "2152820002").select("2018")
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[17]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[17]/div[2]/div[1]/div[1]/div[1]/label[5]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[18]/div[2]/div[1]/div[1]/div[1]/label[2]/div[1]").click()
    #     self.driver.find_element(By.ID, "149138475").clear()
    #     self.driver.find_element(By.ID, "149138475").select("Price - Lowest")
    #
    # def test_kbb_56cac423(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='superHeroBannerContainer']/div[2]/div[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").select("2005")
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").select("Toyota")
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").select("Corolla")
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/form[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='fsrFocusFirst']/svg[1]").click()
    #
    # def test_kbb_4af615be(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='superheroSection']/div[1]/div[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").select("2006")
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").select("Honda")
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").select("Civic")
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/form[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overview']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/a[1]/span[1]").click()
    #
    # def test_kbb_93d0190f(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='superHeroBannerContainer']/div[2]/div[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").select("2012")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[6]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//img[@alt='Close']").click()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").select("Honda")
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").select("Civic")
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/form[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='subnav5']/div[1]/div[1]").click()
    #
    # def test_kbb_988ff1b8(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cars for Sale')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cars for Sale')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mountNode']/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/span[1]/span[1]/span[2]").click()
    #     self.driver.find_element(By.ID, "564749857").clear()
    #     self.driver.find_element(By.ID, "564749857").send_keys("50000")
    #
    # def test_kbb_9dfba9af(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cars for Sale')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Free Dealer Price Quote')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").select("Kia")
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").select("Carnival")
    #     self.driver.find_element(By.ID, "zipInput").clear()
    #     self.driver.find_element(By.ID, "zipInput").send_keys("11101")
    #     self.driver.find_element(By.XPATH, "//button[@id='Step1Button']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='Step2Button']/span[1]").click()
    #
    # def test_kbb_efa705c1(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Car Repair')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Auto Repair Prices')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").select("2022")
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").select("Toyota")
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").select("Corolla")
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Style']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@placeholder='Style']").select("L Sedan 4D")
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@title='No thanks']").click()
    #     self.driver.find_element(By.ID, "serviceSelectorSearchFilterBar").clear()
    #     self.driver.find_element(By.ID, "serviceSelectorSearchFilterBar").send_keys("ac recharge")
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "name").clear()
    #     self.driver.find_element(By.ID, "name").send_keys("James Smith")
    #     self.driver.find_element(By.ID, "email").clear()
    #     self.driver.find_element(By.ID, "email").send_keys("buckeye.foobar@gmail.com")
    #     self.driver.find_element(By.ID, "phone").clear()
    #     self.driver.find_element(By.ID, "phone").send_keys("6157075521")
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
    #
    # def test_kbb_f1db33c6(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Car Reviews')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Best Cars')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='slp-category-module']/div[3]/div[1]/label[1]/a[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='otherBestCategories']/div[4]/div[2]/div[3]/div[3]/a[1]/span[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='vehicle_card_1']/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='consumerreview']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ymmCrList']/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #
    # def test_kbb_fb9c0e7f(self):
    #     # self.driver.get("https://kbb.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cars for Sale')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cars for Sale')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search by Make, Model, Body Style or Keyword']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search by Make, Model, Body Style or Keyword']").send_keys("Mustang")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-1-item-0']/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "149138475").clear()
    #     self.driver.find_element(By.ID, "149138475").select("Price - Lowest")
    #     self.driver.find_element(By.XPATH, "//div[@id='592587506']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mountNode']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Save')]").click()
    