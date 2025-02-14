import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates, switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestRentalcars:
    def test_rentalcars_81835704(self):
        # self.driver.get("https://rentalcars.com")
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]").clear()
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]").send_keys("Heathrow")
        self.driver.find_element(By.ID, "searchbox-toolbox-fts-pickup").clear()
        self.driver.find_element(By.ID, "searchbox-toolbox-fts-pickup").send_keys("Heathrow Airport")

        self.driver.find_element(By.XPATH, "//li[@id='searchbox-toolbox-fts-pickup-suggestion-0']/div[1]/div[1]/div[1]/div[1]").click()

        # self.driver.find_element(By.XPATH, "//button[@id='searchbox-toolbox-date-picker-pickup-date']/div[1]/div[2]/div[1]/div[2]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/span[1]/span[1]").click()
        # self.driver.find_element(By.ID, "searchbox-toolbox-pickup-time").clear()
        # self.driver.find_element(By.ID, "searchbox-toolbox-pickup-time").select("2 00 PM")
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='searchbox-toolbox-date-picker-dropoff-date']/div[1]/div[2]/div[1]/div[2]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[7]/span[1]/span[1]").click()
        # self.driver.find_element(By.ID, "searchbox-toolbox-dropoff-time").clear()
        # self.driver.find_element(By.ID, "searchbox-toolbox-dropoff-time").select("1 00 PM")
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

        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='searchbox-toolbox-submit-button']").click()

        # self.driver.find_element(By.XPATH, "//ul[@id='__bui-6']/li[5]/button[1]/div[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/button[1]/span[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[6]/div[1]/button[1]/span[2]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='__bui-21-label']/div[1]/div[2]/h3[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Show premium cars']").click()
        self.driver.find_element(By.XPATH, "//div[./input[@data-testid='minimumFourDoors-filter-option-true']]").click()
        self.driver.find_element(By.XPATH, "//div[./input[@data-testid='mileage-filter-option-UNLIMITED']]").click()
        self.driver.find_element(By.XPATH, "//div[./input[@data-testid='transmission-filter-option-AUTOMATIC']]").click()

        # wait for a few seconds to make sure the filters are applied and the page is fully loaded, otherwise it will click a wrong item from the page before refreshed
        time.sleep(3)

        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]/div[7]/button[1]/span[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='insurance-portal-root']/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='bff-container']/div[1]//button[@aria-label='View deal']").click()
        switch_to_new_tab(self.driver)
        self.driver.find_element(By.XPATH, "//button[@data-testid='package-deal-cta']").click()
