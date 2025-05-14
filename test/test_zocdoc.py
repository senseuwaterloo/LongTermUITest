import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from browser_helper import get_control_key


@pytest.mark.usefixtures("driver_session")
class TestZocdoc:
    def test_zocdoc_73178018(self):
        self.driver.get("https://zocdoc.com")

        self.driver.find_element(By.XPATH, "//input[@name='patient-powered-search-input' and @value='' and @type='text' and @placeholder='Condition, procedure, doctor...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='patient-powered-search-input' and @value='' and @type='text' and @placeholder='Condition, procedure, doctor...']").send_keys("chi")

        self.driver.find_element(By.XPATH, "//div[@data-test='combined-specialty-procedure-item-0']").click()

        self.driver.find_element(By.ID, "location-picker-input").send_keys(get_control_key() + "a")
        self.driver.find_element(By.ID, "location-picker-input").send_keys(Keys.DELETE)
        self.driver.find_element(By.NAME, "location-picker-input").send_keys("new york")
        self.driver.find_element(By.XPATH, "//div[@data-test='location-picker-option-0']").click()

        self.driver.find_element(By.XPATH, "//button[@data-test='search-bar-search-button' and @title='Search for doctors']").click()

        self.driver.find_element(By.XPATH, "//div[@data-test='search-filters-availability-facet' and @role='button']").click()
        self.driver.find_element(By.XPATH, "//label[@for='radio-timeframe2' and @data-test='radio-button-label']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='availability-picker-dropdown-done']").click()

        self.driver.find_element(By.XPATH, "//p[@data-test='selected-insurance-state-name-v2']").click()
        self.driver.find_element(By.XPATH, "//div[@data-test='insurance-picker-row-v2-all-carrier-883']").click()
        self.driver.find_element(By.XPATH, "//div[@data-test='insurance-picker-row-v2-all-plan-8651']").click()

        self.driver.find_element(By.XPATH, "//div[@data-test='facet-chip-button' and text()='In-person/video']").click()
        self.driver.find_element(By.ID, "in_person").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='overlay-primary-button']").click()

        self.driver.find_element(By.XPATH, "//div[@data-test='facet-chip-button' and text()='Distance']").click()
        self.driver.find_element(By.ID, "to_5_mile").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='overlay-primary-button']").click()

        self.driver.find_element(By.XPATH, "//div[@data-test='facet-chip-button' and text()='More filters']").click()
        self.driver.find_element(By.XPATH, "//label[@for='male']").click()
        self.driver.find_element(By.XPATH, "//div[./div[text()='Languages spoken']]//button[text()='See more']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Gujarati']").click()

        self.driver.find_element(By.XPATH, "//button[@data-test='overlay-primary-button']").click()
