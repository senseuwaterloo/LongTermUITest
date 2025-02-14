import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestTheweathernetwork:
    def test_theweathernetwork_7ba05167(self):
        # self.driver.get("https://theweathernetwork.com")

        # logic changed, need to assign a location then check the highway conditions
        self.driver.find_element(By.ID, "InputField").clear()
        self.driver.find_element(By.ID, "InputField").send_keys("Vancouver")
        # time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@data-testid='search-result-item']/div[text()='Vancouver, British Columbia']").click()

        # self.driver.find_element(By.XPATH, "//nav[@id='main-nav']/div[1]/div[1]/div[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Maps & Roads')]").click()
        # somehow need to wait for a few second to let the layout be stable (mostly for the ads be stable) so that after clicking on map button
        # it will show the Vancouver area otherwise the map will show current area
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//nav[@data-testid='header-navigation-bar']/a[2]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Highway Conditions')]").click()
        self.driver.find_element(By.XPATH, "//button[@title='Highway Conditions']").click()

        # self.driver.find_element(By.ID, "regiondropdownlist").clear()
        # self.driver.find_element(By.ID, "regiondropdownlist").select("Vancouver")
