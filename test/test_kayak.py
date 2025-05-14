import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_full_month_name, switch_to_new_tab


@pytest.mark.usefixtures("driver_session")
class TestKayak:
    def test_kayak_f7c2c65f(self):
        self.driver.get("https://www.kayak.com/?ispredir=true")

        self.driver.find_element(By.XPATH, "//div[text()='Round-trip']").click()

        self.driver.find_element(By.XPATH, "//li[@id='oneway']/span[1]").click()

        self.driver.find_element(By.XPATH, "//div[@class='c_neb-item-close']").click()

        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='From?']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='From?']").send_keys("NEW YORK")

        self.driver.find_element(By.XPATH, "//li[@id='NYC_ap_All airports, New York, United States, (NYC)']/div[1]/div[2]").click()

        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='To?']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='To?']").send_keys("PARIS")

        self.driver.find_element(By.XPATH, "//li[@id='PAR_ap_All airports, Paris, France, (PAR)']/div[1]/div[2]").click()

        self.driver.find_element(By.XPATH, "//div[contains(text(), '1 adult')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Adults')]//button[@aria-label='Increment']").click()

        self.driver.find_element(By.XPATH, "//div[@role='button' and @aria-label='Start date']").click()

        departure_date, _ = calculate_dates_full_month_name(32, 32)
        self.driver.find_element(By.XPATH, f"//div[contains(@aria-label, '{departure_date}')]").click()

        self.driver.find_element(By.XPATH, "//span[text()='Economy']").click()
        self.driver.find_element(By.XPATH, "//li[@aria-label='Business']/span").click()

        self.driver.find_element(By.XPATH, "//label[text()='Direct flights only']").click()

        self.driver.find_element(By.XPATH, "//span[text()='0 bags']").click()
        self.driver.find_element(By.XPATH, "//div[./div[contains(text(), 'Carry-on bag')]]//button[@aria-label='Increment']").click()
        self.driver.find_element(By.XPATH, "//div[./div[contains(text(), 'Checked bag')]]//button[@aria-label='Increment']").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='submit' and @aria-label='Search']").click()

        switch_to_new_tab(self.driver)
        self.driver.find_element(By.XPATH, "//div[@aria-label='Quickest']").click()
