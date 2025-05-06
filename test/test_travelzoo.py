import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestTravelzoo:
    def test_travelzoo_b770af80(self):
        self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()

        self.driver.find_element(By.XPATH, "//div[contains(@id, 'ui-id-') and text()='Hotels']").click()

        self.driver.find_element(By.XPATH, "//div[contains(@id, 'ui-id-') and text()='Anywhere']").click()

        self.driver.find_element(By.ID, "when-field-1").click()

        self.driver.find_element(By.XPATH, "//h3[contains(@id, 'ui-id-') and text()='Select a Month']").click()

        self.driver.find_element(By.XPATH, "//li[@data-date-type='SpecificMonth' and @data-month='5' and text()='May']").click()

        guest_number_dropdown = self.driver.find_element(By.ID, "guests-field-1")
        guest_number_select = Select(guest_number_dropdown)
        guest_number_select.select_by_value("1")

        self.driver.find_element(By.ID, "search-button-1").click()
        self.driver.find_element(By.ID, "refine-search-toggle").click()

        self.driver.find_element(By.XPATH, "//button[@type='button' and (text()='Pet-Friendly' or text()='Pet-friendly')]").click()

        self.driver.find_element(By.XPATH, "//button[@type='button' and (text()='Last-Minute' or text()='Last Minute')]").click()

        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[3]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@class='result-group-content']/ul[1]/li[2]//h2[@class='deal-headline']").click()
