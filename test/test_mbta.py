import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_weekday_abbr_without_year_format


@pytest.mark.usefixtures("driver_session")
class TestMbta:
    def test_mbta_504c0c6b(self):
        self.driver.get("https://mbta.com")

        self.driver.find_element(By.XPATH, "//a[normalize-space(text())='Transit']").click()

        self.driver.find_element(By.XPATH, "//div[@id='transit']/div[1]/div[4]/a[4]/div[1]").click()

        self.driver.find_element(By.XPATH, "//div[@class='c-cms__sidebar']//a[contains(text(),'Find Parking Lots')]").click()

        self.driver.find_element(By.ID, "cms-10661-title").click()

        self.driver.find_element(By.XPATH, "//a[text()='Gloucester']").click()

        self.driver.find_element(By.XPATH, "//a[normalize-space(text())='Transit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='transit']/div[1]/div[4]/a[1]/div[1]").click()
        self.driver.find_element(By.ID, "from").clear()
        self.driver.find_element(By.ID, "from").send_keys("Gloucester")
        self.driver.find_element(By.XPATH, "//a[@data-objectid='stop-place-GB-0316']").click()

        self.driver.find_element(By.ID, "to").clear()
        self.driver.find_element(By.ID, "to").send_keys("NORTH PLYMOUTH")
        self.driver.find_element(By.XPATH, "//a[@id='hit-location-0']/span[2]/em[2]").click()

        self.driver.find_element(By.XPATH, "//label[@for='depart']").click()

        self.driver.find_element(By.XPATH, "//div[@id='trip-plan-datepicker']/div[1]").click()
        departure_date, _ = calculate_dates_weekday_abbr_without_year_format(1, 1)

        self.driver.find_element(By.XPATH, f"//span[contains(@aria-label, '{departure_date}')]").click()

        self.driver.find_element(By.XPATH, "//input[@type='number' and @aria-label='Hour' and @min='1' and @max='12']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='number' and @aria-label='Hour' and @min='1' and @max='12']").send_keys("2")

        self.driver.find_element(By.XPATH, "//input[@type='number' and @aria-label='Hour' and @min='1' and @max='12']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='number' and @aria-label='Minute' and @min='0' and @max='59']").send_keys("30")

        if self.driver.find_element(By.XPATH, "//span[@title='Click to toggle' and text()='AM']") is not None:
            self.driver.find_element(By.XPATH, "//span[@title='Click to toggle' and text()='AM']").click()
        self.driver.find_element(By.XPATH, "//a[@title='toggle calendar picker']").click()

        self.driver.find_element(By.ID, "trip-plan__submit").click()
