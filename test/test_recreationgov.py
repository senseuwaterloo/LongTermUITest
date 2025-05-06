import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_full_month_name


@pytest.mark.usefixtures("setup_class")
class TestRecreationGov:
    def test_recreationgov_986bfa5e(self):
        self.driver.get("https://www.recreation.gov/")

        self.driver.find_element(By.ID, "tabs-button-1").click()

        self.driver.find_element(By.ID, "hero-camping-search-input").clear()
        self.driver.find_element(By.ID, "hero-camping-search-input").send_keys("Illinois")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hero-camping-search-input-section-1-item-0']/div[1]/div[2]/span[1]").click()

        self.driver.find_element(By.XPATH, "//button[@id='homepage-search-options']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='homepage-search-options-popup']/div[1]/div[2]/div[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//button[@data-component='Button' and @type='button' and @role='combobox' and @aria-haspopup='dialog']").click()

        start_date_str, end_date_str = calculate_dates_full_month_name(14, 17)
        self.driver.find_element(By.XPATH, f"//div[contains(@aria-label, '{start_date_str}')]").click()
        self.driver.find_element(By.XPATH, f"//div[contains(@aria-label, '{end_date_str}')]").click()
        self.driver.find_element(By.ID, "calendar-button-handler").click()

        self.driver.find_element(By.XPATH, "//div[@id='tabs-panel-1']/div[1]/button[1]").click()

        sort_dropdown = self.driver.find_element(By.ID, "search-sort-dropdown")
        sort_select = Select(sort_dropdown)
        sort_select.select_by_value("price asc")
