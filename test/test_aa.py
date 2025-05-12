import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestAa:
    def test_aa_6c28458c(self):
        self.driver.get("https://www.aa.com/homePage.do")
        adc_header_element = self.driver.find_element(By.CSS_SELECTOR, "adc-header")
        main_navigation_element = adc_header_element.shadow_root.find_element(By.ID, "main-navigation")
        plan_travel_element = main_navigation_element.find_element(By.CSS_SELECTOR, "adc-tab[label='Plan travel']")
        plan_travel_element.click()

        new_adc_header_element = self.driver.find_element(By.CSS_SELECTOR, "adc-header")
        new_main_navigation_element = new_adc_header_element.shadow_root.find_element(By.ID, "main-navigation")
        hp_header_link_element = new_main_navigation_element.find_element(By.CSS_SELECTOR, "hp-header-link[href*='/reservation/roundTripSearchAccess.do'][class='panel-links adc-link']")
        self.driver.execute_script("arguments[0].click()", hp_header_link_element.shadow_root.find_element(By.CSS_SELECTOR, "a"))
        # self.driver.find_element(By.XPATH, "//span[contains(.,'Multi city')]").click()
        trip_type_adc_dropdown_shadow = self.driver.find_element(By.ID, "trip-type")
        trip_type_adc_dropdown_shadow.click()
        trip_type_adc_dropdown_list = trip_type_adc_dropdown_shadow.shadow_root.find_element(By.CSS_SELECTOR, "div > div.aileron-dropdown__menu > adc-dropdown-listbox")
        multi_city_option = trip_type_adc_dropdown_list.shadow_root.find_element(By.ID, "adc-lb-2")
        multi_city_option.click()

        first_origin_airport_shadow = self.driver.find_element(By.ID, "originAirport1")
        first_origin_airport_input_shadow = first_origin_airport_shadow.shadow_root.find_element(By.ID, "airport-code-input")
        geolocator_input_shadow = first_origin_airport_input_shadow.shadow_root.find_element(By.ID, "geolocator-input")
        first_origin_input = geolocator_input_shadow.shadow_root.find_element(By.CSS_SELECTOR, "#container > input")
        first_origin_input.click()
        first_origin_input.clear()
        first_origin_input.send_keys("JFK")
        # self.driver.find_element(By.ID, "segments0.origin").click()
        # self.driver.find_element(By.ID, "segments0.origin").clear()
        # self.driver.find_element(By.ID, "segments0.origin").send_keys("JFK")
        self.driver.find_element(By.XPATH, "//a[contains(.,'JFK - New York John F Kennedy Intl, NY')]").click()

        self.driver.find_element(By.ID, "segments0.destination").click()
        self.driver.find_element(By.ID, "segments0.destination").clear()
        self.driver.find_element(By.ID, "segments0.destination").send_keys("Heathrow")
        self.driver.find_element(By.XPATH, "//a[contains(., 'LHR - London Heathrow, United Kingdom')]").click()

        self.driver.find_element(By.ID, "segments0.travelDate").clear()
        self.driver.find_element(By.ID, "segments0.travelDate").send_keys("08/19/2025")
        self.driver.find_element(By.ID, "segments1.origin").click()
        self.driver.find_element(By.ID, "segments1.origin").clear()
        self.driver.find_element(By.ID, "segments1.origin").send_keys("Heathrow")
        self.driver.find_element(By.XPATH, "/html/body/ul[3]/li/a").click()

        self.driver.find_element(By.ID, "segments1.destination").click()
        self.driver.find_element(By.ID, "segments1.destination").clear()
        self.driver.find_element(By.ID, "segments1.destination").send_keys("CDG")
        self.driver.find_element(By.XPATH, "//a[contains(., 'CDG - Paris Charles de Gaulle, France')]").click()

        self.driver.find_element(By.ID, "segments1.travelDate").clear()
        self.driver.find_element(By.ID, "segments1.travelDate").send_keys("08/21/2025")

        self.driver.find_element(By.ID, "addFlightLink").click()
        self.driver.find_element(By.ID, "segments2.origin").click()
        self.driver.find_element(By.ID, "segments2.origin").clear()
        self.driver.find_element(By.ID, "segments2.origin").send_keys("CDG")
        self.driver.find_element(By.XPATH, "/html/body/ul[5]/li/a").click()

        self.driver.find_element(By.ID, "segments2.destination").click()
        self.driver.find_element(By.ID, "segments2.destination").clear()
        self.driver.find_element(By.ID, "segments2.destination").send_keys("JFK")
        self.driver.find_element(By.XPATH, "/html/body/ul[6]/li/a").click()

        self.driver.find_element(By.ID, "segments2.travelDate").clear()
        self.driver.find_element(By.ID, "segments2.travelDate").send_keys("08/23/2025")

        self.driver.find_element(By.ID, "flightSearchSubmitBtn").click()

        self.driver.find_element(By.ID, "btn-sort-by-duration").click()
    