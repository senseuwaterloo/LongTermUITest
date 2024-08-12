import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestPinterest:
    
    # def test_pinterest_2c7f54d8(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='HeaderContent']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[5]/div[1]/div[1]/button[1]/div[1]/div[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Settings']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[7]/a[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/div[1]/div[1]").click()
    #
    # def test_pinterest_332ed50d(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='HeaderContent']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[4]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Board']").click()
    #     self.driver.find_element(By.ID, "boardEditName").clear()
    #     self.driver.find_element(By.ID, "boardEditName").send_keys("Fitness")
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Create')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Done')]").click()
    #
    # def test_pinterest_422fe656(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='HeaderContent']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[5]/div[1]/div[1]/button[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Tune your home feed']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]").click()
    #
    # def test_pinterest_4ccaf154(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").send_keys("male outfits beach vacation")
    #     self.driver.find_element(By.XPATH, "//div[@id='SuggestionGroup-Option-0-0']/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[2]/span[1]").click()
    #
    # def test_pinterest_52fc45f3(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").send_keys("Low poly")
    #     self.driver.find_element(By.XPATH, "//div[@id='SuggestionGroup-Option-0-0']/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
    #
    # def test_pinterest_5e58544f(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='HeaderContent']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[5]/div[1]/div[1]/button[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Settings']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[6]/a[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "video_autoplay_setting_on").click()
    #
    # def test_pinterest_67d910dd(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").send_keys("sticker mania")
    #     self.driver.find_element(By.XPATH, "//div[@id='SuggestionGroup-Option-0-1']/a[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/button[1]/div[1]/div[1]/svg[1]/path[1]").click()
    
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
    
    # def test_pinterest_9253dcd5(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").send_keys("bodyweight routine")
    #     self.driver.find_element(By.XPATH, "//div[@id='SuggestionGroup-Option-0-3']/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='gradient']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='gradient']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #
    # def test_pinterest_a4c1b00d(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").send_keys("Halloween costume")
    #     self.driver.find_element(By.XPATH, "//div[@id='SuggestionGroup-Option-0-0']/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='gradient']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]").click()
    #
    # def test_pinterest_b7716f95(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='HeaderContent']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[4]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/div[1]/div[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='board_actions-item-2']/div[1]").click()
    #     self.driver.find_element(By.ID, "boardEditName").clear()
    #     self.driver.find_element(By.ID, "boardEditName").send_keys("Home Decor Inspiration")
    #     self.driver.find_element(By.ID, "secret").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Create')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Done')]").click()
    #
    # def test_pinterest_cd9c70b3(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='HeaderContent']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='inbox-overflow-menu-item-0']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #
    # def test_pinterest_e0e3b176(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='HeaderContent']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[4]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Board']").click()
    #     self.driver.find_element(By.ID, "boardEditName").clear()
    #     self.driver.find_element(By.ID, "boardEditName").send_keys("Quotes")
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Create')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Done')]").click()
    #
    # def test_pinterest_f63e7816(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='HeaderContent']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[4]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Board']").click()
    #     self.driver.find_element(By.ID, "boardEditName").clear()
    #     self.driver.find_element(By.ID, "boardEditName").send_keys("Healthy Eating")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Done')]").click()
    #
    # def test_pinterest_02e0f797(self):
    #     # self.driver.get("https://pinterest.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='searchBoxInput' and @value='' and @type='text' and @placeholder='Search']").send_keys("seafood pasta")
    #     self.driver.find_element(By.XPATH, "//div[@id='SuggestionGroup-Option-0-0']/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__PWS_ROOT__']/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='gradient']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='gradient']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/button[1]/svg[1]/rect[1]").click()
    #
