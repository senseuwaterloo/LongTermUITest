import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestStubhub:
    def test_stubhub_1567bfa7(self):
        self.driver.get("https://stubhub.com")
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//input[@placeholder='Search events, artists, teams, and more']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search events, artists, teams, and more']").send_keys("MIAMI HEAT")

        self.driver.find_element(By.XPATH, "//p[./em[text()='Miami'] and ./em[text()='Heat'] and not(preceding-sibling::*) and not(following-sibling::*)]").click()

        self.driver.find_element(By.XPATH, "//div[@aria-label='Filter by location']/div[1]").click()

        self.driver.find_element(By.XPATH, "//input[@placeholder='Country, State, City']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Country, State, City']").send_keys("NEW YORK")

        self.driver.find_element(By.XPATH, "//div[text()='New York, NY, USA']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text()='Home/Away']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Away games']").click()

        self.driver.find_element(By.XPATH, "//ul[./li[1]/div[1]/div[1]/div[text()='New York']]/li[2]//button[text()='See tickets']").click()
        switch_to_new_tab(self.driver)

        tickets_dropdown = self.driver.find_element(By.XPATH, "//div[@id='modal-root']//select[@aria-label='Number of tickets']")
        tickets_select = Select(tickets_dropdown)
        tickets_select.select_by_visible_text("6 tickets")
        self.driver.find_element(By.XPATH, "//button[text()='Continue']").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='filter']/div[text()='Zones']").click()

        self.driver.find_element(By.XPATH, "//li[contains(@id, 'picker-') and ./div[1]/div[1]/div[text()='VIP']]/div[2]/div[1]/span[1]").click()

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div").click()

        self.driver.find_element(By.XPATH, "//div[@id='stubhub-event-detail-listings-sort-dropdown']/div").click()
        self.driver.find_element(By.XPATH, "//ul[@id='stubhub-event-detail-sort-dropdown-options']/li[text()='Price']").click()
