import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_down


@pytest.mark.usefixtures("driver_session")
class TestKbb:
    def test_kbb_d3a4e6c3(self):
        self.driver.get("https://kbb.com")

        self.driver.find_element(By.XPATH, "//div/a[contains(text(),'Car Values')]").click()

        time.sleep(3)
        # if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']") is not None:
        #     self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        scroll_down(self.driver, 500)

        self.driver.find_element(By.XPATH, "//div[text()=\"My Car's Value\"]").click()

        year_dropdown = self.driver.find_element(By.XPATH, "//select[@aria-label='Year' and @placeholder='Year' and not(.//option[@value='2027'])]")
        year_select = Select(year_dropdown)
        year_select.select_by_visible_text('2016')
        make_dropdown = self.driver.find_element(By.XPATH, "//select[@aria-label='Make' and @placeholder='Make' and .//option[@value='Acura']]")
        make_select = Select(make_dropdown)
        make_select.select_by_value('Toyota')
        model_dropdown = self.driver.find_element(By.XPATH, "//select[@aria-label='Model' and @placeholder='Model' and .//option[@value='Camry']]")
        model_select = Select(model_dropdown)
        model_select.select_by_value('Camry')
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'mileage') and @type='tel']").clear()
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'mileage') and @type='tel']").send_keys("40000")

        self.driver.find_element(By.XPATH, "//input[contains(@class, 'zipcode') and @type='tel' and ./ancestor::label[1]/preceding-sibling::label]").clear()
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'zipcode') and @type='tel' and ./ancestor::label[1]/preceding-sibling::label]").send_keys("07055")

        self.driver.find_element(By.XPATH, "//button[@data-testid='vehicle_picker_submit_button' and not(@disabled)]").click()

        time.sleep(3)
        # if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']") is not None:
        #     self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        scroll_down(self.driver, 500)

        self.driver.find_element(By.XPATH, "//div[@id='box-style']/div[4]/label[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()

        scroll_down(self.driver, 500)

        self.driver.find_element(By.XPATH, "//div[text()='Select Your Options']").click()

        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//img[@alt='Black image']").click()

        self.driver.find_element(By.XPATH, "//div[text()='Selling my car']").click()

        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//button[@data-lean-auto='optionsNextButton']").click()

        self.driver.find_element(By.XPATH, "//button[@data-lean-auto='next-btn']").click()

        scroll_down(self.driver, 500)

        self.driver.find_element(By.XPATH, "//div[text()='Has repairable cosmetic defects and mechanical problems']").click()
        self.driver.find_element(By.XPATH, "//button[@data-lean-auto='conditionNextButton']").click()
