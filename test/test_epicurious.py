import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestEpicurious:
    def test_epicurious_d7fb2a4f(self):
        # self.driver.get("https://epicurious.com")
        # self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
        self.driver.find_element(By.ID, "search-form-text-field-q").click()

        # self.driver.find_element(By.ID, "inputTerms").clear()
        # self.driver.find_element(By.ID, "inputTerms").send_keys("CURRY")
        self.driver.find_element(By.ID, "search-form-text-field-q").clear()
        self.driver.find_element(By.ID, "search-form-text-field-q").send_keys("CURRY")

        # self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
        self.driver.find_element(By.ID, "search-form-text-field-q").send_keys(Keys.RETURN)

        # website logic changed, now can only filter dinner and south asian food
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[6]/h3[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[9]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[15]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h3[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/h3[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[9]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[28]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[2]/h3[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'react-select-') and contains(@id, '-placeholder') and text()='Popular']").click()

        # somehow clicking the label element in the div is not working
        # Just tried again, somehow seems fine now.
        self.driver.find_element(By.ID, "react-select-2-option-5").click() # somehow clicking the label element in the div is not working
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'react-select-') and contains(@id, '-placeholder') and text()='Cuisines & Flavors']").click()

        # somehow clicking the label element in the div is not working
        self.driver.find_element(By.ID, "react-select-4-option-7").click()
        # was using the following step to close the dropdown in case click interception happens, also seems unnecessary and fine now.
        # self.driver.find_element(By.XPATH, "//div[contains(@id, 'react-select-') and contains(@id, '-placeholder') and text()='Cuisines & Flavors']").click()
        self.driver.find_element(By.XPATH, "//div[@id='0-Recipes']/div[2]/section/div/div/div/div[1]/div[1]/div[1]/span").click()
