import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestThumbtack:
    def test_thumbtack_5a55aaa5(self):
        # self.driver.get("https://www.thumbtack.com/")
        # TODO looks like this website provide two interact logics regarding the time selection! So the test steps can be different for different run! Need to think about it! Consider remove.

        # self.driver.find_element(By.XPATH, "//div[@title='Phone or Tablet Repair']").click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Search on Thumbtack']").clear()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Search on Thumbtack']").send_keys("Phone or Tablet Repair")

        # self.driver.find_element(By.XPATH, "//input[@value='43235' and @type='text' and @placeholder='Enter a zip code']").clear()
        # self.driver.find_element(By.XPATH, "//input[@value='43235' and @type='text' and @placeholder='Enter a zip code']").send_keys("89116")
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/form[1]/div[1]/button[1]").click()
        self.driver.find_element(By.NAME, "zip_code").clear()
        self.driver.find_element(By.NAME, "zip_code").send_keys("89116")
        # somehow need to wait for a few seconds before clicking on the search button otherwise the code will pass but the click action is not actually triggered
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Search' and @type='button' and text()='Search']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app-page-root']/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app-page-root']/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[16]/label[1]/svg[1]/g[1]/circle[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app-page-root']/div[1]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/label[1]/svg[1]/g[1]/circle[1]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[text()='iPad mini']").click()
        self.driver.find_element(By.XPATH, "//section//div[text()='Water damage']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app-page-root']/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[2]/div[1]/p[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='pro-list-result-price-info']").click()

        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId7']/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId8']/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId9']/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='request-flow-step--active']//button[@type='submit' and ./span[text()='Next']]").click()
        # deselect the at my home option since we want it to be done at the pro's location
        self.driver.find_element(By.XPATH, "//span[text()='My home, venue, etc.']").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='request-flow-step--active']//button[@type='submit' and ./span[text()='Next']]").click()
        # choose "Flexible on timeline" to avoid extra steps
        self.driver.find_element(By.XPATH, "//span[text()='Flexible on timeline']").click()
        # logic changed, need to input the description here
        self.driver.find_element(By.XPATH, "//textarea[@data-test='request-flow-text-box']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@data-test='request-flow-text-box']").send_keys("not turning on")
        self.driver.find_element(By.XPATH, "//div[@data-testid='request-flow-step--active']//button[@type='submit' and ./span[text()='Next']]").click()

        # need to input an email address in the new web app
        self.driver.find_element(By.XPATH, "//input[@data-test='request-flow-text-box']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-test='request-flow-text-box']").send_keys("joe@joebloggs.com")
        self.driver.find_element(By.XPATH, "//div[@data-testid='request-flow-step--active']//button[@type='submit' and ./span[text()='Next']]").click()

        # logic changed, customize time to morning or afternoon is no longer available. Just select the flexible time option now
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId10']/div[1]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[2]/label[1]/div[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId10']/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId11']/div[1]/div[1]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId11']/div[1]/div[1]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[7]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId11']/div[1]/div[1]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId11']/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId12']/div[1]/div[1]/ol[1]/li[1]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId12']/div[1]/div[1]/ol[1]/li[1]/div[1]/div[2]/div[2]/label[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId12']/div[1]/div[1]/ol[1]/li[1]/div[1]/div[2]/div[5]/label[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId12']/div[2]/div[1]/div[1]/button[1]/span[1]").click()

        # moved to above
        # self.driver.find_element(By.XPATH, "//textarea[@placeholder='Describe the task or project in more detail']").clear()
        # self.driver.find_element(By.XPATH, "//textarea[@placeholder='Describe the task or project in more detail']").send_keys("not turning on")

        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId13']/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='uniqueId14']/div[2]/div[1]/div[1]/button[1]/span[1]").click()
        # need to give a phone number and click on submit now. Just give a fake number and click on the "Back" button to avoid sending spam data
        self.driver.find_element(By.XPATH, "//input[@data-test='request-flow-text-box' and @type='tel']").clear()
        self.driver.find_element(By.XPATH, "//input[@data-test='request-flow-text-box' and @type='tel']").send_keys("1239990000")
        self.driver.find_element(By.XPATH, "//div[@data-testid='request-flow-step--active']//button[@type='button' and ./span[text()='Back']]").click()
