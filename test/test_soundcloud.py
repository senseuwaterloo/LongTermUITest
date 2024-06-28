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
class TestSoundcloud:
    
    def test_soundcloud_81b4816a(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//div[@id='app']/header[1]/div[1]/div[3]/div[2]/a[1]/div[2]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Likes')]").click()
    
    def test_soundcloud_96016e7b(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("trending playlists")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Playlists')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Play')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Like']").click()
    
    def test_soundcloud_23cbeb29(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("Indian classical")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tracks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Past month')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'> 30 min')]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button' and @title='More']").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Add to playlist']").click()
        self.driver.find_element(By.ID, "formControl_22667").clear()
        self.driver.find_element(By.ID, "formControl_22667").send_keys("Meditation Music")
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Save']").click()
    
    def test_soundcloud_b4aeab35(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("Pop Workout")
        self.driver.find_element(By.XPATH, "//div[@id='searchMenuList']/div[2]/ul[1]/li[1]/div[1]/a[1]/div[2]/h2[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Playlists')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[5]/span[1]").click()
    
    def test_soundcloud_973bf55c(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("rock")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Playlists')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Repost']").click()
    
    def test_soundcloud_978760ca(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("Chill")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'People')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Follow']").click()
    
    def test_soundcloud_d4f9c67f(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Try Next Pro')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rootElement']/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/button[1]").click()
    
    def test_soundcloud_efe9051b(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("Nirvana")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Nirvana')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Popular tracks')]").click()
    
    def test_soundcloud_4c623130(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("Mark Knight")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mark Knight')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Follow']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Popular tracks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/button[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-button-26335']/div[1]/div[1]/button[1]/span[1]/span[1]").click()
    
    def test_soundcloud_57f72023(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("SOUTH AFRICAN HISTORY PODCAST")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tracks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'10-30 min')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/a[1]/span[1]").click()
    
    def test_soundcloud_9e9d7935(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Hip-hop & Rap')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button' and @title='More']").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-button-26241']/div[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Create a playlist')]").click()
        self.driver.find_element(By.ID, "formControl_26271").clear()
        self.driver.find_element(By.ID, "formControl_26271").send_keys("Top Hip Hop")
        self.driver.find_element(By.XPATH, "//div[@id='overlay_26255']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/section[1]/div[2]/div[1]/label[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Save']").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Close']").click()
    
    def test_soundcloud_a338a731(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("Selena Gomez")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Selena Gomez')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Popular tracks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/button[5]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Add to playlist']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Create a playlist')]").click()
        self.driver.find_element(By.ID, "formControl_46506").clear()
        self.driver.find_element(By.ID, "formControl_46506").send_keys("Love")
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Save']").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Close']").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/button[5]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Add to playlist']").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @title='']").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Close']").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/button[5]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Add to playlist']").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @title='']").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Close']").click()
    
    def test_soundcloud_0a2623c8(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("Taylor Swift")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Taylor Swift')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Follow']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Playlists')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/button[5]/span[1]/span[1]").click()
    
    def test_soundcloud_3e0d115f(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Library')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'History')]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button' and @title='Clear all history']").click()
        self.driver.find_element(By.XPATH, "//div[@id='dropdown-button-24040']/div[1]/form[1]/div[2]/button[1]").click()
    
    def test_soundcloud_48ca542f(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("game mix")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Albums')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Like']").click()
    
    def test_soundcloud_58badcfc(self):
        # self.driver.get("https://soundcloud.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Search']").send_keys("Ricky Kej")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tracks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Past year')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'2-10 min')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'To share')]").click()
    