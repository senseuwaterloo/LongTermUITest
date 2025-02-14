import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_first_last_dates, scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestSeatgeek:
    def test_seatgeek_8f6261cf(self):
        # self.driver.get("https://seatgeek.com")

        # element click intercepted if located to the child span
        change_location_button = self.driver.find_element(By.XPATH, "//span[contains(.,'Change Location')]/parent::button")
        scroll_to_element(self.driver, change_location_button)
        change_location_button.click()

        # self.driver.find_element(By.ID, "downshift-2-input").clear()
        # self.driver.find_element(By.ID, "downshift-2-input").send_keys("New York")
        self.driver.find_element(By.ID, "downshift-0-input").clear()
        # TODO: NEED TO SEND THE TEXT Character by character because somehow only the last character will send to the input if directly use send_keys to send all the content at once!
        [self.driver.find_element(By.ID, "downshift-0-input").send_keys(each_char) for each_char in "New York"]

        # self.driver.find_element(By.XPATH, "//li[@id='downshift-2-item-0']/p[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/p[1]").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Filter by')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='date-filter-button']").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[contains(.,'1')]").click()
        # self.driver.find_element(By.XPATH, "//div[contains(.,'30')]").click()
        # self.driver.find_element(By.XPATH, "//span[contains(.,'Apply')]").click()
        start_date_str, end_date_str = calculate_first_last_dates()
        self.driver.find_element(By.XPATH, f"//div[@data-testid='{start_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//div[@data-testid='{end_date_str}']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='date-filter-apply-button']").click()
