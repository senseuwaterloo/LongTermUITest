import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestDmvVirginiaGov:
    def test_dmvvirginiagov_7752731f(self):
        # self.driver.get("https://www.dmv.virginia.gov/")
        # navigation logic and page layout changed
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Make an Appointment')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Book or Cancel Your Appointment')]").click()
        # self.driver.find_element(By.ID, "apptLink").click()
        # self.driver.find_element(By.XPATH, "//div[@id='5611b18f-4c1b-42b2-86c6-d0bd8358c476']/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='a2777b13-6fb2-4f42-af90-c4f6ae2a72a2']/div[1]/div[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='36e4a071-79fa-4483-8b73-3499f0e9633c']/div[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='e4e8d106-ccfb-4c66-ac7b-39bc56c107d9']/div[1]/div[1]/div[1]/div[2]").click()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_0__Value").clear()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_0__Value").send_keys("James")
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_1__Value").clear()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_1__Value").send_keys("Smith")
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_2__Value").clear()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_2__Value").send_keys("abac@abc.com")
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_3__Value").clear()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_3__Value").send_keys("abac@abc.com")
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").click()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").clear()
        # self.driver.find_element(By.ID, "StepControls_2__Model_Value_Properties_4__Value").send_keys("888899778")
        # self.driver.find_element(By.XPATH, "//input[@value='Next' and @type='submit']").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Make an Appointment')]").click()

        self.driver.find_element(By.XPATH, "//body[@id='top']/div[3]/div/header/div[2]/div/div/div/a").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div[3]/div/div[1]/div/div/div[1]/div/a").click()
        # can't use relative id xpath since dynamic id will be introduced
        self.driver.find_element(By.XPATH, "//button[@data-id='CALENDAR']").click()
        # can't use relative id xpath since dynamic id will be introduced
        self.driver.find_element(By.XPATH, "//button[@data-id='5']").click()
        # can't use relative id xpath since dynamic id will be introduced
        self.driver.find_element(By.XPATH, "//button[@data-id='38']").click()
        # can't use relative id xpath since dynamic id will be introduced
        self.driver.find_element(By.XPATH, "//button[@data-latitude='36.7176']").click()

        self.driver.find_element(By.XPATH, "//a[@aria-label='Go to next page of dates available']").click()
        # need to wait some time otherwise the list will be closed
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@aria-label='Select a time']/div[5]/div[2]/div[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@aria-label='Select a time']/div[5]/div[2]/div[2]/div[2]").click()
        # sleep to avoid: Element click intercepted: xpath = //button[@type='submit' and @class='next-button-alt'] - Message: element click intercepted: Element is not clickable at point (1283, 1028)
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
