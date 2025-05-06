import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates, switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestRentalcars:
    def test_rentalcars_81835704(self):
        self.driver.get("https://rentalcars.com")

        self.driver.find_element(By.ID, "searchbox-toolbox-fts-pickup").clear()
        self.driver.find_element(By.ID, "searchbox-toolbox-fts-pickup").send_keys("Heathrow Airport")

        self.driver.find_element(By.XPATH, "//li[@id='searchbox-toolbox-fts-pickup-suggestion-0']/div[1]/div[1]/div[1]/div[1]").click()

        self.driver.find_element(By.ID, "searchbox-toolbox-date-picker-pickup-date").click()
        start_date_str, end_date_str = calculate_dates(7, 11)
        self.driver.find_element(By.XPATH, f"//span[@data-date='{start_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//span[@data-date='{end_date_str}']").click()
        pickup_time_dropdown = self.driver.find_element(By.NAME, "pickup-time")
        pickup_time_select = Select(pickup_time_dropdown)
        pickup_time_select.select_by_value("14:00")
        dropoff_time_dropdown = self.driver.find_element(By.NAME, "dropoff-time")
        dropoff_select = Select(dropoff_time_dropdown)
        dropoff_select.select_by_value("13:00")

        self.driver.find_element(By.XPATH, "//button[@data-testid='searchbox-toolbox-submit-button']").click()

        self.driver.find_element(By.XPATH, "//button[@aria-label='Show premium cars']").click()
        self.driver.find_element(By.XPATH, "//div[./input[@data-testid='minimumFourDoors-filter-option-true']]").click()
        self.driver.find_element(By.XPATH, "//div[./input[@data-testid='mileage-filter-option-UNLIMITED']]").click()
        self.driver.find_element(By.XPATH, "//div[./input[@data-testid='transmission-filter-option-AUTOMATIC']]").click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "//div[@data-testid='bff-container']/div[1]//button[@aria-label='View deal']").click()
        switch_to_new_tab(self.driver)
        self.driver.find_element(By.XPATH, "//button[@data-testid='package-deal-cta']").click()
