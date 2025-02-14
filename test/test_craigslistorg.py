import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestCraigslistOrg:
    def test_craigslistorg_3154d1c8(self):
        # self.driver.get("https://craigslist.org")
        # changed the locator of this test case
        self.driver.find_element(By.XPATH, "//h5[text()='us cities']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'new') and contains(text(), 'york') and @href='//newyork.craigslist.org']").click()
        # self.driver.find_element(By.XPATH, "//b[contains(.,'new york city')]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='hhh0']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='hasPic' and @value='1' and @type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-toolbars-1']/div[1]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'gallery')]").click()

        # self.driver.find_element(By.XPATH, "//select[@name='availabilityMode']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='availabilityMode']").select("within 30 days")
        all_dates_dropdown = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/form/div[3]/div[2]/select")
        all_dates_select = Select(all_dates_dropdown)
        all_dates_select.select_by_value('1')

        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/form/div[3]/div[2]/div[8]/label[8]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/form/div[3]/div[2]/div[8]/label[3]").click()
        self.driver.find_element(By.XPATH, "//input[@name='min_bedrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='min_bedrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").send_keys("1")
        self.driver.find_element(By.XPATH, "//input[@name='min_bathrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='min_bathrooms' and @type='tel' and @placeholder='min' and @title='whole number, no letters or symbols']").send_keys("1")
        self.driver.find_element(By.XPATH, "//span[contains(.,'apply')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'parking')]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'attached garage')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'apply')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-results-page-1']/ol/li[1]/div/div[1]/div[1]/a/div[1]/div/div[1]").click()
        self.driver.find_element(By.ID, "printme").click()
    