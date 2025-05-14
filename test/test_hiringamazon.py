import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import switch_to_new_tab_and_close_old


@pytest.mark.usefixtures("driver_session")
class TestHiringAmazon:
    def test_hiringamazon_7b56daf2(self):
        self.driver.get("https://hiring.amazon.com")

        self.driver.find_element(By.XPATH, "//div[@data-test-component='StencilText' and text()='Job Opportunities']").click()

        self.driver.find_element(By.XPATH, "//div[@data-test-component='StencilText' and text()='DSP Delivery Driver']").click()

        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply with a Delivery Service Partner')]").get_native_element())

        switch_to_new_tab_and_close_old(self.driver)

        self.driver.find_element(By.XPATH, "//div[text()='Accept All']").click()

        self.driver.find_element(By.ID, "address").clear()

        self.driver.find_element(By.ID, "address").send_keys("New York")

        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[text()='New York, NY']").get_native_element())

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()

        switch_to_new_tab_and_close_old(self.driver)

        self.driver.find_element(By.ID, "firstname").clear()
        self.driver.find_element(By.ID, "firstname").send_keys("Nelson")
        self.driver.find_element(By.ID, "lastname").clear()
        self.driver.find_element(By.ID, "lastname").send_keys("Freeman")
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys("Nelsonfree@gmail.com")

        self.driver.find_element(By.ID, "phone").clear()
        self.driver.find_element(By.ID, "phone").send_keys("2034556656")

        self.driver.find_element(By.XPATH, "//div[@id='is_21_or_older']/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='has_valid_drivers_license']/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='us_emplyment_auth']/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'I agree to allow my phone number to be used for calls or texts regarding my application')]").click()

        self.driver.find_element(By.XPATH, "//span[text()='Continue']").click()
    