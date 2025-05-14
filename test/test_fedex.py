import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab


@pytest.mark.usefixtures("driver_session")
class TestFedex:
    def test_fedex_27437134(self):
        self.driver.get("https://www.fedex.com/en-us/home.html")
        time.sleep(6)
        self.driver.find_element(By.XPATH, "//span[contains(.,'Shipping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shipping Rates & Delivery Times')]").click()

        self.driver.find_element(By.CSS_SELECTOR, "#e2e-appBar > nav > div > fdx-app-bar-items.left-menu > ul > li > button").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'LTL Rates')]").click()

        switch_to_new_tab(self.driver)

        self.driver.find_element(By.ID, "fromAddress").clear()
        self.driver.find_element(By.ID, "fromAddress").send_keys("Chicago")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]").click()
        self.driver.find_element(By.ID, "toAddress").clear()
        self.driver.find_element(By.ID, "toAddress").send_keys("Kansas")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]").click()

        handling_unit_type_dropdown = self.driver.find_element(By.ID, "uomData_0")
        handling_unit_type_select = Select(handling_unit_type_dropdown)
        handling_unit_type_select.select_by_value('SELFPACKAGE_CARTON')

        self.driver.find_element(By.ID, "weight_0").clear()
        self.driver.find_element(By.ID, "weight_0").send_keys("5000")

        class_type_dropdown = self.driver.find_element(By.ID, "classData_0")
        class_type_select = Select(class_type_dropdown)
        class_type_select.select_by_value('CLASS_050')

        self.driver.find_element(By.ID, "number_0").clear()
        self.driver.find_element(By.ID, "number_0").send_keys("2")

        self.driver.find_element(By.ID, "declaredValue").click()
        self.driver.find_element(By.ID, "declaredValue").clear()
        self.driver.find_element(By.ID, "declaredValue").send_keys("20000")

        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form/fieldset/div/div[2]/div[3]/app-addtional-services/form/div[5]/div/div[1]/div/button").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form/fieldset/div/div[2]/div[3]/app-addtional-services/form/div[5]/div/div[1]/div[2]/div[3]/label").click()

        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form/fieldset/div/div[2]/div[3]/app-addtional-services/form/div[5]/div/div[2]/div/button").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form/fieldset/div/div[2]/div[3]/app-addtional-services/form/div[5]/div/div[2]/div[2]/div[4]/label").click()

        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form/fieldset/div/div[2]/div[3]/app-addtional-services/form/div[5]/div/div[3]/div/button").click()
        self.driver.find_element(By.XPATH, "//div[@id='main-container']/form/fieldset/div/div[2]/div[3]/app-addtional-services/form/div[5]/div/div[3]/div[2]/div[5]/label").click()

        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
