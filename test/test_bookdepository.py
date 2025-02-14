import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestBookdepository:
    def test_bookdepository_c1f584e2(self):
        # self.driver.get("https://bookdepository.com")
        # book depository is closing soon, so we revised this test case for https://www.barnesandnoble.com/
        self.driver.find_element(By.XPATH, "//a[contains(., ' My Account')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Sign In')]").click()

        login_iframe = self.driver.find_element(By.XPATH, "//iframe[@title='Sign in or Create an Account']").get_native_element()
        self.driver.switch_to.frame(login_iframe)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("UITestStudy2024")
        self.driver.find_element(By.XPATH, "//button[contains(., 'Sign In & Continue')]").click()
        self.driver.switch_to.default_content()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search by Title, Author, Keyword or ISBN']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search by Title, Author, Keyword or ISBN']").send_keys("game of thrones")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Search button']").click()

        language_filter = self.driver.find_element(By.XPATH, "//div[@aria-label='left-nav']//div[@id='Language_category']")
        scroll_to_element(self.driver, language_filter)
        language_filter.click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='left-nav']//div[@id='Language_category']/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='left-nav']//ul[@id='sidebar-section-0']/li[11]/a").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'filter-section justify-content-md-end')]//a[@id='list-view']/div").click()

        self.driver.find_element(By.XPATH, "//form[@id='addToBagForm_0700304046659']/input[11]").click()
        self.driver.find_element(By.XPATH, "//form[@id='addToBagForm_0810011720022']/input[11]").click()

        self.driver.find_element(By.ID, "cartIcon").click()
        self.driver.find_element(By.XPATH, "//input[@id='continue' and @value='CONTINUE TO CHECKOUT']").click()
    