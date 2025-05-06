import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_slash_format, switch_to_new_tab, get_control_key, scroll_down, scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestJetblue:
    def test_jetblue_1ee63f83(self):
        self.driver.get("https://www.jetblue.com/")

        self.driver.find_element(By.XPATH, "//span[text()='Stays']").click()

        self.driver.find_element(By.NAME, "jtp-hotel-destination").send_keys(get_control_key() + "a")
        self.driver.find_element(By.NAME, "jtp-hotel-destination").send_keys(Keys.DELETE)
        self.driver.find_element(By.NAME, "jtp-hotel-destination").send_keys("TEXAS CITY")

        self.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'Texas City')] and ./span[contains(text(), ' TX, USA')]]").click()

        self.driver.find_element(By.NAME, "dates").click()

        first_flight_date, second_flight_date = calculate_dates_slash_format(30, 37)
        self.driver.find_element(By.NAME, "dates").clear()
        self.driver.find_element(By.NAME, "dates").send_keys(f"{first_flight_date} - {second_flight_date}")

        self.driver.find_element(By.ID, "jtp-stays-room-composition").click()

        self.driver.find_element(By.XPATH, "//div[./div/span[text()='Rooms']]//button[@aria-label='subtract 1']").click()

        self.driver.find_element(By.XPATH, "//h2[text()='Room 1']/following-sibling::div//span[text()='Adults']/ancestor::div[1]/following-sibling::div//button[@aria-label='add 1']").click()

        self.driver.find_element(By.XPATH, "//h2[text()='Room 1']/following-sibling::div//span[text()='Children']/ancestor::div[1]/following-sibling::div//button[@aria-label='subtract 1']").click()

        self.driver.find_element(By.XPATH, "//div[./label[text()='Child Age']]").click()
        self.driver.find_element(By.XPATH, "//li[contains(@id, 'bui') and contains(@id, 'val-6') and @role='option']").click()

        self.driver.find_element(By.XPATH, "//button[@data-testid='jtp-button' and text()='Search stays']").click()

        switch_to_new_tab(self.driver)

        self.driver.find_element(By.XPATH, "//button[text()='Search without signing in']").click()

        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_rating']/div[2]/label[5]/span[1]").click()

        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_amenities']/div[2]/label[1]/div[2]/span[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_amenities']/div[2]/label[3]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter_hotel_amenities']/div[2]/label[9]/div[2]/span[1]").click()

        sort_dropdown = self.driver.find_element(By.XPATH, "//div[@value='RECOMMENDED']")
        scroll_to_element(self.driver, sort_dropdown)
        sort_dropdown.click()

        self.driver.find_element(By.XPATH, "//div[text()='Price (Low to High)']").click()
