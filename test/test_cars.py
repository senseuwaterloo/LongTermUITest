import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestCars:
    def test_cars_135d86d4(self):
        self.driver.get("https://www.cars.com/")

        car_search_form_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#panel-19 > cars-search-form")
        spark_select_button = car_search_form_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "form > spark-fieldset > spark-select:nth-child(2)")
        spark_select_button.click()
        make_select_dropdown = spark_select_button.shadow_root.find_element(By.ID, "input")
        make_select = Select(make_select_dropdown)
        make_select.select_by_value('bmw')
        car_search_form_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "form > spark-fieldset > hubcap-button").click()

        stock_type_dropdown = self.driver.find_element(By.ID, "stock-type-select")
        stock_select = Select(stock_type_dropdown)
        stock_select.select_by_value('used')

        min_price_dropdown = self.driver.find_element(By.ID, "price_list_price_min_select")
        min_price_select = Select(min_price_dropdown)
        min_price_select.select_by_value('25000')
        max_price_dropdown = self.driver.find_element(By.ID, "price_list_price_max_select")
        max_price_select = Select(max_price_dropdown)
        max_price_select.select_by_value('50000')

        min_year_dropdown = self.driver.find_element(By.ID, "year_year_min_select")
        min_year_select = Select(min_year_dropdown)
        min_year_select.select_by_value('2005')
        max_year_dropdown = self.driver.find_element(By.ID, "year_year_max_select")
        max_year_select = Select(max_year_dropdown)
        max_year_select.select_by_value('2015')

        mileage_dropdown = self.driver.find_element(By.ID, "mileage-select")
        mileage_select = Select(mileage_dropdown)
        mileage_select.select_by_value('50000')

        trigger_cylinders = self.driver.find_element(By.ID, "trigger_cylinders")
        scroll_to_element(self.driver, trigger_cylinders)
        trigger_cylinders.click()
        self.driver.find_element(By.XPATH, "//label[@for='cylinders_8']").click()

        sort_dropdown = self.driver.find_element(By.ID, "sort-dropdown")
        sort_select = Select(sort_dropdown)
        sort_select.select_by_value('list_price')
    