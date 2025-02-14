import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_budget_dates


@pytest.mark.usefixtures("setup_class")
class TestUmichEdu:
    def test_umichedu_bcfeed8e(self):
        # self.driver.get("https://umich.edu")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Life at Michigan')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='life-at-michigan']/div[2]/div[2]/div[1]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Events Calendar']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Events')]").click()
        self.driver.find_element(By.ID, "start-date").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'5')]").click()
        (start_date_year, start_date_month_adjusted, start_date_day), (end_date_year, end_date_month_adjusted, end_date_day) = calculate_budget_dates(2, 9)
        start_date_cell = self.driver.find_element(By.XPATH, f"//td[@data-year='{start_date_year}' and @data-month='{start_date_month_adjusted}']/a[text()='{start_date_day}']")
        if start_date_cell is None:
            self.driver.find_element(By.XPATH, "//a[@title='Next']").click()
        start_date_cell.click()

        self.driver.find_element(By.ID, "end-date").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'12')]").click()
        end_date_cell = self.driver.find_element(By.XPATH, f"//td[@data-year='{end_date_year}' and @data-month='{end_date_month_adjusted}']/a[text()='{end_date_day}']")
        if end_date_cell is None:
            self.driver.find_element(By.XPATH, "//a[@title='Next']").click()
        end_date_cell.click()

        self.driver.find_element(By.XPATH, "//section[@id='content']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Workshop / Seminar')]").click()
        self.driver.find_element(By.ID, "7").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Museum of Art')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Museum of Art']").click()
        time.sleep(1)
