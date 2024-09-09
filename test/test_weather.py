import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestWeather:
    
    # def test_weather_3cad7a9a(self):
    #     # self.driver.get("https://weather.com/")
    #     self.driver.find_element(By.ID, "LocationSearch_input").clear()
    #     self.driver.find_element(By.ID, "LocationSearch_input").send_keys("seatlle")
    #     self.driver.find_element(By.ID, "LocationSearch_listbox-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[1]/a[2]/span[1]").click()
    #
    # def test_weather_7480540d(self):
    #     # self.driver.get("https://weather.com/")
    #     self.driver.find_element(By.ID, "LocationSearch_input").clear()
    #     self.driver.find_element(By.ID, "LocationSearch_input").send_keys("90028")
    #     self.driver.find_element(By.ID, "LocationSearch_listbox-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[1]/a[3]/span[1]").click()
    
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
    
    # def test_weather_c9461be7(self):
    #     # self.driver.get("https://weather.com/")
    #     self.driver.find_element(By.ID, "LocationSearch_input").clear()
    #     self.driver.find_element(By.ID, "LocationSearch_input").send_keys("10019")
    #     self.driver.find_element(By.ID, "LocationSearch_listbox-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[1]/a[5]/span[1]").click()
    #     self.driver.find_element(By.ID, "month-picker").clear()
    #     self.driver.find_element(By.ID, "month-picker").select("Mar")
    #     self.driver.find_element(By.XPATH, "//div[@id='WxuCalendar-main-69bb61a5-2a5f-4a3e-879c-53f37030c238']/section[1]/div[2]/nav[1]/div[1]/button[1]/span[1]").click()
    #
    # def test_weather_5ef9bea9(self):
    #     # self.driver.get("https://weather.com/")
    #     self.driver.find_element(By.ID, "LocationSearch_input").clear()
    #     self.driver.find_element(By.ID, "LocationSearch_input").send_keys("90210")
    #     self.driver.find_element(By.ID, "LocationSearch_listbox-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[1]/a[2]/span[1]").click()
    #
    # def test_weather_707a0f16(self):
    #     # self.driver.get("https://weather.com/")
    #     self.driver.find_element(By.ID, "LocationSearch_input").clear()
    #     self.driver.find_element(By.ID, "LocationSearch_input").send_keys("90028")
    #     self.driver.find_element(By.ID, "LocationSearch_listbox-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[1]/a[5]/span[1]").click()
    #
    # def test_weather_5be3e9e7(self):
    #     # self.driver.get("https://weather.com/")
    #     self.driver.find_element(By.ID, "LocationSearch_input").clear()
    #     self.driver.find_element(By.ID, "LocationSearch_input").send_keys("10019")
    #     self.driver.find_element(By.ID, "LocationSearch_listbox-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[2]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff-9a1a-d99a39f16abe']/div[1]/nav[1]/div[1]/div[2]/nav[1]/div[1]/div[1]/nav[1]/div[1]/a[5]/span[1]").click()
    #
    # def test_weather_cb8b0cd3(self):
    #     # self.driver.get("https://weather.com/")
    #     self.driver.find_element(By.ID, "LocationSearch_input").clear()
    #     self.driver.find_element(By.ID, "LocationSearch_input").send_keys("Los Angeles")
    #     self.driver.find_element(By.ID, "LocationSearch_listbox-0").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='Wxu-MapCard-Module']/div[1]/a[1]/div[1]/div[1]/div[1]").click()
    #
    # def test_weather_aa065caa(self):
    #     # self.driver.get("https://weather.com/")
    #     self.driver.find_element(By.ID, "LocationSearch_input").clear()
    #     self.driver.find_element(By.ID, "LocationSearch_input").send_keys("Denver")
    #     self.driver.find_element(By.ID, "LocationSearch_listbox-0").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See Details')]").click()
    