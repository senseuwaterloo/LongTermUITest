import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestDmvVirginiaGov:
    
    # def test_dmvvirginiagov_f670ae67(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Highway Safety')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Request a Police Crash Report')]").click()
    #
    # def test_dmvvirginiagov_f9dc7f3e(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Online Service')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'General')]").click()
    #     self.driver.find_element(By.XPATH, "//h3[@id='DWR at DMV']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hunting and Fishing Licenses')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hunting & Fishing Licenses')]").click()
    #
    # def test_dmvvirginiagov_feacf6a1(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vehicle Registration Renewal')]").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnContinue").click()
    #
    # def test_dmvvirginiagov_a844bd83(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"DMV's Mobile Offices\")]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View Calendar by Location')]").click()
    #     self.driver.find_element(By.XPATH, "//body[@id='top']/section[1]/article[1]/article[1]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'HIGHLAND')]").click()
    #
    # def test_dmvvirginiagov_ae26c7ab(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Highway Safety')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Teen Driver Safety')]").click()
    #
    # def test_dmvvirginiagov_b1823198(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vehicle Registration Renewal')]").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnContinue").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtTitleNo").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtTitleNo").send_keys("X123456")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtVIN").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtVIN").send_keys("1234")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSubmit").click()
    #
    # def test_dmvvirginiagov_c73c9013(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vehicles')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Emissions Inspections')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Emissions Inspections')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Virginia Department of Environmental Quality')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Renewable Energy')]").click()
    #
    # def test_dmvvirginiagov_c764c41f(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Practice Exams')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Study and Practice for a Driver's License\")]").click()
    #     self.driver.find_element(By.XPATH, "//body[@id='ng-app']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/i[1]").click()
    #
    # def test_dmvvirginiagov_ecfeb19a(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtAddress").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtAddress").send_keys("Richmond")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnGeocode").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='Select' and @type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@title='Richmond Central']").click()
    
    def test_dmvvirginiagov_7752731f(self):
        # self.driver.get("https://www.dmv.virginia.gov/")
        # navigation logic and page layout changed
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Make an Appointment')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Book or Cancel Your Appointment')]").click()
        # self.driver.find_element(By.ID, "apptLink").click()
        # self.driver.find_element(By.XPATH, "//div[@id='5611b18f-4c1b-42b2-86c6-d0bd8358c476']/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='a2777b13-6fb2-4f42-af90-c4f6ae2a72a2']/div[1]/div[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='36e4a071-79fa-4483-8b73-3499f0e9633c']/div[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='e4e8d106-ccfb-4c66-ac7b-39bc56c107d9']/div[1]/div[1]/div[1]/div[2]").click()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_0__Value").clear()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_0__Value").send_keys("James")
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_1__Value").clear()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_1__Value").send_keys("Smith")
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_2__Value").clear()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_2__Value").send_keys("abac@abc.com")
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_3__Value").clear()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_3__Value").send_keys("abac@abc.com")
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").click()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").clear()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").send_keys("888899778")
        # self.driver.find_element(By.XPATH, "//input[@value='Next' and @type='submit']").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Make an Appointment')]").click()

        self.driver.find_element(By.XPATH, "//body[@id='top']/div[3]/div/header/div[2]/div/div/div/a").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[3]/div/div[1]/div/div/div[1]/div/a").click()
        # can't use relative id xpath since dynamic id will be introduced
        self.driver.find_element(By.XPATH, "//button[@data-id='CALENDAR']").click()
        # can't use relative id xpath since dynamic id will be introduced
        self.driver.find_element(By.XPATH, "//button[@data-id='5']").click()
        # can't use relative id xpath since dynamic id will be introduced
        self.driver.find_element(By.XPATH, "//button[@data-id='38']").click()
        # can't use relative id xpath since dynamic id will be introduced
        self.driver.find_element(By.XPATH, "//button[@data-latitude='36.7176']").click()

        self.driver.find_element(By.XPATH, "//a[@aria-label='Go to next page of dates available']").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='Select a time']/div[5]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='Select a time']/div[5]/div[2]/div[2]/div[2]").click()
        # sleep to avoid: Element click intercepted: xpath = //button[@type='submit' and @class='next-button-alt'] - Message: element click intercepted: Element is not clickable at point (1283, 1028)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @class='next-button-alt']").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_0__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_0__Value").send_keys("James")
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_1__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_1__Value").send_keys("Smith")
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_2__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_2__Value").send_keys("5145778593")
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_3__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_3__Value").send_keys("abac@abc.com")
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").send_keys("abac@abc.com")
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").send_keys("abac@abc.com")
        self.driver.find_element(By.XPATH, "//main[@id='maincontent']/form/div[3]/div[2]/button").click()

    # def test_dmvvirginiagov_7dbd1196(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//body[@id='top']/section[1]/section[1]/article[2]/div[1]/a[1]/h4[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Eligibility')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Non-residents')]").click()
    #
    # def test_dmvvirginiagov_87e6932d(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vehicles')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Replacement Titles')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Substitute Titles')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Transferring a Vehicle from a Deceased Owner')]").click()
    #
    # def test_dmvvirginiagov_0e11b90f(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Highway Safety')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Crash Investigation')]").click()
    #
    # def test_dmvvirginiagov_0ef35dfc(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Reserve Your Spot')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Book or Cancel Your Appointment')]").click()
    #     self.driver.find_element(By.ID, "apptLink").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='5611b18f-4c1b-42b2-86c6-d0bd8358c476']/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='a2777b13-6fb2-4f42-af90-c4f6ae2a72a2']/div[1]/div[1]/div[1]").click()
    #
    # def test_dmvvirginiagov_26ee4ce0(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Forms')]").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_drpCategory").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_drpCategory").select("Driver")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch").click()
    #
    # def test_dmvvirginiagov_2ca5a61f(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Practice Exams')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Study and Practice for a Motorcycle License')]").click()
    #     self.driver.find_element(By.XPATH, "//body[@id='ng-app']/div[1]/div[1]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[2]/i[1]").click()
    #
    # def test_dmvvirginiagov_3c287094(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'All')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Attending a Driver Training School')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Driver Training Schools')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Driver Training School Near You')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bristol District')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Dublin')]").click()
    #
    # def test_dmvvirginiagov_453894ae(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'All')]").click()
    #     self.driver.find_element(By.XPATH, "//body[@id='top']/section[1]/article[1]/div[1]/article[3]/div[1]/a[1]/h4[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Personalized Plate Guidelines and Restrictions')]").click()
    #
    # def test_dmvvirginiagov_5e459a8f(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Forms')]").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtSearch").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtSearch").send_keys("Customer Concern Report")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'CSMA 14')]").click()
    #
    # def test_dmvvirginiagov_6a3cc218(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vehicle Registration Renewal')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='accordion']/div[3]/div[1]/a[1]/strong[1]").click()
    #
    # def test_dmvvirginiagov_70f488de(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Drivers / ID Cards')]").click()
    #     self.driver.find_element(By.XPATH, "//h3[@id=\"Driver's License Reinstatement\"]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Eligibility')]").click()
    #
    # def test_dmvvirginiagov_72bb2bfd(self):
    #     # self.driver.get("https://www.dmv.virginia.gov/")
    #     self.driver.find_element(By.XPATH, "//body[@id='top']/section[1]/section[1]/article[1]/div[1]/a[1]/h4[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vehicle Registration Renewal')]").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnContinue").click()
    