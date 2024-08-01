import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestIgn:
    
    # def test_ign_01c6e863(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[2]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='reviews-menu']/div[2]/div[2]/a[2]/div[1]").click()
    #     self.driver.find_element(By.ID, "scoreRange").clear()
    #     self.driver.find_element(By.ID, "scoreRange").select("10")
    #     self.driver.find_element(By.ID, "genre").clear()
    #     self.driver.find_element(By.ID, "genre").select("Board")
    #
    # def test_ign_36b6bb33(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "term").clear()
    #     self.driver.find_element(By.ID, "term").send_keys("Breath of the wild")
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Zelda: Breath of the Wild')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Walkthrough')]").click()
    #
    # def test_ign_b11eded9(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/a[4]/svg[1]").click()
    #     self.driver.find_element(By.ID, "rewards-filter-select").clear()
    #     self.driver.find_element(By.ID, "rewards-filter-select").select("Games")
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[2]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[2]/div[1]/div[3]/div[1]/div[3]/div[1]/div[5]/div[1]/button[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
    #
    # def test_ign_620185b2(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/a[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "term").clear()
    #     self.driver.find_element(By.ID, "term").send_keys("Assasians Creed")
    #     self.driver.find_element(By.XPATH, "//div[contains(.,\"Assassin's Creed Valhalla\")]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Walkthrough')]").click()
    #
    # def test_ign_00e83fae(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='reviews-menu']/div[2]/div[2]/a[3]/div[1]").click()
    #     self.driver.find_element(By.ID, "platform").clear()
    #     self.driver.find_element(By.ID, "platform").select("PC")
    #     self.driver.find_element(By.ID, "sortBy").clear()
    #     self.driver.find_element(By.ID, "sortBy").select("Sort by Score")
    #
    # def test_ign_b49f88ac(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "term").clear()
    #     self.driver.find_element(By.ID, "term").send_keys("Deathloop")
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Deathloop')]").click()
    #
    # def test_ign_701bc7ed(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//svg[@role='presentation']").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Discover']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='discover-menu']/div[2]/div[2]/a[3]/div[1]").click()
    #     self.driver.find_element(By.ID, "platformSlug").clear()
    #     self.driver.find_element(By.ID, "platformSlug").select("PS5")
    #     self.driver.find_element(By.XPATH, "//button[@id='7-2023']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[3]/div[1]/a[1]/div[2]/div[1]").click()
    #
    # def test_ign_763deda0(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "term").clear()
    #     self.driver.find_element(By.ID, "term").send_keys("Guardians of the Galaxy")
    #     self.driver.find_element(By.XPATH, "//button[@id='filter1']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Guardians of the Galaxy Vol. 3')]").click()
    #
    # def test_ign_851998b2(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//svg[@role='presentation']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/a[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pre-Orders')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='gf-tree']/div[3]/div[2]/div[2]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
    
    def test_ign_5ad0f114(self):
        # self.driver.get("https://ign.com")

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/a[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/aside/nav/div[1]/div[1]/div[2]/div[3]/a[2]/div").click()

        # self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[2]/section[1]/div[2]/div[2]/button[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[2]/section/div[2]/div/button/div/div").click()

        self.driver.find_element(By.ID, "term").clear()
        self.driver.find_element(By.ID, "term").send_keys("Uncharted Legacy of Thieves Collection")

        # self.driver.find_element(By.XPATH, "//div[contains(.,'Uncharted: Legacy of Thieves Collection')]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Uncharted: Legacy of Thieves Collection']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[3]/section[2]/div[1]/a[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div/div[4]/section[2]/div/div/a/div/button").click()

        # comment following step since its redundant
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/button[1]/svg[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/a[1]/div[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Collectibles')]").click()
        # two links and we need to locate to the second one
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[3]/div[4]/div/div[2]/section[1]/section[9]/ul/li[2]/a").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),\"The Queen's Bracelet\")]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\"The Queen's Bracelet\")]").click()
    
    # def test_ign_c53a4a47(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "term").clear()
    #     self.driver.find_element(By.ID, "term").send_keys("Elden Ring")
    #
    # def test_ign_d637c171(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[3]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='news-menu']/div[2]/div[2]/a[10]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/a[1]/div[2]").click()
    #
    # def test_ign_db289bef(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[1]/svg[1]/g[1]/path[1]").click()
    #     self.driver.find_element(By.ID, "term").clear()
    #     self.driver.find_element(By.ID, "term").send_keys("ps5")
    #
    # def test_ign_39b037ac(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[1]/svg[1]/g[1]/path[2]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter1']/div[1]").click()
    #     self.driver.find_element(By.ID, "term").clear()
    #     self.driver.find_element(By.ID, "term").send_keys("Prometheus")
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Prometheus')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='reviews']/div[1]").click()
    #
    # def test_ign_3be7acd4(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/button[2]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/a[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[1]/section[1]/div[1]/div[3]/div[1]/a[1]/div[1]/button[1]").click()
    #
    # def test_ign_4f395aad(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search...']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search...']").send_keys("Star Wars The Mandalorian statue")
    #     self.driver.find_element(By.XPATH, "//div[@id='ui-id-4']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@name='add' and @type='submit']").click()
    #
    # def test_ign_4faf56f2(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='reviews-menu']/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='discover-menu']/div[2]/div[2]/a[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='4-2023']/div[1]").click()
    #
    # def test_ign_521aa0aa(self):
    #     # self.driver.get("https://ign.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[2]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "term").clear()
    #     self.driver.find_element(By.ID, "term").send_keys("Cyberpunk 2077")
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Cyberpunk 2077')]").click()
    