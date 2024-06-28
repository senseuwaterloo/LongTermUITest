import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.mark.usefixtures("setup_class")
class TestAccuweather:
    
    def test_accuweather_f53ce927(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Atlanta")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Atlanta, GA, US')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Monthly')]").click()
    
    def test_accuweather_fe537b30(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Tokyo, Japan")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Health & Activities')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Sinus Pressure')]").click()
        self.driver.find_element(By.XPATH, "//h2[contains(.,'Health & Activities')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Running')]").click()

    def test_accuweather_4c224b36(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Belo Horizonte")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Belo Horizonte, Minas Gerais, BR')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//h3[contains(.,'Radar & Maps')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Wind Flow')]").click()

    def test_accuweather_5635a86d(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("florida city")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Florida City, FL, US')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Monthly')]").click()

    def test_accuweather_5a855cec(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Mumbai")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Mumbai, Maharashtra, IN')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Health & Activities')]").click()

    def test_accuweather_86fdac44(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Miami")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Miami, FL, US')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'See Interactive Map')]").click()

    def test_accuweather_8843420a(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("New York City")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New York City, New York, US')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Daily')]").click()

    def test_accuweather_89ca5e83(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").click()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("reno nevada")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Daily')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[5]/div[1]/div[1]/div[6]/a[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Overnight')]").click()

    def test_accuweather_0c5bba5d(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//h3[contains(.,'Hurricane Tracker')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/svg[2]").click()

    def test_accuweather_0e12f051(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Madison, WI")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Daily')]").click()

    def test_accuweather_3a9af9da(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//h3[contains(.,'Hurricane Tracker')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See all')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[7]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'2020')]").click()
        self.driver.find_element(By.XPATH, "//h2[contains(.,'All Oceans')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[7]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/a[5]").click()

    def test_accuweather_bcac5fe8(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[6]/div[1]/div[3]/a[6]").click()
        self.driver.find_element(By.XPATH, "//img[@alt='Everything Under The Sun']").click()
        self.driver.find_element(By.XPATH, "//span[@id='episode-11']/img[1]").click()

    def test_accuweather_ddc28045(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Boston")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Boston, MA, US')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Hourly')]").click()

    def test_accuweather_e61e4271(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("New York City")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New York City, New York, US')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Air Quality')]").click()

    def test_accuweather_f304652c(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Tallahassee, FL")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'More Details')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'5 mph')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'94%')]").click()

    def test_accuweather_8cfafcc6(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Health & Activities')]").click()
        self.driver.find_element(By.XPATH, "//h1[contains(.,'Maine North, County Cork')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("salt lake city")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Salt Lake City, UT, US')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Health & Activities')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[3]/a[5]/div[2]").click()

    def test_accuweather_0c131eb5(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("MANCHESTER")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Manchester, Manchester, GB')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[7]/div[1]/div[1]/div[8]/a[3]").click()
        self.driver.find_element(By.XPATH, "//h2[contains(.,'April')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[5]").click()

    def test_accuweather_9d02190d(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Los Angeles")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Los Angeles, CA, US')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'MinuteCast')]").click()

    def test_accuweather_a3d2c7ab(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//h3[contains(.,'Radar & Maps')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Wind Flow')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='windflow-container-legacy']/div[1]/div[1]/div[1]").click()

    def test_accuweather_a5b1f3a6(self):
        # self.driver.get("https://www.accuweather.com/")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Maine North, Ireland")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Air Quality')]").click()
        self.driver.find_element(By.XPATH, "//h1[contains(.,'Reno, NV')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Location')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Maine Nortyh Ireland")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("Maine North, County Cork, Ireland")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").click()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @type='text' and @placeholder='Search']").send_keys("maine north")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Maine North, County Cork, IE')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Air Quality')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='view-more-pollutants']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pollutants']/div[6]/h3[1]").click()
    