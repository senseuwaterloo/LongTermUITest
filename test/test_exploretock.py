import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_with_suffix


@pytest.mark.usefixtures("driver_session")
class TestExploretock:
    def test_exploretock_a6372f23(self):
        self.driver.get("https://exploretock.com")

        reservation_type_dropdown = self.driver.find_element(By.ID, "reservations-city-search-type")
        reservation_type_select = Select(reservation_type_dropdown)
        reservation_type_select.select_by_value('wineries')

        self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div/div[1]/div[1]/div/div/div[2]/div/div/button").click()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Find a location']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Find a location']").send_keys("NAPA VALLEY")
        self.driver.find_element(By.XPATH, "//ul[@aria-label='Location search results']//span[text()='Napa Valley']").click()

        self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div/div[1]/div[1]/div/div/div[3]/div/div").click()
        start_date_str, end_date_str = calculate_dates_with_suffix(7, 7)
        self.driver.find_element(By.XPATH, f"//button[@aria-label='{start_date_str}']").click()

        reservation_time_dropdown = self.driver.find_element(By.ID, "wineries-city-search-time")
        reservation_time_select = Select(reservation_time_dropdown)
        reservation_time_select.select_by_value('10:00')

        guest_size_dropdown = self.driver.find_element(By.ID, "wineries-city-search-guests")
        guest_zise_select = Select(guest_size_dropdown)
        guest_zise_select.select_by_value('4')
        self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div/div[1]/div[1]/div/div/div[6]/a").click()

        self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div/div[2]/button[4]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Outdoors']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Wine tasting']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Update search']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div/div[3]/div[1]/div/div/div[1]/div/ul/li[1]/div/a").click()
