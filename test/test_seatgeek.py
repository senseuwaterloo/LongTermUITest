import time

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
    
    # def test_seatgeek_918d7ef3(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Help & Support')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Buying Tickets')]").click()
    #
    # def test_seatgeek_9c3cba90(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/nav[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hamilton')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[7]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/section[2]/div[2]/ul[1]/li[3]/a[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[4]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/button[3]").click()
    #     self.driver.find_element(By.ID, "promo-toggle").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[4]/div[1]/div[1]/div[2]/section[3]/div[1]/span[2]/span[1]/div[1]/span[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[4]/div[1]/div[1]/div[2]/section[3]/div[1]/span[2]/div[1]/div[1]/div[1]/button[3]/div[1]/span[1]").click()
    #
    # def test_seatgeek_10de6ac5(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Trending')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Beyonce')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/section[2]/div[2]/ul[1]/li[1]/a[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/img[1]").click()
    #
    # def test_seatgeek_563ec938(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/nav[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'WWE')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Wrestlemania')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Parking')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/section[2]/div[2]/ul[1]/li[2]/a[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]/div[1]/span[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/button[3]/div[1]/span[1]").click()
    #
    # def test_seatgeek_6760de22(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/nav[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'NBA')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Los Angeles Lakers')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Parking')]").click()
    #
    # def test_seatgeek_74226fab(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Genres')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pop')]").click()
    #
    # def test_seatgeek_78915162(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//input[@name='search' and @value='' and @type='text' and @placeholder='Search by team, artist, event, or venue']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='search' and @value='' and @type='text' and @placeholder='Search by team, artist, event, or venue']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='search' and @value='' and @type='text' and @placeholder='Search by team, artist, event, or venue']").send_keys("Coldplay")
    #     self.driver.find_element(By.XPATH, "//p[@title='Coldplay']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[2]/span[1]").click()
    #
    # def test_seatgeek_e93fe82b(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Genres')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Classic Rock')]").click()
    #
    # def test_seatgeek_fbaa5c83(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Change Location')]").click()
    #     self.driver.find_element(By.ID, "downshift-2-input").clear()
    #     self.driver.find_element(By.ID, "downshift-2-input").send_keys("Chicago")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-2-item-0']/p[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/ul[1]/li[8]/a[1]/div[1]/div[2]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[6]/div[1]/div[1]/main[1]/div[2]/button[1]/div[1]/span[2]").click()
    #
    # def test_seatgeek_c50985ee(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Festivals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'M3 Rock Festival')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/section[2]/div[2]/ul[1]/li[1]/a[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/button[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/button[4]/span[1]").click()
    #
    # def test_seatgeek_c7058499(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Genres')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Jazz')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[5]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/div[1]/button[4]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[5]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/p[2]/button[1]").click()
    #
    # def test_seatgeek_ac59be41(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Change Location')]").click()
    #     self.driver.find_element(By.ID, "downshift-0-input").clear()
    #     self.driver.find_element(By.ID, "downshift-0-input").send_keys("New York")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/p[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]/div[1]/div[2]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[6]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]/div[1]/div[2]/span[1]/img[1]").click()
    #
    # def test_seatgeek_b20d38a9(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/nav[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'NBA')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'NBA Finals')]").click()
    #
    # def test_seatgeek_bb3e2b61(self):
    #     # self.driver.get("https://seatgeek.com")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Change Location')]").click()
    #     self.driver.find_element(By.ID, "downshift-0-input").clear()
    #     self.driver.find_element(By.ID, "downshift-0-input").send_keys("Los Angeles")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Filter by')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'16')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'16')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Apply')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]/div[1]/div[2]/span[1]/img[1]").click()
    