import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_budget_dates


@pytest.mark.usefixtures("driver_session")
class TestKoa:
    def test_koa_6de5b415(self):
        self.driver.get("https://koa.com")
        self.driver.find_element(By.ID, "txtLocation").clear()
        self.driver.find_element(By.ID, "txtLocation").send_keys("Orlando")

        self.driver.find_element(By.XPATH, "//li[@class='ui-menu-item' and contains(text(), ', FL, USA')]//b[text()='Orlando']").click()

        self.driver.find_element(By.ID, "checkInDate").click()

        (start_date_year, start_date_month_adjusted, start_date_day), (end_date_year, end_date_month_adjusted, end_date_day) = calculate_budget_dates(21, 22)
        self.driver.find_element(By.XPATH, f"//td[@data-month='{start_date_month_adjusted}' and @data-year='{start_date_year}']//a[text()='{start_date_day}']").click()

        self.driver.find_element(By.ID, "checkOutDate").click()

        self.driver.find_element(By.XPATH, f"//td[@data-month='{end_date_month_adjusted}' and @data-year='{end_date_year}']//a[text()='{end_date_day}']").click()

        self.driver.find_element(By.ID, "btnBasicSearch").click()

        adults_dropdown = self.driver.find_element(By.ID, "Adults")
        adults_select = Select(adults_dropdown)
        adults_select.select_by_visible_text('2')

        self.driver.find_element(By.ID, "btnApplyFilter").click()
