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
class TestFoxsports:
    
    def test_foxsports_2daa15a5(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='nav']/div[2]/div[2]/ul[1]/li[6]/a[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Leagues, teams, players, shows, personalities...']").click()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Leagues, teams, players, shows, personalities...']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Leagues, teams, players, shows, personalities...']").send_keys("formula 1")
        self.driver.find_element(By.XPATH, "//div[@id='exploreApp']/div[3]/div[1]/div[2]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/button[1]/span[2]").click()
    
    def test_foxsports_691c18cc(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ssrExploreSports']/div[2]/a[13]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[2]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a[8]/div[2]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[3]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[1]").click()
    
    def test_foxsports_ed60077a(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/a[5]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='nav']/div[2]/div[2]/ul[1]/li[5]/a[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='14139d99-2e1e-53c3-a10f-960c9b9d907d']/div[5]/div[1]/button[1]/img[1]").click()
    
    def test_foxsports_20b51cb9(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/a[9]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[3]/h2[1]").click()
    
    def test_foxsports_e4bb7e5b(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[2]/h2[1]").click()
    
    def test_foxsports_fce75183(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/a[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[7]/h2[1]").click()
    
    def test_foxsports_00cef5a2(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='nav']/div[2]/div[2]/ul[1]/li[7]/a[1]/div[2]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Leagues, teams, players, shows, personalities...']").click()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Leagues, teams, players, shows, personalities...']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Leagues, teams, players, shows, personalities...']").send_keys("Chicago Bulls")
        self.driver.find_element(By.XPATH, "//div[@id='exploreApp']/div[3]/div[1]/div[2]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[2]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[3]").click()
    
    def test_foxsports_af97084c(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ssrExploreSports']/div[2]/a[7]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ssrExploreApp-https://api.foxsports.com/bifrost/v1/explore/browse/sports/soccer']/div[2]/div[3]/a[5]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='exploreApp']/div[2]/div[3]/a[5]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[7]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]").click()
    
    def test_foxsports_c254dcec(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ssrExploreSports']/div[2]/a[7]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ssrExploreApp-https://api.foxsports.com/bifrost/v1/explore/browse/sports/soccer']/div[2]/div[3]/a[22]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='exploreApp']/div[2]/div[3]/a[15]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[5]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//table[@id='roster-table-3']/tbody[1]/tr[8]/td[1]/div[1]/a[1]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[2]/h2[1]").click()
    
    def test_foxsports_e6c7934b(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='nav']/div[2]/div[2]/ul[1]/li[4]/a[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/a[5]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'UEFA CHAMPIONS LEAGUE')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[2]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]/a[1]/div[2]/div[2]/div[1]/div[2]/button[1]").click()
    
    def test_foxsports_0ad8d621(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/a[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]/ul[1]/li[1]/a[1]/h2[1]").click()
    
    def test_foxsports_14d4edf5(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='nav']/div[2]/div[2]/ul[1]/li[2]/a[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/a[6]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'FEATURED MATCHES')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'ENGLISH PREMIER LEAGUE')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[29]").click()
    
    def test_foxsports_14f5587e(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='nav']/div[2]/div[2]/ul[1]/li[7]/a[1]/div[2]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Leagues, teams, players, shows, personalities...']").click()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Leagues, teams, players, shows, personalities...']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Leagues, teams, players, shows, personalities...']").send_keys("Lebron James")
        self.driver.find_element(By.XPATH, "//div[@id='exploreApp']/div[3]/div[1]/div[2]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[2]/h2[1]").click()
    
    def test_foxsports_85bd1881(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='nav']/div[2]/div[2]/ul[1]/li[4]/a[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/a[5]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/a[2]/h2[1]").click()
    
    def test_foxsports_86ea50f5(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/a[5]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]/ul[1]/li[2]/a[1]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]").click()
    
    def test_foxsports_8ab30c9e(self):
        # self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='nav']/div[2]/div[2]/ul[1]/li[2]/a[1]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/a[4]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]/span[1]").click()
    