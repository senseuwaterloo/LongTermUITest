import time

import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestGlassdoor:
    def test_glassdoor_36113c94(self):
        # self.driver.get("https://glassdoor.com")
        # uiteststudy@gmail.com:Pass4Glassdoor2024!
        # time.sleep(7)
        # add login steps
        self.driver.find_element(By.XPATH, "//div[@id='SignInButton']/button[1]").click()
        self.driver.find_element(By.ID, "modalUserEmail").clear()
        self.driver.find_element(By.ID, "modalUserEmail").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//div[@data-test='authModalContainerV2-content']//button[@data-test='email-form-button']").click()
        self.driver.find_element(By.ID, "modalUserPassword").clear()
        self.driver.find_element(By.ID, "modalUserPassword").send_keys("Pass4Glassdoor2024!")

        time.sleep(2)
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted.
        # if locate to div then will overlap with element "show password" and be intercepted
        # If located to button then will intercept by parent div
        # if locate to span then will intercept by parent div
        # STILL NOT WORKING EVEN TRY TO USE action perform. have to use offset to avoid clicking on the overlap part
        # self.driver.find_element(By.XPATH, "//div[@id='InlineLoginModule']/div/div[1]/div[1]/div/div/div/form/div[2]/button[1]/span[1]").click()
        # self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='InlineLoginModule']/div/div[1]/div[1]/div/div/div/form/div[2]/button[1]").get_native_element())
        login_button = self.driver.find_element(By.XPATH, "//div[@id='InlineLoginModule']/div/div[1]/div[1]/div/div/div/form/div[2]").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(login_button, 15, 15)
        action.click().perform()

        time.sleep(2)
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found
        self.driver.find_element(By.XPATH, "//div[@id='globalNavContainer']/div/ul/li[2]").click()

        # self.driver.find_element(By.ID, "sc.keyword").clear()
        # self.driver.find_element(By.ID, "sc.keyword").send_keys("copywriter")
        # self.driver.find_element(By.ID, "sc.location").clear()
        # self.driver.find_element(By.ID, "sc.location").send_keys("mumbai")
        self.driver.find_element(By.ID, "searchBar-jobTitle").clear()
        self.driver.find_element(By.ID, "searchBar-jobTitle").send_keys("copywriter")
        self.driver.find_element(By.ID, "searchBar-location").clear()
        self.driver.find_element(By.ID, "searchBar-location").send_keys("mumbai")
        self.driver.find_element(By.ID, "searchBar-location").send_keys(Keys.RETURN)

        # self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[1]/div[1]/div[1]/div[1]/span[1]/b[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='Discover']/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/strong[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='JAModal']/div[1]/div[2]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_jobType']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='PrimaryDropdown']/ul[1]/li[2]/button[1]/div[1]").click()
        # self.driver.find_element(By.ID, "filter_fromAge").click()
        # self.driver.find_element(By.XPATH, "//div[@id='PrimaryDropdown']/ul[1]/li[4]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_radius']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='PrimaryDropdown']/ul[1]/li[6]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//header[@id='DKFilters']/div[1]/div[1]/div[2]").click()
        # self.driver.find_element(By.XPATH, "//header[@id='DKFilters']/div[1]/div[1]/div[2]/div[2]/div[14]/label[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//header[@id='DKFilters']/div[1]/div[1]/div[2]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//article[@id='MainCol']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//article[@id='MainCol']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/button[1]/div[2]").click()
        # self.driver.find_element(By.XPATH, "//article[@id='MainCol']/div[1]/ul[1]/li[1]/div[2]/div[1]/div[1]/button[1]/span[1]/svg[1]").click()

        # NEED TO close a popup window
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
