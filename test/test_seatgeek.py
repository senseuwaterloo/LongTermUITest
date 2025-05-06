import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_first_last_dates, scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestSeatgeek:
    def test_seatgeek_8f6261cf(self):
        self.driver.get("https://seatgeek.com")

        change_location_button = self.driver.find_element(By.XPATH, "//span[contains(.,'Change Location')]/parent::button")
        scroll_to_element(self.driver, change_location_button)
        change_location_button.click()

        self.driver.find_element(By.ID, "downshift-0-input").clear()
        [self.driver.find_element(By.ID, "downshift-0-input").send_keys(each_char) for each_char in "New York"]

        self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/p[1]").click()

        self.driver.find_element(By.XPATH, "//button[@data-testid='date-filter-button']").click()

        start_date_str, end_date_str = calculate_first_last_dates()
        self.driver.find_element(By.XPATH, f"//div[@data-testid='{start_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//div[@data-testid='{end_date_str}']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='date-filter-apply-button']").click()
