import pytest
from selenium.webdriver.common.by import By

from browser_helper import switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestCaGov:
    def test_cagov_1b4901e9(self):
        self.driver.get("https://www.ca.gov/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav_list']/li[7]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Look Up My Representatives')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='launch-look-up-my-representatives']/span[2]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'State Senate')]").click()
        switch_to_new_tab(self.driver)
        self.driver.find_element(By.ID, "street").clear()
        self.driver.find_element(By.ID, "street").send_keys("2043 E Lewis Ave")
        self.driver.find_element(By.ID, "city").clear()
        self.driver.find_element(By.ID, "city").send_keys("Fresno")
        self.driver.find_element(By.ID, "ZIP").clear()
        self.driver.find_element(By.ID, "ZIP").send_keys("93701")
        self.driver.find_element(By.ID, "locate_label").click()
