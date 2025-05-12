import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestAdoptapet:
    def test_adoptapet_b49c669d(self):
        self.driver.get("https://adoptapet.com")

        # self.driver.find_element(By.XPATH, "//span[contains(text(),'Find a pet')]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Find a Pet']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a dog')]").click()

        time.sleep(1)

        breed_element = self.driver.find_element(By.ID, "location-1")
        scroll_to_element(self.driver, breed_element)

        self.driver.find_element(By.ID, "location-1").clear()
        self.driver.find_element(By.ID, "location-1").send_keys("10019")

        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div/div[2]/div[2]/ul/div[1]/input").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div/div[2]/div[2]/ul/div[1]/input").send_keys("jack russell")
        self.driver.find_element(By.XPATH, "//label[contains(text(),'Jack Russell Terrier')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        self.driver.find_element(By.XPATH, "//button[contains(.,'Create an Alert')]").click()

        self.driver.find_element(By.ID, "email-2").clear()
        self.driver.find_element(By.ID, "email-2").send_keys("uiteststudy@gmail.com")

        self.driver.find_element(By.XPATH, "//*[@id='livewire-ui-modal']/div/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div[2]").click()

        self.driver.find_element(By.XPATH, "//button[contains(text(),'Subscribe Now')]").click()
    