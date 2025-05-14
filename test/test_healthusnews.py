import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("driver_session")
class TestHealthUsnews:
    def test_healthusnews_de3a4315(self):
        self.driver.get("https://health.usnews.com")

        self.driver.find_element(By.XPATH, "//a[text()='Doctors' and @data-tracking-id='top_nav']").click()

        geriatric_medicine_link = self.driver.find_element(By.XPATH, "//a[text()='Geriatric Medicine']")

        scroll_to_element(self.driver, geriatric_medicine_link)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cardiology')]").click()

        self.driver.find_element(By.XPATH, "//input[@name='location' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='location' and @type='text']").send_keys("Houston, TX")

        self.driver.find_element(By.ID, "react-autowhatever-1--item-0").click()

        self.driver.find_element(By.XPATH, "//button[@data-tracking-id='search_button']").click()

        self.driver.find_element(By.XPATH, "//span[text()='More Filters']").click()

        doctor_gender_dropdown = self.driver.find_element(By.XPATH, "//fieldset[legend[text()='Physician Gender']]//select")
        doctor_gender_select = Select(doctor_gender_dropdown)
        doctor_gender_select.select_by_value('female')

        self.driver.find_element(By.XPATH, "//button[@type='submit' and @data-tracking-id='doctors_internal']").click()
    