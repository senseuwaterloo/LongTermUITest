import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("driver_session")
class TestLandwatch:
    def test_landwatch_b3691435(self):
        self.driver.get("https://landwatch.com")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Timberland')]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='Georgia ']").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'51 - 100 Acres')]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='For Sale ']").click()

        date_listed_dropdown = self.driver.find_element(By.ID, "Date Listed")
        date_listed_select = Select(date_listed_dropdown)
        date_listed_select.select_by_visible_text('Past 7 days')

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'dropdown')]/div[1]/span[1]").click()

        self.driver.find_element(By.ID, "Price_-").click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='name' and @value='' and @type='text' and @placeholder='Name']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='name' and @value='' and @type='text' and @placeholder='Name']").send_keys("James Smith")

        self.driver.find_element(By.XPATH, "//input[@name='tel' and @value='' and @type='tel' and @placeholder='Phone Number']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='tel' and @value='' and @type='tel' and @placeholder='Phone Number']").send_keys("52465235214")
    