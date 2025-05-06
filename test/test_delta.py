import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_slash_format


@pytest.mark.usefixtures("setup_class")
class TestDelta:
    def test_delta_295380ed(self):
        self.driver.get("https://www.delta.com")

        self.driver.find_element(By.XPATH, "//a[@id='fromAirportName']/span[1]").click()
        self.driver.find_element(By.ID, "search_input").clear()
        self.driver.find_element(By.ID, "search_input").send_keys("LGA")
        self.driver.find_element(By.XPATH, "//div[@id='airport-serach-panel']/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[@id='toAirportName']/span[1]").click()
        self.driver.find_element(By.ID, "search_input").clear()
        self.driver.find_element(By.ID, "search_input").send_keys("PHL")
        self.driver.find_element(By.XPATH, "//div[@id='airport-serach-panel']/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]/span[2]").click()
        self.driver.find_element(By.ID, "selectTripType-val").click()
        self.driver.find_element(By.ID, "ui-list-selectTripType1").click()

        self.driver.find_element(By.ID, "input_departureDate_1").click()
        flight_date, _ = calculate_dates_slash_format(21, 37)
        self.driver.find_element(By.XPATH, f"//a[contains(@data-date,'{flight_date}')]").click()

        self.driver.find_element(By.XPATH, "//button[@value='done' and @type='button']").click()
        self.driver.find_element(By.ID, "adv-search").click()
        self.driver.find_element(By.ID, "faresFor-val").click()
        self.driver.find_element(By.ID, "ui-list-faresFor3").click()
        self.driver.find_element(By.ID, "btnSubmit").click()
