import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_budget_dates


@pytest.mark.usefixtures("setup_class")
class TestNyc:
    
    # def test_nyc_d6545454(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'hotels.')]").click()
    #     self.driver.find_element(By.ID, "dp1678884099792").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'17')]").click()
    #     self.driver.find_element(By.ID, "dp1678884099793").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'20')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='rooms']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='rooms']").select("1 Room")
    #     self.driver.find_element(By.XPATH, "//select[@name='r1a']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='r1a']").select("2 Adults")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[6]/div[1]/div[1]/form[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='priceRange' and @value='200' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='area' and @value='n-11' and @type='radio']").click()
    #
    # def test_nyc_62a611ff(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'sports.')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'View Tickets')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sea-inventory-filtersBtncnt']/div[1]/div[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sea-filterCard-wrapper']/div[3]/fieldset[1]/div[1]/label[3]").click()
    #     self.driver.find_element(By.ID, "sea-all-in-pricing-toggle-btn").click()
    #     self.driver.find_element(By.ID, "sea-filterCard-submit-btn").click()
    #
    # def test_nyc_e5fdff20(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'tours.')]").click()
    #     self.driver.find_element(By.XPATH, "//li[contains(.,'Top Tours')]").click()
    #
    # def test_nyc_196cde81(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'shopping.')]").click()
    #     self.driver.find_element(By.XPATH, "//li[contains(.,'Neighborhood')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Chelsea')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bookstore (3)')]").click()
    #
    # def test_nyc_1a807a1c(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'restaurants.')]").click()
    #     self.driver.find_element(By.XPATH, "//li[contains(.,'Cuisine')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'African')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'east village (2)')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'$16 to $30 (2)')]").click()
    
    def test_nyc_1cc13b4e(self):
        # self.driver.get("https://nyc.com")

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'hotels.')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='container' and not(ancestor::footer)]/nav[@class='topnav']/ul[1]//a[text()='hotels.']").click()

        # self.driver.find_element(By.ID, "dp1679077297101").click()
        # self.driver.find_element(By.NAME, "checkin").click()
        # self.driver.find_element(By.XPATH, "//span[text()='Check In']").click()
        # click will be intercepted if use span check in, so try to use its parent
        self.driver.find_element(By.XPATH, "//span[text()='Check In']/ancestor::*[1][self::label]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'24')]").click()
        (start_date_year, start_date_month_adjusted, start_date_day), (end_date_year, end_date_month_adjusted, end_date_day) = calculate_budget_dates(7, 10)
        if self.driver.find_element(By.XPATH, f"//td[@data-year='{start_date_year}' and @data-month='{start_date_month_adjusted}']//a[text()='{start_date_day}']") is None:
            self.driver.find_element(By.XPATH, "//a[@data-handler='next' and @data-event='click' and @title='Next']").click()

        self.driver.find_element(By.XPATH, f"//td[@data-year='{start_date_year}' and @data-month='{start_date_month_adjusted}']//a[text()='{start_date_day}']").click()

        # self.driver.find_element(By.ID, "dp1679077297102").click()
        # self.driver.find_element(By.NAME, "checkout").click()
        #  Elements not found: xpath = //span[text()='Check Out']/ancestor::*[1][self::label]. page changed after click check in so be careful with the locator. "-"
        self.driver.find_element(By.XPATH, "//span[text()='Check-Out']/ancestor::*[1][self::label]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'27')]").click()
        if self.driver.find_element(By.XPATH, f"//td[@data-year='{end_date_year}' and @data-month='{end_date_month_adjusted}']//a[text()='{end_date_day}']") is None:
            self.driver.find_element(By.XPATH, "//a[@data-handler='next' and @data-event='click' and @title='Next']").click()

        self.driver.find_element(By.XPATH, f"//td[@data-year='{end_date_year}' and @data-month='{end_date_month_adjusted}']//a[text()='{end_date_day}']").click()

        # self.driver.find_element(By.XPATH, "//select[@name='rooms']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='rooms']").select("1 Room")
        room_dropdown = self.driver.find_element(By.NAME, "rooms")
        room_select = Select(room_dropdown)
        room_select.select_by_visible_text("1 Room")

        # self.driver.find_element(By.XPATH, "//select[@name='r1a']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='r1a']").select("2 Adults")
        adult_dropdown = self.driver.find_element(By.NAME, "r1a")
        adult_select = Select(adult_dropdown)
        adult_select.select_by_visible_text("2 Adults")

        # self.driver.find_element(By.XPATH, "//select[@name='r1c']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='r1c']").select("1 Child")
        child_dropdown = self.driver.find_element(By.NAME, "r1c")
        child_select = Select(child_dropdown)
        child_select.select_by_visible_text("1 Child")

        # self.driver.find_element(By.XPATH, "//select[@name='r1c1a']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='r1c1a']").select("0")
        age_dropdown = self.driver.find_element(By.NAME, "r1c1a")
        age_select = Select(age_dropdown)
        age_select.select_by_visible_text("0")

        self.driver.find_element(By.XPATH, "/html/body[1]/div[6]/div[1]/div[1]/form[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='priceRange' and @value='200' and @type='radio']").click()
        self.driver.find_element(By.XPATH, "//input[@name='area' and @value='' and @type='radio']").click()

        # self.driver.find_element(By.NAME, "area").click()
        self.driver.find_element(By.XPATH, "//label[contains(., 'Central Park') and ./input[@id='area' and @type='radio'] and ancestor::*[1][self::div and not(@class='more')]]").click()
    
    # def test_nyc_f5d4d405(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'sports.')]").click()
    #     self.driver.find_element(By.NAME, "searchbyname").clear()
    #     self.driver.find_element(By.NAME, "searchbyname").send_keys("New york knicks")
    #     self.driver.find_element(By.XPATH, "//p[contains(.,'New York Knicks')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'View Tickets')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sea-inventory-filtersBtncnt']/div[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "price-filter-max").clear()
    #     self.driver.find_element(By.ID, "price-filter-max").send_keys("200")
    #     self.driver.find_element(By.ID, "price-filter-min").clear()
    #     self.driver.find_element(By.ID, "price-filter-min").send_keys("100")
    #     self.driver.find_element(By.ID, "sea-filterCard-submit-btn").click()
    #
    # def test_nyc_2ef75333(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'tours.')]").click()
    #     self.driver.find_element(By.XPATH, "//li[contains(.,'Boat Tours')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[2]/div[3]/article[75]/div[5]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'View Tickets Now')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[5]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/div[1]/div[2]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='inputOverlay']/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[1]/div[3]/div[2]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[1]/div[3]/div[2]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
    #
    # def test_nyc_4fe76361(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'broadway.')]").click()
    #     self.driver.find_element(By.XPATH, "//li[contains(.,'Shows By Date')]").click()
    #
    # def test_nyc_7ad37a91(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'restaurants.')]").click()
    #     self.driver.find_element(By.XPATH, "//li[contains(.,'Cuisine')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Indian/Pakistani')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'east village (9)')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'$16 to $30 (4)')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Reservations')]").click()
    #
    # def test_nyc_86897828(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'concerts.')]").click()
    #     self.driver.find_element(By.NAME, "searchbyname").clear()
    #     self.driver.find_element(By.NAME, "searchbyname").send_keys("all star stand up comedy")
    #     self.driver.find_element(By.XPATH, "//p[contains(.,'All Star Stand Up Comedy')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'View Tickets')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sea-inventory-filtersBtncnt']/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "sort-type-label").click()
    #     self.driver.find_element(By.ID, "sea-filterCard-submit-btn").click()
    #
    # def test_nyc_8aedabbf(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'restaurants.')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/section[1]/div[1]/div[1]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='name' and @type='text' and @placeholder='Search by restaurant name, cuisine, or anything between _']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='name' and @type='text' and @placeholder='Search by restaurant name, cuisine, or anything between _']").send_keys("La Bergamote")
    #     self.driver.find_element(By.XPATH, "//input[@value='Search' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//h2[contains(.,'La Bergamote — Midtown')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Reservation')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='mainContent']/div[1]/div[2]/div[1]/section[1]/nav[1]/ol[1]/li[3]/button[1]").click()
    #     self.driver.find_element(By.ID, "menu-tab-button-dinner-menu").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='restProfileMenuContent']/div[1]/button[1]").click()
    #
    # def test_nyc_a531a379(self):
    #     # self.driver.get("https://nyc.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'attractions.')]").click()
    #     self.driver.find_element(By.XPATH, "//li[contains(.,'Neighborhood')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Midtown')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Art Galleries (5)')]").click()
    