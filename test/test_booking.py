import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates


@pytest.mark.usefixtures("setup_class")
class TestBooking:
    def test_booking_fc552b69(self):
        # self.driver.get("https://booking.com")
        self.driver.find_element(By.XPATH, "//span[text()='Sign in or register']").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//span[text()='Continue with email']").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("UITestStudy4Booking")
        self.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//a[@id='flights']").click()
        self.driver.find_element(By.XPATH, "//label[@for='search_type_option_MULTISTOP']").click()
        self.driver.find_element(By.XPATH, "//button[@data-ui-name='input_location_from_segment_0']").click()
        # time.sleep(200)
        # need to click the cross mark sometimes
        # self.driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div/div/div/div/div/div/label/span/span[2]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Airport or city' and @data-ui-name='input_text_autocomplete']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Airport or city' and @data-ui-name='input_text_autocomplete']").send_keys("NEW YORK")
        self.driver.find_element(By.XPATH, "//span[contains(., 'NYC') and contains(., 'New York All airports')]").click()

        self.driver.find_element(By.XPATH, "//button[@data-ui-name='input_location_to_segment_0']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Airport or city' and @data-ui-name='input_text_autocomplete']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Airport or city' and @data-ui-name='input_text_autocomplete']").send_keys("TOKYO")
        self.driver.find_element(By.XPATH, "//span[contains(., 'TYO') and contains(., 'Tokyo All airports')]").click()

        first_flight_date, second_flight_date = calculate_dates(30, 37)
        self.driver.find_element(By.XPATH, "//button[@data-ui-name='button_date_segment_0']").click()
        self.driver.find_element(By.XPATH, f"//span[@data-date='{first_flight_date}']").click()

        self.driver.find_element(By.XPATH, "//button[@data-ui-name='input_location_from_segment_1']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Airport or city' and @data-ui-name='input_text_autocomplete']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Airport or city' and @data-ui-name='input_text_autocomplete']").send_keys("TOKYO")
        self.driver.find_element(By.XPATH, "//span[contains(., 'TYO') and contains(., 'Tokyo All airports')]").click()

        self.driver.find_element(By.XPATH, "//button[@data-ui-name='input_location_to_segment_1']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Airport or city' and @data-ui-name='input_text_autocomplete']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Airport or city' and @data-ui-name='input_text_autocomplete']").send_keys("NEW DELHI")
        self.driver.find_element(By.XPATH, "//span[contains(., 'DEL') and contains(., 'Delhi International Airport')]").click()

        self.driver.find_element(By.XPATH, "//button[@data-ui-name='button_date_segment_1']").click()
        self.driver.find_element(By.XPATH, f"//span[@data-date='{second_flight_date}']").click()

        self.driver.find_element(By.XPATH, "//button[@data-ui-name='button_search_submit']").click()

        # self.driver.find_element(By.XPATH, "//div[contains(text(), 'Nonstop only')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(), '12:00 - 17:59')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='search_tabs_FASTEST']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='flight_card_bound_select_flight' and @aria-label='View details Flexible ticket upgrade available']").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='flight_details_inner_modal_select_button']").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='title' and text()='Flexible ticket']").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='checkout_ticket_type_inner_next']").click()
    