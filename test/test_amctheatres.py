import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates


@pytest.mark.usefixtures("driver_session")
class TestAmctheatres:
    def test_amctheatres_29f47ddb(self):
        self.driver.get("https://www.amctheatres.com")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Sign In to AMC Stubs Account']").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("UITestStudy2024")
        self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Sign In']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Change Theatre Location']").click()
        self.driver.find_element(By.XPATH, "//input[@aria-labelledby='theatreLocatorHeadline']").click()
        self.driver.find_element(By.XPATH, "//input[@aria-labelledby='theatreLocatorHeadline']").send_keys("AMC Grove City 14")
        self.driver.find_element(By.XPATH, "//i[@aria-label='Submit Search']").click()
        self.driver.find_element(By.XPATH, "//*[@id='modal-body']/div[2]/div/div/div/div[2]/ul/li[1]/label/div[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='modal-body']/div[2]/div/div/div/div[3]/button").click()
        self.driver.find_element(By.XPATH, "//li[@id='qa-desktop-sub-nav-find-a-theatre']/div/a").click()

        theatre_dropdown_element = self.driver.find_element(By.ID, "showtimes-theatre-filter")
        select = Select(theatre_dropdown_element)
        select.select_by_value('amc-grove-city-14')

        date_dropdown_element = self.driver.find_element(By.ID, "showtimes-date-filter")
        select = Select(date_dropdown_element)
        start_date_str, end_date_str = calculate_dates(1, 2)
        select.select_by_value(start_date_str)

        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div[3]/main/div/div[1]/section/div/div[1]/div/div[2]/div[1]/div/section/div[1]/div/div[1]/a").click()

        self.driver.find_element(By.XPATH, "//*[@id='react-container']/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[1]/ul/li[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='react-container']/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[1]/ul/li[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='react-container']/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[1]/ul/li[3]").click()
        self.driver.find_element(By.XPATH, "//*[@id='react-container']/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[1]/ul/li[4]").click()
        self.driver.find_element(By.ID, "checkout-continue").click()
    