import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates


@pytest.mark.usefixtures("setup_class")
class TestAgoda:
    def test_agoda_e3486ac5(self):
        # self.driver.get("https://agoda.com")

        # Never mind about the following code, just navigate to the home tab to start test
        self.driver.find_element(By.XPATH, "//li[@id='tab-home']/div[1]/div[1]").click()

        # self.driver.find_element(By.ID, "textInput").clear()
        # self.driver.find_element(By.ID, "textInput").send_keys("bali")
        self.driver.find_element(By.ID, "textInput").clear()
        self.driver.find_element(By.ID, "textInput").send_keys("bali")

        # self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[1]/div[2]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[6]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='SearchBoxContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/span[1]").click()
        # data-selenium-date="2024-09-01"
        # change the way to input date and change the locator
        start_date_str, end_date_str = calculate_dates(20, 24)
        self.driver.find_element(By.CSS_SELECTOR, f"span[data-selenium-date='{start_date_str}']").click()
        self.driver.find_element(By.CSS_SELECTOR, f"span[data-selenium-date='{end_date_str}']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[1]/div[2]/div[3]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='occupancy-selector']/div[1]/div[1]/div[2]/div[2]/div[3]/svg[1]").click()
        # 1. relative xpath changed to //div[@id="FocusTrap"]/div/div/div[1]/div[2]/button[2]/svg meaning that the web app is updated, also selenium xpath doesn't work with svg
        self.driver.find_element(By.XPATH, "//button[@data-selenium='plus' and @data-element-name='occupancy-selector-panel-adult']").click()
        self.driver.find_element(By.XPATH, "//button[@data-selenium='plus' and @data-element-name='occupancy-selector-panel-children']").click()
        self.driver.find_element(By.XPATH, "//button[@data-selenium='plus' and @data-element-name='occupancy-selector-panel-children']").click()

        dropdown_element = self.driver.find_element(By.XPATH, "//select[@data-selenium='dropdownInput' and contains(@aria-label, 'Age of Child 1')]")
        select = Select(dropdown_element)
        select.select_by_value('5')
        dropdown_element = self.driver.find_element(By.XPATH, "//select[@data-selenium='dropdownInput' and contains(@aria-label, 'Age of Child 2')]")
        select = Select(dropdown_element)
        select.select_by_value('12')

        self.driver.find_element(By.XPATH, "//*[@data-selenium='occupancyBox']").click()
        self.driver.find_element(By.XPATH, "//button[@data-selenium='searchButton']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Homestay') and @data-selenium='filter-item-text']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Balcony/terrace') and @data-selenium='filter-item-text']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Breakfast included')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Double') and @data-selenium='filter-item-text']").click()
        self.driver.find_element(By.XPATH, "//a[@data-element-name='search-sort-price']").click()
    