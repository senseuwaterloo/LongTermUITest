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
class TestReddit:
    
    def test_reddit_ea02c8da(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("Amazon")
        self.driver.find_element(By.ID, "header-search-bar").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Top')]").click()
    
    def test_reddit_f83262c3(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("r/news")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/div[1]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("football")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'New')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_12jvnb0']/div[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='vote-arrows-t1_jg0oupw']/button[1]/span[1]/i[1]").click()
    
    def test_reddit_623bf065(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.XPATH, "//div[@id='SHORTCUT_FOCUSABLE_DIV']/div[1]/header[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='focus-Popular']/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='CountrySort--CountrySortPicker']/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Japan')]").click()
    
    def test_reddit_2e621fbb(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("gift card exchange")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/h6[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_11w5brh']/div[3]/div[2]/div[1]/a[1]/div[1]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_11w5brh']/div[1]/div[5]/div[1]/div[4]/button[1]/span[1]/i[1]").click()
    
    def test_reddit_2f2c00fd(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("MOVIES")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/div[1]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\"This week's trailers\")]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_12ij3vp']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/a[1]/div[1]/h3[1]").click()
        self.driver.find_element(By.ID, "View--GiveAward--t3_12ij3vp--lightbox").click()
    
    def test_reddit_3f17e5ec(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").click()
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("announcements")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/div[1]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[2]/a[2]").click()
        self.driver.find_element(By.XPATH, "//button[@id='upvote-button-t3_pg006s']/span[1]/i[1]").click()
    
    def test_reddit_43d5637a(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("fitness")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/div[1]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
    
    def test_reddit_158027d3(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("politics")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/div[1]/a[1]/div[2]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
    
    def test_reddit_159c4719(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("blind people")
        self.driver.find_element(By.ID, "header-search-bar").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/h6[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
    
    def test_reddit_16f742f7(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("12 monkeys")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/div[1]/a[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("James Cole")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'New')]").click()
    
    def test_reddit_6decc1e5(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("MUSIC")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/div[1]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_12hsz54']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/h3[1]").click()
    
    def test_reddit_7593311c(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.XPATH, "//div[@id='change-username-tooltip-id']/span[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='tooltip-container']/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_reddit_98986fb1(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("Donald Trump")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[23]/div[1]/a[2]/button[1]").click()
    
    def test_reddit_beb061ad(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/a[4]").click()
        self.driver.find_element(By.XPATH, "//button[@id='TimeSort--SortPicker']/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'All Time')]").click()
    
    def test_reddit_5b0a7257(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("work")
        self.driver.find_element(By.ID, "header-search-bar").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/h6[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='ListingSort--Overflow']/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Rising')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_12ju84n']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_12ju84n']/div[1]/div[5]/div[1]/div[4]/button[1]/span[2]").click()
    
    def test_reddit_5d1d86c2(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("separate-camp7202")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[4]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]/h6[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Comments')]").click()
    
    def test_reddit_d432b611(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("Fortnite")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[1]/div[1]/h6[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='SHORTCUT_FOCUSABLE_DIV']/div[4]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
    
    def test_reddit_daae8cfa(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.XPATH, "//div[@id='change-username-tooltip-id']/span[3]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Title']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Title']").send_keys("Cryptocurreny Suggestions")
        self.driver.find_element(By.XPATH, "//div[@role='textbox']").clear()
        self.driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("Please suggest crypto trading which is profitable.")
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div[1]/div[1]/div[2]/button[1]").click()
    
    def test_reddit_e0b26822(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Create Post')]").click()
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Title']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Title']").send_keys("post")
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div[1]/div[1]/div[2]/button[1]").click()
    
    def test_reddit_e918a537(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("meme")
        self.driver.find_element(By.ID, "header-search-bar").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Most Comments')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Past Week')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_12iblsj']/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.ID, "comment_search-bar").clear()
        self.driver.find_element(By.ID, "comment_search-bar").send_keys("hip hop")
        self.driver.find_element(By.ID, "comment_search-bar").click()
    
    def test_reddit_30542c68(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("cars")
        self.driver.find_element(By.ID, "header-search-bar").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Relevance')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'r/Unexpected')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]/div[4]/div[1]/div[2]/a[1]").click()
    
    def test_reddit_306b3d76(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("games")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Most Comments')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Past Year')]").click()
    
    def test_reddit_3272dc52(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("anti aging")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Most Comments')]").click()
    
    def test_reddit_11b2f1f0(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.XPATH, "//button[@id='ListingSort--Overflow']/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Rising')]").click()
        self.driver.find_element(By.XPATH, "//button[@id='LayoutSwitch--picker']/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'compact')]").click()
    
    def test_reddit_123e87a4(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.XPATH, "//div[@id='SHORTCUT_FOCUSABLE_DIV']/div[1]/header[1]/div[1]/div[2]/div[1]/div[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='ListingSort--Overflow']/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Rising')]").click()
        self.driver.find_element(By.XPATH, "//button[@id='LayoutSwitch--picker']/span[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'compact')]").click()
    
    def test_reddit_1d2c6252(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.XPATH, "//div[@id='SHORTCUT_FOCUSABLE_DIV']/div[1]/header[1]/div[1]/div[2]/div[1]/div[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='CountrySort--CountrySortPicker']/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Chile')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/a[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_12hi8k9-share-menu']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Copy link')]").click()
    
    def test_reddit_233be033(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("r/answers")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/div[1]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-answers']/button[1]/span[2]").click()
    
    def test_reddit_2c31fb6a(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "create-community-button").click()
        self.driver.find_element(By.XPATH, "//div[@id='SHORTCUT_FOCUSABLE_DIV']/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text']").send_keys("mycommunity")
        self.driver.find_element(By.XPATH, "//div[@id='SHORTCUT_FOCUSABLE_DIV']/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/button[2]").click()
    
    def test_reddit_689331b4(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/a[4]").click()
        self.driver.find_element(By.XPATH, "//button[@id='TimeSort--SortPicker']/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'This Month')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_12dna0j']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='overlayScrollContainer']/div[2]/div[1]/div[3]/div[4]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='overlayScrollContainer']/div[30]/div[1]/a[5]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='vote-arrows-t1_jf709qv']/button[2]/span[1]/i[1]").click()
    
    def test_reddit_6bc6d924(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("AskReddit")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/div[1]/a[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[2]/a[3]").click()
        self.driver.find_element(By.XPATH, "//button[@id='TimeSort--SortPicker']/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'This Month')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]/span[1]").click()
    
    def test_reddit_cfe4eed2(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("nature")
        self.driver.find_element(By.ID, "header-search-bar").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'New')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_12k572d']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/div[1]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_12k572d-overlay-share-menu']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='overlayScrollContainer']/div[29]/div[1]/button[2]/span[2]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Choose a community']").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search communities']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search communities']").send_keys("nationalpark")
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/button[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
    
    def test_reddit_caa0d9a3(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("food")
        self.driver.find_element(By.XPATH, "//div[@id='SearchDropdown']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Most Comments')]").click()
    
    def test_reddit_cd2c8a3f(self):
        # self.driver.get("https://reddit.com")
        self.driver.find_element(By.ID, "header-search-bar").clear()
        self.driver.find_element(By.ID, "header-search-bar").send_keys("covid")
        self.driver.find_element(By.ID, "header-search-bar").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Relevance')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Past Year')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_11olhic']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/div[1]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='t3_11olhic']/div[1]/div[2]/button[1]/i[1]").click()
    