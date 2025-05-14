import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("driver_session")
class TestCarmax:
    def test_carmax_8bfeeb54(self):
        self.driver.get("https://carmax.com")

        self.driver.find_element(By.XPATH, "//section[@id='first-time-visitor-hero']/div/div/div/div/hzn-button").click()
        self.driver.find_element(By.XPATH, "//div[@id='Distance']/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.ID, "store-chooser-keyword-input").click()
        self.driver.find_element(By.ID, "store-chooser-keyword-input").clear()
        self.driver.find_element(By.ID, "store-chooser-keyword-input").send_keys("07470")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Set My Store']").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-chooser-modal-body']/ul[1]/li[2]/div[2]/button[1]").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='Distance']/button[1]").click()

        distance_select_shadow_root = self.driver.find_element(By.ID, "distanceSelect")
        distance_dropdown = distance_select_shadow_root.shadow_root.find_element(By.ID, "select")
        distance_select = Select(distance_dropdown)
        distance_select.select_by_value('100')

        self.driver.find_element(By.CSS_SELECTOR, "hzn-toggle[label='Out-of-market']").click()

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Make']/button[1]").click()

        self.driver.find_element(By.CSS_SELECTOR, "hzn-checkbox[value='Honda']").click()

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Model']/button[1]").click()

        self.driver.find_element(By.CSS_SELECTOR, "hzn-checkbox[value='Civic']").click()

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='Year']/button[1]").click()

        year_from_shadow_root = self.driver.find_element(By.ID, "from")
        year_from_dropdown = year_from_shadow_root.shadow_root.find_element(By.ID, "select")
        year_from_select = Select(year_from_dropdown)
        year_from_select.select_by_value('2017')

        year_to_shadow_root = self.driver.find_element(By.ID, "to")
        year_to_dropdown = year_to_shadow_root.shadow_root.find_element(By.ID, "select")
        year_to_select = Select(year_to_dropdown)
        year_to_select.select_by_value('2024')

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='FeatureNames']/button[1]").click()

        self.driver.find_element(By.CSS_SELECTOR, "hzn-checkbox[value='Sunroof(s)']").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='ExteriorColor']/button[1]").click()
        self.driver.find_element(By.CSS_SELECTOR, "hzn-checkbox[value='Black']").click()

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='Sort']/button[1]").click()
        sort_radio_shadow_root = self.driver.find_element(By.NAME, "sort-group")
        lowest_price_radio = sort_radio_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "fieldset > hzn-stack > hzn-stack.radio-group > label:nth-child(3)")
        lowest_price_radio.click()
    