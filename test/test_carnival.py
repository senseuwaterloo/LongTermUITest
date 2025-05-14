import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestCarnival:
    def test_carnival_c1b8361d(self):
        self.driver.get("https://www.carnival.com/")
        self.driver.find_element(By.ID, "cdc-destinations").click()

        self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[16]/button[1]").click()
        self.driver.find_element(By.ID, "cdc-ports").click()
        self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[3]/button[1]").click()

        self.driver.find_element(By.XPATH, "//a[@id='cdc-dates']/span[1]/span[1]").click()

        self.driver.find_element(By.XPATH, "//button[@aria-label='November 2025 ']").click()
        self.driver.find_element(By.ID, "cdc-durations").click()
        self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]").click()

        self.driver.find_element(By.XPATH, "//button[@aria-label='Show 1 Date']").click()

        self.driver.find_element(By.XPATH, "//a[@data-testid='selectSailingDateButton']").click()

        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/button[1]/span[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/button").click()

        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div/div/div/div/div/div/div[3]/div/div/div[2]/button").click()

        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[3]/button").click()

        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/button[1]").click()
    