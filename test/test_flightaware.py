import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestFlightaware:
    
    # def test_flightaware_f9c80513(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[5]/div[1]/div[3]/ul[1]/li[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//table[@id='ember32']/thead[1]/tr[1]/th[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'What’s going on with my setup?')]").click()
    
    def test_flightaware_4ffca7c8(self):
        # self.driver.get("https://www.flightaware.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[2]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()

        # self.driver.find_element(By.ID, "firstname-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").clear()
        # self.driver.find_element(By.ID, "firstname-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").send_keys("John")
        self.driver.find_element(By.NAME, "firstname").clear()
        self.driver.find_element(By.NAME, "firstname").send_keys("John")

        # self.driver.find_element(By.ID, "lastname-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").clear()
        # self.driver.find_element(By.ID, "lastname-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").send_keys("Smith")
        self.driver.find_element(By.NAME, "lastname").clear()
        self.driver.find_element(By.NAME, "lastname").send_keys("Smith")

        # self.driver.find_element(By.ID, "company-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").clear()
        # self.driver.find_element(By.ID, "company-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").send_keys("ACNE AB")
        self.driver.find_element(By.NAME, "company").clear()
        self.driver.find_element(By.NAME, "company").send_keys("ACNE AB")

        # self.driver.find_element(By.ID, "email-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").clear()
        # self.driver.find_element(By.ID, "email-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").send_keys("abc@abc.com")
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys("abc@abc.com")

        # self.driver.find_element(By.ID, "phone-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").clear()
        # self.driver.find_element(By.ID, "phone-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").send_keys("888889999")
        self.driver.find_element(By.NAME, "phone").clear()
        self.driver.find_element(By.NAME, "phone").send_keys("888889999")

        # self.driver.find_element(By.ID, "tell_us_a_little_bit_about_your_data_needs-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").clear()
        # self.driver.find_element(By.ID, "tell_us_a_little_bit_about_your_data_needs-a05b6318-e6f7-499a-9c97-ae4bb150c289_8963").send_keys("Send Brochure")
        self.driver.find_element(By.NAME, "tell_us_a_little_bit_about_your_data_needs").clear()
        self.driver.find_element(By.NAME, "tell_us_a_little_bit_about_your_data_needs").send_keys("Send Brochure")

        # self.driver.find_element(By.XPATH, "//input[@value='Submit' and @type='submit']").click()
    
    # def test_flightaware_8a39a66d(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Tiers Now')]").click()
    #
    # def test_flightaware_cb1fecfb(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[4]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[4]/div[1]/div[2]/ul[1]/li[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='origin' and @type='text' and @placeholder='e.g. KJFK or New York' and @title='e.g. KJFK or New York']").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,\"Indira Gandhi Int'l (New Delhi)  - DEL - VIDP\")]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='destination' and @type='text' and @placeholder='e.g. KLAX or Los Angeles' and @title='e.g. KLAX or Los Angeles']").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,\"Los Cabos Int'l (Los Cabos)  - SJD - MMSD\")]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='findflightForm']/div[1]/div[2]/button[1]/img[1]").click()
    #
    # def test_flightaware_dc2aa3f8(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//input[@name='origin' and @value='KOSU' and @type='text' and @placeholder='Origin' and @title='Origin']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='origin' and @value='KOSU' and @type='text' and @placeholder='Origin' and @title='Origin']").send_keys("Ohio")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='findRouteMain']/div[2]/div[1]/form[1]/div[3]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='findRouteMain']/div[2]/div[1]/form[1]/div[3]/div[1]/input[1]").send_keys("New York")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[8]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='findRouteMain']/div[2]/div[2]/button[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='Status']/legend[1]").click()
    #     self.driver.find_element(By.ID, "r_Diverted").click()
    #
    # def test_flightaware_e8603513(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[1]/div[1]/div[2]/ul[1]/li[2]/a[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Subscriptions')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Upgrade')]").click()
    #
    # def test_flightaware_ecb649da(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//input[@name='origin' and @value='KOSU' and @type='text' and @placeholder='Origin' and @title='Origin']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='origin' and @value='KOSU' and @type='text' and @placeholder='Origin' and @title='Origin']").send_keys("Calgary")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='findRouteMain']/div[2]/div[1]/form[1]/div[3]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='findRouteMain']/div[2]/div[1]/form[1]/div[3]/div[1]/input[1]").send_keys("New York")
    #     self.driver.find_element(By.XPATH, "//strong[contains(.,'New York')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='findRouteMain']/div[2]/div[2]/button[1]/img[1]").click()
    #
    # def test_flightaware_ef09c913(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.ID, "s2id_autogen1").click()
    #     self.driver.find_element(By.ID, "s2id_autogen1").clear()
    #     self.driver.find_element(By.ID, "s2id_autogen1").send_keys("KCCR")
    #     self.driver.find_element(By.XPATH, "//div[@id='select2-result-label-11']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Map & Diagram')]").click()
    #
    # def test_flightaware_ccd8d9f9(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[4]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[4]/div[1]/div[2]/ul[1]/li[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='origin' and @type='text' and @placeholder='e.g. KJFK or New York' and @title='e.g. KJFK or New York']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='origin' and @type='text' and @placeholder='e.g. KJFK or New York' and @title='e.g. KJFK or New York']").send_keys("Washington")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='destination' and @type='text' and @placeholder='e.g. KLAX or Los Angeles' and @title='e.g. KLAX or Los Angeles']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='destination' and @type='text' and @placeholder='e.g. KLAX or Los Angeles' and @title='e.g. KLAX or Los Angeles']").send_keys("New York")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='findflightForm']/div[1]/div[2]/button[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='Status']/legend[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'only')]").click()
    #
    # def test_flightaware_d538537c(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//input[@name='origin' and @value='KOSU' and @type='text' and @placeholder='Origin' and @title='Origin']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='origin' and @value='KOSU' and @type='text' and @placeholder='Origin' and @title='Origin']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='origin' and @value='KOSU' and @type='text' and @placeholder='Origin' and @title='Origin']").send_keys("SFO")
    #     self.driver.find_element(By.XPATH, "//div[contains(.,\"San Francisco Int'l (San Francisco)  -\")]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='findRouteMain']/div[2]/div[1]/form[1]/div[3]/div[1]/input[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='findRouteMain']/div[2]/div[1]/form[1]/div[3]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='findRouteMain']/div[2]/div[1]/form[1]/div[3]/div[1]/input[1]").send_keys("EWR")
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Newark Liberty Intl (Newark)  -')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='findRouteMain']/div[2]/div[2]/button[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='Aircraft']/legend[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'only')]").click()
    #
    # def test_flightaware_0991035b(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[6]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Career Opportunities')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='department']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='department']").select("Product Management")
    #
    # def test_flightaware_2ff0909b(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[5]/div[1]/div[1]/ul[1]/li[3]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "photoSearchAircraftType").clear()
    #     self.driver.find_element(By.ID, "photoSearchAircraftType").select("Adam A-500 (twin-piston) (26)")
    #
    # def test_flightaware_30e310ca(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[5]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "photoSearchAirline").clear()
    #     self.driver.find_element(By.ID, "photoSearchAirline").select('Aegean Airlines "Aegean" (AEE) (452)')
    #
    # def test_flightaware_44284a24(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.ID, "s2id_autogen1").clear()
    #     self.driver.find_element(By.ID, "s2id_autogen1").send_keys("039028")
    #     self.driver.find_element(By.XPATH, "//div[@id='headerSearchForm']/div[1]/div[5]/button[1]/img[1]").click()
    #
    # def test_flightaware_52a8bace(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[3]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[3]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mainBody']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]").click()
    #
    # def test_flightaware_ca80bb42(self):
    #     # self.driver.get("https://www.flightaware.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='headerSearchForm']/div[1]/div[1]/div[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='headerSearchForm']/div[1]/div[1]/div[1]/select[1]").select("Airport")
    #     self.driver.find_element(By.ID, "airport_name_or_city").clear()
    #     self.driver.find_element(By.ID, "airport_name_or_city").send_keys("Camarillo")
    #     self.driver.find_element(By.XPATH, "//strong[contains(.,'Camarillo')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='headerSearchForm']/div[1]/div[5]/button[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View KCMA Airport Stats')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Weather')]").click()
    