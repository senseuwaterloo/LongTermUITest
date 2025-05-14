import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from browser_helper import calculate_budget_dates, scroll_to_element


@pytest.mark.usefixtures("driver_session")
class TestParking:
    def test_parking_1c0acb0e(self):
        self.driver.get("https://parking.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find your city')]").click()
        self.driver.find_element(By.ID, "state_name").click()
        self.driver.find_element(By.ID, "state_37_item").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Arlington')]").click()

        self.driver.find_element(By.ID, "txtsearch").clear()

        self.driver.find_element(By.ID, "txtsearch").send_keys("5601 Chapin Ave, Alexandria")

        time.sleep(2)
        self.driver.find_element(By.ID, "txtsearch").send_keys(Keys.ENTER)

        time.sleep(2)
        self.driver.find_element(By.ID, "entranceDateFormatted").click()

        (start_date_year, start_date_month_adjusted, start_date_day), (end_date_year, end_date_month_adjusted, end_date_day) = calculate_budget_dates(7, 8)
        if self.driver.find_element(By.XPATH, f"//div[@role='calendar' and not(contains(@style, 'display: none;'))]//td[@year='{start_date_year}' and @month='{start_date_month_adjusted}' and @day='{start_date_day}']") is None:
            self.driver.find_element(By.XPATH, "//div[@role='calendar' and not(contains(@style, 'display: none;'))]//div[@role='navigator']/div[3]/i").click()
        self.driver.find_element(By.XPATH, f"//div[@role='calendar' and not(contains(@style, 'display: none;'))]//td[@year='{start_date_year}' and @month='{start_date_month_adjusted}' and @day='{start_date_day}']").click()

        self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[2]/strong[1]/span[1]").click()

        start_time_ele = self.driver.find_element(By.XPATH, "//strong[@data-toggle='dropdown' and @aria-expanded='true']//a[contains(text(),'10:00AM')]")
        scroll_to_element(self.driver, start_time_ele)
        start_time_ele.click()

        self.driver.find_element(By.ID, "exitDateFormatted").click()

        if self.driver.find_element(By.XPATH, f"//div[@role='calendar' and not(contains(@style, 'display: none;'))]//td[@year='{end_date_year}' and @month='{end_date_month_adjusted}' and @day='{end_date_day}']") is None:
            self.driver.find_element(By.XPATH, "//div[@role='calendar' and not(contains(@style, 'display: none;'))]//div[@role='navigator']/div[3]/i").click()
        self.driver.find_element(By.XPATH, f"//div[@role='calendar' and not(contains(@style, 'display: none;'))]//td[@year='{end_date_year}' and @month='{end_date_month_adjusted}' and @day='{end_date_day}']").click()

        self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[7]/strong[1]/span[1]").click()

        end_time_ele = self.driver.find_element(By.XPATH, "//strong[@data-toggle='dropdown' and @aria-expanded='true']//a[contains(text(),'10:00AM')]")
        scroll_to_element(self.driver, end_time_ele)
        end_time_ele.click()

        self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[9]/button[1]").click()

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/strong[1]").click()

        self.driver.find_element(By.ID, "filter_category_general_3").click()
        self.driver.find_element(By.ID, "filter_category_general_7").click()
        self.driver.find_element(By.ID, "filter_category_facility_2").click()
        self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div/span[2]/div/div[2]/ul/li[2]/div/div[1]/div[2]/a").click()
