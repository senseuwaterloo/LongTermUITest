import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestSportsYahoo:
    
    # def test_sportsyahoo_353ab375(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='subnavhtml-NBA']/div[1]/div[1]/div[1]/div[1]/div[1]/a[5]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sub-nav']/ul[1]/li[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Col1-0-Team-Proxy']/div[1]/div[3]/div[3]/table[1]/tbody[1]/tr[3]/td[1]/div[1]").click()
    #
    # def test_sportsyahoo_ae969e05(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "ybar-nav-more-menu").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Soccer')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Premier League')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Standings')]").click()
    #
    # def test_sportsyahoo_b3a28e48(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_3").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ybar-navigation']/div[1]/ul[1]/li[4]/div[1]/ul[1]/li[6]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Col1-1-GraphStats-Proxy']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]").click()
    #
    # def test_sportsyahoo_dd38e3f0(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_1").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ybar-navigation']/div[1]/ul[1]/li[2]/div[1]/ul[1]/li[13]/a[1]/div[1]").click()
    #
    # def test_sportsyahoo_f45b0783(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_4").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Teams')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Los Angeles Lakers')]").click()
    #
    # def test_sportsyahoo_673841c2(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ybar-navigation']/div[1]/ul[1]/li[5]/div[1]/ul[1]/li[5]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Col1-0-LeagueStandings-Proxy']/div[1]/div[2]/table[2]/tbody[1]/tr[1]/th[1]/div[1]/div[1]/a[1]/span[2]").click()
    
    def test_sportsyahoo_92b51ef3(self):
        # self.driver.get("https://sports.yahoo.com/?guccounter=1")

        self.driver.find_element(By.ID, "ybar-sbq").clear()
        self.driver.find_element(By.ID, "ybar-sbq").send_keys("lebron james")

        # self.driver.find_element(By.XPATH, "//form[@id='ybar-sf']/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//img[@alt='LeBron James']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='sub-nav']/ul[1]/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sub-nav']/ul[1]/li[4]/a[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='Col1-1-SportsStream']/ul[1]/li[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Col1-1-SportsStream']/ul[1]/li[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='shareMenuTooltip']/div[1]/a[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='shareMenuTooltip']/div[1]/a[2]").click()
    
    # def test_sportsyahoo_94bd2a0f(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_1").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Fantasy Basketball')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Leaders')]").click()
    #
    # def test_sportsyahoo_96c35c7a(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_10").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ybar-navigation']/div[1]/ul[1]/li[11]/div[1]/ul[1]/li[6]/a[1]/div[1]").click()
    #
    # def test_sportsyahoo_9a462751(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='subnavhtml-NBA']/div[1]/div[1]/div[2]/div[1]/div[1]/a[4]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sub-nav']/ul[1]/li[5]/a[1]/span[1]").click()
    #
    # def test_sportsyahoo_9b03e9a1(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_5").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Scores/Schedules')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='scoreboard-group-1']/div[1]/div[1]/div[1]/a[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='scoreboard-group-1']/div[1]/div[1]/div[1]/a[2]/svg[1]").click()
    #
    # def test_sportsyahoo_9f57055d(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ybar-navigation']/div[1]/ul[1]/li[5]/div[1]/ul[1]/li[11]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Col1-1-LeagueOdds-Proxy']/div[1]/div[2]/div[1]/ul[1]/li[3]/button[1]").click()
    #
    # def test_sportsyahoo_0692908b(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "ybar-sbq").clear()
    #     self.driver.find_element(By.ID, "ybar-sbq").send_keys("las vegas raiders")
    #     self.driver.find_element(By.XPATH, "//form[@id='ybar-sf']/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Col2-8-TeamSchedule-Proxy']/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #
    # def test_sportsyahoo_0c577209(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "ybar-sbq").clear()
    #     self.driver.find_element(By.ID, "ybar-sbq").send_keys("phoenix suns")
    #     self.driver.find_element(By.XPATH, "//li[@role='link' and @title='Phoenix']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Col2-8-TeamSchedule-Proxy']/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]").click()
    #
    # def test_sportsyahoo_37564222(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_3").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Scores/Schedule')]").click()
    #
    # def test_sportsyahoo_3e142eee(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ybar-navigation']/div[1]/ul[1]/li[5]/div[1]/ul[1]/li[9]/a[1]/div[1]").click()
    #
    # def test_sportsyahoo_56e4a9c1(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='subnavhtml-NBA']/div[1]/div[1]/div[2]/div[3]/div[1]/a[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Col1-0-Team-Proxy']/div[1]/div[1]/div[1]/div[2]/h1[1]/button[1]/span[1]/span[1]").click()
    #
    # def test_sportsyahoo_63d1f820(self):
    #     # self.driver.get("https://sports.yahoo.com/?guccounter=1")
    #     self.driver.find_element(By.ID, "root_4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='subnavhtml-NBA']/div[1]/div[1]/div[1]/div[3]/div[1]/a[2]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sub-nav']/ul[1]/li[3]/a[1]/span[1]").click()
    