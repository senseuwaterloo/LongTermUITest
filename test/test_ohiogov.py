import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab_and_close_old


@pytest.mark.usefixtures("driver_session")
class TestOhioGov:
    def test_ohiogov_77269ea5(self):
        self.driver.get("https://ohio.gov/")
        self.driver.find_element(By.XPATH, "//nav[@id='main-nav-container']/ul[1]/li[3]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/section[1]/div[2]/div[1]/div[2]/div[2]/a[1]/div[2]/h3[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[2]/aside[1]/section[1]/div[1]/a[1]/span[1]").click()

        switch_to_new_tab_and_close_old(self.driver)

        self.driver.find_element(By.XPATH, "//span[contains(text(),'Search for Child Care')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Search for Child Care']").click()
        switch_to_new_tab_and_close_old(self.driver)

        country_dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_ddlCounty")
        country_select = Select(country_dropdown)
        country_select.select_by_visible_text("Clinton")

        step_up_dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_ddlRating")
        step_up_select = Select(step_up_dropdown)
        step_up_select.select_by_visible_text("ANY")

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtCity").clear()
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtCity").send_keys("Midland")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_chkSaturday").click()
        self.driver.find_element(By.ID, "ContentPlaceHolder1_chkSixNoon").click()
        self.driver.find_element(By.ID, "ContentPlaceHolder1_chkTransportation").click()
        self.driver.find_element(By.XPATH, "//div[@id='formActions']/a[1]/span[1]").click()
