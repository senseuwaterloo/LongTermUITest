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
class TestUhaul:
    
    def test_uhaul_fd4a3605(self):
        # self.driver.get("https://uhaul.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trailers & Towing')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='EquipmentSearch']/fieldset[1]/div[1]/div[2]/div[4]/button[1]").click()
        self.driver.find_element(By.ID, "Year_ValueTowing").clear()
        self.driver.find_element(By.ID, "Year_ValueTowing").select("2015")
        self.driver.find_element(By.ID, "Make_ValueTowing").clear()
        self.driver.find_element(By.ID, "Make_ValueTowing").select("Dodge")
        self.driver.find_element(By.ID, "VehicleModel_ValueTowing").clear()
        self.driver.find_element(By.ID, "VehicleModel_ValueTowing").select("Challenger")
    
    def test_uhaul_2c1b0530(self):
        # self.driver.get("https://uhaul.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Storage')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Climate Controlled Storage')]").click()
        self.driver.find_element(By.ID, "movingFromInput").clear()
        self.driver.find_element(By.ID, "movingFromInput").send_keys("Los Angeles")
        self.driver.find_element(By.ID, "ui-id-3").click()
        self.driver.find_element(By.ID, "selectboxUnitSizeInput").click()
        self.driver.find_element(By.XPATH, "//div[@id='storageUnitSizes']/ul[1]/li[2]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='locationSearchForm']/fieldset[1]/div[1]/div[1]/div[4]/button[1]").click()
    
    def test_uhaul_55a8e749(self):
        # self.driver.get("https://uhaul.com")
        self.driver.find_element(By.XPATH, "//li[@id='QuotesComponent']/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='QuotesComponent']/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[2]/dl[1]").click()
        self.driver.find_element(By.ID, "btnAddToCart_89a1e2a2-8d1c-4851-9008-7281c0a19e80").click()
        self.driver.find_element(By.XPATH, "//ul[@id='accountMenu']/li[2]/a[1]").click()
        self.driver.find_element(By.ID, "btnAddToCart_89a1e2a2-8d1c-4851-9008-7281c0a19e80").click()
        self.driver.find_element(By.ID, "aEditEquipmentLink").click()
        self.driver.find_element(By.ID, "aEditQuoteEquipmentLink").click()
        self.driver.find_element(By.ID, "submit_TT").click()
        self.driver.find_element(By.XPATH, "//dialog[@id='dvShowNewTowing_TT']/div[1]/div[2]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "btnContinue_Row0_Entity775073").click()
        self.driver.find_element(By.ID, "SelectedScheduleTime_Row0_Entity775073").clear()
        self.driver.find_element(By.ID, "SelectedScheduleTime_Row0_Entity775073").select("12 00 AM Midnight")
        self.driver.find_element(By.ID, "btnContinue_Row0_Entity775073").click()
        self.driver.find_element(By.XPATH, "//div[@id='sharedRevealContent']/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "btnSelectDropoffNoPreference").click()
        self.driver.find_element(By.ID, "btnContinueSafeTrip").click()
        self.driver.find_element(By.ID, "linkNoSafeTrip").click()
        self.driver.find_element(By.XPATH, "//ul[@id='accountMenu']/li[2]/a[1]").click()
    
    def test_uhaul_6d95fd0c(self):
        # self.driver.get("https://uhaul.com")
        self.driver.find_element(By.XPATH, "//main[@id='mainRow']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/div[2]").click()
        self.driver.find_element(By.ID, "movingFromInput").clear()
        self.driver.find_element(By.ID, "movingFromInput").send_keys("Anchorage, Alaska")
        self.driver.find_element(By.ID, "ui-id-3").click()
        self.driver.find_element(By.XPATH, "//form[@id='locationFilterForm']/fieldset[1]/div[1]/div[3]/fieldset[1]/ul[1]/li[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='locationFilterForm']/fieldset[1]/div[1]/div[4]/fieldset[1]/ul[1]/li[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='locationFilterForm']/fieldset[1]/div[1]/div[5]/div[2]/button[1]").click()
    
    def test_uhaul_727142ca(self):
        # self.driver.get("https://uhaul.com")
        self.driver.find_element(By.ID, "PickupLocation-TruckOnly").clear()
        self.driver.find_element(By.ID, "PickupLocation-TruckOnly").send_keys("Chicago")
        self.driver.find_element(By.ID, "ui-id-7").click()
        self.driver.find_element(By.XPATH, "//form[@id='EquipmentSearch']/div[3]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']/div[1]/table[1]/tbody[1]/tr[4]/td[4]").click()
        self.driver.find_element(By.XPATH, "//form[@id='EquipmentSearch']/div[3]/div[2]/button[1]").click()
    
    def test_uhaul_7ef4398b(self):
        # self.driver.get("https://uhaul.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Boxes & Packing Supplies')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='divProductCategory_Boxes']/ul[1]/li[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.ID, "addToCart").click()
    
    def test_uhaul_9d8ba96c(self):
        # self.driver.get("https://uhaul.com")
        self.driver.find_element(By.ID, "PickupLocation-TruckOnly").clear()
        self.driver.find_element(By.ID, "PickupLocation-TruckOnly").send_keys("Birmingham, Alabama")
        self.driver.find_element(By.ID, "ui-id-7").click()
        self.driver.find_element(By.ID, "DropoffLocation-TruckOnly").clear()
        self.driver.find_element(By.ID, "DropoffLocation-TruckOnly").send_keys("mobile alabama")
        self.driver.find_element(By.XPATH, "//form[@id='EquipmentSearch']/div[3]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//a[@title='Next']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'29')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='EquipmentSearch']/div[3]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "submit_DC").click()
        self.driver.find_element(By.XPATH, "//dialog[@id='dvShowNewTowing_DC']/div[1]/div[2]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "SelectedScheduleTime_Row0_Entity775073").clear()
        self.driver.find_element(By.ID, "SelectedScheduleTime_Row0_Entity775073").select("12 00 AM Midnight")
        self.driver.find_element(By.ID, "btnContinue_Row0_Entity775073").click()
        self.driver.find_element(By.XPATH, "//div[@id='sharedRevealContent']/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "btnContinueSafeTrip").click()
        self.driver.find_element(By.ID, "linkNoSafeTrip").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'No thanks, I do not need these items')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'No thanks, I do not need storage')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'No thanks, I do not need supplies')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='SkipLocationBottomForm']/button[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='SkipLocationBottomForm']/button[1]").click()
        self.driver.find_element(By.ID, "hlSaveQuote").click()
        self.driver.find_element(By.XPATH, "//form[@id='SaveCustomerQuoteForm']/button[1]").click()
    
    def test_uhaul_bcc293b4(self):
        # self.driver.get("https://uhaul.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Storage')]").click()
        self.driver.find_element(By.ID, "movingFromInput").clear()
        self.driver.find_element(By.ID, "movingFromInput").send_keys("90001")
        self.driver.find_element(By.ID, "ui-id-3").click()
        self.driver.find_element(By.ID, "selectboxUnitSizeInput").click()
        self.driver.find_element(By.XPATH, "//div[@id='storageUnitSizes']/ul[1]/li[2]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "selectboxInput").click()
        self.driver.find_element(By.XPATH, "//form[@id='locationSearchForm']/fieldset[1]/div[1]/div[1]/div[4]/button[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='locationFilterForm']/fieldset[1]/div[1]/div[4]/fieldset[1]/ul[1]/li[2]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='locationFilterForm']/fieldset[1]/div[1]/div[5]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='locationFilterForm']/fieldset[1]/div[1]/fieldset[1]/ul[1]/li[2]/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//form[@id='locationFilterForm']/fieldset[1]/div[1]/div[5]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "viewRates_712027").click()
        self.driver.find_element(By.ID, "panel2-1c04b873-label").click()
    
    def test_uhaul_0c5b953a(self):
        # self.driver.get("https://uhaul.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Hitches & Accessories')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trailer Hitches')]").click()
        self.driver.find_element(By.ID, "uhhvd-Make").clear()
        self.driver.find_element(By.ID, "uhhvd-Make").select("Honda")
        self.driver.find_element(By.ID, "uhhvd-Model").clear()
        self.driver.find_element(By.ID, "uhhvd-Model").select("Civic")
        self.driver.find_element(By.ID, "Trim-Details").clear()
        self.driver.find_element(By.ID, "Trim-Details").select("Sedan")
        self.driver.find_element(By.XPATH, "//form[@id='hitchControl']/fieldset[1]/div[1]/div[3]/div[1]/div[1]/div[1]/fieldset[1]/ul[1]/li[3]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "ZipCode").clear()
        self.driver.find_element(By.ID, "ZipCode").send_keys("10019")
        self.driver.find_element(By.ID, "Installation_SelectedDate").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'19')]").click()
        self.driver.find_element(By.ID, "btnFindHitches").click()
    