import time
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestAa:
    def test_aa_6c28458c(self):
        # self.driver.get("https://www.aa.com/homePage.do")
        # self.driver.find_element(By.ID, "plan-travel-expander").click()
        # get shadow root first then find element under the shadow root, can only use css selector under shadow root, element has no id after introduced shadow root
        adc_header_element = self.driver.find_element(By.CSS_SELECTOR, "adc-header")
        main_navigation_element = adc_header_element.shadow_root.find_element(By.ID, "main-navigation")
        plan_travel_element = main_navigation_element.find_element(By.CSS_SELECTOR, "adc-tab[label='Plan travel']")
        plan_travel_element.click()

        # wrapped click with wait for element to be clickable, no need to use thread sleep here
        # time.sleep(3)

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Flights')]").click()
        # get shadow root first then find element under the shadow root, can only use css selector under shadow root, element changed from <a> to <hp-header-link>
        new_adc_header_element = self.driver.find_element(By.CSS_SELECTOR, "adc-header")
        new_main_navigation_element = new_adc_header_element.shadow_root.find_element(By.ID, "main-navigation")
        hp_header_link_element = new_main_navigation_element.find_element(By.CSS_SELECTOR, "hp-header-link[href*='/reservation/roundTripSearchAccess.do'][class='panel-links adc-link']")
        # https://stackoverflow.com/questions/49906451/web-driver-click-on-element-within-shadowdom-is-returning-error-messageunk
        # selenium.common.exceptions.JavascriptException: Message: javascript error: Cannot read properties of undefined (reading 'defaultView')
        # seems like a bug with the framework: https://issues.chromium.org/issues/42322743
        self.driver.execute_script("arguments[0].click()", hp_header_link_element.shadow_root.find_element(By.CSS_SELECTOR, "a"))
        # hp_header_link_element.shadow_root.find_element(By.CSS_SELECTOR, "a").click()

        # wrapped click with wait for element to be clickable, no need to use thread sleep here
        # time.sleep(5)

        # self.driver.find_element(By.XPATH, "//a[@id='ui-id-5']/span[2]").click()
        # avoid using dynamic id
        self.driver.find_element(By.XPATH, "//span[contains(.,'Multi city')]").click()

        self.driver.find_element(By.ID, "segments0.origin").click()
        self.driver.find_element(By.ID, "segments0.origin").clear()
        self.driver.find_element(By.ID, "segments0.origin").send_keys("JFK")

        # self.driver.find_element(By.ID, "ui-id-11").click()
        # avoid using dynamic id
        self.driver.find_element(By.XPATH, "//a[contains(.,'JFK - New York John F Kennedy Intl, NY')]").click()

        self.driver.find_element(By.ID, "segments0.destination").click()
        self.driver.find_element(By.ID, "segments0.destination").clear()
        self.driver.find_element(By.ID, "segments0.destination").send_keys("Heathrow")

        # self.driver.find_element(By.ID, "ui-id-12").click()
        # avoid using dynamic id
        self.driver.find_element(By.XPATH, "//a[contains(., 'LHR - London Heathrow, United Kingdom')]").click()

        self.driver.find_element(By.ID, "segments0.travelDate").clear()

        # self.driver.find_element(By.ID, "segments0.travelDate").send_keys("04/19/2023")
        # input a relative far date
        self.driver.find_element(By.ID, "segments0.travelDate").send_keys("04/19/2025")

        self.driver.find_element(By.ID, "segments1.origin").click()
        self.driver.find_element(By.ID, "segments1.origin").clear()
        self.driver.find_element(By.ID, "segments1.origin").send_keys("Heathrow")

        # self.driver.find_element(By.ID, "ui-id-13").click()
        # avoid using dynamic id
        self.driver.find_element(By.XPATH, "/html/body/ul[3]/li/a").click()

        self.driver.find_element(By.ID, "segments1.destination").click()
        self.driver.find_element(By.ID, "segments1.destination").clear()
        self.driver.find_element(By.ID, "segments1.destination").send_keys("CDG")

        # self.driver.find_element(By.ID, "ui-id-14").click()
        # avoid using dynamic id
        self.driver.find_element(By.XPATH, "//a[contains(., 'CDG - Paris Charles de Gaulle, France')]").click()

        self.driver.find_element(By.ID, "segments1.travelDate").clear()

        # self.driver.find_element(By.ID, "segments1.travelDate").send_keys("04/21/2023")
        # input a relative far date
        self.driver.find_element(By.ID, "segments1.travelDate").send_keys("04/21/2025")

        self.driver.find_element(By.ID, "addFlightLink").click()
        self.driver.find_element(By.ID, "segments2.origin").click()
        self.driver.find_element(By.ID, "segments2.origin").clear()
        self.driver.find_element(By.ID, "segments2.origin").send_keys("CDG")

        # self.driver.find_element(By.ID, "ui-id-17").click()
        # avoid using dynamic id
        self.driver.find_element(By.XPATH, "/html/body/ul[5]/li/a").click()

        self.driver.find_element(By.ID, "segments2.destination").click()
        self.driver.find_element(By.ID, "segments2.destination").clear()
        self.driver.find_element(By.ID, "segments2.destination").send_keys("JFK")

        # self.driver.find_element(By.ID, "ui-id-18").click()
        # avoid using dynamic id
        self.driver.find_element(By.XPATH, "/html/body/ul[6]/li/a").click()

        self.driver.find_element(By.ID, "segments2.travelDate").clear()

        # self.driver.find_element(By.ID, "segments2.travelDate").send_keys("04/23/2023")
        # input a relative far date
        self.driver.find_element(By.ID, "segments2.travelDate").send_keys("04/23/2025")

        self.driver.find_element(By.ID, "flightSearchSubmitBtn").click()

        # wrapped click with wait for element to be clickable, no need to use thread sleep here. Need to set the maximum timeout to 60s
        # time.sleep(60)

        self.driver.find_element(By.ID, "btn-sort-by-duration").click()
    