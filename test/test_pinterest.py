import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestPinterest:
    def test_pinterest_70cb365b(self):
        # self.driver.get("https://pinterest.com")
        # uiteststudy@gmail.com:Pass4Pinterest2024!

        # add login steps because login is required to download the images
        # won't show search result after login, so try not to login and not download.
        # Finally decided to just to download the images at the home page
        self.driver.find_element(By.XPATH, "//div[@data-test-id='simple-login-button']/button").click()
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys("Pass4Pinterest2024!")
        self.driver.find_element(By.XPATH, "//div[@data-test-id='registerFormSubmitButton']/button").click()

        # add extra step to navigate to the explore page
        # self.driver.find_element(By.XPATH, "//span[text()='Explore']").click()

        # self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").clear()
        # self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").send_keys("christian quotes")
        self.driver.find_element(By.NAME, "searchBoxInput").clear()
        self.driver.find_element(By.NAME, "searchBoxInput").send_keys("christian quotes")

        # self.driver.find_element(By.XPATH, "//div[@id='SuggestionGroup-Option-0-1']/a[1]/div[1]/div[1]/div[1]/div[1]").click()
        # somehow the searching result page is black, not sure whether the return key properly send, so try to add some sleep time. And it turned out the sleep solves the problem.
        time.sleep(2)
        self.driver.find_element(By.NAME, "searchBoxInput").send_keys(Keys.RETURN)

        # go back to the home page since the search result is often blank
        self.driver.back()

        # self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='gradient']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='max-width-container']/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='closeup-action-bar-button']//button[@aria-label='More options']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()

        # navigate back to the search result page to click other image
        self.driver.back()

        # self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='gradient']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='gradient']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[22]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='gradient']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='gradient']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()

        self.driver.find_element(By.XPATH, "//div[@data-test-id='max-width-container']/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='closeup-action-bar-button']//button[@aria-label='More options']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()

        # navigate back to the search result page to click other image
        self.driver.back()

        self.driver.find_element(By.XPATH, "//div[@data-test-id='max-width-container']/div[1]/div[1]/div[3]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='closeup-action-bar-button']//button[@aria-label='More options']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()

        # navigate back to the search result page to click other image
        self.driver.back()

        self.driver.find_element(By.XPATH, "//div[@data-test-id='max-width-container']/div[1]/div[1]/div[4]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='closeup-action-bar-button']//button[@aria-label='More options']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()

        # navigate back to the search result page to click other image
        self.driver.back()

        self.driver.find_element(By.XPATH, "//div[@data-test-id='max-width-container']/div[1]/div[1]/div[5]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test-id='closeup-action-bar-button']//button[@aria-label='More options']").click()

        self.driver.find_element(By.XPATH, "//span[@title='Download image']").click()
