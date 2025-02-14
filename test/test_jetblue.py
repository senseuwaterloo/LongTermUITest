import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_slash_format, switch_to_new_tab, get_control_key, scroll_down, scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestJetblue:
    def test_jetblue_1ee63f83(self):
        # self.driver.get("https://www.jetblue.com/")
        # need VPN to access https://www.paisly.com/ from Canada normally

        # self.driver.find_element(By.XPATH, "//button[@id='jb-tab-id-20']/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Stays']").click()

        # following action is redundant
        # self.driver.find_element(By.XPATH, "//jb-tab-panel[@id='jb-tabpanel-id-20']/div[1]/jb-renderer-template[1]/dot-booker-hotel-points[1]/jb-static-booker-pod[1]/div[1]/a[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='google-city-search']/div[1]/div[1]/div[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='google-city-search']/div[1]/div[1]/div[1]").send_keys("TEXAS CITY")
        # somehow clear is not working and we need to use the following options
        self.driver.find_element(By.NAME, "jtp-hotel-destination").send_keys(get_control_key() + "a")
        self.driver.find_element(By.NAME, "jtp-hotel-destination").send_keys(Keys.DELETE)
        self.driver.find_element(By.NAME, "jtp-hotel-destination").send_keys("TEXAS CITY")

        # self.driver.find_element(By.ID, "react-select-3-option-0").click()
        self.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'Texas City')] and ./span[contains(text(), ' TX, USA')]]").click()

        # self.driver.find_element(By.XPATH, "//input[@name='' and @value='Sun, Mar 26 – Sun, Apr 2' and @type='text' and @placeholder='Select dates']").click()
        self.driver.find_element(By.NAME, "dates").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[4]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[7]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[5]/div[3]/div[1]").click()
        first_flight_date, second_flight_date = calculate_dates_slash_format(30, 37)
        self.driver.find_element(By.NAME, "dates").clear()
        self.driver.find_element(By.NAME, "dates").send_keys(f"{first_flight_date} - {second_flight_date}")

        # self.driver.find_element(By.XPATH, "//button[@id='details-room-composition']/div[1]").click()
        self.driver.find_element(By.ID, "jtp-stays-room-composition").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[./div/span[text()='Rooms']]//button[@aria-label='subtract 1']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/button[2]").click()
        self.driver.find_element(By.XPATH, "//h2[text()='Room 1']/following-sibling::div//span[text()='Adults']/ancestor::div[1]/following-sibling::div//button[@aria-label='add 1']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//h2[text()='Room 1']/following-sibling::div//span[text()='Children']/ancestor::div[1]/following-sibling::div//button[@aria-label='subtract 1']").click()

        # self.driver.find_element(By.XPATH, "//li[@id='bui264val-6']/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[./label[text()='Child Age']]").click()
        self.driver.find_element(By.XPATH, "//li[contains(@id, 'bui') and contains(@id, 'val-6') and @role='option']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='hotel_results_search_button']/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='jtp-button' and text()='Search stays']").click()

        # need to switch to new tab
        switch_to_new_tab(self.driver)

        # self.driver.find_element(By.XPATH, "//div[@id='ba6402-41a-0e11-edf1-d517027da63']/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Search without signing in']").click()

        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_rating']/div[2]/label[5]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_amenities']/div[2]/label[1]/span[1]").click()
        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_amenities']/div[2]/label[1]/div[2]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_amenities']/div[2]/label[3]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_amenities']/div[2]/label[9]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_amenities']/div[2]/label[3]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_amenities']/div[2]/label[9]/div[2]/span[1]").click()

        sort_dropdown = self.driver.find_element(By.XPATH, "//div[@value='RECOMMENDED']")
        scroll_to_element(self.driver, sort_dropdown)
        sort_dropdown.click()

        # self.driver.find_element(By.XPATH, "//li[@id='bui8val-1']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Price (Low to High)']").click()

        # remove the resting two steps, just to show the result.
        # self.driver.find_element(By.XPATH, "//div[@id='jtp_hotel_search_results']/div[2]/a[1]/div[1]/div[2]/div[1]/div[1]/h2[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='order-summary-reserve-button']/div[1]").click()
