import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestEpicurious:
    def test_epicurious_d7fb2a4f(self):
        self.driver.get("https://epicurious.com")
        self.driver.find_element(By.ID, "search-form-text-field-q").click()

        self.driver.find_element(By.ID, "search-form-text-field-q").clear()
        self.driver.find_element(By.ID, "search-form-text-field-q").send_keys("CURRY")

        self.driver.find_element(By.ID, "search-form-text-field-q").send_keys(Keys.RETURN)

        self.driver.find_element(By.XPATH, "//div[contains(@id, 'react-select-') and contains(@id, '-placeholder') and text()='Popular']").click()

        self.driver.find_element(By.ID, "react-select-2-option-5").click() # somehow clicking the label element in the div is not working
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'react-select-') and contains(@id, '-placeholder') and text()='Cuisines & Flavors']").click()

        self.driver.find_element(By.ID, "react-select-4-option-7").click()

        self.driver.find_element(By.XPATH, "//div[@id='0-Recipes']/div[2]/section/div/div/div/div[1]/div[1]/div[1]/span").click()
