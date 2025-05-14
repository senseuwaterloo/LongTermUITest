import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestWeather:
    def test_weather_8cfb8d75(self):
        self.driver.get("https://weather.com/")
        self.driver.find_element(By.ID, "LocationSearch_input").clear()
        self.driver.find_element(By.ID, "LocationSearch_input").send_keys("Champaign, IL")

        self.driver.find_element(By.XPATH, "//div[@id='LocationSearch_listbox']/button[1]").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='More Forecasts']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Air Quality Forecast']").click()

        self.driver.find_element(By.XPATH, "//span[text()='More Forecasts']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Cold & Flu']").click()
        time.sleep(1)
