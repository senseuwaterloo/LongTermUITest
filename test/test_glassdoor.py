import time

import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestGlassdoor:
    def test_glassdoor_36113c94(self):
        self.driver.get("https://glassdoor.com")

        self.driver.find_element(By.XPATH, "//div[@id='SignInButton']/button[1]").click()
        self.driver.find_element(By.ID, "modalUserEmail").clear()
        self.driver.find_element(By.ID, "modalUserEmail").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//div[@data-test='authModalContainerV2-content']//button[@data-test='email-form-button']").click()
        self.driver.find_element(By.ID, "modalUserPassword").clear()
        self.driver.find_element(By.ID, "modalUserPassword").send_keys("Pass4Glassdoor2024!")

        time.sleep(2)

        login_button = self.driver.find_element(By.XPATH, "//div[@id='InlineLoginModule']/div/div[1]/div[1]/div/div/div/form/div[2]").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(login_button, 15, 15)
        action.click().perform()

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@id='globalNavContainer']/div/ul/li[2]").click()

        self.driver.find_element(By.ID, "searchBar-jobTitle").clear()
        self.driver.find_element(By.ID, "searchBar-jobTitle").send_keys("copywriter")
        self.driver.find_element(By.ID, "searchBar-location").clear()
        self.driver.find_element(By.ID, "searchBar-location").send_keys("mumbai")
        self.driver.find_element(By.ID, "searchBar-location").send_keys(Keys.RETURN)

        self.driver.find_element(By.XPATH, "//button[@aria-label='Cancel']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='expand-filters']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='jobTypeIndeed-option' and contains(., 'Full-time')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='fromAge' and text()='Date posted']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='fromAge-option' and contains(., 'Last week')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='radius' and text()='Distance']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='radius-option' and contains(., '50 miles')]").click()
        self.driver.find_element(By.XPATH, "//label[@aria-label='Easy Apply only']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='apply-search-filters' and contains(., 'Apply filters')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='sortBy' and text()='Most relevant']").click()
        self.driver.find_element(By.XPATH, "//button[@role='option' and text()='Most recent']").click()
