import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_down


@pytest.mark.usefixtures("setup_class")
class TestKbb:
    def test_kbb_d3a4e6c3(self):
        # self.driver.get("https://kbb.com")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Car Values')]").click()
        # not sure why I changed this
        self.driver.find_element(By.XPATH, "//div/a[contains(text(),'Car Values')]").click()

        # add extra step to handle popup
        time.sleep(3)
        if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']") is not None:
            self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        scroll_down(self.driver, 500)

        # self.driver.find_element(By.XPATH, "//a[contains(text(),\"My Car's Value\")]").click()
        self.driver.find_element(By.XPATH, "//div[text()=\"My Car's Value\"]").click()

        # the following step is redundant
        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[2]/div[1]/div[1]/div[1]").click()

        # self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").clear()
        # self.driver.find_element(By.XPATH, "//select[@placeholder='Year']").select("2016")
        # self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").clear()
        # self.driver.find_element(By.XPATH, "//select[@placeholder='Make']").select("Toyota")
        # self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").clear()
        # self.driver.find_element(By.XPATH, "//select[@placeholder='Model']").select("Camry")
        # self.driver.find_element(By.XPATH, "//input[@value='' and @type='tel' and @placeholder=' ']").clear()
        # self.driver.find_element(By.XPATH, "//input[@value='' and @type='tel' and @placeholder=' ']").send_keys("40000")
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

        # extra steps to input postal code
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'zipcode') and @type='tel' and ./ancestor::label[1]/preceding-sibling::label]").clear()
        self.driver.find_element(By.XPATH, "//input[contains(@class, 'zipcode') and @type='tel' and ./ancestor::label[1]/preceding-sibling::label]").send_keys("07055")

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='vehicle_picker_submit_button' and not(@disabled)]").click()

        # add extra step to handle popup
        time.sleep(3)
        if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']") is not None:
            self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        scroll_down(self.driver, 500)

        self.driver.find_element(By.XPATH, "//div[@id='box-style']/div[4]/label[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()

        # add extra step to handle popup
        # time.sleep(3)
        # if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']"):
        #     self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        scroll_down(self.driver, 500)

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Select Your Options']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/div[1]").click()
        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//img[@alt='Black image']").click()

        # add extra step
        self.driver.find_element(By.XPATH, "//div[text()='Selling my car']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//button[@data-lean-auto='optionsNextButton']").click()

        # add extra step to handle popup
        # time.sleep(3)
        # if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']"):
        #     self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        # scroll_down(self.driver, 500)

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/label[2]/span[3]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-lean-auto='next-btn']").click()

        # add extra step to handle popup
        # time.sleep(3)
        # if self.driver.find_element(By.XPATH, "//button[text()='No Thanks']"):
        #     self.driver.find_element(By.XPATH, "//button[text()='No Thanks']").click()
        scroll_down(self.driver, 500)

        # self.driver.find_element(By.XPATH, "//div[@id='BodyDivFlex']/div[2]/div[1]/ol[1]/li[1]/div[1]").click()
        # self.driver.find_element(By.ID, "license-plate-entry").clear()
        # self.driver.find_element(By.ID, "license-plate-entry").send_keys("AZXA46")
        # self.driver.find_element(By.ID, "state-entry").clear()
        # self.driver.find_element(By.ID, "state-entry").select("AZ")
        # self.driver.find_element(By.XPATH, "//div[@id='BodyDivFlex']/div[2]/div[1]/div[3]/div[3]/button[1]").click()
        # page logic changed
        self.driver.find_element(By.XPATH, "//div[text()='Has repairable cosmetic defects and mechanical problems']").click()
        self.driver.find_element(By.XPATH, "//button[@data-lean-auto='conditionNextButton']").click()
