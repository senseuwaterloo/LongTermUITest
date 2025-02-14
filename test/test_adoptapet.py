import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestAdoptapet:
    def test_adoptapet_b49c669d(self):
        # self.driver.get("https://adoptapet.com")

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/header[1]/div[3]/div[1]/nav[1]/ul[1]/li[1]").click()
        # change absolute xpath
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Find a pet')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a dog')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a dog')]").click()

        # use sleep to avoid selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found
        # Sometimes pass, sometimes fail, need wait to be more robust
        # test logic should be structured in a way that anticipates and handles dynamic changes in the DOM.
        time.sleep(1)

        # add scroll action
        breed_element = self.driver.find_element(By.ID, "location-1")
        scroll_to_element(self.driver, breed_element)

        # self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").clear()
        # self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("10019")
        # changed locator. There was no id before.
        self.driver.find_element(By.ID, "location-1").clear()
        self.driver.find_element(By.ID, "location-1").send_keys("10019")

        # self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[1]/input[1]").clear()
        # self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[1]/input[1]").send_keys("jack russell")
        # The structure.layout of the dom is changed
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div/div[2]/div[2]/ul/div[1]/input").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div/div[2]/div[2]/ul/div[1]/input").send_keys("jack russell")
        # Never mind about the code below, just to make sure the item is selected
        self.driver.find_element(By.XPATH, "//label[contains(text(),'Jack Russell Terrier')]").click()

        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[2]/div[1]/div[2]/button[1]").click()
        # change absolute xpath to text-based locator
        self.driver.find_element(By.XPATH, "//button[contains(.,'Create an Alert')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]/span[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]/span[1]").send_keys("buckeye.foobar@gmail.com")
        # changed locator. There was no id before.
        self.driver.find_element(By.ID, "email-2").clear()
        self.driver.find_element(By.ID, "email-2").send_keys("uiteststudy@gmail.com")

        # self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[2]").click()
        # Note that the dom layout changed.
        self.driver.find_element(By.XPATH, "//*[@id='livewire-ui-modal']/div/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div[2]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/button[1]").click()
        # change absolute xpath to text-based locator
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Subscribe Now')]").click()
    