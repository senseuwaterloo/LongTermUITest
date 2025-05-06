import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestSportsYahoo:
    def test_sportsyahoo_92b51ef3(self):
        self.driver.get("https://sports.yahoo.com/?guccounter=1")

        self.driver.find_element(By.ID, "ybar-sbq").clear()
        self.driver.find_element(By.ID, "ybar-sbq").send_keys("lebron james")

        self.driver.find_element(By.XPATH, "//img[@alt='LeBron James']").click()

        self.driver.find_element(By.XPATH, "//div[@id='sub-nav']/ul[1]/li[4]/a[1]/span[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='Col1-1-SportsStream']/ul[1]/li[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='shareMenuTooltip']/div[1]/a[2]").click()
