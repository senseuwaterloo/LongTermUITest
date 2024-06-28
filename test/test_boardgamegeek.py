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
class TestBoardgamegeek:
    
    def test_boardgamegeek_d2171cc3(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.XPATH, "//button[contains(.,'GeekLists')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Hot')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/gg-app[1]/div[1]/gg-header[1]/header[1]/nav[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Browse')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Boardgames')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Brass: Birmingham')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='mainbody']/div[2]/div[1]/div[1]/div[2]/ng-include[1]/div[1]/ng-include[1]/div[1]/div[2]/div[2]/div[4]/span[3]/ng-include[1]/div[1]/div[2]/span[1]/span[2]/span[1]/span[1]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='global-header-outer']/header[1]/nav[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='global-header-outer']/header[1]/nav[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Boardgames')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Pandemic Legacy: Season 1')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='mainbody']/div[2]/div[1]/div[1]/div[2]/ng-include[1]/div[1]/ng-include[1]/div[1]/div[2]/div[2]/div[4]/span[3]/ng-include[1]/div[1]/div[2]/span[1]/span[2]/span[1]/span[1]/span[1]/button[1]").click()
        self.driver.find_element(By.ID, "inputUsername").clear()
        self.driver.find_element(By.ID, "inputUsername").send_keys("james9091")
        self.driver.find_element(By.ID, "inputPassword").clear()
        self.driver.find_element(By.ID, "inputPassword").send_keys("bbui")
    
    def test_boardgamegeek_9f4b6bd4(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Browse')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Publishers')]").click()
    
    def test_boardgamegeek_b040b35d(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.ID, "1").clear()
        self.driver.find_element(By.ID, "1").send_keys("frosthaven")
        self.driver.find_element(By.XPATH, "//button[@id='ngb-typeahead-0-0']/a[1]/ngb-highlight[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='mainbody']/div[2]/div[1]/div[1]/div[2]/ng-include[1]/div[1]/ng-include[1]/div[1]/div[2]/div[2]/div[2]/gameplay-module[1]/div[1]/div[1]/ul[1]/li[4]/div[2]").click()
    
    def test_boardgamegeek_c4ca9c7a(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.ID, "1").clear()
        self.driver.find_element(By.ID, "1").send_keys("gloomhaven")
        self.driver.find_element(By.XPATH, "//button[@id='ngb-typeahead-0-0']/a[1]/ngb-highlight[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Ratings')]").click()
    
    def test_boardgamegeek_c95b0276(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Shopping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'BGG Store')]").click()
        self.driver.find_element(By.ID, "SiteNavLabel-clothing").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shirts and Hoodies')]").click()
    
    def test_boardgamegeek_61c8e051(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Shopping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Trades')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Recent Trades')]").click()
    
    def test_boardgamegeek_87d1206c(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.ID, "1").clear()
        self.driver.find_element(By.ID, "1").send_keys("Atlantis")
        self.driver.find_element(By.XPATH, "/html/body[1]/gg-app[1]/div[1]/gg-header[1]/header[1]/nav[1]/div[1]/gg-header-search[1]/gg-search-container[1]/gg-search[1]/form[1]/div[1]/button[1]/fa-icon[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Atlantis')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='mainbody']/div[2]/div[1]/div[1]/div[2]/ng-include[1]/div[1]/ng-include[1]/div[1]/div[2]/div[2]/div[4]/span[3]/ng-include[1]/div[1]/div[2]/span[1]/span[2]/span[1]/span[1]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Save')]").click()
    
    def test_boardgamegeek_020bc054(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.XPATH, "//div[@id='global-header-outer']/header[1]/nav[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Boardgames')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Ark Nova')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='mainbody']/div[2]/div[1]/div[1]/div[2]/ng-include[1]/div[1]/div[1]/ui-view[1]/ui-view[1]/div[1]/overview-module[1]/marketplace-module[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/geekmarket-legacy-overview-module[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/div[2]/name-with-year[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@title='Send GeekMail to user']").click()
    
    def test_boardgamegeek_360eeaa8(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Community')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Users')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'User Search')]").click()
        self.driver.find_element(By.ID, "geeksearch").clear()
        self.driver.find_element(By.ID, "geeksearch").send_keys("Joe Bloggs")
        self.driver.find_element(By.XPATH, "//input[@name='B1' and @value='Go' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='maincontent']/table[1]/tbody[1]/tr[3]/td[4]/div[1]/div[4]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/img[1]").click()
    
    def test_boardgamegeek_54112d86(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Help')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Guide to BGG')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Submit game listings')]").click()
    
    def test_boardgamegeek_562d8516(self):
        # self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Shopping')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'GeekMarket')]").click()
        self.driver.find_element(By.ID, "itemsearch").clear()
        self.driver.find_element(By.ID, "itemsearch").send_keys("king of tokyo")
        self.driver.find_element(By.XPATH, "//li[@id='typeahead-4-5947-option-0']/a[1]/strong[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price (lowest first)')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Ship Location')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page-wrapper']/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Canada')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'King of Tokyo')]").click()
        self.driver.find_element(By.XPATH, "//button[@title='Send GeekMail to user']").click()
    