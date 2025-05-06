import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestFoxsports:
    def test_foxsports_af97084c(self):
        self.driver.get("https://foxsports.com")
        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ssrExploreSports']/div[2]/a[7]/div[1]/div[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='exploreApp']/div[2]/div[3]/a[6]/div[2]").click()

        self.driver.find_element(By.XPATH, "//div[@id='exploreApp']/div[2]/div[3]/a[4]/div[2]/div[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a[6]/h2[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='__layout']/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[1]/div/a[1]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(), 'J. Musiala')]").click()
