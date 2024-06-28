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
class TestNba:
    
    def test_nba_3284c80e(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'History')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[1]/div[1]/div[2]/div[1]/a[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div[3]/div[1]/div[2]/section[1]/div[1]/div[2]/ul[1]/li[10]/div[1]/article[1]/div[1]/div[1]/a[1]/header[1]/h3[1]/span[1]").click()
    
    def test_nba_33567ac0(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[13]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "typeahead-input-desktop").clear()
        self.driver.find_element(By.ID, "typeahead-input-desktop").send_keys("Devin Booker")
        self.driver.find_element(By.XPATH, "//strong[contains(.,'devin')]").click()
        self.driver.find_element(By.XPATH, "//img[@alt=\"Men's Phoenix Suns Devin Booker Nike Purple 2022/23 Swingman Jersey - Classic Edition\"]").click()
        self.driver.find_element(By.XPATH, "//div[@id='size-selector-list']/a[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Add to Cart')]").click()
    
    def test_nba_802babc8(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[14]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "5").click()
        self.driver.find_element(By.XPATH, "//nav[@id='side-nav']/div[2]/div[1]/div[4]/div[2]/ul[1]/li[3]/a[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='side-nav']/div[2]/div[2]/div[6]/div[2]/ul[1]/li[3]/a[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='side-nav']/div[2]/div[2]/div[6]/div[2]/ul[1]/li[3]/a[1]").click()
    
    def test_nba_86abe4d3(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Players')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='players_traditional']/div[3]/a[1]/h2[1]").click()
    
    def test_nba_97c9f03c(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'NBA TV')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/a[1]/figure[1]/img[1]").click()
    
    def test_nba_a6cb6d95(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[7]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[7]/div[1]/div[1]/div[1]/div[1]/a[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/header[1]/div[3]/nav[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Team Stats')]").click()
        self.driver.find_element(By.XPATH, "//select[@name='']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='']").select("2021-22")
        self.driver.find_element(By.XPATH, "//button[@id='bx-close-inside-2078917']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[2]/label[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[2]/label[1]/div[1]/select[1]").select("Regular Season")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[4]/label[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[4]/label[1]/div[1]/select[1]").select("In Game Splits")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[3]/label[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[3]/label[1]/div[1]/select[1]").select("Per Game")
    
    def test_nba_ca2d4bc8(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Leaders')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div[3]/section[1]/div[1]/div[1]/div[4]/label[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div[3]/section[1]/div[1]/div[1]/div[4]/label[1]/div[1]/select[1]").select("BLK")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div[3]/section[1]/div[1]/div[1]/div[3]/label[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div[3]/section[1]/div[1]/div[1]/div[3]/label[1]/div[1]/select[1]").select("Totals")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Brook Lopez')]").click()
    
    def test_nba_d457bbda(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'League Pass Schedule')]").click()
        self.driver.find_element(By.XPATH, "//select[@name='team']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='team']").select("Boston Celtics")
    
    def test_nba_b94d41fd(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[14]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/section[2]/section[2]/div[1]/section[1]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "/html/body[1]/section[2]/section[2]/div[1]/section[1]/div[1]/div[1]/select[1]").select("March")
        self.driver.find_element(By.XPATH, "/html/body[1]/section[2]/section[2]/div[1]/section[1]/div[1]/div[2]/select[1]").clear()
        self.driver.find_element(By.XPATH, "/html/body[1]/section[2]/section[2]/div[1]/section[1]/div[1]/div[2]/select[1]").select("Chicago Bulls")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Tickets')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See More')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Buy Tickets')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modalContent']/div[3]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@role='text' and @value='$645+' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='text' and @value='$645+' and @type='text']").send_keys("500")
        self.driver.find_element(By.XPATH, "//span[@role='tab' and @value='best']").click()
        self.driver.find_element(By.ID, "edp-quantity-filter-button").click()
        self.driver.find_element(By.XPATH, "//form[@id='edp-filter']/div[1]/div[1]/div[4]/div[1]/button[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='edp-filter']/div[1]/div[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='edp-filter']/div[1]/div[1]/div[1]/select[1]").select("1 Ticket")
    
    def test_nba_c7f8145b(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tickets')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/section[2]/section[2]/div[1]/section[1]/div[1]/div[2]/select[1]").clear()
        self.driver.find_element(By.XPATH, "/html/body[1]/section[2]/section[2]/div[1]/section[1]/div[1]/div[2]/select[1]").select("Atlanta Hawks")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Tickets')]").click()
    
    def test_nba_d45a8834(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'2022-23 Season Schedule')]").click()
        self.driver.find_element(By.XPATH, "//select[@name='cal']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='cal']").select("April")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'PREVIEW')]").click()
    
    def test_nba_d806070d(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[8]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search Players']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search Players']").send_keys("Devin Booker")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[2]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/a[1]/div[2]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Stats')]").click()
        self.driver.find_element(By.XPATH, "//select[@name='']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='']").select("Playoffs")
        self.driver.find_element(By.XPATH, "//th[@title='Points']").click()
    
    def test_nba_dfd411d4(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Leaders')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div[3]/section[1]/div[1]/div[1]/div[4]/label[1]/div[1]/select[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div[3]/section[1]/div[1]/div[1]/div[4]/label[1]/div[1]/select[1]").select("AST")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'James Harden')]").click()
    
    def test_nba_e002abb1(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Power Rankings')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div[2]/div[2]/div[1]/ul[1]/li[1]/div[1]/article[1]/div[1]/div[1]/a[1]/header[1]/h3[1]/span[1]").click()
    
    def test_nba_ead2dce9(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//select[@name='cal']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='cal']").select("March")
        self.driver.find_element(By.XPATH, "//button[@id='bx-close-inside-2078917']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//select[@name='team']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='team']").select("Denver Nuggets")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'TICKETS')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='modalContent']/div[3]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "filter-bar-quantity").clear()
        self.driver.find_element(By.ID, "filter-bar-quantity").select("1 Ticket")
        self.driver.find_element(By.XPATH, "//input[@role='text' and @value='$115' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='text' and @value='$115' and @type='text']").send_keys("200")
        self.driver.find_element(By.XPATH, "//input[@role='number' and @value='$4,000+' and @type='number']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='number' and @value='$4,000+' and @type='number']").send_keys("200")
    
    def test_nba_0c381f1c(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[8]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search Players']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search Players']").send_keys("chris paul")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[2]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/a[1]/div[2]/p[1]").click()
    
    def test_nba_0e6568b3(self):
        # self.driver.get("https://www.nba.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[7]/a[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[7]/div[1]/div[1]/div[1]/div[5]/a[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/header[1]/div[3]/nav[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Group Tickets')]").click()
    