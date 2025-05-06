import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestJusticeGov:
    def test_justicegov_ec10879f(self):
        self.driver.get("https://www.justice.gov/")
        self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-4']/div[1]/div[1]/div[3]/div[1]/a[1]/span[1]").click()

        agency_dropdown = self.driver.find_element(By.NAME, "field_component_target_id")
        agency_select = Select(agency_dropdown)
        agency_select.select_by_visible_text('Civil Division')

        self.driver.find_element(By.ID, "edit-submit-resources").click()

        self.driver.find_element(By.NAME, "title").clear()
        self.driver.find_element(By.NAME, "title").send_keys("radiation exposure")

        self.driver.find_element(By.ID, "edit-submit-resources").click()

        self.driver.find_element(By.XPATH, "//input[@value='Reset Filters']").click()

        agency_dropdown = self.driver.find_element(By.NAME, "field_component_target_id")
        agency_select = Select(agency_dropdown)
        agency_select.select_by_visible_text('Civil Division')
        self.driver.find_element(By.ID, "edit-submit-resources").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Form Title')]").click()
