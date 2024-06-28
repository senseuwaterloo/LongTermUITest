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
class TestImdb:
    
    def test_imdb_e39333ef(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("Donnie Darko")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-0']/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/section[4]/div[1]/div[1]/a[1]/h3[1]/span[1]").click()
    
    def test_imdb_e8b1cc02(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.XPATH, "//label[@id='imdbHeader-navDrawerOpen']/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/ul[1]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@title='Click to add to watchlist']").click()
    
    def test_imdb_38093911(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("terminator")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-3']/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[2]/div[2]/div[1]/div[2]/button[1]/span[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
    
    def test_imdb_5fe49ab4(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("Prometheus")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-0']/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/section[7]/div[5]/ul[1]/li[1]/a[2]/svg[1]").click()
    
    def test_imdb_73782df1(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.XPATH, "//label[@id='imdbHeader-navDrawerOpen']/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/ul[1]/a[3]/span[1]").click()
        self.driver.find_element(By.ID, "lister-sort-by-options").clear()
        self.driver.find_element(By.ID, "lister-sort-by-options").select("IMDb Rating")
    
    def test_imdb_4bce534f(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "iconContext-menu").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/div[1]/ul[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'1990')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Denzel Washington')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[3]/section[2]/div[5]/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[3]/section[2]/div[5]/div[1]/div[1]/div[4]/div[1]/ul[1]/li[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[3]/section[2]/div[5]/div[1]/div[1]/div[4]/div[1]/ul[1]/li[2]/div[1]/div[1]/svg[1]").click()
    
    def test_imdb_4ee87dc8(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/div[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@title='Edit']").click()
    
    def test_imdb_4f208b8b(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("The Last of Us")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-0']/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[3]/div[2]/div[2]/div[3]/div[1]/button[1]/div[1]/div[1]").click()
    
    def test_imdb_551ab381(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.XPATH, "//label[@id='imdbHeader-navDrawerOpen']/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[1]/div[1]/div[1]/ul[1]/a[1]/span[1]").click()
    
    def test_imdb_55518089(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.XPATH, "//label[@id='imdbHeader-navDrawerOpen']/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/ul[1]/a[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='Comedy']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'User Rating')]").click()
    
    def test_imdb_5a181549(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").click()
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("The Flash")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-3']/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[3]/div[1]/div[2]/div[2]/div[4]/div[1]").click()
    
    def test_imdb_78c52592(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("Star Wars")
        self.driver.find_element(By.XPATH, "//button[@id='suggestion-search-button']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Star Wars: Episode IV - A New Hope')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[3]/div[1]/div[2]/div[2]/div[4]/div[1]").click()
    
    def test_imdb_81fb481b(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.XPATH, "//svg[@id='iconContext-menu']/path[2]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/ul[1]/a[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Horror')]").click()
        self.driver.find_element(By.XPATH, "//div[@title='Click to add to watchlist']").click()
    
    def test_imdb_9e3786bf(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "imdbHeader-navDrawerOpen").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/div[1]/ul[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='widget-nav']/div[2]/div[2]/ul[1]/li[3]/a[1]/span[1]").click()
    
    def test_imdb_a6080a77(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("creed III")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-0']/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[3]/div[2]/div[2]/ul[1]/li[2]/a[1]/span[1]/span[2]").click()
    
    def test_imdb_db53ba89(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.XPATH, "//svg[@id='iconContext-menu']/path[2]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/ul[1]/a[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Superhero')]").click()
        self.driver.find_element(By.XPATH, "//input[@name='superhero-sci-fi' and @value='on' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@name='based-on-comic-book' and @value='on' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//select[@name='min' and @value='0.0']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='min' and @value='0.0']").select("7.0")
        self.driver.find_element(By.XPATH, "//select[@name='max' and @value='10.0']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='max' and @value='10.0']").select("9.0")
        self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/div[1]/div[1]/span[1]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//select[@name='sort']").clear()
        self.driver.find_element(By.XPATH, "//select[@name='sort']").select("Number of Votes")
        self.driver.find_element(By.XPATH, "//span[@title='Compact view']").click()
        self.driver.find_element(By.XPATH, "//div[@title='Click to add to watchlist']").click()
        self.driver.find_element(By.XPATH, "//div[@title='Click to add to watchlist']").click()
        self.driver.find_element(By.XPATH, "//div[@title='Click to add to watchlist']").click()
    
    def test_imdb_265cd715(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("Jerry Trainor")
        self.driver.find_element(By.XPATH, "//button[@id='suggestion-search-button']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Jerry Trainor')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[3]/section[2]/div[5]/div[1]/div[1]/div[1]/label[1]/span[1]/ul[1]/li[1]").click()
    
    def test_imdb_60e1de47(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").click()
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("Prometheus")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-0']/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[3]/div[2]/div[2]/div[3]/div[1]/button[1]").click()
    
    def test_imdb_6c107328(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("The Elephant Whisperers")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-2']/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[3]/div[2]/div[2]/div[3]/div[1]/button[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("The Magician's Elephant")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-0']/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[3]/div[2]/div[2]/div[3]/div[1]/button[1]/div[1]/div[1]").click()
    
    def test_imdb_6f1fe14d(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.ID, "suggestion-search").clear()
        self.driver.find_element(By.ID, "suggestion-search").send_keys("Aaron Horvath")
        self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-0']/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[3]/section[2]/div[7]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
    
    def test_imdb_f4555944(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.XPATH, "//label[@id='imdbHeader-navDrawerOpen']/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/div[1]/ul[1]/a[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'2022')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Eo')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Jerzy Skolimowski')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[3]/div[2]/div[2]/section[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Create new list')]").click()
        self.driver.find_element(By.ID, "list-create-name").clear()
        self.driver.find_element(By.ID, "list-create-name").send_keys("Directors")
        self.driver.find_element(By.ID, "list-create-description").clear()
        self.driver.find_element(By.ID, "list-create-description").send_keys("To Watch")
        self.driver.find_element(By.ID, "list-create-type").clear()
        self.driver.find_element(By.ID, "list-create-type").select("People")
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    
    def test_imdb_de1045f4(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.XPATH, "//label[@id='imdbHeader-navDrawerOpen']/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/ul[1]/a[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Documentary')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'User Rating')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Going Postal')]").click()
    
    def test_imdb_f2f531ff(self):
        # self.driver.get("https://imdb.com")
        self.driver.find_element(By.XPATH, "//svg[@id='iconContext-menu']/path[2]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/ul[1]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sci-Fi')]").click()
        self.driver.find_element(By.ID, "iconContext-menu").click()
        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/ul[1]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sci-Fi')]").click()
    