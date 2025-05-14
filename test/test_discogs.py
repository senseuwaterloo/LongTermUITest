import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab, scroll_to_element


@pytest.mark.usefixtures("driver_session")
class TestDiscogs:
    def test_discogs_ec472065(self):
        self.driver.get("https://discogs.com")
        self.driver.find_element(By.ID, "log_in_link").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("JohnSmith2024")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("Pass4John!")
        self.driver.find_element(By.NAME, "action").click()

        self.driver.find_element(By.XPATH, "//div[contains(@id, '__header_root_')]/div/header/div/nav[1]/div[1]/div[1]/button").click()

        self.driver.find_element(By.XPATH, "//div[starts-with(@class, '_desktop_')]//ul[contains(.,'Genres')]//a[contains(text(),'Rock')]").click()

        self.driver.find_element(By.XPATH, "//ul[@id='top_artists']/li[1]/a[1]/span[2]/img[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='page']/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//section[@id='curated-lists']/header[1]/button[1]").click()

        self.driver.find_element(By.ID, "new").click()
        self.driver.find_element(By.ID, "title").clear()
        self.driver.find_element(By.ID, "title").send_keys("MyMusicList")
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[16]/div[1]/div[1]/form[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[contains(@id, '__header_root_')]/div/header/div/nav[1]/div[1]/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//div[starts-with(@class, '_desktop_')]//ul[contains(.,'Genres')]//a[contains(text(),'Electronic')]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='top_artists']/li[1]/a[1]/span[2]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//section[@id='curated-lists']/header[1]/button[1]").click()

        music_list = self.driver.find_element(By.ID, "list")
        music_select = Select(music_list)
        music_select.select_by_visible_text('MyMusicList')
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[16]/div[1]/div[1]/form[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[contains(@id, '__header_root_')]/div/header/div/nav[1]/div[1]/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//div[starts-with(@class, '_desktop_')]//ul[contains(.,'Discover')]//a[contains(text(),'Explore All')]").click()

        self.driver.find_element(By.XPATH, "//div[@id='page_aside']/div[2]/ul[1]/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='search_results']/li[1]/a[1]/span[2]/img[1]").click()

        time.sleep(5)
        scroll_to_element(self.driver, self.driver.find_element(By.XPATH, "//section[@id='curated-lists']/header[1]/button[1]"))
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//section[@id='curated-lists']/header[1]/button[1]").click()

        music_list = self.driver.find_element(By.ID, "list")
        music_select = Select(music_list)
        music_select.select_by_visible_text('MyMusicList')
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[20]/div[1]/div[1]/form[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[contains(@id, '__header_root_')]/div/header/div/nav[1]/div[1]/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//div[starts-with(@class, '_desktop_')]//ul[contains(.,'Discover')]//a[contains(text(),'List Explorer')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Manage My Lists')]").click()

        switch_to_new_tab(self.driver)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'MyMusicList')]").click()
        self.driver.find_element(By.XPATH, "//section[@id='actions']/header[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='actions']/div[1]/div[1]/div[5]/button[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='actions']/div/div/div[1]/div/div/button[1]").click()
