import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestCareersWalmart:
    def test_careerswalmart_051a421d(self):
        self.driver.get("https://careers.walmart.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Career Areas')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sam’s Club Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See All Openings')]").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("DALLAS")
        self.driver.find_element(By.XPATH, "//ul[@id='search-location-list']/li[8]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='type-accordion']/div[1]/div[3]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rate-accordion']/div[1]/div[2]/label[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@id='department-accordion']/div[1]/div[5]/h6[1]").click()
        self.driver.find_element(By.XPATH, "//label[@for='dep-410']").click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'(USA) Member Specialist: Internship ( Unlocked Potential )')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='job-data__apply']//a[contains(text(),'Apply')]").click()
    