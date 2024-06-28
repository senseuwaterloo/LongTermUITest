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
class TestSeatgeek:
    
    def test_seatgeek_8f6261cf(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Change Location')]").click()
        self.driver.find_element(By.ID, "downshift-2-input").clear()
        self.driver.find_element(By.ID, "downshift-2-input").send_keys("New York")
        self.driver.find_element(By.XPATH, "//li[@id='downshift-2-item-0']/p[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Filter by')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'1')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'30')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Apply')]").click()
    
    def test_seatgeek_918d7ef3(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Help & Support')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Buying Tickets')]").click()
    
    def test_seatgeek_9c3cba90(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/nav[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Hamilton')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[7]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/section[2]/div[2]/ul[1]/li[3]/a[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[4]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/button[3]").click()
        self.driver.find_element(By.ID, "promo-toggle").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[4]/div[1]/div[1]/div[2]/section[3]/div[1]/span[2]/span[1]/div[1]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[4]/div[1]/div[1]/div[2]/section[3]/div[1]/span[2]/div[1]/div[1]/div[1]/button[3]/div[1]/span[1]").click()
    
    def test_seatgeek_10de6ac5(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trending')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Beyonce')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/section[2]/div[2]/ul[1]/li[1]/a[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/img[1]").click()
    
    def test_seatgeek_563ec938(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/nav[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'WWE')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Wrestlemania')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Parking')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/section[2]/div[2]/ul[1]/li[2]/a[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]/div[1]/span[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/button[3]/div[1]/span[1]").click()
    
    def test_seatgeek_6760de22(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/nav[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'NBA')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Los Angeles Lakers')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Parking')]").click()
    
    def test_seatgeek_74226fab(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Genres')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Pop')]").click()
    
    def test_seatgeek_78915162(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//input[@name='search' and @value='' and @type='text' and @placeholder='Search by team, artist, event, or venue']").click()
        self.driver.find_element(By.XPATH, "//input[@name='search' and @value='' and @type='text' and @placeholder='Search by team, artist, event, or venue']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='search' and @value='' and @type='text' and @placeholder='Search by team, artist, event, or venue']").send_keys("Coldplay")
        self.driver.find_element(By.XPATH, "//p[@title='Coldplay']").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[4]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[2]/span[1]").click()
    
    def test_seatgeek_e93fe82b(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Genres')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Classic Rock')]").click()
    
    def test_seatgeek_fbaa5c83(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Change Location')]").click()
        self.driver.find_element(By.ID, "downshift-2-input").clear()
        self.driver.find_element(By.ID, "downshift-2-input").send_keys("Chicago")
        self.driver.find_element(By.XPATH, "//li[@id='downshift-2-item-0']/p[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/ul[1]/li[8]/a[1]/div[1]/div[2]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[6]/div[1]/div[1]/main[1]/div[2]/button[1]/div[1]/span[2]").click()
    
    def test_seatgeek_c50985ee(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Festivals')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'M3 Rock Festival')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/main[1]/div[1]/div[2]/div[1]/section[2]/div[2]/ul[1]/li[1]/a[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/button[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/button[4]/span[1]").click()
    
    def test_seatgeek_c7058499(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Genres')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Jazz')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[5]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[1]/div[1]/div[2]/div[1]/div[1]/button[4]").click()
        self.driver.find_element(By.XPATH, "//div[@id='start-of-content']/div[5]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/p[2]/button[1]").click()
    
    def test_seatgeek_ac59be41(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Change Location')]").click()
        self.driver.find_element(By.ID, "downshift-0-input").clear()
        self.driver.find_element(By.ID, "downshift-0-input").send_keys("New York")
        self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/p[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]/div[1]/div[2]/span[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[6]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]/div[1]/div[2]/span[1]/img[1]").click()
    
    def test_seatgeek_b20d38a9(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/nav[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'NBA')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'NBA Finals')]").click()
    
    def test_seatgeek_bb3e2b61(self):
        # self.driver.get("https://seatgeek.com")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Change Location')]").click()
        self.driver.find_element(By.ID, "downshift-0-input").clear()
        self.driver.find_element(By.ID, "downshift-0-input").send_keys("Los Angeles")
        self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/p[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Filter by')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'16')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'16')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Apply')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]/div[1]/div[2]/span[1]/img[1]").click()
    