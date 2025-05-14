import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestYellowpages:
    def test_yellowpages_32174c75(self):
        self.driver.get("https://www.yellowpages.com/")

        self.driver.find_element(By.XPATH, "//span[@class='icon attorneys']").click()

        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("west hollywood")
        self.driver.find_element(By.XPATH, "//ul[@id='autosuggest-location']/li[2]/a[1]/b[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='search-form']/button[1]/span[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='search-filters']/header[1]/section[1]/div[1]/div[1]/a[2]").click()

        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/label[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/h3[3]").click()

        self.driver.find_element(By.XPATH, "//label[@for='2languages2' and text()='Spanish']").click()

        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/h3[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/div[2]/div[2]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='facebox']/div[1]/div[1]/section[1]/button[1]").click()
        self.driver.find_element(By.ID, "js-sort-toggle").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Distance')]").click()
