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
class TestNfl:
    
    def test_nfl_ae088c6f(self):
        # self.driver.get("https://www.nfl.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='mobile-expanded-menu']/ul[1]/li[8]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[4]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/a[1]/div[2]").click()
    
    def test_nfl_9c14e1b7(self):
        # self.driver.get("https://www.nfl.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='mobile-expanded-menu']/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "Season").clear()
        self.driver.find_element(By.ID, "Season").select("2019")
        self.driver.find_element(By.ID, "Week").clear()
        self.driver.find_element(By.ID, "Week").select("Super Bowl")
    
    def test_nfl_91843d71(self):
        # self.driver.get("https://www.nfl.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='mobile-expanded-menu']/ul[1]/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tom Brady')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Stats')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Career')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[3]/div[1]/div[1]/div[1]/div[2]/table[1]/thead[1]/tr[1]/th[10]").click()
    
    def test_nfl_9ebd069a(self):
        # self.driver.get("https://www.nfl.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='mobile-expanded-menu']/ul[1]/li[17]/a[1]/span[1]/span[1]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='2ndlevel']/li[10]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'WATCH')]").click()
    
    def test_nfl_a1d1f6c0(self):
        # self.driver.get("https://www.nfl.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='mobile-expanded-menu']/ul[1]/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Team Schedules')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedule')]").click()
    
    def test_nfl_c577375b(self):
        # self.driver.get("https://www.nfl.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='mobile-expanded-menu']/ul[1]/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "player-search-input").clear()
        self.driver.find_element(By.ID, "player-search-input").send_keys("James Smith")
        self.driver.find_element(By.ID, "player-search-button").click()
    
    def test_nfl_cb07d410(self):
        # self.driver.get("https://www.nfl.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='mobile-expanded-menu']/ul[1]/li[7]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Field Goals')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Justin Tucker')]").click()
    
    def test_nfl_f75e33a6(self):
        # self.driver.get("https://www.nfl.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='mobile-expanded-menu']/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "Season").clear()
        self.driver.find_element(By.ID, "Season").select("2020")
    
    def test_nfl_fc81025d(self):
        # self.driver.get("https://www.nfl.com/")
        self.driver.find_element(By.XPATH, "//nav[@id='mobile-expanded-menu']/ul[1]/li[17]/a[1]/span[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='2ndlevel']/li[10]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[6]/div[1]/div[2]/div[2]/button[2]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[6]/div[1]/div[2]/div[1]/div[1]/div[8]/div[1]/a[1]/div[1]/h3[1]").click()
    
    def test_nfl_03e45ce0(self):
        # self.driver.get("https://www.nfl.com/")
        self.driver.find_element(By.XPATH, "//div[@id='nfl-o-headlinestack__tab-panel-a4ed51ed-31c1-44fd-8f1e-a0dc3bc1637a']/ol[1]/li[1]/div[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/article[1]/div[2]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[3]/a[1]/span[1]/svg[1]/use[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/article[1]/div[2]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[3]/a[1]/span[1]/svg[1]").click()
    