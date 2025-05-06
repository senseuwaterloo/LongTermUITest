import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_weekday_abbr_format


@pytest.mark.usefixtures("setup_class")
class TestMarriott:
    def test_marriott_06a6d90b(self):
        self.driver.get("https://www.marriott.com")

        self.driver.find_element(By.ID, "downshift-0-input").clear()
        self.driver.find_element(By.ID, "downshift-0-input").send_keys("NIAGRA FALLS")

        self.driver.find_element(By.ID, "downshift-0-item-0").click()

        self.driver.find_element(By.ID, "date-picker").click()
        start_date, end_date = calculate_dates_weekday_abbr_format(30, 33)
        self.driver.find_element(By.XPATH, f"//div[@aria-label='{start_date}' and @aria-disabled='false']/div[1]").click()
        self.driver.find_element(By.XPATH, f"//div[@aria-label='{end_date}' and @aria-disabled='false']/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-custom_click_track_value='Search Form Dates Module| Done button |internal']").click()

        self.driver.find_element(By.ID, "Rooms & Guests").click()
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Search form | Rooms Increment button |internal']").click()
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Search form | Adults Increment button |internal']").click()
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Search form | Adults Increment button |internal']").click()
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Search form | Children Increment button |internal']").click()
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Search form | Children age Increment button |internal']").click()
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Search form | Children age Increment button |internal']").click()
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Search form | Children age Increment button |internal']").click()
        self.driver.find_element(By.XPATH, "//button[@data-custom_click_track_value='Search Form | Find Hotels |internal']").click()

        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Phoenix Search Results| Filter Selection: All Filters |internal']").click()

        self.driver.find_element(By.XPATH, "//span[@role='switch' and ./input[@custom_click_track_value='Phoenix Search Results| Show available hotels only Selection |internal']]").click()
        self.driver.find_element(By.XPATH, "//label[contains(text(), '100 - 200 USD')]").click()
        self.driver.find_element(By.XPATH, "//span[@role='switch' and ./input[@custom_click_track_value='Phoenix Search Results| Show rates with taxes and all fees |internal']]").click()
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Phoenix Search Results| Footer Button: Apply Button |internal']").click()
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Phoenix Search Results|  Filters: Free breakfast |internal']").click()
        self.driver.find_element(By.XPATH, "//button[@custom_click_track_value='Phoenix Search Results|  Filters: Pool |internal']").click()
        self.driver.find_element(By.XPATH, "//div[@custom_click_track_value='Phoenix Search Results| Sort-by options dropdown |internal']").click()
        self.driver.find_element(By.XPATH, "//div[@custom_click_track_value='Phoenix Search Results| Sort-by option: Price (Low-to-High) |internal']").click()
        self.driver.find_element(By.XPATH, "//div[@data-pnum='0']//button[@custom_click_track_value='Phoenix Search Results| Hotel Details Page |internal']").click()
        self.driver.find_element(By.XPATH, "//a[@custom_click_track_value='HQV AEM| View Rates |internal']/button[1]").click()
    