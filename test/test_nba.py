import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab, switch_to_new_tab_and_close_old


@pytest.mark.usefixtures("setup_class")
class TestNba:
    def test_nba_a6cb6d95(self):
        # self.driver.get("https://www.nba.com/")
        # self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[7]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@data-id='nba:navigation:category:link' and @data-content='Teams']/span").click()

        # self.driver.find_element(By.XPATH, "//ul[@id='nav-ul']/li[7]/div[1]/div[1]/div[1]/div[1]/a[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[text()='New York Knicks']").click()
        switch_to_new_tab_and_close_old(self.driver)

        if self.driver.find_element(By.XPATH, "//button[@type='button' and @aria-label='Close popup']") is not None:
            self.driver.find_element(By.XPATH, "//button[@type='button' and @aria-label='Close popup']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/header[1]/div[3]/nav[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@class='menu-item' and @role='menuitem']/a[1]/span[text()='TEAM']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Team Stats')]").click()
        # use its immediate preceding sibling in the locator
        self.driver.find_element(By.XPATH, "//a[text()='Team & Player Stats' and preceding-sibling::*[1][self::h1 and text()='Roster']]").click()
        switch_to_new_tab(self.driver)

        # add extra steps
        self.driver.find_element(By.XPATH, "//span[text()='Roster']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Team Stats' and @role='button']").click()

        # self.driver.find_element(By.XPATH, "//select[@name='']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='']").select("2021-22")
        season_dropdown = self.driver.find_element(By.XPATH, "//select[@name='' and contains(@class, 'DropDown_select__') and ancestor::div[preceding-sibling::*[1][self::p and text()='Season']]]")
        season_select = Select(season_dropdown)
        season_select.select_by_value("2021-22")

        # self.driver.find_element(By.XPATH, "//button[@id='bx-close-inside-2078917']/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[2]/label[1]/div[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[2]/label[1]/div[1]/select[1]").select("Regular Season")
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[4]/label[1]/div[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[4]/label[1]/div[1]/select[1]").select("In Game Splits")
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[3]/label[1]/div[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[2]/main[1]/div[3]/section[2]/div[1]/div[1]/div[3]/label[1]/div[1]/select[1]").select("Per Game")
        season_type_dropdown = self.driver.find_element(By.XPATH,
                                                        "//select[@name='' and contains(@class, 'DropDown_select__') and ancestor::div[preceding-sibling::*[1][self::p and text()='Season Type']]]")
        season_type_select = Select(season_type_dropdown)
        season_type_select.select_by_value("Regular Season")
        per_mode_dropdown = self.driver.find_element(By.XPATH,
                                                     "//select[@name='' and contains(@class, 'DropDown_select__') and ancestor::div[preceding-sibling::*[1][self::p and text()='Per Mode']]]")
        per_mode_select = Select(per_mode_dropdown)
        per_mode_select.select_by_value("PerGame")
        split_dropdown = self.driver.find_element(By.XPATH, "//select[@name='' and contains(@class, 'DropDown_select__') and ancestor::div[preceding-sibling::*[1][self::p and text()='Split']]]")
        split_select = Select(split_dropdown)
        split_select.select_by_value("ingame")
