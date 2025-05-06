import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element, scroll_down


@pytest.mark.usefixtures("setup_class")
class TestIndeed:
    def test_indeed_4ce51ed5(self):
        self.driver.get("https://www.indeed.com/worldwide")

        self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[1]/ul[1]/li[58]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Browse Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'England')]").click()

        chelmsford_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs in Chelmsford')]")
        scroll_to_element(self.driver, chelmsford_link)
        scroll_down(self.driver, 500)
        chelmsford_link.click()

        time.sleep(3)
        sort_date_button = self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']/div[1]").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element(sort_date_button)
        action.click().perform()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Last 24 hours')]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='filter-srctype']/div[1]").click()

        self.driver.find_element(By.XPATH, "//a[text()='Employer']").click()

        time.sleep(3)
        self.driver.find_element(By.ID, "filter-taxo2").click()

        self.driver.find_element(By.XPATH, "//span[text()='Healthcare']").click()
        self.driver.find_element(By.XPATH, "//button[@form='filter-taxo2-menu']").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='filter-jobtype']/div[1]").click()

        self.driver.find_element(By.XPATH, "//a[text()='Part-time']").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='filter-salary-estimate']/div[1]").click()

        self.driver.find_element(By.XPATH, "//a[text()='£20,000+']").click()

        self.driver.find_element(By.ID, "dateLabel").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[@id='mosaic-provider-jobcards']/ul/li[1]/div/div/div/div/div/table/tbody/tr/td[2]/button").click()

        self.driver.find_element(By.XPATH, "//div[@data-valuetext='Report job']").click()

        self.driver.find_element(By.XPATH, "//span[text()='It seems like a fake job']").click()

        self.driver.find_element(By.ID, "ifl-TextAreaFormField-8").clear()
        self.driver.find_element(By.ID, "ifl-TextAreaFormField-8").send_keys("Seems fake")
    