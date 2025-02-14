import time
import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element, switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestAmtrak:
    def test_amtrak_b910229f(self):
        # self.driver.get("https://amtrak.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'DEALS') and @data-automation-id='sitePrimarySubnav']").click()
        self.driver.find_element(By.XPATH, "//a[@data-automation-id='VACATIONS & RAIL TOURS']").click()
        all_destinations_element = self.driver.find_element(By.XPATH, "//a[@data-automation-id='See all destinations']")
        scroll_to_element(self.driver, all_destinations_element)
        all_destinations_element.click()
        self.driver.find_element(By.XPATH, "//a[text()='AmtrakVacations.com']").click()
        switch_to_new_tab(self.driver, "https://amtrak.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Travel Styles')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Cross Country Journeys')]").click()

        second_trip_details = self.driver.find_element(By.XPATH, "//*[@id='ylg-ms__listings-search']/div/div/div[3]/div[1]/div/div/div/div[3]/a")
        scroll_to_element(self.driver, second_trip_details)
        second_trip_details.click()
        # //*[@id="ylg-ms__listings-search"]/div/div/div[3]/div[2]/div/div/div/div[3]/a

        instant_quote = self.driver.find_element(By.XPATH, "//*[@id='tour-details-container__actions']/div[2]/button[1]")
        scroll_to_element(self.driver, instant_quote)
        instant_quote.click()
        # always select the first day of next month
        self.driver.find_element(By.XPATH, "//*[@id='ylg-ms__listings-details']/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[4]/div/img").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='days-cell']//span[text()='1']").click()

        self.driver.find_element(By.XPATH, "//*[@id='ylg-ms__listings-details']/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div/button").click()
        leaving_from = self.driver.find_element(By.ID, "edit-add-additional-departure-city")
        scroll_to_element(self.driver, leaving_from)
        leaving_from.send_keys("Chicago")

        pre_post_rail = self.driver.find_element(By.XPATH, "//*[@id='edit-need-pre-post-rail']/div[2]/label")
        scroll_to_element(self.driver, pre_post_rail)
        pre_post_rail.click()

        deluxe_bedroom = self.driver.find_element(By.ID, "edit-private-bedroom")
        scroll_to_element(self.driver, deluxe_bedroom)
        deluxe_bedroom.click()

        adult_num = self.driver.find_element(By.ID, "edit-adults-num")
        scroll_to_element(self.driver, adult_num)
        adult_num.clear()
        adult_num.send_keys("2")

        about_trip = self.driver.find_element(By.XPATH, "//textarea[@data-drupal-selector='edit-about-your-trip']")
        scroll_to_element(self.driver, about_trip)
        about_trip.clear()
        about_trip.send_keys("Wedding Anniversary")

        next_step = self.driver.find_element(By.ID, "edit-actions-wizard-next")
        scroll_to_element(self.driver, next_step)
        next_step.click()
        # new form will scroll up so need to wait for a few seconds to avoid selenium.common.exceptions.ElementClickInterceptedException:
        # Message: element click intercepted: Element is not clickable at point
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-first-name']").click()
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-first-name']").send_keys("John")
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-last-name']").click()
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-last-name']").send_keys("Mark")
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-email-address']").click()
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-email-address']").send_keys("Johnmark@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-phone-number']").click()
        self.driver.find_element(By.XPATH, "//input[@data-drupal-selector='edit-phone-number']").send_keys("234567890")
        self.driver.find_element(By.XPATH, "//div[@data-drupal-selector='edit-travel-advisor-select']/div[1]/div[1]/label").click()

        submit_button = self.driver.find_element(By.XPATH, "//div[@data-drupal-selector='edit-actions']/div[2]/input")
        scroll_to_element(self.driver, submit_button)
        submit_button.click()
    