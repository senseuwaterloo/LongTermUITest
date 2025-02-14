import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab, scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestDiscogs:
    def test_discogs_ec472065(self):
        # (JohnSmith2024)uiteststudy@gmail.com:Pass4John!
        # self.driver.get("https://discogs.com")
        self.driver.find_element(By.ID, "log_in_link").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("JohnSmith2024")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("Pass4John!")
        self.driver.find_element(By.NAME, "action").click()

        # self.driver.find_element(By.XPATH, "//li[@id='section_nav_explore']/button[1]").click()
        # locator change and also introduced dynamic id. Different element may need different kind of locators and different locator may need different repairing strategies.
        self.driver.find_element(By.XPATH, "//div[contains(@id, '__header_root_')]/div/header/div/nav[1]/div[1]/div[1]/button").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Rock')]").click()
        # only use keyword "Rock" to locate the element is too general, need to integrate more info to uniquely locate the element
        self.driver.find_element(By.XPATH, "//div[starts-with(@class, '_desktop_')]//ul[contains(.,'Genres')]//a[contains(text(),'Rock')]").click()

        self.driver.find_element(By.XPATH, "//ul[@id='top_artists']/li[1]/a[1]/span[2]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'David Bowie')]").click()
        # above locator is too general, multiple elements can be located
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a").click()

        # need to wait for several seconds since the link is loaded later than the expanding btn and somehow selenium click is clicking on that button. Maybe because of layout shift
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//section[@id='curated-lists']/header[1]/button[1]").click()

        self.driver.find_element(By.ID, "new").click()
        self.driver.find_element(By.ID, "title").clear()
        self.driver.find_element(By.ID, "title").send_keys("MyMusicList")
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[16]/div[1]/div[1]/form[1]/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[1]/header[1]/div[1]/div[1]/span[1]/nav[1]/div[1]/ul[1]/li[1]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Electronic')]").click()
        # self.driver.find_element(By.XPATH, "//ul[@id='top_artists']/li[2]/a[1]/span[2]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Like A Virgin')]").click()
        # save as above code change
        self.driver.find_element(By.XPATH, "//div[contains(@id, '__header_root_')]/div/header/div/nav[1]/div[1]/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//div[starts-with(@class, '_desktop_')]//ul[contains(.,'Genres')]//a[contains(text(),'Electronic')]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='top_artists']/li[1]/a[1]/span[2]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a").click()

        # need to wait for several seconds since the link is loaded later than the expanding btn and somehow selenium click is clicking on that button
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//section[@id='curated-lists']/header[1]/button[1]").click()

        # self.driver.find_element(By.ID, "list").clear()
        # self.driver.find_element(By.ID, "list").select("MyMusicList")
        music_list = self.driver.find_element(By.ID, "list")
        music_select = Select(music_list)
        music_select.select_by_visible_text('MyMusicList')
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[16]/div[1]/div[1]/form[1]/button[1]").click()

        # self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore All')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, '__header_root_')]/div/header/div/nav[1]/div[1]/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//div[starts-with(@class, '_desktop_')]//ul[contains(.,'Discover')]//a[contains(text(),'Explore All')]").click()

        self.driver.find_element(By.XPATH, "//div[@id='page_aside']/div[2]/ul[1]/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='search_results']/li[1]/a[1]/span[2]/img[1]").click()

        # need to wait for several seconds since the link is loaded later than the expanding btn and somehow selenium click is clicking on that button
        # also seems that the link will only be loaded when scroll to it so need to scroll down and wait for several seconds
        time.sleep(5)
        scroll_to_element(self.driver, self.driver.find_element(By.XPATH, "//section[@id='curated-lists']/header[1]/button[1]"))
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//section[@id='curated-lists']/header[1]/button[1]").click()

        # self.driver.find_element(By.ID, "list").clear()
        # self.driver.find_element(By.ID, "list").select("New")
        music_list = self.driver.find_element(By.ID, "list")
        music_select = Select(music_list)
        music_select.select_by_visible_text('MyMusicList')
        self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[20]/div[1]/div[1]/form[1]/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[1]/header[1]/div[1]/div[1]/span[1]/nav[1]/div[1]/ul[1]/li[1]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'List Explorer')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, '__header_root_')]/div/header/div/nav[1]/div[1]/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//div[starts-with(@class, '_desktop_')]//ul[contains(.,'Discover')]//a[contains(text(),'List Explorer')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Manage My Lists')]").click()
        # need to switch to the new tab
        switch_to_new_tab(self.driver)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'MyMusicList')]").click()
        self.driver.find_element(By.XPATH, "//section[@id='actions']/header[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='actions']/div[1]/div[1]/div[5]/button[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='actions']/div/div/div[1]/div/div/button[1]").click()
