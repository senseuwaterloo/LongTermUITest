import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestNpsGov:
    def test_npsgov_0db002f6(self):
        self.driver.get("https://www.nps.gov/")
        self.driver.find_element(By.XPATH, "//button[@id='GlobalNav-toggle']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Passes')]").click()

        annual_pass_link = self.driver.find_element(By.XPATH, "//a[@href='https://store.usgs.gov/pass']")
        scroll_to_element(self.driver, annual_pass_link)
        annual_pass_link.click()

        overview_annual_pas_link = self.driver.find_element(By.XPATH, "//button[text()='Overview of the Annual Pass']")
        scroll_to_element(self.driver, overview_annual_pas_link)
        overview_annual_pas_link.click()

        internet_question_btn = self.driver.find_element(By.XPATH, "//button[text()='Annual Pass Internet Order Questions']")
        scroll_to_element(self.driver, internet_question_btn)
        internet_question_btn.click()

        pass_use_btn = self.driver.find_element(By.XPATH, "//button[text()='Annual Pass Use']")
        scroll_to_element(self.driver, pass_use_btn)
        pass_use_btn.click()

        further_info_btn = self.driver.find_element(By.XPATH, "//button[text()='Annual Pass - Further Information']")
        scroll_to_element(self.driver, further_info_btn)
        further_info_btn.click()
