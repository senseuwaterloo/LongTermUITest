import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestUps:
    def test_ups_8ae1041c(self):
        self.driver.get("https://www.ups.com/us/en/Home.page")
        self.driver.find_element(By.XPATH, "//a[@id='tabs_0_tab_1']/span[1]").click()
        self.driver.find_element(By.ID, "ups-ship-from").clear()
        self.driver.find_element(By.ID, "ups-ship-from").send_keys("10001")
        self.driver.find_element(By.XPATH, "//div[@id='ship-from-input']/div[1]/div[1]/div[1]/div[1]/span[2]/span[1]").click()
        self.driver.find_element(By.ID, "ups-ship-to").clear()

        self.driver.find_element(By.ID, "ups-ship-to").send_keys("95814")
        self.driver.find_element(By.XPATH, "//div[@id='ship-to-input']/div[1]/div[1]/div[1]/div[1]/span[2]/span[1]").click()
        self.driver.find_element(By.ID, "ups-ship-weight").clear()
        self.driver.find_element(By.ID, "ups-ship-weight").send_keys("5")

        self.driver.find_element(By.ID, "ups-ship-length").clear()
        self.driver.find_element(By.ID, "ups-ship-length").send_keys("5")
        self.driver.find_element(By.ID, "ups-ship-width").clear()
        self.driver.find_element(By.ID, "ups-ship-width").send_keys("5")
        self.driver.find_element(By.ID, "ups-ship-height").clear()
        self.driver.find_element(By.ID, "ups-ship-height").send_keys("5")

        self.driver.find_element(By.ID, "widget-get-quote-cta").click()

        self.driver.find_element(By.XPATH, "//span[text()=' Fastest ']").click()
