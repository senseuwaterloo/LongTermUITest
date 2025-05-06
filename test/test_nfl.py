import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestNfl:
    def test_nfl_91843d71(self):
        self.driver.get("https://www.nfl.com/")

        self.driver.find_element(By.XPATH, "//a[@aria-label='More menu choices' and @aria-controls='2ndlevel']").click()
        self.driver.find_element(By.XPATH, "//ul[@id='2ndlevel']/li[1]/a/span").click()

        self.driver.find_element(By.ID, "player-search-input").clear()
        self.driver.find_element(By.ID, "player-search-input").send_keys("Joe Burrow")
        self.driver.find_element(By.ID, "player-search-button").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Joe Burrow')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Stats')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']//a[contains(text(),'Career')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[3]/div[1]/div[1]/div[1]/div[2]/table[1]/thead[1]/tr[1]/th[10]").click()
