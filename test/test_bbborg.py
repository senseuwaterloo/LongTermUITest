import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestBbbOrg:
    def test_bbborg_c96d460a(self):
        self.driver.get("https://bbb.org")
        self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div/div/div[2]/form/div/div[2]/div[2]/div/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div/div/div[2]/form/div/div[2]/div[2]/ul/li[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']//input[@placeholder='businesses, category']").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']//input[@placeholder='businesses, category']").send_keys("SOLAR")
        time.sleep(2)
        self.driver.find_element(By.ID, "downshift-2-item-0").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']//input[@name='find_loc']").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']//input[@name='find_loc']").send_keys("MIAMI")
        time.sleep(2)
        self.driver.find_element(By.ID, "downshift-3-item-0").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']//button[@type='submit' and text()='Search']").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']/div/div[3]/div/div[1]/div[1]/section/form/details[1]/summary").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//main[@id='content']//input[@id='default']").get_native_element())
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//main[@id='content']/div/div[3]/div/div[1]/div[1]/section/form/details[2]/summary").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.ID, "distance-10").get_native_element())
        self.driver.find_element(By.XPATH, "//main[@id='content']/div/div[3]/div/div[1]/div[1]/section/form/details[4]/summary").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.ID, "C").get_native_element())
        self.driver.find_element(By.XPATH, "//main[@id='content']/div/div[3]/div/div[1]/div[2]/div[4]/div/div[2]/a").click()
    