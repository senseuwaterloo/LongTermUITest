import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.mark.usefixtures("setup_class")
class TestTicketcenter:
    
    def test_ticketcenter_9223f1b4(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("Wicked")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/ul[1]/li[1]/a[1]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterContainer']/div[2]/span[6]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Select Date Range']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[2]/div[2]/table[1]/thead[1]/tr[1]/th[3]/i[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[2]/div[2]/table[1]/thead[1]/tr[1]/th[3]/i[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[2]/div[2]/table[1]/thead[1]/tr[1]/th[3]").click()
        self.driver.find_element(By.XPATH, "//td[contains(.,'1')]").click()
        self.driver.find_element(By.XPATH, "//td[contains(.,'24')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='daterangepicker_start' and @value='' and @type='text']").click()
        self.driver.find_element(By.XPATH, "//input[@name='daterangepicker_start' and @value='' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='daterangepicker_start' and @value='' and @type='text']").send_keys("10/5/23")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
    
    def test_ticketcenter_6bf5cdf6(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").click()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("Amy Grant")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/ul[1]/li[1]/a[1]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[1]/td[3]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "price-selected-label").click()
        self.driver.find_element(By.ID, "price-filter-min").click()
        self.driver.find_element(By.ID, "price-filter-min").clear()
        self.driver.find_element(By.ID, "price-filter-min").send_keys("200")
        self.driver.find_element(By.ID, "price-filter-max").click()
        self.driver.find_element(By.ID, "price-filter-max").clear()
        self.driver.find_element(By.ID, "price-filter-max").send_keys("300")
        self.driver.find_element(By.ID, "filter-price-done").click()
    
    def test_ticketcenter_7dfdeddd(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Theatre')]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[2]/td[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//tbody[@id='content-area']/tr[1]/td[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pre-checkout-delivery-ctn']/div[1]").click()
    
    def test_ticketcenter_bf7321eb(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'NBA')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Miami Heat')]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[4]/td[3]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "qty-selected-label").click()
        self.driver.find_element(By.XPATH, "//div[@id='qty-hidden-filter']/div[1]/label[6]").click()
        self.driver.find_element(By.XPATH, "//tbody[@id='content-area']/tr[14]/td[3]/table[1]/tbody[1]/tr[1]/td[4]/button[1]/span[1]").click()
    
    def test_ticketcenter_2177b546(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("adele")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/ul[1]/li[1]/a[1]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[5]/td[3]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "qty-filter").click()
        self.driver.find_element(By.XPATH, "//div[@id='qty-hidden-filter']/div[1]/label[3]").click()
        self.driver.find_element(By.XPATH, "//tbody[@id='content-area']/tr[55]/td[3]/table[1]/tbody[1]/tr[1]/td[4]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys("adelefan@hotmail.com")
        self.driver.find_element(By.ID, "delivery-entry-submit-button").click()
    
    def test_ticketcenter_c55b9949(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'City Guides')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Phoenix')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterContainer']/div[2]/span[8]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Next 3 days')]").click()
    
    def test_ticketcenter_d1e46885(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").click()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("New york yankees")
        self.driver.find_element(By.XPATH, "//a[@role='option']").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[2]/td[3]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "type-filter").click()
        self.driver.find_element(By.XPATH, "//div[@id='ticket-types']/label[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sea-type-filter-modal-child']/div[6]/button[1]").click()
    
    def test_ticketcenter_d7631fa2(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Concerts')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rap / Hip Hop')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterContainer']/div[2]/span[6]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'This weekend')]").click()
    
    def test_ticketcenter_da800367(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").click()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("Lubbock, Texas")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/span[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@title='All dates']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Next 7 days')]").click()
    
    def test_ticketcenter_f3850ec8(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'City Guides')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Boston')]").click()
    
    def test_ticketcenter_fb73611b(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//div[@id='sports-geo']/table[1]/tbody[1]/tr[7]/td[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='qty-filter']/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='qty-hidden-filter']/div[1]/label[6]").click()
        self.driver.find_element(By.XPATH, "//tbody[@id='content-area']/tr[1]/td[3]/table[1]/tbody[1]/tr[1]/td[4]/button[1]").click()
    
    def test_ticketcenter_fdcac1e8(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("los angeles kings")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/ul[1]/li[1]/a[1]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterContainer']/div[2]/span[6]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'This weekend')]").click()
    
    def test_ticketcenter_acc194d4(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Concerts')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Reggae')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterContainer']/div[2]/span[6]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'This weekend')]").click()
    
    def test_ticketcenter_bb02400d(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'WWE Tickets')]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[5]/td[3]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "qty-selected-label").click()
        self.driver.find_element(By.XPATH, "//div[@id='qty-hidden-filter']/div[1]/label[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='legend-ctn']/div[2]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='legend-ctn']/div[2]/ul[1]/li[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//tbody[@id='content-area']/tr[1]/td[3]/table[1]/tbody[1]/tr[1]/td[4]/button[1]/span[1]").click()
    
    def test_ticketcenter_5b85b4e5(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tickets as Gifts – Best Tickets to Buy Online')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Dave Chapelle')]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[1]/td[3]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "qty-selected-label").click()
        self.driver.find_element(By.XPATH, "//div[@id='qty-hidden-filter']/div[1]/label[3]").click()
        self.driver.find_element(By.XPATH, "//tbody[@id='content-area']/tr[90]/td[3]/table[1]/tbody[1]/tr[1]/td[4]/button[1]").click()
    
    def test_ticketcenter_5e01c2f7(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'NFL')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Chicago Bears')]").click()
    
    def test_ticketcenter_6a56a1fb(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'City Guides')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Los Angeles')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterContainer']/div[2]/span[8]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'This weekend')]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[1]/td[3]/a[1]/span[1]").click()
    
    def test_ticketcenter_904bd858(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").click()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("New york knicks")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/ul[1]/li[1]/a[1]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[1]/td[3]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-hidden-label']/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sort-cntr']/div[3]/div[1]").click()
    
    def test_ticketcenter_9b18e5e4(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'WWE Tickets')]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[2]/td[3]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "price-selected-label").click()
        self.driver.find_element(By.ID, "price-filter-min").clear()
        self.driver.find_element(By.ID, "price-filter-min").send_keys("50")
        self.driver.find_element(By.ID, "price-filter-max").clear()
        self.driver.find_element(By.ID, "price-filter-max").send_keys("100")
        self.driver.find_element(By.ID, "filter-price-done").click()
        self.driver.find_element(By.XPATH, "//tbody[@id='content-area']/tr[1]/td[3]/table[1]/tbody[1]/tr[1]/td[4]/button[1]/span[1]").click()
    
    def test_ticketcenter_2bce1096(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Theatre')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Off-Broadway')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterContainer']/div[2]/span[6]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Select Date Range']").click()
        self.driver.find_element(By.XPATH, "//td[contains(.,'19')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='daterangepicker_end' and @value='' and @type='text']").click()
        self.driver.find_element(By.XPATH, "//td[contains(.,'19')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
    
    def test_ticketcenter_4d73937b(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All MLB Tickets')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterContainer']/div[2]/span[6]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'This weekend')]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[1]/td[3]/a[1]/span[1]").click()
    
    def test_ticketcenter_5199e802(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("Ballet")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/span[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='filterContainer']/div[2]/span[8]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Next 30 days')]").click()
    
    def test_ticketcenter_549452ab(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'NFL')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All NFL Tickets')]").click()
    
    def test_ticketcenter_55631305(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("red sox vs yankees")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/span[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[9]/td[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='qty-filter']/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='qty-hidden-filter']/div[1]/label[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='price-filter']/div[2]/span[1]").click()
        self.driver.find_element(By.ID, "price-filter-max").clear()
        self.driver.find_element(By.ID, "price-filter-max").send_keys("200")
        self.driver.find_element(By.XPATH, "//label[@id='sea-all-in-price-toggle']/span[1]").click()
        self.driver.find_element(By.ID, "filter-price-done").click()
        self.driver.find_element(By.XPATH, "//tbody[@id='content-area']/tr[1]/td[3]/table[1]/tbody[1]/tr[1]/td[4]/button[1]/span[1]").click()
    
    def test_ticketcenter_73de3022(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("Hamilton")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/ul[1]/li[1]/a[1]/strong[1]").click()
    
    def test_ticketcenter_8d9e09e1(self):
        # self.driver.get("https://ticketcenter.com")
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='query' and @value='' and @type='text' and @placeholder='Search for artists, teams or venues...']").send_keys("professional boxing")
        self.driver.find_element(By.XPATH, "//div[@id='spotlight']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/ul[1]/li[1]/a[1]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'CES Boxing')]").click()
        self.driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']/tbody[1]/tr[1]/td[3]/a[1]/span[1]").click()
    