import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestTvguide:
    def test_tvguide_9cc81f50(self):
        self.driver.get("https://tvguide.com")

        self.driver.find_element(By.XPATH, "//a[text()='See Full Schedule']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Provider']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("99201")
        self.driver.find_element(By.XPATH, "//button[text()='Antenna']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Broadcast TV Spokane (3)']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Apply']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Skip']").click()
        self.driver.find_element(By.XPATH, "//div[text()='CH 2.1']").click()
