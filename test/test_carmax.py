import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestCarmax:
    def test_carmax_8bfeeb54(self):
        # self.driver.get("https://carmax.com")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Search Cars')]").click()
        # target element is in shadow dom after web page change, need to find its parent element that is not in shadow dom
        self.driver.find_element(By.XPATH, "//section[@id='first-time-visitor-hero']/div/div/div/div/hzn-button").click()
        self.driver.find_element(By.XPATH, "//div[@id='Distance']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        # above element is in a shadow dom now so can't directly locate it, better to locate its parent that is not in shadow dom
        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.ID, "store-chooser-keyword-input").click()
        self.driver.find_element(By.ID, "store-chooser-keyword-input").clear()
        self.driver.find_element(By.ID, "store-chooser-keyword-input").send_keys("07470")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Set My Store']").click()
        self.driver.find_element(By.XPATH, "//div[@id='store-chooser-modal-body']/ul[1]/li[2]/div[2]/button[1]").click()

        # following wait is to avoid: selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='Distance']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/button[1]").click()
        # modified locator of above code to handle the selecting a dropdown, the dropdown is in a shadow dom so also need to handle that
        distance_select_shadow_root = self.driver.find_element(By.ID, "distanceSelect")
        distance_dropdown = distance_select_shadow_root.shadow_root.find_element(By.ID, "select")
        distance_select = Select(distance_dropdown)
        distance_select.select_by_value('100')

        # self.driver.find_element(By.ID, "switch-Pk738UI-").click()
        # above switch toggle is in shadow dom now, better to click its parent
        self.driver.find_element(By.CSS_SELECTOR, "hzn-toggle[label='Out-of-market']").click()

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Make']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[13]").click()
        # change locator of above code
        self.driver.find_element(By.CSS_SELECTOR, "hzn-checkbox[value='Honda']").click()

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Model']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]").click()
        # change locator of above code
        self.driver.find_element(By.CSS_SELECTOR, "hzn-checkbox[value='Civic']").click()

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='YearFilter']/button[1]").click()
        # change locator of above code
        self.driver.find_element(By.XPATH, "//div[@id='Year']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[7]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[7]/button[1]").click()
        # change above code to select dropdown, also need to handle shadow dom
        year_from_shadow_root = self.driver.find_element(By.ID, "from")
        year_from_dropdown = year_from_shadow_root.shadow_root.find_element(By.ID, "select")
        year_from_select = Select(year_from_dropdown)
        year_from_select.select_by_value('2017')

        year_to_shadow_root = self.driver.find_element(By.ID, "to")
        year_to_dropdown = year_to_shadow_root.shadow_root.find_element(By.ID, "select")
        year_to_select = Select(year_to_dropdown)
        # change the year range compared to the original task to avoid no result returned
        year_to_select.select_by_value('2024')

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='Features']/button[1]").click()
        # locator change of above code
        self.driver.find_element(By.XPATH, "//div[@id='FeatureNames']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[5]").click()
        # change locator of above code
        self.driver.find_element(By.CSS_SELECTOR, "hzn-checkbox[value='Sunroof(s)']").click()
        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='ExteriorColor']/button[1]").click()
        # self.driver.find_element(By.XPATH, "//li[@role='presentation']").click()
        # change locator of above code
        self.driver.find_element(By.CSS_SELECTOR, "hzn-checkbox[value='Black']").click()

        self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='Sort']/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter-panel']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/label[1]").click()
        # change locator of above code and handle shadow dom
        sort_radio_shadow_root = self.driver.find_element(By.NAME, "sort-group")
        lowest_price_radio = sort_radio_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "fieldset > hzn-stack > hzn-stack.radio-group > label:nth-child(3)")
        lowest_price_radio.click()
    