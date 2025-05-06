import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestTesla:
    def test_tesla_fdc94e3a(self):
        self.driver.get("https://tesla.com")

        self.driver.find_element(By.ID, "dx-nav-item--vehicles").click()
        self.driver.find_element(By.XPATH, "//img[@alt='Model Y']").click()

        self.driver.find_element(By.XPATH, "//a[@title='Demo Drive' and @data-gtm-drawer='hero']").click()

        self.driver.find_element(By.ID, "edit-lastname-td").clear()
        self.driver.find_element(By.ID, "edit-lastname-td").send_keys("Adams")
        self.driver.find_element(By.ID, "edit-firstname-td").clear()
        self.driver.find_element(By.ID, "edit-firstname-td").send_keys("Roy")
        self.driver.find_element(By.ID, "edit-phonenumber-td").clear()
        self.driver.find_element(By.ID, "edit-phonenumber-td").send_keys("123-999-0000")
        self.driver.find_element(By.ID, "edit-usermail-td").clear()
        self.driver.find_element(By.ID, "edit-usermail-td").send_keys("RA@gmail.com")

        schedule_button = self.driver.find_element(By.ID, "edit-submit-td-ajax0").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element(schedule_button).perform()
