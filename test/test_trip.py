import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_ticketcenter_format, scroll_down


@pytest.mark.usefixtures("driver_session")
class TestTrip:
    def test_trip_b5cabe51(self):
        self.driver.get("https://us.trip.com/?locale=en-us")
        self.driver.find_element(By.XPATH, "//div[@id='main-search-box']/div[2]/div[1]/div[1]/ul[1]/li[3]/span[1]").click()

        self.driver.find_element(By.XPATH, "//input[contains(@class, 'index-module_input_') and @placeholder='From' and @value='']").click()
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'index-module_input_') and @placeholder='Departure Station' and @value='']").clear()
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'index-module_input_') and @placeholder='Departure Station' and @value='']").send_keys("BUSAN")

        self.driver.find_element(By.XPATH, "//span[contains(@class, 'index-module_station_') and ./span/span[text()='Busan']]").click()

        self.driver.find_element(By.XPATH, "//div[contains(@class, 'index-module_stations_')]//ul/li/span[text()='Seoul']").click()

        start_day, start_month_year, _, _ = calculate_dates_ticketcenter_format(14, 14)
        self.driver.find_element(By.XPATH, f"//div[@style='display: block;']//div[@class='c-calendar-month' and ./div[@class='c-calendar-month__title' and text()='{start_month_year}']]//span[text()='{start_day}']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class,'search-btn')]/span[text()='Search']").click()

        self.driver.find_element(By.XPATH, "//div[@data-ubt-key='trn-list_bd-r']/div/li[1]//div[@data-ubt-key='button closed']/span[text()='Select']").click()
        self.driver.find_element(By.XPATH, "//li[@data-ubt-key='trn-list_p2p-item' and position()=1]//div[@data-ubt-key='trn-list_p2p-item-package' and position()=1]//div[@data-ubt-key='book' and text()='Book']").click()

        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Last name']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Last name']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Last name']").send_keys("SMITH")
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='First name & middle name']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='First name & middle name']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='First name & middle name']").send_keys("AGENT")

        self.driver.find_element(By.XPATH, "//input[@placeholder='Please provide date of birth' and @type='text']").click()
        self.driver.find_element(By.XPATH, "//div[@data-ubt-key='dp2-dropdown-block-item' and text()='Jan']").click()
        self.driver.find_element(By.XPATH, "//div[@data-ubt-key='dp2-dropdown-block-item' and text()='1']").click()
        self.driver.find_element(By.XPATH, "//div[@data-ubt-key='dp2-dropdown-block-item' and text()='1998']").click()
        self.driver.find_element(By.XPATH, "//div[@data-ubt-key='dp2-footer-button' and text()='Done']").click()

        self.driver.find_element(By.XPATH, "//input[@placeholder='Country or region' and @type='text' and @data-ubt-key='na-1 input-el cursor-pointer']").click()
        self.driver.find_element(By.XPATH, "//span[@data-ubt-key='country-name' and text()='Australia']").click()

        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys("AGENT.SMITH@MATRIX.COM")
        scroll_down(self.driver, 500)

        continue_button = self.driver.find_element(By.XPATH, "//div[@data-ubt-key='btn-submit']").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element(continue_button).perform()
