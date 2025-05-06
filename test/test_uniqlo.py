import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestUniqlo:
    def test_uniqlo_122178b3(self):
        self.driver.get("https://www.uniqlo.com/us/en/")

        self.driver.find_element(By.XPATH, "//div[@role='button' and contains(@class, 'fr-ec-bottom-navigation__icon-wrapper-center')]").click()

        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by keyword']").click()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by keyword']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by keyword']").send_keys("blazer")

        self.driver.find_element(By.XPATH, "//mark[text()='blazer' and not(following-sibling::*) and not(preceding-sibling::*)]").click()

        self.driver.find_element(By.XPATH, "//h4[@title='Gender > Category']").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@role='option' and @value='22211']").click()

        self.driver.find_element(By.XPATH, "//button[contains(@class, 'fr-ec-utility-bar__modal__close-icon')]/div[1]").click()

        self.driver.find_element(By.XPATH, "//h4[@title='Color']").click()

        self.driver.find_element(By.XPATH, "//section//fieldset[@id='colorFilterCheckBox']/div[1]/div[2]/div[1]/label[1]/span[1]").click()

        self.driver.find_element(By.XPATH, "//button[contains(@class, 'fr-ec-utility-bar__modal__close-icon')]/div[1]").click()

        self.driver.find_element(By.XPATH, "//h4[@title='Size']").click()
        self.driver.find_element(By.XPATH, "//section//label[@for='check-L']").click()
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'fr-ec-utility-bar__modal__close-icon')]/div[1]").click()

        time.sleep(6)
