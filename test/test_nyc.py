import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_budget_dates


@pytest.mark.usefixtures("setup_class")
class TestNyc:
    def test_nyc_1cc13b4e(self):
        self.driver.get("https://nyc.com")

        self.driver.find_element(By.XPATH, "//div[@class='container' and not(ancestor::footer)]/nav[@class='topnav']/ul[1]//a[text()='hotels.']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Check In']/ancestor::*[1][self::label]").click()

        (start_date_year, start_date_month_adjusted, start_date_day), (end_date_year, end_date_month_adjusted, end_date_day) = calculate_budget_dates(7, 10)
        if self.driver.find_element(By.XPATH, f"//td[@data-year='{start_date_year}' and @data-month='{start_date_month_adjusted}']//a[text()='{start_date_day}']") is None:
            self.driver.find_element(By.XPATH, "//a[@data-handler='next' and @data-event='click' and @title='Next']").click()

        self.driver.find_element(By.XPATH, f"//td[@data-year='{start_date_year}' and @data-month='{start_date_month_adjusted}']//a[text()='{start_date_day}']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Check-Out']/ancestor::*[1][self::label]").click()

        if self.driver.find_element(By.XPATH, f"//td[@data-year='{end_date_year}' and @data-month='{end_date_month_adjusted}']//a[text()='{end_date_day}']") is None:
            self.driver.find_element(By.XPATH, "//a[@data-handler='next' and @data-event='click' and @title='Next']").click()

        self.driver.find_element(By.XPATH, f"//td[@data-year='{end_date_year}' and @data-month='{end_date_month_adjusted}']//a[text()='{end_date_day}']").click()

        room_dropdown = self.driver.find_element(By.NAME, "rooms")
        room_select = Select(room_dropdown)
        room_select.select_by_visible_text("1 Room")

        adult_dropdown = self.driver.find_element(By.NAME, "r1a")
        adult_select = Select(adult_dropdown)
        adult_select.select_by_visible_text("2 Adults")

        child_dropdown = self.driver.find_element(By.NAME, "r1c")
        child_select = Select(child_dropdown)
        child_select.select_by_visible_text("1 Child")

        age_dropdown = self.driver.find_element(By.NAME, "r1c1a")
        age_select = Select(age_dropdown)
        age_select.select_by_visible_text("0")

        self.driver.find_element(By.XPATH, "/html/body[1]/div[6]/div[1]/div[1]/form[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='priceRange' and @value='200' and @type='radio']").click()
        self.driver.find_element(By.XPATH, "//input[@name='area' and @value='' and @type='radio']").click()

        self.driver.find_element(By.XPATH, "//label[contains(., 'Central Park') and ./input[@id='area' and @type='radio'] and ancestor::*[1][self::div and not(@class='more')]]").click()
