import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates


@pytest.mark.usefixtures("setup_class")
class TestAmctheatres:
    
    # def test_amctheatres_925a2307(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Check Gift Card Balance')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='number' and @value='' and @type='number' and @placeholder='Gift Card Number']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='number' and @value='' and @type='number' and @placeholder='Gift Card Number']").send_keys("87654321")
    #     self.driver.find_element(By.XPATH, "//input[@name='pin' and @value='' and @type='number' and @placeholder='Gift Card Pin']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='pin' and @value='' and @type='number' and @placeholder='Gift Card Pin']").send_keys("9753")
    #     self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]").click()
    #
    # def test_amctheatres_2cdee3d3(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[17]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Get Tickets')]").click()
    #     self.driver.find_element(By.ID, "showtimes-theatre-filter").clear()
    #     self.driver.find_element(By.ID, "showtimes-theatre-filter").select("Change Location...")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").send_keys("90028")
    #     self.driver.find_element(By.ID, "icon_search").click()
    #
    # def test_amctheatres_330d5618(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Food & Drinks')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore Menu')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View Full Menu')]").click()
    #
    # def test_amctheatres_36ab5d78(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Our Theatres')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Theatre')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").send_keys("10001")
    #     self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/i[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[2]/a[1]/span[1]").click()
    #
    # def test_amctheatres_66d12284(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Food & Drinks')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Order Food & Drinks')]").click()
    #     self.driver.find_element(By.ID, "showtimes-theatre-filter").clear()
    #     self.driver.find_element(By.ID, "showtimes-theatre-filter").select("AMC Grove City 14")
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-body']/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='concessions-categories']/div[3]/button[1]/picture[1]/source[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='concessions-categories']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Add to Order')]").click()
    #
    # def test_amctheatres_6b831239(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'On Demand')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Now Trending')]").click()
    #
    # def test_amctheatres_779cec8e(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Our Theatres')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search by City, Zip or Theatre']").send_keys("10001")
    #     self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/i[1]/svg[1]").click()
    #
    # def test_amctheatres_90557510(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See A Movie')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Coming Soon')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[1]/label[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[1]/label[1]/select[1]").select("AMC Artisan Films")
    #
    # def test_amctheatres_cfaa49bd(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Our Theatres')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Theatre')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Wichita')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ShowtimesScroll']/main[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/h2[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Get Tickets')]").click()
    #
    # def test_amctheatres_05e1f2bd(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Check Balance')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='number' and @value='' and @type='number' and @placeholder='Gift Card Number']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='number' and @value='' and @type='number' and @placeholder='Gift Card Number']").send_keys("1000000000000000")
    #     self.driver.find_element(By.XPATH, "//input[@name='pin' and @value='' and @type='number' and @placeholder='Gift Card Pin']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='pin' and @value='' and @type='number' and @placeholder='Gift Card Pin']").send_keys("1222")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    # def test_amctheatres_130b1cd5(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'On Demand')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'On Sale Now')]").click()
    #     self.driver.find_element(By.ID, "RG9kUHJvZHVjdDo4MDQyNDE=").click()
    #     self.driver.find_element(By.ID, "vod-cta-Rent").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-container']/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]").click()
    #
    # def test_amctheatres_22509b64(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Food & Drinks')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore Menu')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View Full Menu')]").click()
    
    def test_amctheatres_29f47ddb(self):
        # self.driver.get("https://www.amctheatres.com")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Sign In to AMC Stubs Account']").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("UITestStudy2024")
        self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Sign In']").click()
        # need to wait for a few second to wait for the login window to disappear to avoid: selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Change Theatre Location']").click()
        self.driver.find_element(By.XPATH, "//input[@aria-labelledby='theatreLocatorHeadline']").click()
        self.driver.find_element(By.XPATH, "//input[@aria-labelledby='theatreLocatorHeadline']").send_keys("AMC Grove City 14")
        self.driver.find_element(By.XPATH, "//i[@aria-label='Submit Search']").click()
        self.driver.find_element(By.XPATH, "//*[@id='modal-body']/div[2]/div/div/div/div[2]/ul/li[1]/label/div[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='modal-body']/div[2]/div/div/div/div[3]/button").click()
        self.driver.find_element(By.XPATH, "//li[@id='qa-desktop-sub-nav-find-a-theatre']/div/a").click()

        theatre_dropdown_element = self.driver.find_element(By.ID, "showtimes-theatre-filter")
        select = Select(theatre_dropdown_element)
        select.select_by_value('amc-grove-city-14')

        date_dropdown_element = self.driver.find_element(By.ID, "showtimes-date-filter")
        select = Select(date_dropdown_element)
        start_date_str, end_date_str = calculate_dates(1, 2)
        select.select_by_value(start_date_str)
        # select the first movie and first timeslot from the page
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div[3]/main/div/div[1]/section/div/div[1]/div/div[2]/div[1]/div/section/div[1]/div/div[1]/a").click()
        # select the first 4 seats in the first row to avoid seats being unavailable
        self.driver.find_element(By.XPATH, "//*[@id='react-container']/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[1]/ul/li[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='react-container']/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[1]/ul/li[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='react-container']/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[1]/ul/li[3]").click()
        self.driver.find_element(By.XPATH, "//*[@id='react-container']/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[1]/ul/li[4]").click()
        self.driver.find_element(By.ID, "checkout-continue").click()
    
    # def test_amctheatres_f8428085(self):
    #     # self.driver.get("https://amctheatres.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'On Demand')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'New Releases')]").click()
    