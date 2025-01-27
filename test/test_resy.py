import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_full_month_name, scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestResy:
    
    # def test_resy_790ba0ec(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-menu-container[1]/div[1]/button[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Profile')]").click()
    #     self.driver.find_element(By.ID, "DateInput__month").clear()
    #     self.driver.find_element(By.ID, "DateInput__month").select("January")
    #     self.driver.find_element(By.ID, "DateInput__day").clear()
    #     self.driver.find_element(By.ID, "DateInput__day").select("05")
    #     self.driver.find_element(By.ID, "DateInput__year").clear()
    #     self.driver.find_element(By.ID, "DateInput__year").select("1980")
    #     self.driver.find_element(By.ID, "bio").clear()
    #     self.driver.find_element(By.ID, "bio").send_keys("Love Ramen Noodles")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-account[1]/article[1]/section[1]/div[2]/resy-account-profile[1]/div[1]/form[1]/div[1]/div[2]/div[6]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-account[1]/article[1]/section[1]/div[2]/resy-account-profile[1]/div[1]/form[1]/div[1]/div[2]/div[6]/div[1]/div[5]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-account[1]/article[1]/section[1]/div[2]/resy-account-profile[1]/div[1]/form[1]/div[1]/div[2]/button[1]/span[1]").click()
    #
    # def test_resy_96cf7de0(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Toronto')]").click()
    #     self.driver.find_element(By.ID, "region-new").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[5]/i[1]").click()
    #     self.driver.find_element(By.ID, "DateSelector__button").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='DayPicker']/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[7]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/div[4]/div[11]/div[2]/div[2]/div[3]/button[5]").click()
    #     self.driver.find_element(By.ID, "rgs://resy/67572/1994781/2/2023-04-22/2023-04-22/21:00:00/2/Dining Room").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[2]/div[4]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[3]/div[4]/div[1]/button[1]/span[1]").click()
    #
    # def test_resy_f61456ed(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").send_keys("Tsiakkos & Charcoal")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-1-item-0']/div[1]/div[2]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/venue-page[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/p[1]").click()
    #
    # def test_resy_4b33554f(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").send_keys("Pizza")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']/span[1]/span[1]/b[1]").click()
    #     self.driver.find_element(By.ID, "party_size").clear()
    #     self.driver.find_element(By.ID, "party_size").select("6 Guests")
    #
    # def test_resy_51b75f3d(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]/i[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Austin')]").click()
    #     self.driver.find_element(By.ID, "region-new").click()
    #     self.driver.find_element(By.ID, "DateSelector__button").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='DayPicker']/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[6]/button[1]").click()
    #     self.driver.find_element(By.ID, "party_size").clear()
    #     self.driver.find_element(By.ID, "party_size").select("2 Guests")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='rgs://resy/62880/2090838/3/2023-04-21/2023-04-21/12:00:00/2/Dining']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[2]/div[4]/div[1]/button[1]/span[1]").click()
    #
    # def test_resy_5f09e15c(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]/i[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Miami')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-autowhatever-1']/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[2]/i[1]/i[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/events-by-location[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/a[1]").click()
    #     self.driver.find_element(By.ID, "tickets").clear()
    #     self.driver.find_element(By.ID, "tickets").select("3 Tickets")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/event-details-container[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[2]/div[4]/div[1]/button[1]").click()
    #
    # def test_resy_1bb8d48f(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View All Open Positions')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main-container']/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Software Development')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hybrid')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main-container']/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/p[1]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pcs-body-container']/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/span[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "dialogTemplate-dialogForm-StatementBeforeAuthentificationContent-ContinueButton").click()
    #
    # def test_resy_3596733f(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").send_keys("vegetarian")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']/span[1]/span[1]/b[1]").click()
    #     self.driver.find_element(By.ID, "DateSelector__button").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='DayPicker']/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/button[1]").click()
    #
    # def test_resy_3eae65d9(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").send_keys("high tide")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-1-item-0']/div[1]/div[2]/h3[1]").click()
    #     self.driver.find_element(By.ID, "DropdownGroup__selector--date--selection").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='DayPicker']/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[2]/button[1]").click()
    #     self.driver.find_element(By.ID, "party_size").clear()
    #     self.driver.find_element(By.ID, "party_size").select("2 Guests")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/venue-page[1]/div[1]/div[1]/div[1]/div[3]/div[4]/div[1]/button[1]/span[1]").click()
    #
    # def test_resy_4a4ecf18(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]/i[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Los Angeles')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").send_keys("diner")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-1-item-0']/div[1]/div[2]/h3[1]").click()
    #     self.driver.find_element(By.ID, "party_size").clear()
    #     self.driver.find_element(By.ID, "party_size").select("3 Guests")
    #     self.driver.find_element(By.ID, "DropdownGroup__selector--date--selection").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='DayPicker']/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[6]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='rgs://resy/11465/1776860/2/2023-03-10/2023-03-10/21:00:00/3/Dining Room']/div[1]").click()
    #
    # def test_resy_126b4604(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Los Angeles')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-home[1]/algorithmic-lists[1]/div[1]/article[1]/section[1]/div[1]/div[1]/article[3]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]").click()
    #     self.driver.find_element(By.ID, "DropdownGroup__selector--date--selection").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='DayPicker']/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[6]/button[1]").click()
    #     self.driver.find_element(By.ID, "party_size").clear()
    #     self.driver.find_element(By.ID, "party_size").select("3 Guests")
    #     self.driver.find_element(By.XPATH, "//button[@id='rgs://resy/66715/1972183/2/2023-04-07/2023-04-07/17:00:00/3/Outdoor Table']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[2]/div[4]/div[1]/button[1]").click()
    #
    # def test_resy_164cf025(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Seattle')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-autowhatever-1']/div[1]/div[1]/button[9]/span[2]").click()
    #
    # def test_resy_92869590(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sydney')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").send_keys("pasta")
    #     self.driver.find_element(By.XPATH, "//input[@value='pasta' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/i[1]/svg[1]/path[1]").click()
    #
    # def test_resy_ab1ae27a(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").send_keys("CHIANTI")
    #     self.driver.find_element(By.ID, "party_size").clear()
    #     self.driver.find_element(By.ID, "party_size").select("4 Guests")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/venue-page[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[5]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='rgs://rgs/62634/1916772/3/2023-03-30/2023-03-30/13:30:00/4/Dining Room']/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[2]/div[4]/div[1]/button[1]/span[1]").click()
    #
    # def test_resy_b1055658(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'see more ›')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/events-by-location[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/a[1]").click()
    #     self.driver.find_element(By.ID, "tickets").clear()
    #     self.driver.find_element(By.ID, "tickets").select("1 Ticket")
    #     self.driver.find_element(By.XPATH, "//button[@id='rgs://resy/5013/2141070/6/2023-04-13/2023-04-13/17:00:00/1/Lounge']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[2]/div[4]/div[1]/button[1]/span[1]").click()
    #
    # def test_resy_e031c695(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-home[1]/home-header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='content']/div[1]/div[1]/div[1]/article[3]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@title='Twitter']").click()
    #
    # def test_resy_e0ff7945(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'New York')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").send_keys("indian")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']/span[1]/span[1]/b[1]").click()
    #     self.driver.find_element(By.ID, "DateSelector__button").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='DayPicker']/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[4]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/button[5]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='rgs://resy/63515/1949649/2/2023-04-12/2023-04-12/20:15:00/2/C4']/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[2]/div[4]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/confirmation-page[1]/div[1]/div[2]/div[3]/button[1]/span[1]").click()
    #
    # def test_resy_ef23fbf3(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]/i[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Atlanta')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").send_keys("pizza")
    #     self.driver.find_element(By.XPATH, "//input[@value='pizza' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").click()
    #
    # def test_resy_f4bad8a9(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-home[1]/home-header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='content']/div[1]/div[2]/div[1]/article[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='venue-1']/div[2]/p[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='rgs://resy/70556/2112637/3/2023-04-06/2023-04-06/12:30:00/2/Outdoor Counter']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[2]/div[4]/div[1]/button[1]/span[1]").click()
    #
    # def test_resy_f4c21e9f(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search restaurants, cuisines, etc.']").send_keys("thai")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-1-item-1']/div[1]/div[2]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page-content']/venue-page[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/button[47]/span[1]").click()
    #     self.driver.find_element(By.ID, "end-time").clear()
    #     self.driver.find_element(By.ID, "end-time").select("7 00 PM")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Confirm')]").click()
    #
    # def test_resy_60bfb72f(self):
    #     # self.driver.get("https://resy.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]/i[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Boston')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'see more ›')]").click()
    #     self.driver.find_element(By.ID, "DateSelector__button").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='DayPicker']/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[7]/button[1]").click()

    def test_resy_75db63ac(self):
        # self.driver.get("https://resy.com")

        nearby_restaurants_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Nearby Restaurants')]")
        scroll_to_element(self.driver, nearby_restaurants_link)
        nearby_restaurants_link.click()

        # self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/resy-nav[1]/header[1]/div[2]/resy-locations-container[1]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
        # //div[@id="page-wrapper"]/resy-nav/header/div[2]/div[1]/resy-locations-container/div/div/button/div/div
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'LocationsContainer__click-container') and contains(@aria-label, 'Location')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Chicago')]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Chicago']").click()

        # add extra step to handle possible popups
        if self.driver.find_element(By.XPATH, "//button[@data-test-id='announcement_modal-button-close']") is not None:
            self.driver.find_element(By.XPATH, "//button[@data-test-id='announcement_modal-button-close']").click()

        self.driver.find_element(By.ID, "DateSelector__button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='DayPicker']/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[5]/button[1]").click()
        start_date_str, _ = calculate_dates_full_month_name(7, 7)
        if self.driver.find_element(By.XPATH, f"//button[contains(@aria-label, '{start_date_str}')]") is None:
            self.driver.find_element(By.XPATH, "//button[@aria-label='Next month']").click()
        self.driver.find_element(By.XPATH, f"//button[contains(@aria-label, '{start_date_str}')]").click()

        # self.driver.find_element(By.ID, "party_size").clear()
        # self.driver.find_element(By.ID, "party_size").select("7 Guests")
        party_size_dropdown = self.driver.find_element(By.ID, "party_size")
        party_size_select = Select(party_size_dropdown)
        party_size_select.select_by_value("7")

        # self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[5]/i[1]/i[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='page-content']/resy-search[1]/resy-search-container[1]/div[1]/div[1]/div[1]/div[4]/div[5]/div[2]/div[2]/div[4]/button[5]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='rgs://resy/61091/1808411/3/2023-04-20/2023-04-20/14:00:00/7/Dining Room']/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/summary-page[1]/div[1]/div[2]/div[4]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/confirmation-page[1]/div[1]/div[2]/div[3]/button[1]/span[1]").click()
        top_rated_restaurant = self.driver.find_element(By.XPATH, "//article[@aria-labelledby='region-top-rated']/div[1]/div[1]/div[1]")
        scroll_to_element(self.driver, top_rated_restaurant)
        top_rated_restaurant.click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        party_time_dropdown = self.driver.find_element(By.ID, "time")
        party_time_select = Select(party_time_dropdown)
        party_time_select.select_by_value("1400")
        self.driver.find_element(By.XPATH, "//button[@data-test-id='venue-page-save']").click()
    