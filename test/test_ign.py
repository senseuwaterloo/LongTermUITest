import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestIgn:
    def test_ign_5ad0f114(self):
        self.driver.get("https://ign.com")

        self.driver.find_element(By.XPATH, "//div[@id='__next']/aside/nav/div[1]/div[1]/div[2]/div[3]/a[2]/div").click()

        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[2]/section/div[2]/div/button/div/div").click()

        self.driver.find_element(By.ID, "term").clear()
        self.driver.find_element(By.ID, "term").send_keys("Uncharted Legacy of Thieves Collection")

        self.driver.find_element(By.XPATH, "//div[text()='Uncharted: Legacy of Thieves Collection']").click()

        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div/div[4]/section[2]/div/div/a/div/button").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/aside[1]/nav[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/a[1]/div[1]").click()

        self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[3]/div[4]/div/div[2]/section[1]/section[9]/ul/li[2]/a").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),\"The Queen's Bracelet\")]").click()
