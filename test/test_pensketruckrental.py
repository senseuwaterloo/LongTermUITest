import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_day_month_format, scroll_down


@pytest.mark.usefixtures("setup_class")
class TestPensketruckrental:
    
    def test_pensketruckrental_d1c3d4d2(self):
        # self.driver.get("https://pensketruckrental.com")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='right-side']//a[contains(text(),'Locations')]").click()

        # redundant action in the new web page
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Location')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Massachusetts')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Norwood')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='big-container no-map']//a[contains(text(),'Norwood')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'All Seasons Rent All')]").click()
        # page is still loading and lead to selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted:
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Seasons Rent')]").click()

        # self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
        # self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("NORWOOD")
        # self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[2]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='appRoot']/section[1]/form[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='appRoot']/section[1]/form[1]/fieldset[2]/div[1]/div[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[18]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[19]/span[1]").click()
        # self.driver.find_element(By.ID, "truck_size_select").clear()
        # self.driver.find_element(By.ID, "truck_size_select").select("High Roof Cargo Van (Up to 1 Room)")
        # self.driver.find_element(By.XPATH, "//div[@id='appRoot']/section[1]/form[1]/div[2]/div[1]/button[1]").click()

        # page is still loading and lead to selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted:
        time.sleep(3)
        self.driver.find_element(By.ID, "returntoSB").click()
        # somehow dropdown will not expand with typical click method. Try click with JS
        # self.driver.find_element(By.XPATH, "//div[contains(@id, 'sSidebar_Posts_')]//div[@class='quote_truck_size_select']/span[text()='Truck Size']").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[contains(@id, 'sSidebar_Posts_')]//div[@class='quote_truck_size_select']/span[text()='Truck Size']").get_native_element())
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'sSidebar_Posts_')]//span[@data-truck-name='Cargo Van (Up to 1 Room)']").click()
        start_day, start_month, end_day, end_month = calculate_dates_day_month_format(14, 15)
        self.driver.find_element(By.ID, "mat-input-1").click()
        self.driver.find_element(By.XPATH, f"//div[contains(@class, 'month-container')]/month[./header/p[text()='{start_month}']]/div[1]/date[./div/span[text()='{start_day}']]").click()
        self.driver.find_element(By.XPATH, f"//div[contains(@class, 'month-container')]/month[./header/p[text()='{end_month}']]/div[1]/date[./div/span[text()='{end_day}']]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Continue ']").click()
        self.driver.find_element(By.ID, "submitbuttonSB").click()
    
    # def test_pensketruckrental_ed4fe7c1(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Commercial Rental')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Commercial Trucks')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='s_menu__commercial-items_0_0_28_0_0_1_2_0_2_0']/button[1]").click()
    #     self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
    #     self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("newark")
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='quoteFormId']/fieldset[1]/div[1]/div[1]/div[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='quoteFormId']/fieldset[2]/div[1]/div[1]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[13]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[15]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Select')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='container']/section[1]/div[5]/div[1]/button[1]").click()
    #
    # def test_pensketruckrental_0ea84d8f(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Renting from Penske')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Plan Your Move')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Load')]").click()
    #
    # def test_pensketruckrental_31bd1b59(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
    #     self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("Detroit")
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "drop_location_txtbox").clear()
    #     self.driver.find_element(By.ID, "drop_location_txtbox").send_keys("Cleveland")
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "pickupdate").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[18]/span[1]").click()
    #     self.driver.find_element(By.ID, "quote_truck_size_select").clear()
    #     self.driver.find_element(By.ID, "quote_truck_size_select").select("12 Foot Truck (1-2 Rooms)")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #
    # def test_pensketruckrental_4288a464(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Renting from Penske')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'How to Load a Moving Truck')]").click()
    #
    # def test_pensketruckrental_56cb11f2(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Trucks')]").click()
    #     self.driver.find_element(By.ID, "view-comparison").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='desktop-view-trucks']/table[2]/tbody[1]/tr[1]/td[4]/a[1]/strong[1]").click()
    #
    # def test_pensketruckrental_5abf54a3(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Trucks')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='s_menu__main-items_0_0_19_0_0_1_2_0_1_1']/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
    #     self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("Oregon")
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]").click()
    #     self.driver.find_element(By.ID, "drop_location_txtbox").clear()
    #     self.driver.find_element(By.ID, "drop_location_txtbox").send_keys("Cleveland")
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #
    # def test_pensketruckrental_6a414da4(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Trucks')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Truck Wizard')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'+')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sPost_0_0_19_0_53_1_2_2_0']/div[1]/article[1]/div[1]/div[1]/div[1]/div[4]/div[1]/truckwizard-app[1]/room-items[1]/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/ul[1]/li[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'+')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Get a Quote')]").click()
    #
    # def test_pensketruckrental_7137b440(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
    #     self.driver.find_element(By.ID, "loc_input").click()
    #     self.driver.find_element(By.ID, "loc_input").clear()
    #     self.driver.find_element(By.ID, "loc_input").send_keys("Dallas")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Dallas')]").click()
    #     self.driver.find_element(By.ID, "dosearch").click()
    #
    # def test_pensketruckrental_9d57aa74(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Supplies & Services')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Self-Storage Rentals')]").click()
    #     self.driver.find_element(By.ID, "sparefoot-zip").clear()
    #     self.driver.find_element(By.ID, "sparefoot-zip").send_keys("02155")
    #     self.driver.find_element(By.ID, "sparefootSubmit").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='sqft' and @value='100' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='order' and @value='price' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='amenities' and @value='twenty_four_hour_access' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='search-results']/table[1]/tbody[1]/tr[1]/td[2]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
    #
    # def test_pensketruckrental_bcf178b2(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Trucks')]").click()
    #     self.driver.find_element(By.ID, "view-comparison").click()
    #
    # def test_pensketruckrental_c25e97d4(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Locations')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Location')]").click()
    #     self.driver.find_element(By.ID, "loc_input").clear()
    #     self.driver.find_element(By.ID, "loc_input").send_keys("Seattle")
    #     self.driver.find_element(By.ID, "dosearch").click()
    #
    # def test_pensketruckrental_ef760dc5(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Trucks')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='s_menu__main-items_0_0_19_0_0_1_2_0_0_1']/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "pickup_location_txtbox").clear()
    #     self.driver.find_element(By.ID, "pickup_location_txtbox").send_keys("DAYTON")
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "drop_location_txtbox").clear()
    #     self.driver.find_element(By.ID, "drop_location_txtbox").send_keys("TEXAS CITY")
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "pickupdate").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='web-component-container']/div[1]/div[1]/ul[1]/li[34]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #
    # def test_pensketruckrental_f0ae88cd(self):
    #     # self.driver.get("https://pensketruckrental.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='featured-jobs']/div[1]/article[1]/div[2]/div[1]/a[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='main-search']/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='btn-direct_stateDisambig']/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'New York (25)')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='btn-direct_cityDisambig']/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rochester, NY (5)')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='btn-direct_sortOptions']/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sort by Date')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='direct_listingDiv']/ul[2]/li[1]/h4[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply Now')]").click()
    