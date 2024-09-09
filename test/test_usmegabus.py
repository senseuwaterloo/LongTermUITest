import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_full_month_name


@pytest.mark.usefixtures("setup_class")
class TestUsMegabus:
    
    # def test_usmegabus_a3b7ff6e(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Help')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'What do I do if I lost an item on the bus?')]").click()
    #
    # def test_usmegabus_f464de6d(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Check my bus')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Track my bus')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @placeholder='From']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @placeholder='From']").send_keys("Abbotsford")
    #     self.driver.find_element(By.XPATH, "//div[@id='react-tabs-1']/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-tabs-9']/div[2]/div[1]/div[1]/div[1]").click()
    #
    # def test_usmegabus_3358dffd(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.ID, "startingAt").clear()
    #     self.driver.find_element(By.ID, "startingAt").send_keys("Houston")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/mb-typeahead-component[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "goingTo").clear()
    #     self.driver.find_element(By.ID, "goingTo").send_keys("Dallas")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/mb-typeahead-component[1]/div[1]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.ID, "mat-input-0").click()
    #     self.driver.find_element(By.XPATH, "//mat-calendar[@id='mat-datepicker-0']/mat-calendar-header[1]/div[1]/div[1]/button[3]").click()
    #     self.driver.find_element(By.XPATH, "//mat-calendar[@id='mat-datepicker-0']/div[1]/mat-month-view[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "mat-input-1").click()
    #     self.driver.find_element(By.XPATH, "//mat-calendar[@id='mat-datepicker-1']/div[1]/mat-month-view[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "findTickets").click()
    #
    # def test_usmegabus_44ad28c9(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.ID, "startingAt").clear()
    #     self.driver.find_element(By.ID, "startingAt").send_keys("Albany, NY")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/mb-typeahead-component[1]/div[1]/div[1]/div[2]/div[2]").click()
    #     self.driver.find_element(By.ID, "goingTo").clear()
    #     self.driver.find_element(By.ID, "goingTo").send_keys("Bloomington, NY")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/mb-typeahead-component[1]/div[1]/div[1]/div[2]/div[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "mat-input-0").click()
    #     self.driver.find_element(By.XPATH, "//mat-calendar[@id='mat-datepicker-0']/mat-calendar-header[1]/div[1]/div[1]/button[3]").click()
    #     self.driver.find_element(By.XPATH, "//mat-calendar[@id='mat-datepicker-0']/div[1]/mat-month-view[1]/table[1]/tbody[1]/tr[3]/td[2]/div[1]").click()
    #     self.driver.find_element(By.ID, "findTickets").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='heading2']/div[1]/div[2]/button[1]").click()
    #
    # def test_usmegabus_4b99412b(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Check my bus')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Track my bus')]").click()
    #     self.driver.find_element(By.ID, "react-tabs-2").click()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @placeholder='Search by Service Number']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @placeholder='Search by Service Number']").send_keys("10000001")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='10000001' and @placeholder='Search by Service Number']").click()
    
    def test_usmegabus_54d60a7c(self):
        # self.driver.get("https://us.megabus.com")

        # Need to handle popup...
        if self.driver.find_element(By.XPATH, "//button[text()='Decline Offer']") is not None:
            self.driver.find_element(By.XPATH, "//button[text()='Decline Offer']").click()

        self.driver.find_element(By.ID, "startingAt").clear()
        self.driver.find_element(By.ID, "startingAt").send_keys("albany")

        # self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/mb-typeahead-component[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
        # need to wait for a few seconds otherwise a wrong item will be selected
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[./input[@id='startingAt']]//div[@title='Enter a town or city']/div[1]/div[2]").click()

        self.driver.find_element(By.ID, "goingTo").clear()
        self.driver.find_element(By.ID, "goingTo").send_keys("New York")

        # self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/mb-typeahead-component[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
        # need to wait for a few seconds otherwise a wrong item will be selected
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[./input[@id='goingTo']]//div[@title='Enter a town or city']/div[1]/div[2]").click()

        # need to wait for a few seconds otherwise the calendar will close immediately after opening due to the previous actions is finishing
        time.sleep(2)
        self.driver.find_element(By.ID, "mat-input-0").click()

        # self.driver.find_element(By.XPATH, "//mat-calendar[@id='mat-datepicker-0']/div[1]/mat-month-view[1]/table[1]/tbody[1]/tr[3]/td[7]/div[1]").click()
        start_date_str, end_date_str = calculate_dates_full_month_name(7, 14)
        if self.driver.find_element(By.XPATH, f"//td[@aria-label='{start_date_str}']") is None:
            self.driver.find_element(By.XPATH, "//button[@aria-label='Next month']").click()

        self.driver.find_element(By.XPATH, f"//td[@aria-label='{start_date_str}']").click()

        self.driver.find_element(By.ID, "mat-input-1").click()

        # self.driver.find_element(By.XPATH, "//mat-calendar[@id='mat-datepicker-1']/div[1]/mat-month-view[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]").click()
        if self.driver.find_element(By.XPATH, f"//td[@aria-label='{end_date_str}']") is None:
            self.driver.find_element(By.XPATH, "//button[@aria-label='Next month']").click()

        self.driver.find_element(By.XPATH, f"//td[@aria-label='{end_date_str}']").click()

        self.driver.find_element(By.ID, "totalPassengers").clear()
        self.driver.find_element(By.ID, "totalPassengers").send_keys("3")
        self.driver.find_element(By.ID, "findTickets").click()
    
    # def test_usmegabus_7eff6c15(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Check my bus')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Track my bus')]").click()
    #     self.driver.find_element(By.ID, "react-tabs-2").click()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @placeholder='Search by Service Number']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @placeholder='Search by Service Number']").send_keys("SE4")
    #     self.driver.find_element(By.XPATH, "//div[@id='react-tabs-3']/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    # def test_usmegabus_ab139e9d(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Check my bus')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Track my bus')]").click()
    #     self.driver.find_element(By.ID, "react-tabs-2").click()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @placeholder='Search by Service Number']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @placeholder='Search by Service Number']").send_keys("5456165184")
    #
    # def test_usmegabus_ba5e0124(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/fieldset[1]/mb-radio-group[1]/div[1]/label[1]").click()
    #     self.driver.find_element(By.ID, "startingAt").clear()
    #     self.driver.find_element(By.ID, "startingAt").send_keys("New York")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/mb-typeahead-component[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "goingTo").clear()
    #     self.driver.find_element(By.ID, "goingTo").send_keys("Washington")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/mb-typeahead-component[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='totalPassengers_plus']/span[2]").click()
    #     self.driver.find_element(By.ID, "findTickets").click()
    #     self.driver.find_element(By.ID, "sortselected").clear()
    #     self.driver.find_element(By.ID, "sortselected").select("Price")
    #     self.driver.find_element(By.XPATH, "//div[@id='heading1']/a[1]").click()
    #
    # def test_usmegabus_0592744b(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Help')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Can I cancel and/or get a refund for my reservation?')]").click()
    #
    # def test_usmegabus_122af0dc(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.ID, "startingAt").clear()
    #     self.driver.find_element(By.ID, "startingAt").send_keys("Chicago")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/mb-typeahead-component[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "goingTo").clear()
    #     self.driver.find_element(By.ID, "goingTo").send_keys("Ann Arbor")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/mb-typeahead-component[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "findTickets").click()
    #
    # def test_usmegabus_2ce0a80e(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bus stops')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Altavista, VA')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Altavista Commons (Walmart parking lot)')]").click()
    #
    # def test_usmegabus_2e2cb6d9(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bus stops')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Abbotsford, WI')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Super 39 Shell')]").click()
    #
    # def test_usmegabus_14b5885e(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Route map')]").click()
    #     self.driver.find_element(By.ID, "startingAt").clear()
    #     self.driver.find_element(By.ID, "startingAt").send_keys("Abbotsford")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Abbotsford, WI')]").click()
    #     self.driver.find_element(By.ID, "goingTo").clear()
    #     self.driver.find_element(By.ID, "goingTo").send_keys("Sheboygan")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Sheboygan, WI')]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.ID, "mat-input-0").click()
    #     self.driver.find_element(By.XPATH, "//mat-calendar[@id='mat-datepicker-0']/div[1]/mat-month-view[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "findTickets").click()
    #
    # def test_usmegabus_1538e37b(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bus stops')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Alanson, MI')]").click()
    #
    # def test_usmegabus_21e5c264(self):
    #     # self.driver.get("https://us.megabus.com")
    #     self.driver.find_element(By.ID, "startingAt").clear()
    #     self.driver.find_element(By.ID, "startingAt").send_keys("New York")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/mb-typeahead-component[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "goingTo").clear()
    #     self.driver.find_element(By.ID, "goingTo").send_keys("Alfred")
    #     self.driver.find_element(By.XPATH, "//main[@id='homepageContentArea']/div[1]/mb-user-home[1]/div[1]/div[1]/div[1]/div[1]/div[1]/mb-journey-planner-lite[1]/div[1]/div[1]/mb-journey-search[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/mb-typeahead-component[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "mat-input-0").click()
    #     self.driver.find_element(By.XPATH, "//mat-calendar[@id='mat-datepicker-0']/div[1]/mat-month-view[1]/table[1]/tbody[1]/tr[5]/td[6]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='totalPassengers_plus']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='totalPassengers_plus']/span[2]").click()
    #     self.driver.find_element(By.ID, "findTickets").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='heading1']/div[1]/div[2]/button[1]").click()
    