import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestUsps:
    
    def test_usps_277e3468(self):
        # self.driver.get("https://usps.com")

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Quick Tools')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Quick Tools']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='g-navigation']/div[1]/nav[1]/ul[1]/li[1]/div[1]/ul[1]/li[3]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//p[text()='Find USPS Locations']").click()

        # self.driver.find_element(By.ID, "city-state-input").clear()
        # self.driver.find_element(By.ID, "city-state-input").send_keys("60505")
        self.driver.find_element(By.ID, "searchMainType").clear()
        self.driver.find_element(By.ID, "searchMainType").send_keys("60505")

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Passport Appointments')]").click()
        self.driver.find_element(By.XPATH, "//label[@for='Passport-appointments-checkbox-1']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedule an Appointment')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedule a') and contains(text(),'Passport ')]").click()
        switch_to_new_tab(self.driver)

        # self.driver.find_element(By.ID, "passportappointmentType").clear()
        # self.driver.find_element(By.ID, "passportappointmentType").select("New Passport Only")
        # self.driver.find_element(By.ID, "adultCount").clear()
        # self.driver.find_element(By.ID, "adultCount").select("1")
        service_type_dropdown = self.driver.find_element(By.NAME, "passportappointmentType")
        service_type_select = Select(service_type_dropdown)
        service_type_select.select_by_value("newpassport")
        adult_dropdown = self.driver.find_element(By.NAME, "adultCount")
        adult_select = Select(adult_dropdown)
        adult_select.select_by_value("1")

        self.driver.find_element(By.XPATH, "//div[@id='searchBySection']/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "SEARCH_ZIP5").clear()
        self.driver.find_element(By.ID, "SEARCH_ZIP5").send_keys("60505")

        # redundant
        # self.driver.find_element(By.ID, "SEARCH_ZIP5").click()

        self.driver.find_element(By.ID, "searchFacilitiesButton").click()
        self.driver.find_element(By.XPATH, "//div[@id='1353701']/div[2]/button[1]").click()

        # add select date action
        # need to wait for a few second for the loading image to fully disappear
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

        # agree to Term and Conditions
        self.driver.find_element(By.XPATH, "//p[text()='I have read, understand, and agree to the ']").click()

        # self.driver.find_element(By.ID, "standardizeButton").click()
        # don click to avoid spam data
        self.driver.find_element(By.ID, "sendCodeBtn")
    
    # def test_usps_1c73e566(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.ID, "mail-ship-width").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shipping Restrictions')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='1569211481354']/section[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h4[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='1569211481354']/section[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/p[2]/a[1]/strong[1]").click()
    #
    # def test_usps_56bb259c(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Quick Tools')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='g-navigation']/div[1]/nav[1]/ul[1]/li[1]/div[1]/ul[1]/li[10]/a[1]/p[1]").click()
    #     self.driver.find_element(By.ID, "searchHero").clear()
    #     self.driver.find_element(By.ID, "searchHero").send_keys("54620")
    #     self.driver.find_element(By.ID, "searchHero").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='filterButton']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='filterOptions']/div[1]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "applyFiltersButton").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='1382437']/span[1]").click()
    #
    # def test_usps_7a8f2c58(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.ID, "mail-ship-width").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Calculate a Price')]").click()
    #     self.driver.find_element(By.ID, "Origin").clear()
    #     self.driver.find_element(By.ID, "Origin").send_keys("77449")
    #     self.driver.find_element(By.ID, "Destination").click()
    #     self.driver.find_element(By.ID, "Destination").clear()
    #     self.driver.find_element(By.ID, "Destination").send_keys("77084")
    #     self.driver.find_element(By.XPATH, "//div[@id='options-section']/div[1]/div[3]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Normal Delivery Time')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='Continue' and @type='submit']").click()
    #
    # def test_usps_fa73b47e(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Stamps & Supplies')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shopping Cart  (')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='ci20242001452' and @value='1' and @type='text' and @placeholder='']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='ci20242001452' and @value='1' and @type='text' and @placeholder='']").send_keys("5")
    #     self.driver.find_element(By.ID, "atg_store_update").click()
    #
    # def test_usps_e8a2c53e(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Quick Tools')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='g-navigation']/div[1]/nav[1]/ul[1]/li[1]/div[1]/ul[1]/li[3]/a[1]/img[1]").click()
    #     self.driver.find_element(By.ID, "city-state-input").clear()
    #     self.driver.find_element(By.ID, "city-state-input").send_keys("90210")
    #     self.driver.find_element(By.ID, "within-select").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'10 Miles')]").click()
    #     self.driver.find_element(By.ID, "searchLocations").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='1440481']/div[1]/div[1]/div[1]/h2[1]/strong[1]").click()
    #
    # def test_usps_ef84bb55(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shipping Supplies')]").click()
    #     self.driver.find_element(By.XPATH, "//img[@alt='Priority Mail Flat Rate® Padded Envelope']").click()
    #     self.driver.find_element(By.ID, "addToCartVisBtnEP14PE_X").click()
    #
    # def test_usps_312f86f8(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.ID, "home-input").clear()
    #     self.driver.find_element(By.ID, "home-input").send_keys("90019847161684486")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/form[1]/span[1]/div[1]/div[1]/button[1]").click()
    #
    # def test_usps_480f3147(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.ID, "link-locator").click()
    #     self.driver.find_element(By.ID, "city-state-input").clear()
    #     self.driver.find_element(By.ID, "city-state-input").send_keys("84043")
    #     self.driver.find_element(By.ID, "within-select").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'50 Miles')]").click()
    #     self.driver.find_element(By.ID, "searchLocations").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(@href, 'link://#')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/div[2]/div[3]/div[3]/div[2]/div[1]/label[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/div[2]/div[3]/div[3]/div[2]/div[3]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/div[2]/div[3]/div[3]/div[2]/div[4]/label[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(@href, 'link://#')]").click()
    #     self.driver.find_element(By.ID, "searchLocations").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='1370151']/div[1]/div[1]/div[1]/h2[1]").click()
    #
    # def test_usps_97f68d19(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Business')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Every Door Direct Mail')]").click()
    #     self.driver.find_element(By.ID, "cityOrZipCode").clear()
    #     self.driver.find_element(By.ID, "cityOrZipCode").send_keys("04401")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Table')]").click()
    #     self.driver.find_element(By.XPATH, "//img[@alt='Sort icon']").click()
    #     self.driver.find_element(By.XPATH, "//img[@alt='Sort icon']").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Next Step')]").click()
    #
    # def test_usps_b11977d2(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Quick Tools')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='g-navigation']/div[1]/nav[1]/ul[1]/li[1]/div[1]/ul[1]/li[3]/a[1]/img[1]").click()
    #     self.driver.find_element(By.ID, "city-state-input").clear()
    #     self.driver.find_element(By.ID, "city-state-input").send_keys("10019")
    #     self.driver.find_element(By.ID, "post-offices-select").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Self-Service Kiosks')]").click()
    #     self.driver.find_element(By.ID, "within-select").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'10 Miles')]").click()
    #     self.driver.find_element(By.ID, "searchLocations").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='1378686']/div[1]/div[1]/div[1]/h2[1]/strong[1]").click()
    #
    # def test_usps_c28495d9(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Gifts')]").click()
    #     self.driver.find_element(By.XPATH, "//label[contains(.,'Toys (21)')]").click()
    #     self.driver.find_element(By.XPATH, "//label[contains(.,'Cars & Trucks (17)')]").click()
    #     self.driver.find_element(By.XPATH, "//label[contains(.,'2023 (1)')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Metal Earth® 3D USPS LLV Model Kit')]").click()
    #     self.driver.find_element(By.ID, "addToCartVisBtn843497").click()
    #     self.driver.find_element(By.ID, "atg_button_checkout").click()
    #
    # def test_usps_c61f4e8d(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Quick Tools')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='g-navigation']/div[1]/nav[1]/ul[1]/li[1]/div[1]/ul[1]/li[6]/a[1]/p[1]").click()
    #     self.driver.find_element(By.ID, "Origin").clear()
    #     self.driver.find_element(By.ID, "Origin").send_keys("46298")
    #     self.driver.find_element(By.ID, "Destination").clear()
    #     self.driver.find_element(By.ID, "Destination").send_keys("06057")
    #     self.driver.find_element(By.ID, "ShippingDate").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'14')]").click()
    #     self.driver.find_element(By.ID, "ShippingTime").clear()
    #     self.driver.find_element(By.ID, "ShippingTime").select("between 11 00 a.m. - 11 30 a.m.")
    #     self.driver.find_element(By.XPATH, "//div[@id='options-section']/div[1]/div[3]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Normal Delivery Time')]").click()
    #     self.driver.find_element(By.ID, "extra-service-b-3").click()
    #     self.driver.find_element(By.ID, "extra-service-b-1").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='Continue' and @type='submit']").click()
    #
    # def test_usps_e5e57875(self):
    #     # self.driver.get("https://usps.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Stamps')]").click()
    #     self.driver.find_element(By.XPATH, "//img[@alt='Snowy Beauty Stamps']").click()
    #     self.driver.find_element(By.ID, "addToCartVisBtn684004").click()
    #     self.driver.find_element(By.ID, "atg_button_checkout").click()
    