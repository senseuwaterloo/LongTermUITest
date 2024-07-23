import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestEspn:
    
    # def test_espn_87e3b392(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.ID, "global-search-trigger").click()
    #     self.driver.find_element(By.ID, "global-search-input").clear()
    #     self.driver.find_element(By.ID, "global-search-input").send_keys("Cristiano Ronaldo")
    #     self.driver.find_element(By.XPATH, "//div[@id='global-search']/div[2]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='nav-link-nav-menu-item-7019']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/select[1]").select("Portugal")
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[2]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[2]/select[1]").select("World Cup")
    #
    # def test_espn_88a8cd3b(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[6]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='submenu-sportsmenusoccer']/ul[1]/li[6]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[6]/div[1]/section[1]/div[1]/a[1]/h2[1]").click()
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav-secondary']/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='schedule-page']/div[1]/div[1]/div[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='schedule-page']/div[1]/div[1]/div[3]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='schedule-page']/div[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[7]").click()
    #
    # def test_espn_0343d8d9(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//button[@id='submenu-button-submenu-pillarwatch']/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='submenu-pillarwatch']/ul[1]/li[4]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Upcoming')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/select[1]").select("Soccer")
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/select[1]").select("ESPN2")
    #
    # def test_espn_0435ac39(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[2]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='submenu-sportsactivemenunba']/ul[2]/li[1]/div[1]/ul[1]/li[3]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='nav-link-nav-menu-item-7933']/span[1]").click()
    #
    # def test_espn_cfb351f8(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.ID, "submenu-button-submenu-sportsmenusoccer").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='submenu-sportsmenusoccer']/ul[1]/li[6]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Stats')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/section[1]/div[1]/div[3]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/section[1]/div[1]/div[3]/select[1]").select("2022")
    #
    # def test_espn_d7ab9bf0(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.ID, "nav-link-nav-menu-item-3422").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='fitt-analytics']/div[1]/header[1]/div[1]/nav[1]/ul[1]/li[6]/div[1]/div[1]/div[1]/ul[1]/section[1]/div[1]/ul[1]/li[2]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Manchester City')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='nav-link-nav-menu-item-8505']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/section[1]/div[1]/div[3]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/section[1]/div[1]/div[3]/select[1]").select("UEFA Champions League")
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/section[1]/div[1]/div[4]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/section[1]/div[1]/div[4]/select[1]").select("2022-23")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Performance')]").click()
    #
    # def test_espn_969f36c3(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.ID, "global-search-trigger").click()
    #     self.driver.find_element(By.ID, "global-search-input").clear()
    #     self.driver.find_element(By.ID, "global-search-input").send_keys("Michael Jordan")
    #     self.driver.find_element(By.ID, "global-search-input").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='a04c6b43b14581a92d42b04dc85fbf9d']/div[2]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='nav-link-nav-menu-item-2450']/span[1]").click()
    #
    # def test_espn_ac35e5a5(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[6]").click()
    #     self.driver.find_element(By.XPATH, "//a[@name='&lpos=sitenavcustom_soccer_team_barcelona']").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='nav-link-nav-menu-item-5591']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/section[1]/div[1]/section[1]/div[2]/div[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/section[1]/div[1]/section[1]/div[2]/div[1]/select[1]").select("Spanish Copa del Rey")
    #
    # def test_espn_b1a1f767(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.ID, "global-search-trigger").click()
    #     self.driver.find_element(By.ID, "global-search-input").clear()
    #     self.driver.find_element(By.ID, "global-search-input").send_keys("Mikal Bridges")
    #     self.driver.find_element(By.XPATH, "//div[@id='global-search']/div[2]/div[1]/div[2]/ul[1]/li[1]/a[1]/div[1]/span[1]").click()
    #
    # def test_espn_bb31a9f4(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[7]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='submenu-nonemore']/ul[1]/li[10]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='main-container']/div[1]/section[1]/article[1]/div[1]/ul[1]/li[1]/a[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='news-feed']/article[2]/section[1]/figure[1]/picture[1]/source[1]/source[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Play Video']").click()
    #
    # def test_espn_6a7eaba3(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[6]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='submenu-sportsmenumma']/ul[1]/li[2]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/select[1]").select("2019")
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/select[1]").select("UFC")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'UFC Fight Night: Edgar vs. The Korean Zombie')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Full Profile')]").click()
    #
    # def test_espn_7a632871(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[2]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@name='&lpos=sitenavcustom+nba_nbascoreboard']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/button[1]/svg[1]/use[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/ul[2]/li[7]").click()
    #
    # def test_espn_e3016f6f(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[2]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@name='&lpos=subnav+subnav__team_dallas_mavericks']").click()
    #     self.driver.find_element(By.ID, "nav-link-nav-menu-item-9023").click()
    #
    # def test_espn_627a99f1(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.ID, "global-search-trigger").click()
    #     self.driver.find_element(By.ID, "global-search-input").clear()
    #     self.driver.find_element(By.ID, "global-search-input").send_keys("Kevin Durant")
    #     self.driver.find_element(By.XPATH, "//div[@id='global-search']/div[2]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='nav-link-nav-menu-item-2127']/span[1]").click()
    #
    # def test_espn_6678924a(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.ID, "global-search-trigger").click()
    #     self.driver.find_element(By.ID, "global-search-input").clear()
    #     self.driver.find_element(By.ID, "global-search-input").send_keys("Golden State Warriors")
    #     self.driver.find_element(By.XPATH, "//div[@id='global-search']/div[2]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='nav-link-nav-menu-item-6922']/span[1]").click()
    
    def test_espn_be5e5f14(self):
        # self.driver.get("https://espn.com")
        self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[1]/a[1]/span[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//nav[@id='global-nav-secondary']/div[1]/ul[1]/li[4]/a[1]/span[1]").click()
        # should click somewhere else to hide the hover window
        self.driver.find_element(By.ID, "global-search-trigger").click()

        self.driver.find_element(By.XPATH, "//nav[@id='global-nav-secondary']/div[1]/ul[1]/li[3]/a[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Calendar']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]/use[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[27]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@class='MonthContainer__WeekList__item']//span[text()='Super Bowl']").click()
    
    # def test_espn_16886ec7(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//button[@id='submenu-button-submenu-sportsmenunba']/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='submenu-sportsmenunba']/ul[1]/li[5]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Points')]").click()
    #
    # def test_espn_254a67f6(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[5]").click()
    #     self.driver.find_element(By.XPATH, "//a[@name='&lpos=sitenavcustom_soccer_teams']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/select[1]").select("Spanish LaLiga")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Stats')]").click()
    #
    # def test_espn_2a440d5f(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[2]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav-secondary']/div[1]/ul[1]/li[7]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='nav-menu-item-2375']/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Season Leaders')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/select[1]").select("2020-21 Regular Season")
    #
    # def test_espn_4b431888(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.ID, "global-search-trigger").click()
    #     self.driver.find_element(By.ID, "global-search-input").clear()
    #     self.driver.find_element(By.ID, "global-search-input").send_keys("Real Madrid")
    #     self.driver.find_element(By.XPATH, "//div[@id='global-search']/div[2]/div[1]/div[2]/ul[1]/li[1]/a[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='nav-link-nav-menu-item-6693']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/section[1]/div[1]/section[1]/div[2]/div[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/section[1]/div[1]/section[1]/div[2]/div[1]/select[1]").select("UEFA Champions League")
    #
    # def test_espn_e6643cfb(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//a[@id='nav-link-nav-menu-item-7360']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Teams')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/a[1]/h2[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Full Team Statistics')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[5]/div[1]/div[1]/section[1]/div[1]/div[5]/section[1]/a[1]/div[1]/div[2]/h3[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #
    # def test_espn_e7e1616e(self):
    #     # self.driver.get("https://espn.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[2]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='submenu-sportsmenunba']/ul[1]/li[2]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/span[1]").click()
    