import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestLastFm:
    def test_lastfm_b83120d9(self):
        # self.driver.get("https://last.fm")
        # JohnSmith2024:uiteststudy@gmail.com:Pass4LastFM2024!
        # add extra login step
        self.driver.find_element(By.XPATH, "//a[contains(text(), ' Log In')]").click()
        self.driver.find_element(By.ID, "id_username_or_email").clear()
        self.driver.find_element(By.ID, "id_username_or_email").send_keys("JohnSmith2024")
        self.driver.find_element(By.ID, "id_password").clear()
        self.driver.find_element(By.ID, "id_password").send_keys("Pass4LastFM2024!")
        self.driver.find_element(By.NAME, "submit").click()

        # self.driver.find_element(By.XPATH, "//div[@id='content']/div[3]/nav[1]/div[1]/div[4]/a[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Playlists')]").click()
        self.driver.find_element(By.XPATH, "//li[not(contains(@class, 'hidden'))]//a[contains(text(),'Playlists')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'New playlist')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[2]/div[2]/form[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//h1[@placeholder='My New Playlist']").click()
        self.driver.find_element(By.XPATH, "//h1[@placeholder='My New Playlist']").clear()
        self.driver.find_element(By.XPATH, "//h1[@placeholder='My New Playlist']").send_keys("Dirty")

        self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[5]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "track-search").clear()
        self.driver.find_element(By.ID, "track-search").send_keys("Doja Cat")
        # self.driver.find_element(By.XPATH, "//div[@id='j-popup-80241031']/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @data-analytics-action='search']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='j-popup-80241031']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[6]/form[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//tbody[@data-playlisting-add-entries]/tr[1]//form[@data-playlisting-add-form and @method='post']").click()

        self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[5]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "track-search").clear()
        self.driver.find_element(By.ID, "track-search").send_keys("Doja Cat")
        # self.driver.find_element(By.XPATH, "//div[@id='j-popup-97033107']/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @data-analytics-action='search']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='j-popup-97033107']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[6]/form[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//tbody[@data-playlisting-add-entries]/tr[2]//form[@data-playlisting-add-form and @method='post']").click()

        self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[5]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "track-search").click()
        self.driver.find_element(By.ID, "track-search").clear()
        self.driver.find_element(By.ID, "track-search").send_keys("Doja Cat")
        # self.driver.find_element(By.XPATH, "//div[@id='j-popup-67441040']/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @data-analytics-action='search']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='j-popup-67441040']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[6]/form[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//tbody[@data-playlisting-add-entries]/tr[3]//form[@data-playlisting-add-form and @method='post']").click()

        self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[5]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "track-search").clear()
        self.driver.find_element(By.ID, "track-search").send_keys("Doja Cat")
        # self.driver.find_element(By.XPATH, "//div[@id='j-popup-29782057']/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @data-analytics-action='search']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='j-popup-29782057']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[6]/form[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//tbody[@data-playlisting-add-entries]/tr[4]//form[@data-playlisting-add-form and @method='post']").click()

        self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[5]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.ID, "track-search").clear()
        self.driver.find_element(By.ID, "track-search").send_keys("Doja Cat")
        # self.driver.find_element(By.XPATH, "//div[@id='j-popup-32977881']/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @data-analytics-action='search']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='j-popup-32977881']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[7]/td[6]/form[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//tbody[@data-playlisting-add-entries]/tr[5]//form[@data-playlisting-add-form and @method='post']").click()

        # add post step action to delete the list for next time testing
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'playlisting-playlist-header-more-button') and @aria-controls='playlisting-playlist-header-more-dropdown']").click()
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'delete') and @data-analytics-action='delete' and text()='Delete']").click()
        self.driver.find_element(By.XPATH, "//button[@data-modal-action='ok' and text()='Delete']").click()
        # just in case, wait a few seconds to wait for the delete action to finish
        time.sleep(2)
