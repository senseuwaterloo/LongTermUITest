import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestRei:
    def test_rei_c59043d8(self):
        self.driver.get("https://www.rei.com/")

        self.driver.find_element(By.XPATH, "//header[@id='headerWrapper']/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[5]/a[1]/span[1]").click()

        activity_dropdown = self.driver.find_element(By.NAME, "activity")
        activity_select = Select(activity_dropdown)
        activity_select.select_by_visible_text("Cycling")

        self.driver.find_element(By.XPATH, "//input[@data-ui='search-banner-location-input']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-ui='search-banner-location-input']").send_keys("new york city")

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='New York City, NY, USA']").click()

        self.driver.find_element(By.XPATH, "//button[@data-ui='search-banner-submit']").click()

        self.driver.find_element(By.XPATH, "//a[@data-filter='cycling-mountain-biking']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='er-results']/div[1]/article[2]/div[2]/div[1]/h2[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Details & sign up')]").click()

        self.driver.find_element(By.XPATH, "//button[@data-ui='register-button']").click()

        self.driver.find_element(By.XPATH, "//input[@data-ui='step-1-main__member-field-firstName']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-ui='step-1-main__member-field-firstName']").send_keys("Joe")
        self.driver.find_element(By.XPATH, "//input[@data-ui='step-1-main__member-field-lastName']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-ui='step-1-main__member-field-lastName']").send_keys("Bloggs")
        self.driver.find_element(By.XPATH, "//input[@data-ui='step-1-main__member-field-email']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-ui='step-1-main__member-field-email']").send_keys("joe@joebloggs.com")
        self.driver.find_element(By.XPATH, "//input[@data-ui='step-1-main__member-field-phone']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-ui='step-1-main__member-field-phone']").send_keys("1111111111")

        self.driver.find_element(By.XPATH, "//button[@data-ui='continue']").click()

        self.driver.find_element(By.XPATH, "//input[@data-ui='emergency-contact-name']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-ui='emergency-contact-name']").send_keys("June Bloggs")
        self.driver.find_element(By.XPATH, "//input[@data-ui='emergency-contact-phone']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-ui='emergency-contact-phone']").send_keys("2222222222")

        self.driver.find_element(By.XPATH, "//span[@data-ui='health-info-health-conditions-no-text']").click()
        self.driver.find_element(By.XPATH, "//span[@data-ui='health-info-needs-accommodation-no']").click()

        self.driver.find_element(By.XPATH, "//input[@data-ui='gear-sizing-height-feet']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-ui='gear-sizing-height-feet']").send_keys("6")
        self.driver.find_element(By.XPATH, "//input[@data-ui='gear-sizing-height-inches']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-ui='gear-sizing-height-inches']").send_keys("0")

        self.driver.find_element(By.XPATH, "//button[@data-ui='continue']").click()

        self.driver.find_element(By.XPATH, "//input[@data-ui='checklist-acknowledged-eighteen-or-older']/parent::label").click()
        self.driver.find_element(By.XPATH, "//input[@data-ui='checklist-acknowledged-waiver']/parent::label").click()
        self.driver.find_element(By.XPATH, "//input[@data-ui='checklist-acknowledged-activity-level']/parent::label").click()
        self.driver.find_element(By.XPATH, "//button[@data-ui='continue']").click()

        self.driver.find_element(By.XPATH, "//button[text()=' Continue Browsing ']").click()
