import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import switch_to_new_tab_and_close_old


@pytest.mark.usefixtures("setup_class")
class TestHiringAmazon:
    def test_hiringamazon_7b56daf2(self):
        # self.driver.get("https://hiring.amazon.com")

        # self.driver.find_element(By.XPATH, "//div[@role='button']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        # logic changed, no first step
        self.driver.find_element(By.XPATH, "//div[@data-test-component='StencilText' and text()='Job Opportunities']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='stencil-flyout-body']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-component='StencilText' and text()='DSP Delivery Driver']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply with an Amazon Delivery Service Partner')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply with a Delivery Service Partner')]").click()
        # somehow the typical selenium click is not working for this element
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply with a Delivery Service Partner')]").get_native_element())
        # need to switch to a new tab
        switch_to_new_tab_and_close_old(self.driver)

        # self.driver.find_element(By.XPATH, "//div[contains(.,'Accept All')]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Accept All']").click()

        self.driver.find_element(By.ID, "address").clear()
        # self.driver.find_element(By.ID, "address").send_keys("Grand Rapids")
        self.driver.find_element(By.ID, "address").send_keys("New York")

        # make the locator more specific and also since now there is no jobs around the given address we need to set the address to New York where there are more jobs
        # self.driver.find_element(By.XPATH, "//div[contains(.,'Grand Rapids, MI')]").click()
        # self.driver.find_element(By.XPATH, "//div[text()='New York, NY']").click()
        # somehow the typical selenium click is not working for this element
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[text()='New York, NY']").get_native_element())

        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        # need to switch to a new tab again
        switch_to_new_tab_and_close_old(self.driver)

        # self.driver.find_element(By.ID, "application_form_first_name").clear()
        # self.driver.find_element(By.ID, "application_form_first_name").send_keys("Nelson")
        # self.driver.find_element(By.ID, "application_form_last_name").clear()
        # self.driver.find_element(By.ID, "application_form_last_name").send_keys("Freeman")
        # self.driver.find_element(By.ID, "application_form_email").clear()
        # self.driver.find_element(By.ID, "application_form_email").send_keys("Nelsonfree@gmail.com")
        self.driver.find_element(By.ID, "firstname").clear()
        self.driver.find_element(By.ID, "firstname").send_keys("Nelson")
        self.driver.find_element(By.ID, "lastname").clear()
        self.driver.find_element(By.ID, "lastname").send_keys("Freeman")
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys("Nelsonfree@gmail.com")

        self.driver.find_element(By.ID, "phone").clear()
        self.driver.find_element(By.ID, "phone").send_keys("2034556656")

        # self.driver.find_element(By.XPATH, "/html/body[1]/article[1]/div[1]/form[1]/div[1]/fieldset[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/article[1]/div[1]/form[1]/div[1]/fieldset[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/article[1]/div[1]/form[1]/div[1]/fieldset[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/article[1]/div[1]/form[1]/div[1]/fieldset[2]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='is_21_or_older']/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='has_valid_drivers_license']/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='us_emplyment_auth']/label[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'I agree to allow my phone number to be used for calls or texts regarding my application')]").click()

        # self.driver.find_element(By.ID, "applicationFormSubmitButton").click()
        self.driver.find_element(By.XPATH, "//span[text()='Continue']").click()
    