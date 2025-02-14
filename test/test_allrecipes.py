import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestAllrecipes:
    def test_allrecipes_87db8a52(self):
        # self.driver.get("https://allrecipes.com")
        self.driver.find_element(By.XPATH, "//nav[@id='mntl-header-nav_1-0']//a[contains(text(),'Ingredients')]").click()
        self.driver.find_element(By.ID, "mntl-search-form--hero__search-input").click()
        self.driver.find_element(By.ID, "mntl-search-form--hero__search-input").clear()
        self.driver.find_element(By.ID, "mntl-search-form--hero__search-input").send_keys("cinnamon")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Click to search' and contains(text(),'GO')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='mntl-card-list-items_1-0']/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//button[@class='mm-recipes-social-share__share-button']/span").click()
    