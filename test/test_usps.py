import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab


@pytest.mark.usefixtures("driver_session")
class TestUsps:
    def test_usps_277e3468(self):
        self.driver.get("https://usps.com")

        self.driver.find_element(By.XPATH, "//a[text()='Quick Tools']").click()

        self.driver.find_element(By.XPATH, "//p[text()='Find USPS Locations']").click()

        self.driver.find_element(By.ID, "searchMainType").clear()
        self.driver.find_element(By.ID, "searchMainType").send_keys("60505")

        self.driver.find_element(By.XPATH, "//label[@for='Passport-appointments-checkbox-1']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedule a') and contains(text(),'Passport ')]").click()
        switch_to_new_tab(self.driver)

        service_type_dropdown = self.driver.find_element(By.NAME, "passportappointmentType")
        service_type_select = Select(service_type_dropdown)
        service_type_select.select_by_value("newpassport")
        adult_dropdown = self.driver.find_element(By.NAME, "adultCount")
        adult_select = Select(adult_dropdown)
        adult_select.select_by_value("1")

        self.driver.find_element(By.XPATH, "//div[@id='searchBySection']/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "SEARCH_ZIP5").clear()
        self.driver.find_element(By.ID, "SEARCH_ZIP5").send_keys("60505")

        self.driver.find_element(By.ID, "searchFacilitiesButton").click()
        self.driver.find_element(By.XPATH, "//div[@id='1353701']/div[2]/button[1]").click()

        time.sleep(2)
        self.driver.find_element(By.ID, "displayDate").click()
        self.driver.find_element(By.XPATH, "//a[@class='ui-state-default']").click()
        self.driver.find_element(By.ID, "selectDateFromModal").click()
        self.driver.find_element(By.XPATH, "//p[@class='availableAppointment']").click()

        self.driver.find_element(By.ID, "standardize_firstName").clear()
        self.driver.find_element(By.ID, "standardize_firstName").send_keys("Ellen")
        self.driver.find_element(By.ID, "standardize_lastName").clear()
        self.driver.find_element(By.ID, "standardize_lastName").send_keys("Walker")
        self.driver.find_element(By.ID, "standardize_tPhone").clear()
        self.driver.find_element(By.ID, "standardize_tPhone").send_keys("123-456-7890")
        self.driver.find_element(By.ID, "standardize_tEmail").clear()
        self.driver.find_element(By.ID, "standardize_tEmail").send_keys("EW@gmail.com")
        self.driver.find_element(By.XPATH, "//div[@id='customerInfoSection']/div[3]/div[1]/div[2]/label[1]/span[1]").click()

        self.driver.find_element(By.XPATH, "//p[text()='I have read, understand, and agree to the ']").click()

        self.driver.find_element(By.ID, "sendCodeBtn")
