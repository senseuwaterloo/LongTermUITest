import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestApartments:
    def test_apartments_e034b288(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "quickSearchLookup").click()
        self.driver.find_element(By.ID, "quickSearchLookup").send_keys("nyc")
        self.driver.find_element(By.XPATH, "//li[contains(@id, 'quickSearchLookup_typeahead') and text()='New York, NY']").click()
        self.driver.find_element(By.ID, "rentRangeLink").click()
        self.driver.find_element(By.ID, "min-input").clear()
        self.driver.find_element(By.ID, "min-input").send_keys("1500")
        self.driver.find_element(By.ID, "max-input").clear()
        self.driver.find_element(By.ID, "max-input").send_keys("2500")
        self.driver.find_element(By.XPATH, "//a[@id='bedRangeLink']/span[2]/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='bedsMinMaxRangeControl']/div/div/div/div[1]/div/button[5]").click()
        self.driver.find_element(By.XPATH, "//*[@id='bedsMinMaxRangeControl']/div/div/div/div[2]/div/button[3]").click()
        self.driver.find_element(By.XPATH, "//a[@id='typeSelect']/span[3]/i[1]").click()
        self.driver.find_element(By.ID, "PropertyType-4").click()
    