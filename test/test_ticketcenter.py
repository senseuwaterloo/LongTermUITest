import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_ticketcenter_format


@pytest.mark.usefixtures("driver_session")
class TestTicketcenter:
    def test_ticketcenter_9223f1b4(self):
        self.driver.get("https://ticketcenter.com")

        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("Wicked")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/ul[1]/li[1]/a[1]/strong[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='filterContainer']/div[2]/span[7]/div[1]/button[1]/i[1]").click()

        self.driver.find_element(By.XPATH, "//input[@placeholder='Select Date Range']").click()

        start_day, start_month_year, end_day, end_month_year = calculate_dates_ticketcenter_format(7, 26)
        self.driver.find_element(By.XPATH, f"//table[@class='table-condensed' and ./thead[1]/tr[1]/th[@class='month' and text()='{start_month_year}']]/tbody/tr/td[text()='{start_day}' and not(contains(@class, 'off'))]").click()
        self.driver.find_element(By.XPATH, f"//table[@class='table-condensed' and ./thead[1]/tr[1]/th[@class='month' and text()='{end_month_year}']]/tbody/tr/td[text()='{end_day}' and not(contains(@class, 'off'))]").click()

        apply_button = self.driver.find_element(By.XPATH, "//div[contains(@style, 'display: block;')]//button[text()='Apply']").get_native_element()
        self.driver.execute_script('arguments[0].click()', apply_button)
