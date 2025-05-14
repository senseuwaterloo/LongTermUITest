import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestCookpad:
    def test_cookpad_ceac063d(self):
        self.driver.get("https://cookpad.com")

        self.driver.find_element(By.ID, "navigation_search").clear()
        self.driver.find_element(By.ID, "navigation_search").send_keys("pancake")
        self.driver.find_element(By.XPATH, "//button[@name='button' and @type='submit']").click()

        self.driver.find_element(By.ID, "search_excluded_ingredients").clear()
        self.driver.find_element(By.ID, "search_excluded_ingredients").send_keys("beetroot")
        self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[2]/div[2]/div/form/div[1]/div[3]/div/div[1]/div/div/div/div").click()
        self.driver.find_element(By.ID, "search_included_ingredients").clear()
        self.driver.find_element(By.ID, "search_included_ingredients").send_keys("wheat")
        self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[2]/div[2]/div/form/div[1]/div[2]/div/div[1]/div/div/div/div").click()
