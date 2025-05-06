import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestDmvVirginiaGov:
    def test_dmvvirginiagov_7752731f(self):
        self.driver.get("https://www.dmv.virginia.gov/")

        self.driver.find_element(By.XPATH, "//body[@id='top']/div[3]/div/header/div[2]/div/div/div/a").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[3]/div/div[1]/div/div/div[1]/div/a").click()

        self.driver.find_element(By.XPATH, "//button[@data-id='CALENDAR']").click()

        self.driver.find_element(By.XPATH, "//button[@data-id='5']").click()

        self.driver.find_element(By.XPATH, "//button[@data-id='38']").click()

        self.driver.find_element(By.XPATH, "//button[@data-latitude='36.7176']").click()

        self.driver.find_element(By.XPATH, "//a[@aria-label='Go to next page of dates available']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@aria-label='Select a time']/div[5]/div[2]/div[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@aria-label='Select a time']/div[5]/div[2]/div[2]/div[2]").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @class='next-button-alt']").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_0__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_0__Value").send_keys("James")
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_1__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_1__Value").send_keys("Smith")
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_2__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_2__Value").send_keys("5145778593")
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_3__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_3__Value").send_keys("abac@abc.com")
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").send_keys("abac@abc.com")
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").click()
        self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").send_keys("abac@abc.com")
        self.driver.find_element(By.XPATH, "//main[@id='maincontent']/form/div[3]/div[2]/button").click()
