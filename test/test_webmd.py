import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from browser_helper import get_control_key


@pytest.mark.usefixtures("driver_session")
class TestWebmd:
    def test_webmd_b3f27ec6(self):
        self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Doctor')]").click()

        self.driver.find_element(By.ID, "searchkeywords_desktop").clear()
        self.driver.find_element(By.ID, "searchkeywords_desktop").send_keys('Botox (Botulinum toxin)')
        self.driver.find_element(By.ID, "searchlocation_desktop").send_keys(get_control_key() + "a")
        self.driver.find_element(By.ID, "searchlocation_desktop").send_keys(Keys.DELETE)
        self.driver.find_element(By.ID, "searchlocation_desktop").send_keys('Bristol, RI')
        self.driver.find_element(By.XPATH, "//span[@class='webmd-input-group__append']/button[@aria-label='Search']").click()

        self.driver.find_element(By.XPATH, "//div[@class='filters-container' and not(@style='display: none;')]//span[text()='Virtual Visit']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Insurance']").click()

        self.driver.find_element(By.XPATH, "//div[contains(@id, 'webmd-popover-')]//span[text()='Aetna']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'webmd-popover-') and @aria-hidden='false']//span[text()=' Apply ']").click()

        self.driver.find_element(By.XPATH, "//div[@class='filters-container' and not(@style='display: none;')]//span[text()=' Accepts New Patients ']").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//span[text()='Request Now']").get_native_element())
