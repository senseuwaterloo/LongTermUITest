import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_weekday_format


@pytest.mark.usefixtures("driver_session")
class TestExpedia:
    def test_expedia_97e3f951(self):
        self.driver.get("https://expedia.com")
        self.driver.find_element(By.XPATH, "//div[@id='multi-product-search-form-1']/div/div/div/div/div[1]/ul/li[2]/a/span").click()

        self.driver.find_element(By.XPATH, "//div[@id='search_form_product_selector_flights']/div/div/div[1]/div/div[1]/div/ul/li[2]/a/span").click()

        self.driver.find_element(By.XPATH, "//div[@id='FlightSearchForm_ONE_WAY']/div/div[3]/div/div[1]/button").click()

        self.driver.find_element(By.XPATH, "//div[@id='FlightSearchForm_ONE_WAY']/div/div[3]/div/div[2]/div/div/section/div[1]/div/div/button[2]").click()

        self.driver.find_element(By.XPATH, "//div[@id='FlightSearchForm_ONE_WAY']/div/div[3]/div/div[2]/div/div/section/div[2]/div[1]/div/button[2]").click()

        self.driver.find_element(By.XPATH, "//div[@id='FlightSearchForm_ONE_WAY']/div/div[3]/div/div[2]/div/div/section/div[3]/div[1]/div/button[2]").click()

        child_age_dropdown = self.driver.find_element(By.ID, "age-traveler_selector_children_age_selector-0")
        child_age_select = Select(child_age_dropdown)
        child_age_select.select_by_value('4')

        infant_age_dropdown = self.driver.find_element(By.ID, "age-traveler_selector_infant_age_selector-0")
        infant_age_select = Select(infant_age_dropdown)
        infant_age_select.select_by_value('0')

        self.driver.find_element(By.ID, "travelers_selector_done_button").click()

        self.driver.find_element(By.ID, "cabin_class").click()

        self.driver.find_element(By.XPATH, "//div[@id='cabin_class_menu']/div/div/button[4]").click()

        self.driver.find_element(By.XPATH, "//div[@id='FlightSearchForm_ONE_WAY']/div/div[2]/div/div/div/div/button").click()

        start_date_str, end_date_str = calculate_dates_weekday_format(21, 22)
        self.driver.find_element(By.XPATH, f"//div[@class='uitk-day-aria-label' and @aria-label='{start_date_str}']/parent::div").click()

        self.driver.find_element(By.XPATH, "//div[@id='FlightSearchForm_ONE_WAY']/div/div[2]/div/section/footer/div/button").click()

        self.driver.find_element(By.XPATH, "//button[@data-stid='origin_select-menu-trigger']").click()
        self.driver.find_element(By.ID, "origin_select").send_keys("jfk")
        self.driver.find_element(By.XPATH, "//div[@id='origin_select-menu']/section/div/div[2]/div/ul/div[1]/li/div/div/button").click()

        self.driver.find_element(By.XPATH, "//button[@data-stid='destination_select-menu-trigger']").click()
        self.driver.find_element(By.ID, "destination_select").send_keys("heathrow")
        self.driver.find_element(By.XPATH, "//div[@id='destination_select-menu']/section/div/div[2]/div/ul/div[1]/li/div/div/button").click()

        self.driver.find_element(By.ID, "search_button").click()
