import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_slash_format


@pytest.mark.usefixtures("setup_class")
class TestEnterprise:
    
    # def test_enterprise_22e33a38(self):
    #     # self.driver.get("https://enterprise.com")
    #     self.driver.find_element(By.XPATH, "//ul[@id='list-adca73d180']/li[6]/article[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "button-ac6a7bd320").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Beverly Hills')]").click()
    #     self.driver.find_element(By.ID, "pickupCalendarFocusable").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[6]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "time-picker-1").clear()
    #     self.driver.find_element(By.ID, "time-picker-1").select("11 00 AM")
    #     self.driver.find_element(By.ID, "dropoffCalendarFocusable").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[6]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "time-picker-2").clear()
    #     self.driver.find_element(By.ID, "time-picker-2").select("5 00 PM")
    #     self.driver.find_element(By.ID, "continueButton").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='2' and @type='checkbox']").click()
    #     self.driver.find_element(By.ID, "vehicleSortBy").clear()
    #     self.driver.find_element(By.ID, "vehicleSortBy").select("Price  Low to High")
    #
    # def test_enterprise_2cb6558b(self):
    #     # self.driver.get("https://enterprise.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='primary-nav']/ul[1]/li[4]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='navContentCarSales']/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rocket-body-b4ddd57-sidebar']/div[1]/div[2]/div[2]/div[1]/div[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rocket-body-b4ddd57-sidebar']/div[1]/div[2]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/div[2]/a[1]/div[1]/div[1]/svg[1]/path[1]").click()
    
    def test_enterprise_d5054276(self):
        # self.driver.get("https://enterprise.com")
        # time.sleep(10)
        self.driver.find_element(By.XPATH, "//nav[@id='primary-nav']/ul[1]/li[3]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='navContentLocations']/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "pickupLocationTextBox").clear()
        self.driver.find_element(By.ID, "pickupLocationTextBox").send_keys("02199")
        self.driver.find_element(By.XPATH, "//li[@id='location-US-02199-Boston']/a[1]/span[1]/span[1]").click()

        time.sleep(1)
        # somehow the following click actions is not performed but passed, tried to add 1-second sleep and issue is solved
        self.driver.find_element(By.ID, "continueButton").click()
        self.driver.find_element(By.ID, "1046329").click()
        self.driver.find_element(By.ID, "pickupCalendarFocusable").click()

        start_date_str, end_date_str = calculate_dates_slash_format(7, 9)
        # self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, f"//button[@data-test-id='{start_date_str}']").click()

        # self.driver.find_element(By.ID, "time-picker-1").clear()
        # self.driver.find_element(By.ID, "time-picker-1").select("11 00 AM")
        pick_up_time_dropdown = self.driver.find_element(By.XPATH, "//select[@data-dtm-tracking='dropdown|PICKUPtime|original']")
        pick_up_time_select = Select(pick_up_time_dropdown)
        pick_up_time_select.select_by_value('11:00 AM')

        self.driver.find_element(By.XPATH, "//button[@id='dropoffCalendarFocusable']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, f"//button[@data-test-id='{end_date_str}']").click()

        # self.driver.find_element(By.ID, "time-picker-2").clear()
        # self.driver.find_element(By.ID, "time-picker-2").select("1 00 PM")
        return_time_dropdown = self.driver.find_element(By.XPATH, "//select[@data-dtm-tracking='dropdown|RETURNtime|original']")
        return_time_select = Select(return_time_dropdown)
        return_time_select.select_by_value('1:00 PM')

        self.driver.find_element(By.ID, "continueButton").click()
        self.driver.find_element(By.XPATH, "//input[@value='300' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@value='2' and @type='checkbox']").click()
        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main']/div/section/ul/li[1]/div/div[1]/div[2]/div/div/div[2]/button").click()

        # self.driver.find_element(By.XPATH, "//main[@id='main']/div[2]/section[1]/div[1]/div[5]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-code='GPS']//button[@aria-label='Add']").click()

        self.driver.find_element(By.XPATH, "//main[@id='main']/div[2]/div[1]/button[1]").click()
    
    # def test_enterprise_9572e7bd(self):
    #     # self.driver.get("https://enterprise.com")
    #     self.driver.find_element(By.ID, "pickupLocationTextBox").clear()
    #     self.driver.find_element(By.ID, "pickupLocationTextBox").send_keys("BIRMINGHAM")
    #     self.driver.find_element(By.XPATH, "//li[@id='location-1019041']/a[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "sameLocation").click()
    #     self.driver.find_element(By.ID, "dropoffLocationTextBox").clear()
    #     self.driver.find_element(By.ID, "dropoffLocationTextBox").send_keys("MONTGOM")
    #     self.driver.find_element(By.XPATH, "//li[@id='location-1020546']/a[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "pickupCalendarFocusable").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[4]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "time-picker-1").clear()
    #     self.driver.find_element(By.ID, "time-picker-1").select("11 00 AM")
    #     self.driver.find_element(By.XPATH, "//button[@id='dropoffCalendarFocusable']/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[7]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "time-picker-2").clear()
    #     self.driver.find_element(By.ID, "time-picker-2").select("5 00 PM")
    #     self.driver.find_element(By.ID, "continueButton").click()
    #     self.driver.find_element(By.ID, "vehicleSortBy").clear()
    #     self.driver.find_element(By.ID, "vehicleSortBy").select("Price  Low to High")
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/button[1]").click()
    #
    # def test_enterprise_1df0723c(self):
    #     # self.driver.get("https://enterprise.com")
    #     self.driver.find_element(By.ID, "pickupLocationTextBox").clear()
    #     self.driver.find_element(By.ID, "pickupLocationTextBox").send_keys("Brooklyn")
    #     self.driver.find_element(By.XPATH, "//li[@id='location-5148346']/small[1]").click()
    #     self.driver.find_element(By.ID, "age").clear()
    #     self.driver.find_element(By.ID, "age").select("18")
    #     self.driver.find_element(By.ID, "continueButton").click()
    #
    # def test_enterprise_8b079ace(self):
    #     # self.driver.get("https://enterprise.com")
    #     self.driver.find_element(By.ID, "pickupLocationTextBox").clear()
    #     self.driver.find_element(By.ID, "pickupLocationTextBox").send_keys("New York JFK")
    #     self.driver.find_element(By.XPATH, "//li[@id='location-1018781']/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='pickupCalendarFocusable']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "dropoffCalendarFocusable").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "continueButton").click()
    #
    # def test_enterprise_67f9fb2d(self):
    #     # self.driver.get("https://enterprise.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='primary-nav']/ul[1]/li[2]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='navContentVehicles']/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore Vehicles')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn More')]").click()
    #
    # def test_enterprise_7180c4d1(self):
    #     # self.driver.get("https://enterprise.com")
    #     self.driver.find_element(By.ID, "pickupLocationTextBox").clear()
    #     self.driver.find_element(By.ID, "pickupLocationTextBox").send_keys("JFK")
    #     self.driver.find_element(By.XPATH, "//li[@id='location-1018781']/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "pickupCalendarFocusable").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "time-picker-1").clear()
    #     self.driver.find_element(By.ID, "time-picker-1").select("11 00 AM")
    #     self.driver.find_element(By.ID, "dropoffCalendarFocusable").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[5]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "continueButton").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='200' and @type='checkbox']").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='vehicleSortBy']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='vehicleSortBy']").select("Low to High")
    #     self.driver.find_element(By.XPATH, "//input[@value='4' and @type='checkbox']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/button[1]").click()
    #
    # def test_enterprise_f7b93dc1(self):
    #     # self.driver.get("https://enterprise.com")
    #     self.driver.find_element(By.ID, "viewModifyCancelBookingWidget").click()
    #     self.driver.find_element(By.ID, "confirmationNumber").clear()
    #     self.driver.find_element(By.ID, "confirmationNumber").send_keys("123456")
    #     self.driver.find_element(By.ID, "firstName").click()
    #     self.driver.find_element(By.ID, "firstName").clear()
    #     self.driver.find_element(By.ID, "firstName").send_keys("James")
    #     self.driver.find_element(By.ID, "lastName").clear()
    #     self.driver.find_element(By.ID, "lastName").send_keys("Buck")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    # def test_enterprise_c0eeead1(self):
    #     # self.driver.get("https://enterprise.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='teaser-a760c8c0ad']/a[1]").click()
    #     self.driver.find_element(By.ID, "first-name").clear()
    #     self.driver.find_element(By.ID, "first-name").send_keys("Allan")
    #     self.driver.find_element(By.ID, "last-name").clear()
    #     self.driver.find_element(By.ID, "last-name").send_keys("Smith")
    #     self.driver.find_element(By.ID, "email").clear()
    #     self.driver.find_element(By.ID, "email").send_keys("allan.smith@gmail.com")
    #     self.driver.find_element(By.ID, "emailConfirm").clear()
    #     self.driver.find_element(By.ID, "emailConfirm").send_keys("allan.smith@gmail.com")
    #     self.driver.find_element(By.ID, "postal").clear()
    #     self.driver.find_element(By.ID, "postal").send_keys("10001")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    # def test_enterprise_ce34bc61(self):
    #     # self.driver.get("https://enterprise.com")
    #     self.driver.find_element(By.ID, "pickupLocationTextBox").clear()
    #     self.driver.find_element(By.ID, "pickupLocationTextBox").send_keys("Brooklyn")
    #     self.driver.find_element(By.ID, "location-5110302").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='pickupCalendarFocusable']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[4]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='dropoffCalendarFocusable']/span[1]/i[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='book']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[7]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "age").clear()
    #     self.driver.find_element(By.ID, "age").select("22")
    #     self.driver.find_element(By.ID, "vehicle-filters-trigger").click()
    #     self.driver.find_element(By.ID, "Vans-402-select").click()
    #     self.driver.find_element(By.XPATH, "//body[@id='page-5757efa00c']/div[7]/div[1]/div[1]/div[1]/div[3]/div[1]/button[2]").click()
    #     self.driver.find_element(By.ID, "continueButton").click()
    