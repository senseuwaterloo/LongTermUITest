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
class TestStoreSteampowered:
    
    def test_storesteampowered_8c82b107(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Farming & Crafting')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[2]/div[1]/div[18]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[2]/div[1]/div[18]/div[3]/div[2]/div[1]").click()
    
    def test_storesteampowered_b4a2fc25(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'buckeye.foobar')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Games')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='application_root']/div[2]/div[1]/a[1]/span[1]").click()
    
    def test_storesteampowered_cd92cea9(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New & Noteworthy')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Most Played')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='application_root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'By Daily Players')]").click()
    
    def test_storesteampowered_d29fd2a4(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'buckeye.foobar')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Games')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='application_root']/div[2]/div[1]/a[5]/span[1]").click()
    
    def test_storesteampowered_fc8342f9(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Simulation')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='game_area_purchase']/div[5]/div[1]/div[4]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='game_area_purchase_top']/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='btn_purchase_self']/span[1]").click()
    
    def test_storesteampowered_96e95a76(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Adventure')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[2]/div[1]/div[18]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[2]/div[1]/div[18]/div[3]/div[2]/div[1]").click()
    
    def test_storesteampowered_a88676d0(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'buckeye.foobar')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Inventory')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='mainContents']/div[3]/div[1]/a[1]/span[1]").click()
    
    def test_storesteampowered_4c578076(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New & Noteworthy')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Popular Upcoming')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tab_popular_comingsoon_content']/div[1]/a[1]/span[1]").click()
    
    def test_storesteampowered_64051efe(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'buckeye.foobar')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Inventory')]").click()
    
    def test_storesteampowered_718ccfb6(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'STORE')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Points Shop')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='application_root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='application_root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]/svg[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='application_root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]").click()
    
    def test_storesteampowered_05238c0f(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.ID, "store_nav_search_term").click()
        self.driver.find_element(By.ID, "store_nav_search_term").clear()
        self.driver.find_element(By.ID, "store_nav_search_term").send_keys("Dota 2")
        self.driver.find_element(By.XPATH, "//div[@id='search_suggestion_contents']/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dlc_purchase_action']/div[2]/a[1]/span[1]").click()
    
    def test_storesteampowered_11344944(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'COMMUNITY')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Discussions')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='tab_games']/span[1]").click()
        self.driver.find_element(By.ID, "quicklistselect_active").click()
        self.driver.find_element(By.ID, "quicklistselect_option_2").click()
    
    def test_storesteampowered_2159d768(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'JRPG')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[1]/div[1]/div[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/svg[1]").click()
    
    def test_storesteampowered_29f639c1(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'COMMUNITY')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Discussions')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='tab_games']/span[1]").click()
        self.driver.find_element(By.ID, "associate_game").clear()
        self.driver.find_element(By.ID, "associate_game").send_keys("Dota 2")
        self.driver.find_element(By.XPATH, "//div[@id='game_select_suggestions']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='forum_General_3703047_1696040635904700731']/a[1]").click()
    
    def test_storesteampowered_3236b068(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New & Noteworthy')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Most Played')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='application_root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'By Daily Players')]").click()
    
    def test_storesteampowered_3bb1c925(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.ID, "store_nav_search_term").clear()
        self.driver.find_element(By.ID, "store_nav_search_term").send_keys("Fallout 4")
        self.driver.find_element(By.XPATH, "//div[@id='search_suggestion_contents']/a[1]/div[1]").click()
        self.driver.find_element(By.ID, "ageYear").clear()
        self.driver.find_element(By.ID, "ageYear").select("1995")
        self.driver.find_element(By.XPATH, "//a[@id='view_product_page_btn']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='RecommendationVoteUpBtnsummary135517985']/span[1]").click()
    
    def test_storesteampowered_3c9442f9(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Massively Multiplayer')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Tab_1']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_93094']/div[1]/div[3]/button[1]").click()
    
    def test_storesteampowered_3d83f3de(self):
        # self.driver.get("https://store.steampowered.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Early Access')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Adventure')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[1]/div[1]/div[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SaleSection_13268']/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]").click()
    