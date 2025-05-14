import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_slash_format


@pytest.mark.usefixtures("driver_session")
class TestThetrainline:
    def test_thetrainline_5b37d2e1(self):
        self.driver.get("https://www.thetrainline.com/en-us")

        self.driver.find_element(By.ID, "jsf-origin-input").clear()
        self.driver.find_element(By.ID, "jsf-origin-input").send_keys("PARIS")

        self.driver.find_element(By.XPATH, "//ul[@id='jsf-origin-menu']/li[contains(@id, 'jsf-origin-item-') and ./span[text()='Paris'] and ./span[text()='FR']]").click()

        self.driver.find_element(By.ID, "jsf-destination-input").clear()
        self.driver.find_element(By.ID, "jsf-destination-input").send_keys("MILAN")
        self.driver.find_element(By.XPATH, "//ul[@id='jsf-destination-menu']/li[contains(@id, 'jsf-destination-item-') and ./div/span[text()='Milano'] and ./div/span[text()='Milan'] and ./span[text()='IT']]").click()

        self.driver.find_element(By.ID, "jsf-outbound-time-input-toggle").click()
        start_date_str, end_date_str = calculate_dates_slash_format(10, 10)
        if self.driver.find_element(By.XPATH, f"//td[@data-date='{start_date_str}']") is None:
            self.driver.find_element(By.ID, "ChevronRight").click()
        self.driver.find_element(By.XPATH, f"//td[@data-date='{start_date_str}']").click()
        leaving_hour_dropdown = self.driver.find_element(By.ID, "jsf-outbound-time-time-picker-hour")
        leaving_hour_select = Select(leaving_hour_dropdown)
        leaving_hour_select.select_by_value("12")
        leaving_minute_dropdown = self.driver.find_element(By.ID, "jsf-outbound-time-time-picker")
        leaving_minute_select = Select(leaving_minute_dropdown)
        leaving_minute_select.select_by_value("00")

        self.driver.find_element(By.ID, "jsf-passengers-input-toggle").click()
        self.driver.find_element(By.ID, "add-youth-passenger-button").click()
        youth_age_dropdown = self.driver.find_element(By.NAME, "passengers.1.age")
        youth_age_select = Select(youth_age_dropdown)
        youth_age_select.select_by_value("16")

        self.driver.find_element(By.XPATH, "//button[@data-testid='jsf-submit']").click()
