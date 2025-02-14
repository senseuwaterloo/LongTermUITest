import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestWeather:
    def test_weather_8cfb8d75(self):
        # self.driver.get("https://weather.com/")
        self.driver.find_element(By.ID, "LocationSearch_input").clear()
        self.driver.find_element(By.ID, "LocationSearch_input").send_keys("Champaign, IL")

        # self.driver.find_element(By.ID, "LocationSearch_listbox-0").click()
        self.driver.find_element(By.XPATH, "//div[@id='LocationSearch_listbox']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[2]/button[1]/span[1]").click()
        # need to wait a few second otherwise dropdown will close immediately due to the loading process of the page. Mostly because of the advertisement
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='More Forecasts']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[2]/nav[1]/div[1]/div[1]/nav[1]/div[1]/a[5]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Air Quality Forecast']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[2]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='More Forecasts']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[2]/nav[1]/div[1]/div[1]/nav[1]/div[1]/a[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Cold & Flu']").click()
        time.sleep(1)
