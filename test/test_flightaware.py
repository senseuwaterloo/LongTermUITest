import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestFlightaware:
    def test_flightaware_4ffca7c8(self):
        self.driver.get("https://www.flightaware.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='listMenuRoot']/li[2]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()

        self.driver.find_element(By.NAME, "firstname").clear()
        self.driver.find_element(By.NAME, "firstname").send_keys("John")

        self.driver.find_element(By.NAME, "lastname").clear()
        self.driver.find_element(By.NAME, "lastname").send_keys("Smith")

        self.driver.find_element(By.NAME, "company").clear()
        self.driver.find_element(By.NAME, "company").send_keys("ACNE AB")

        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys("abc@abc.com")

        self.driver.find_element(By.NAME, "phone").clear()
        self.driver.find_element(By.NAME, "phone").send_keys("888889999")

        self.driver.find_element(By.NAME, "tell_us_a_little_bit_about_your_data_needs").clear()
        self.driver.find_element(By.NAME, "tell_us_a_little_bit_about_your_data_needs").send_keys("Send Brochure")
