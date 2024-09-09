import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestUps:
    
    # def test_ups_39eee42d(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.ID, "mainNavDropdown1").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Calculate Shipping Cost')]").click()
    #     self.driver.find_element(By.ID, "orig_PostalCode").clear()
    #     self.driver.find_element(By.ID, "orig_PostalCode").send_keys("96162")
    #     self.driver.find_element(By.ID, "dest_PostalCode").clear()
    #     self.driver.find_element(By.ID, "dest_PostalCode").send_keys("10013")
    #     self.driver.find_element(By.XPATH, "//div[@id='destResidential']/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='origType']/div[1]/label[1]").click()
    #     self.driver.find_element(By.ID, "ctc_module1_submit").click()
    #
    # def test_ups_55990a0a(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.ID, "mainNavDropdown1").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Location')]").click()
    #     self.driver.find_element(By.ID, "txtQuery").clear()
    #     self.driver.find_element(By.ID, "txtQuery").send_keys("miami")
    #     self.driver.find_element(By.ID, "high_svc_031").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='Find' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Miami, FL')]").click()
    #
    # def test_ups_66e0ff15(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Contact Us')]").click()
    #     self.driver.find_element(By.ID, "tcChat_btnEmail_img").click()
    #     self.driver.find_element(By.ID, "tcChat_emailInput_input").clear()
    #     self.driver.find_element(By.ID, "tcChat_emailInput_input").send_keys("i.contacted@gmail.com")
    #     self.driver.find_element(By.ID, "tcChat_btnSendEmail_img").click()
    #
    # def test_ups_7b6b522c(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.ID, "ups-imagemap4").click()
    #     self.driver.find_element(By.XPATH, "//g[@id='us']/path[3]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'United States - English')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
    #     self.driver.find_element(By.ID, "txtQuery").clear()
    #     self.driver.find_element(By.ID, "txtQuery").send_keys("60504")
    #     self.driver.find_element(By.ID, "a_show_all_options").click()
    #     self.driver.find_element(By.ID, "a_sub_filter_mkg_prg").click()
    #     self.driver.find_element(By.ID, "a_sub_filter_oth_srvc").click()
    #     self.driver.find_element(By.ID, "addn_svc_001").click()
    #     self.driver.find_element(By.ID, "addn_svc_009").click()
    #     self.driver.find_element(By.ID, "a_sub_filter_loc_flt").click()
    #     self.driver.find_element(By.ID, "sel_location_within").clear()
    #     self.driver.find_element(By.ID, "sel_location_within").select("10 mi")
    #     self.driver.find_element(By.XPATH, "//div[@id='gdol_search_box']/div[1]/div[2]/dl[1]/dd[1]/button[2]").click()

    def test_ups_8ae1041c(self):
        # self.driver.get("https://ups.com")
        self.driver.find_element(By.XPATH, "//a[@id='tabs_0_tab_1']/span[1]").click()
        self.driver.find_element(By.ID, "ups-ship-from").clear()
        self.driver.find_element(By.ID, "ups-ship-from").send_keys("10001")
        self.driver.find_element(By.XPATH, "//div[@id='ship-from-input']/div[1]/div[1]/div[1]/div[1]/span[2]/span[1]").click()
        self.driver.find_element(By.ID, "ups-ship-to").clear()
        # the zip code of Truckee seems not valid on UPS, use another one for Sacramento
        # self.driver.find_element(By.ID, "ups-ship-to").send_keys("Truckee California")
        self.driver.find_element(By.ID, "ups-ship-to").send_keys("95814")
        self.driver.find_element(By.XPATH, "//div[@id='ship-to-input']/div[1]/div[1]/div[1]/div[1]/span[2]/span[1]").click()
        self.driver.find_element(By.ID, "ups-ship-weight").clear()
        self.driver.find_element(By.ID, "ups-ship-weight").send_keys("5")

        # length, width, and height are also required to get a quote
        self.driver.find_element(By.ID, "ups-ship-length").clear()
        self.driver.find_element(By.ID, "ups-ship-length").send_keys("5")
        self.driver.find_element(By.ID, "ups-ship-width").clear()
        self.driver.find_element(By.ID, "ups-ship-width").send_keys("5")
        self.driver.find_element(By.ID, "ups-ship-height").clear()
        self.driver.find_element(By.ID, "ups-ship-height").send_keys("5")

        self.driver.find_element(By.ID, "widget-get-quote-cta").click()

        # self.driver.find_element(By.XPATH, "//div[@id='tiles-container']/div[1]/div[1]/div[1]/sqw-service-cell[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()=' Fastest ']").click()

    # def test_ups_0d010ed4(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.XPATH, "//a[@id='tabs_0_tab_1']/span[1]").click()
    #     self.driver.find_element(By.ID, "ups-ship-from").clear()
    #     self.driver.find_element(By.ID, "ups-ship-from").send_keys("Long Beach")
    #     self.driver.find_element(By.XPATH, "//div[@id='ship-from-input']/div[1]/div[1]/div[1]/div[1]/span[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "ups-ship-to").clear()
    #     self.driver.find_element(By.ID, "ups-ship-to").send_keys("Portland")
    #     self.driver.find_element(By.XPATH, "//div[@id='ship-to-input']/div[1]/div[1]/div[1]/div[1]/span[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "ups-ship-weight").clear()
    #     self.driver.find_element(By.ID, "ups-ship-weight").send_keys("10")
    #     self.driver.find_element(By.ID, "widget-get-quote-cta").click()
    #
    # def test_ups_2fbde8a4(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.ID, "mainNavDropdown1").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Calculate Shipping Cost')]").click()
    #     self.driver.find_element(By.ID, "orig_PostalCode").clear()
    #     self.driver.find_element(By.ID, "orig_PostalCode").send_keys("10001")
    #     self.driver.find_element(By.ID, "dest_PostalCode").clear()
    #     self.driver.find_element(By.ID, "dest_PostalCode").send_keys("10023")
    #     self.driver.find_element(By.XPATH, "//button[@id='iconForCalendar']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'10')]").click()
    #     self.driver.find_element(By.ID, "ctc_module1_submit").click()
    #
    # def test_ups_a3c590a8(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.ID, "ups-menuLinks1").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Go to Shipping Support')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View Shipping Options')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn More About Flat Rate Shipping')]").click()
    #     self.driver.find_element(By.ID, "tabs_0_tab_2").click()
    #
    # def test_ups_cf815d4f(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'United States - English')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See Pickup Options')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedule Now')]").click()
    #
    # def test_ups_d361b836(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'United States - English')]").click()
    #     self.driver.find_element(By.ID, "ups-track--qs").clear()
    #     self.driver.find_element(By.ID, "ups-track--qs").send_keys("123456")
    #     self.driver.find_element(By.ID, "stApp_widgetTrkNumBtn").click()
    #
    # def test_ups_dab36052(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.ID, "mainNavDropdown1").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedule a Pickup')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pickup Status')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='ordernumber' and @value='' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='ordernumber' and @value='' and @type='text']").send_keys("123456")
    #     self.driver.find_element(By.XPATH, "//input[@name='SUBMIT_BUTTON_PRN' and @value='Submit' and @type='submit']").click()
    #
    # def test_ups_f53d6c0e(self):
    #     # self.driver.get("https://ups.com")
    #     self.driver.find_element(By.ID, "ups-imagemap4").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'United States - English')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
    #     self.driver.find_element(By.ID, "txtQuery").clear()
    #     self.driver.find_element(By.ID, "txtQuery").send_keys("SPRING, TX")
    #     self.driver.find_element(By.XPATH, "//div[@id='gdol_search_box']/div[1]/div[2]/dl[1]/dd[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Spring, Harris County, TX')]").click()
    #     self.driver.find_element(By.ID, "locationNameTxt0").click()
    #     self.driver.find_element(By.ID, "tab_tab3D").click()
    