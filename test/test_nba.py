import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab, switch_to_new_tab_and_close_old


@pytest.mark.usefixtures("setup_class")
class TestNba:
    def test_nba_a6cb6d95(self):
        self.driver.get("https://www.nba.com/")

        self.driver.find_element(By.XPATH, "//a[@data-id='nba:navigation:category:link' and @data-content='Teams']/span").click()

        self.driver.find_element(By.XPATH, "//a[text()='New York Knicks']").click()
        switch_to_new_tab_and_close_old(self.driver)

        if self.driver.find_element(By.XPATH, "//button[@type='button' and @aria-label='Close popup']") is not None:
            self.driver.find_element(By.XPATH, "//button[@type='button' and @aria-label='Close popup']").click()

        self.driver.find_element(By.XPATH, "//li[@class='menu-item' and @role='menuitem']/a[1]/span[text()='TEAM']").click()

        self.driver.find_element(By.XPATH, "//a[text()='Team & Player Stats' and preceding-sibling::*[1][self::h1 and text()='Roster']]").click()
        switch_to_new_tab(self.driver)

        self.driver.find_element(By.XPATH, "//span[text()='Roster']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Team Stats' and @role='button']").click()

        season_dropdown = self.driver.find_element(By.XPATH, "//select[@name='' and contains(@class, 'DropDown_select__') and ancestor::div[preceding-sibling::*[1][self::p and text()='Season']]]")
        season_select = Select(season_dropdown)
        season_select.select_by_value("2021-22")

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
