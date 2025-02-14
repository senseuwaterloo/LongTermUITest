import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestUdemy:
    def test_udemy_949e33a5(self):
        # self.driver.get("https://www.udemy.com/")

        # self.driver.find_element(By.ID, "u148-search-form-autocomplete--3").clear()
        # self.driver.find_element(By.ID, "u148-search-form-autocomplete--3").send_keys("home workout")
        self.driver.find_element(By.NAME, "q").clear()
        self.driver.find_element(By.NAME, "q").send_keys("home workout")

        # self.driver.find_element(By.XPATH, "//a[@id='u148-search-form-autocomplete--3-0']/div[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.NAME, "q").send_keys(Keys.RETURN)

        # self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='u83-accordion-panel-title--239']/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Video Duration']").click()
        self.driver.find_element(By.XPATH, "//label[text()='0-1 Hour']").click()

        # self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='u83-accordion-panel-title--283']/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Topic']").click()
        self.driver.find_element(By.XPATH, "//label[text()='Weight Loss']").click()

        # self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='u83-accordion-panel-title--254']/span[1]").click()
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Level']").click()
        self.driver.find_element(By.XPATH, "//label[text()='Beginner']").click()

        # self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[3]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='u83-accordion-panel-title--276']/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Subtitles']").click()
        self.driver.find_element(By.XPATH, "//div[./div[1]/h3/button/span[text()='Subtitles']]//label[text()='English']").click()

        # self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[2]/svg[1]").click()
        # self.driver.find_element(By.ID, "u83-form-group--198").clear()
        # self.driver.find_element(By.ID, "u83-form-group--198").select("Newest")
        # need to wait for a few seconds otherwise the dropdown selection will coincident with page refreshing process and wrong item will be selected
        time.sleep(2)
        sort_dropdown = self.driver.find_element(By.NAME, "sort")
        sort_select = Select(sort_dropdown)
        sort_select.select_by_value("newest")
        time.sleep(1)
