import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestSoundcloud:
    def test_soundcloud_57f72023(self):
        self.driver.get("https://soundcloud.com")

        self.driver.find_element(By.XPATH, "//div[@id='content']//input[@name='q' and @type='search']").clear()
        self.driver.find_element(By.XPATH, "//div[@id='content']//input[@name='q' and @type='search']").send_keys("SOUTH AFRICAN HISTORY PODCAST")

        self.driver.find_element(By.XPATH, "//div[@id='content']//button[@type='submit' and text()='Search']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tracks')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'10-30 min')]").click()

        self.driver.find_element(By.XPATH, "//a[@data-tag='audiobooks']").click()
