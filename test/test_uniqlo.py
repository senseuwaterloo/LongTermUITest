import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestUniqlo:
    def test_uniqlo_122178b3(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        # self.driver.find_element(By.XPATH, "//svg[@role='presentation']").click()
        self.driver.find_element(By.XPATH, "//div[@role='button' and contains(@class, 'fr-ec-bottom-navigation__icon-wrapper-center')]").click()

        # self.driver.find_element(By.ID, "Search").clear()
        # self.driver.find_element(By.ID, "Search").send_keys("blazer")
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by keyword']").click()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by keyword']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by keyword']").send_keys("blazer")

        # self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[1]/a[3]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//mark[text()='blazer' and not(following-sibling::*) and not(preceding-sibling::*)]").click()

        self.driver.find_element(By.XPATH, "//h4[@title='Gender > Category']").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@role='option' and @value='22211']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'fr-ec-utility-bar__modal__close-icon')]/div[1]").click()

        self.driver.find_element(By.XPATH, "//h4[@title='Color']").click()

        # self.driver.find_element(By.XPATH, "//fieldset[@id='colorFilterCheckBox']/div[1]/div[2]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section//fieldset[@id='colorFilterCheckBox']/div[1]/div[2]/div[1]/label[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'fr-ec-utility-bar__modal__close-icon')]/div[1]").click()

        # self.driver.find_element(By.XPATH, "//a[@id='E448034-000']/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[3]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[5]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[3]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Size']").click()
        self.driver.find_element(By.XPATH, "//section//label[@for='check-L']").click()
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'fr-ec-utility-bar__modal__close-icon')]/div[1]").click()

        time.sleep(6)
