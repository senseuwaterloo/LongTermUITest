import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestTesla:
    def test_tesla_fdc94e3a(self):
        # self.driver.get("https://tesla.com")

        # add extra steps to navigate to model Y otherwise the element can't be found since we need to scroll down a lot to let element be present
        self.driver.find_element(By.ID, "dx-nav-item--vehicles").click()
        self.driver.find_element(By.XPATH, "//img[@alt='Model Y']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='block-tesla-frontend-content']/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@title='Demo Drive' and @data-gtm-drawer='hero']").click()

        # step is redundant now
        # self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[5]/button[4]").click()

        self.driver.find_element(By.ID, "edit-lastname-td").clear()
        self.driver.find_element(By.ID, "edit-lastname-td").send_keys("Adams")
        self.driver.find_element(By.ID, "edit-firstname-td").clear()
        self.driver.find_element(By.ID, "edit-firstname-td").send_keys("Roy")
        self.driver.find_element(By.ID, "edit-phonenumber-td").clear()
        self.driver.find_element(By.ID, "edit-phonenumber-td").send_keys("123-999-0000")
        self.driver.find_element(By.ID, "edit-usermail-td").clear()
        self.driver.find_element(By.ID, "edit-usermail-td").send_keys("RA@gmail.com")

        # steps are redundant now
        # self.driver.find_element(By.ID, "edit-zipcode-td").clear()
        # self.driver.find_element(By.ID, "edit-zipcode-td").send_keys("90001")

        # self.driver.find_element(By.ID, "edit-submit-td-ajax0").click()
        # just hover on button to avoid sending spam data
        schedule_button = self.driver.find_element(By.ID, "edit-submit-td-ajax0").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element(schedule_button).perform()
