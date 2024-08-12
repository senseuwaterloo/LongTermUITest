import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import switch_to_new_tab, calculate_dates


@pytest.mark.usefixtures("setup_class")
class TestQatarairways:
    
    # def test_qatarairways_c13d245a(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Book')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Travel requirements')]").click()
    #     self.driver.find_element(By.ID, "travelFrom").clear()
    #     self.driver.find_element(By.ID, "travelFrom").send_keys("Tokyo")
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "travelTo").clear()
    #     self.driver.find_element(By.ID, "travelTo").send_keys("Guangzhou")
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/span[1]/div[1]/div[1]/div[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "travelReqBtn").click()
    #
    # def test_qatarairways_0de53aa5(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//input[@value='Doha DOH' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='Doha DOH' and @type='text']").send_keys("Mumbai")
    #     self.driver.find_element(By.XPATH, "//div[@role='menuitem']").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='Washington D.C. IAD' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='Washington D.C. IAD' and @type='text']").send_keys("Stockholm")
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[2]/div[2]/span[1]/div[1]/div[2]/div[3]/div[1]").click()
    #     self.driver.find_element(By.ID, "onewayTrip").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[4]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[5]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[4]/div[4]/div[1]/div[2]/div[3]/div[2]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[11]/div[4]/button[1]").click()
    #
    # def test_qatarairways_7216606d(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Book')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Travel requirements')]").click()
    #     self.driver.find_element(By.ID, "travelFrom").clear()
    #     self.driver.find_element(By.ID, "travelFrom").send_keys("Amsterdam")
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "travelTo").clear()
    #     self.driver.find_element(By.ID, "travelTo").send_keys("Cairo")
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/span[1]/div[1]/div[1]/div[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "travelReqBtn").click()
    #
    # def test_qatarairways_82094208(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Experience')]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='planyourtrip']/li[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='j-poi-tabs']/li[1]/a[1]/span[1]").click()
    #
    # def test_qatarairways_b7cee0c0(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.ID, "managebooking-tab").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[1]/input[1]").send_keys("123456")
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[2]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[2]/input[1]").send_keys("Smith")
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[3]/div[1]/button[1]").click()
    #
    # def test_qatarairways_b28e6a37(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore')]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='ourdestinations']/li[3]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ajax-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Discover')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='New York JFK' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='New York JFK' and @type='text']").send_keys("doha")
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[1]/div[2]/span[1]/div[1]/div[2]/div[3]/div[1]/strong[1]/strong[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='28 May 23' and @type='text']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[4]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[7]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[4]/div[4]/div[1]/div[2]/div[3]/div[2]/button[2]").click()
    #     self.driver.find_element(By.ID, "passenger-field").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='bw-passenger-picker']/div[2]/div[1]/div[6]/div[2]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='bw-passenger-picker']/div[2]/div[1]/div[9]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[11]/div[4]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//booking-flight-result-card[@id='at-flight-search-result-1']/div[1]/div[1]/div[3]/div[1]/div[1]/a[1]/h3[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='fare-details-swiper-0001']/div[1]/booking-fare-card[3]/div[1]/div[2]/button[1]").click()
    #
    # def test_qatarairways_f385156c(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.ID, "Rectangle_2").click()
    #     self.driver.find_element(By.ID, "search-input-text").clear()
    #     self.driver.find_element(By.ID, "search-input-text").send_keys("Membership tier")
    #     self.driver.find_element(By.XPATH, "//div[@id='navbarSupportedContent']/ul[2]/li[3]/div[1]/ul[1]/li[2]/div[1]/form[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Privilege Club Membership Tiers')]").click()
    #
    # def test_qatarairways_31df4f0d(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.ID, "managebooking-tab").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[1]/input[1]").send_keys("1234567890")
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[2]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[2]/input[1]").send_keys("Smith")
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[3]/div[1]/button[1]").click()
    #
    # def test_qatarairways_446e3135(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[1]/div[2]/span[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[1]/div[2]/span[1]/input[1]").send_keys("colombo")
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[1]/div[2]/span[1]/div[1]/div[2]/div[3]/div[1]/strong[1]/strong[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[2]/div[2]/span[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[2]/div[2]/span[1]/input[1]").send_keys("new york")
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[2]/div[2]/span[1]/div[1]/div[2]/div[3]/div[1]/strong[1]/strong[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='28 May 23' and @type='text']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[4]/div[4]/div[1]/div[2]/div[2]/div[2]/table[1]/tbody[1]/tr[4]/td[6]").click()
    #     self.driver.find_element(By.ID, "passenger-field").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='bw-passenger-picker']/div[2]/div[1]/div[6]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='bw-passenger-picker']/div[2]/div[1]/div[5]/div[2]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='bw-passenger-picker']/div[2]/div[1]/div[7]/div[1]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='bw-passenger-picker']/div[2]/div[1]/div[9]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[11]/div[4]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//booking-flight-result-card[@id='at-flight-search-result-1']/div[1]/div[1]/div[3]/div[1]/div[1]/a[1]/h3[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='fare-details-swiper-0001']/div[1]/booking-fare-card[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//booking-flight-result-card[@id='at-flight-search-result-1']/div[1]/div[1]/div[3]/div[1]/div[1]/a[1]/h3[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='fare-details-swiper-0002']/div[1]/booking-fare-card[1]/div[1]/div[3]/button[1]").click()
    #
    # def test_qatarairways_73960473(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//input[@value='Mumbai BOM' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='Mumbai BOM' and @type='text']").send_keys("Chicago")
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[1]/div[2]/span[1]/div[1]/div[2]/div[3]/div[1]/strong[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='Stockholm ARN' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='Stockholm ARN' and @type='text']").send_keys("Paris")
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[2]/div[2]/span[1]/div[1]/div[2]/div[3]/div[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "onewayTrip").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[4]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[4]/div[4]/div[1]/div[2]/div[3]/div[2]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[11]/div[4]/button[1]").click()
    #
    # def test_qatarairways_7f1f085b(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Experience')]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='planyourtrip']/li[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='j-poi-tabs']/li[2]/a[1]/span[1]").click()
    #
    # def test_qatarairways_ff82e848(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'64')]").click()
    #     self.driver.find_element(By.ID, "locationInput").clear()
    #     self.driver.find_element(By.ID, "locationInput").send_keys("india")
    #     self.driver.find_element(By.XPATH, "//ul[@id='locationListDrop']/li[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "ph-search-backdrop").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='LocationBody']/div[1]/div[2]/ul[1]/li[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Customer Experience- Customer Services Agent (Contact Centre - AMD)')]").click()
    #     self.driver.find_element(By.ID, "save-QAAIGLOBAL160106EXTERNALENGLOBAL").click()
    #
    # def test_qatarairways_8d0eda4b(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//input[@value='Chicago ORD' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='Chicago ORD' and @type='text']").send_keys("addis ababa")
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[1]/div[2]/span[1]/div[1]/div[2]/div[3]/div[1]/strong[1]/strong[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='Abu Dhabi AUH' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='Abu Dhabi AUH' and @type='text']").send_keys("accra")
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[2]/div[2]/div[2]/span[1]/div[1]/div[2]/div[3]/div[1]/strong[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "onewayTrip").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[4]/div[4]/div[1]/div[2]/div[2]/div[2]/table[1]/tbody[1]/tr[3]/td[5]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[4]/div[4]/div[1]/div[2]/div[3]/div[2]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flights-search-from']/div[11]/div[4]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//booking-flight-result-card[@id='at-flight-search-result-2']/div[1]/div[1]/div[3]/div[1]/div[1]/a[1]/h3[1]/span[1]").click()
    #
    # def test_qatarairways_4c4ab02e(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//a[@id='managebooking-tab']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[1]/input[1]").send_keys("123456789")
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[2]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[2]/input[1]").send_keys("Smith")
    #     self.driver.find_element(By.XPATH, "//div[@id='managebooking']/div[1]/div[2]/div[3]/div[1]/button[1]").click()
    #
    # def test_qatarairways_cd5d03cc(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.ID, "flightstatus-tab").click()
    #     self.driver.find_element(By.ID, "flightStatusFrom").clear()
    #     self.driver.find_element(By.ID, "flightStatusFrom").send_keys("Abidjan")
    #     self.driver.find_element(By.XPATH, "//div[@id='flight-status-from']/div[1]/div[2]/span[1]/div[1]/div[4]/div[1]/strong[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "flightStatusto").clear()
    #     self.driver.find_element(By.ID, "flightStatusto").send_keys("Accra")
    #     self.driver.find_element(By.XPATH, "//div[@id='flight-status-from']/div[2]/div[2]/span[1]/div[1]/div[4]/div[1]/strong[1]/strong[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='flight-status-from']/div[4]/div[1]/button[1]").click()
    #
    # def test_qatarairways_e437082b(self):
    #     # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Book')]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='planyourtrip']/li[3]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "ss").clear()
    #     self.driver.find_element(By.ID, "ss").send_keys("Las Vegas")
    #     self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/span[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[4]/td[1]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[4]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='search_results_table']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id=':Ra9:']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/button[1]/div[1]/div[1]/span[1]").click()
    
    def test_qatarairways_4786982f(self):
        # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Book')]").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space(text())='Book' and @role='button']").click()

        # self.driver.find_element(By.XPATH, "//ul[@id='planyourtrip']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='planyourtrip']/li[3]/a[1]/span[text()='Hotels']").click()
        switch_to_new_tab(self.driver)

        self.driver.find_element(By.ID, "ss").clear()
        self.driver.find_element(By.ID, "ss").send_keys("washington")
        self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/span[2]/span[1]").click()

        start_date_str, end_date_str = calculate_dates(14, 15)

        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/span[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[2]/div[1]/div[1]/div[5]/ul[1]/li[1]/label[1]/span[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[4]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, f"//td[@data-date='{start_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//td[@data-date='{end_date_str}']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='left_col_wrapper']/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-sb-id='main' and @type='submit']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='left_col_wrapper']/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='left_col_wrapper']/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='left_col_wrapper']/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='left_col_wrapper']/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='occupancy-config']/span[@data-testid='searchbox-form-button-icon']").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='occupancy-popup']/div/div[1]/div[2]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='occupancy-popup']/div/div[1]/div[2]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='occupancy-popup']/div/div[3]/div[2]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='occupancy-popup']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter_group_di_:R44q:']/button[1]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_group_di_:R44q:']/div[9]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_group_hotelfacility_:R3cq:']/button[1]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_group_hotelfacility_:R3cq:']/div[17]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_group_class_:R14q:']/div[10]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='search_results_table']/div[2]/div[1]/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[4]/a[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='hcta']/span[1]").click()
        # need to wait for a second for the page to be refreshed after selecting each filter otherwise the filters will not be properly selected
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='bodyconstraint']//div[@data-testid='filters-group' and @data-filters-group='di']//div[text()='Downtown D.C.']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='bodyconstraint']//button[contains(@aria-controls, 'filter_group_hotelfacility') and @data-testid='filters-group-expand-collapse']").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='filters-group' and @data-filters-group='hotelfacility']//div[text()='Free Wifi']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='bodyconstraint']//div[@data-testid='filters-group' and @data-filters-group='class']//div[text()='5 stars']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@data-testid='sorters-dropdown-trigger']").click()
        self.driver.find_element(By.XPATH, "//button[@data-id='price' and @type='button']//span[text()='Price (lowest first)']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='search_results_table']/div[2]/div/div/div[3]/div[3]//a[@data-testid='availability-cta-btn']").click()
    