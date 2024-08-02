import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestLastFm:
    
    # def test_lastfm_e77dc7d4(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[3]/section[2]/div[1]/ul[1]/li[7]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Mr. Brightside')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/header[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='header-more-actions-65c12c64-9105-460d-9687-4d22519869d6']/li[1]/form[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View your obsession')]").click()
    #
    # def test_lastfm_3ca5cfbb(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Artists')]").click()
    #     self.driver.find_element(By.ID, "masthead-search-field").clear()
    #     self.driver.find_element(By.ID, "masthead-search-field").send_keys("Alan Tam")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tracks')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Top Results')]").click()
    #
    # def test_lastfm_a7000718(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Everyday Is Like Sunday - 2011 Remaster')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/header[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='header-more-actions-40ad0621-e0ac-42a0-a836-d7134268b6d8']/li[1]/form[1]/button[1]").click()
    #
    # def test_lastfm_2cc71f04(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[7]/section[5]/ul[1]/li[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Set Me Free Pt.2')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Play track')]").click()
    #
    # def test_lastfm_34e047fe(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
    #     self.driver.find_element(By.ID, "masthead-search-field").clear()
    #     self.driver.find_element(By.ID, "masthead-search-field").send_keys("Blackpink")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'BLACKPINK')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'On tour')]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='events-section']/table[1]/tbody[1]/tr[1]/td[3]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[2]/section[2]/ul[1]/li[2]/a[1]/img[1]").click()
    #
    # def test_lastfm_0cb50efe(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
    #     self.driver.find_element(By.ID, "masthead-search-field").clear()
    #     self.driver.find_element(By.ID, "masthead-search-field").send_keys("Ariana Grande")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[1]/section[1]/ol[1]/li[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='top-tracks']/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'All time')]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='top-tracks']/div[2]/table[1]/tbody[1]/tr[1]/td[5]").click()
    #
    # def test_lastfm_1d738d01(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Charts')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Weekly')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'The Weeknd')]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='top-tracks']/div[2]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/form[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Play track')]").click()
    #
    # def test_lastfm_6df317e6(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/section[1]/div[1]/ul[1]/li[5]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'More tracks')]").click()
    #
    # def test_lastfm_a747bed0(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Charts')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[1]/section[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/a[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/header[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/button[1]").click()
    #
    # def test_lastfm_a9708ad7(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/section[1]/div[1]/ul[1]/li[4]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'The Smiths')]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='top-tracks']/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Last 30 days')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Play track')]").click()
    #
    # def test_lastfm_b3c7e28e(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/div[3]/nav[1]/div[1]/div[4]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Library')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Albums')]").click()
    
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
    
    # def test_lastfm_d042ee7e(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Events')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[1]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.ID, "location-search").clear()
    #     self.driver.find_element(By.ID, "location-search").send_keys("90028")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'90028')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='events-location']/form[1]/div[4]/div[1]/button[2]/span[1]").click()
    #
    # def test_lastfm_d6a0ab7c(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
    #     self.driver.find_element(By.ID, "masthead-search-field").clear()
    #     self.driver.find_element(By.ID, "masthead-search-field").send_keys("m s subbulakshmi")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'M.S. Subbulakshmi')]").click()
    #     self.driver.find_element(By.ID, "tracks-play-all").click()
    #
    # def test_lastfm_e72f9c32(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
    #     self.driver.find_element(By.ID, "masthead-search-field").clear()
    #     self.driver.find_element(By.ID, "masthead-search-field").send_keys("the weeknd")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[1]/section[1]/ol[1]/li[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View all artists')]").click()
    #
    # def test_lastfm_2bc47bba(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/section[1]/div[1]/ul[1]/li[2]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='top-tracks-section']/table[1]/tbody[1]/tr[1]/td[3]/div[1]/form[1]/button[1]").click()
    #
    # def test_lastfm_39fd14c2(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Merchandise')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='shopify-section-1480936373888']/section[1]/div[2]/div[1]/div[2]/a[1]/p[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "SingleOptionSelector-0").clear()
    #     self.driver.find_element(By.ID, "SingleOptionSelector-0").select("XL")
    #     self.driver.find_element(By.XPATH, "//form[@id='product_form_4373477392502']/div[2]/div[1]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.ID, "AddToCartText").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='shopify-section-header']/header[1]/div[1]/div[1]/div[1]/div[3]/div[1]/a[2]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='checkout' and @value='Check Out' and @type='submit']").click()
    #
    # def test_lastfm_783d5a91(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Music')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/section[1]/div[1]/ul[1]/li[3]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='top-tracks-section']/table[1]/tbody[1]/tr[3]/td[4]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='top-tracks-section']/table[1]/tbody[1]/tr[3]/td[7]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='chartlist-more-03a67c49-9295-4302-b496-51767f43a5a7']/li[2]/form[1]/button[1]").click()
    #
    # def test_lastfm_883fc533(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
    #     self.driver.find_element(By.ID, "masthead-search-field").clear()
    #     self.driver.find_element(By.ID, "masthead-search-field").send_keys("Katy Perry")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[1]/section[1]/ol[1]/li[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='j-popup-27027563']/div[1]/div[2]/div[1]/div[1]/form[1]/ul[1]/li[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View all tracks')]").click()
    #
    # def test_lastfm_998d121b(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Charts')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Weekly')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Taylor Swift')]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='top-tracks']/div[2]/table[1]/tbody[1]/tr[1]").click()
    #
    # def test_lastfm_f9723022(self):
    #     # self.driver.get("https://last.fm")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Events')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[1]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.ID, "location-search").clear()
    #     self.driver.find_element(By.ID, "location-search").send_keys("new york")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'New York')]").click()
    #     self.driver.find_element(By.ID, "id_radius").clear()
    #     self.driver.find_element(By.ID, "id_radius").select("100 km")
    #     self.driver.find_element(By.XPATH, "//div[@id='events-location']/form[1]/div[4]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.ID, "id_from").click()
    #     self.driver.find_element(By.ID, "id_from").clear()
    #     self.driver.find_element(By.ID, "id_from").send_keys("04/01/2023")
    #     self.driver.find_element(By.XPATH, "//div[@id='date-picker6f14879a-7820-46ec-8d94-7424d912a95c']/form[1]/div[2]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'3 going')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/form[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/form[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mantle_skin']/div[3]/div[1]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/form[1]/button[1]").click()
    