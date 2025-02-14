import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_weekday_abbr_without_year_format


@pytest.mark.usefixtures("setup_class")
class TestMbta:
    def test_mbta_504c0c6b(self):
        # self.driver.get("https://mbta.com")

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Transit')]").click()
        # to make the locator uniquely locate the element
        self.driver.find_element(By.XPATH, "//a[normalize-space(text())='Transit']").click()

        self.driver.find_element(By.XPATH, "//div[@id='transit']/div[1]/div[4]/a[4]/div[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Parking Lots')]").click()
        # to make the locator uniquely locate the element
        self.driver.find_element(By.XPATH, "//div[@class='c-cms__sidebar']//a[contains(text(),'Find Parking Lots')]").click()

        self.driver.find_element(By.ID, "cms-10661-title").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Gloucester')]").click()
        # to make the locator uniquely locate the element
        self.driver.find_element(By.XPATH, "//a[text()='Gloucester']").click()

        # page logic changed, no below link now.
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Plan a trip from this station')]").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space(text())='Transit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='transit']/div[1]/div[4]/a[1]/div[1]").click()
        self.driver.find_element(By.ID, "from").clear()
        self.driver.find_element(By.ID, "from").send_keys("Gloucester")
        self.driver.find_element(By.XPATH, "//a[@data-objectid='stop-place-GB-0316']").click()

        self.driver.find_element(By.ID, "to").clear()
        self.driver.find_element(By.ID, "to").send_keys("NORTH PLYMOUTH")
        self.driver.find_element(By.XPATH, "//a[@id='hit-location-0']/span[2]/em[2]").click()

        # self.driver.find_element(By.ID, "trip-plan-departure-title").click()
        self.driver.find_element(By.XPATH, "//label[@for='depart']").click()

        # self.driver.find_element(By.XPATH, "//label[@id='plan-date-label']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trip-plan-datepicker']/div[1]").click()
        departure_date, _ = calculate_dates_weekday_abbr_without_year_format(1, 1)

        # self.driver.find_element(By.ID, "cell28-plan-date-input").click()
        self.driver.find_element(By.XPATH, f"//span[contains(@aria-label, '{departure_date}')]").click()

        # self.driver.find_element(By.ID, "plan_date_time_hour").clear()
        # self.driver.find_element(By.ID, "plan_date_time_hour").send_keys("2")
        self.driver.find_element(By.XPATH, "//input[@type='number' and @aria-label='Hour' and @min='1' and @max='12']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='number' and @aria-label='Hour' and @min='1' and @max='12']").send_keys("2")

        # self.driver.find_element(By.ID, "plan_date_time_minute").clear()
        # self.driver.find_element(By.ID, "plan_date_time_minute").send_keys("30")
        self.driver.find_element(By.XPATH, "//input[@type='number' and @aria-label='Hour' and @min='1' and @max='12']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='number' and @aria-label='Minute' and @min='0' and @max='59']").send_keys("30")

        # self.driver.find_element(By.ID, "plan_date_time_am_pm").clear()
        # self.driver.find_element(By.ID, "plan_date_time_am_pm").select("PM")
        if self.driver.find_element(By.XPATH, "//span[@title='Click to toggle' and text()='AM']") is not None:
            self.driver.find_element(By.XPATH, "//span[@title='Click to toggle' and text()='AM']").click()
        self.driver.find_element(By.XPATH, "//a[@title='toggle calendar picker']").click()

        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.ID, "trip-plan__submit").click()
        # element below is not available anymore in the new page
        # self.driver.find_element(By.ID, "itinerary-1-title").click()
