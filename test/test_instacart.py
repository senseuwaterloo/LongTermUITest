import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import switch_to_new_tab_and_return_old


@pytest.mark.usefixtures("setup_class")
class TestInstacart:
    def test_instacart_10b2af14(self):
        # self.driver.get("https://instacart.com")
        # uiteststudy@gmail.com:Pass4Instacart!
        # signin with gmail: uiteststudy@gmail.com:UITestStudy2024 to avoid verification code

        # add login steps
        self.driver.find_element(By.XPATH, "//button[@data-testid='auth-buttons-login']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Continue with Google']").click()
        original_window = switch_to_new_tab_and_return_old(self.driver)
        self.driver.find_element(By.NAME, "identifier").clear()
        self.driver.find_element(By.NAME, "identifier").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
        self.driver.find_element(By.NAME, "Passwd").clear()
        self.driver.find_element(By.NAME, "Passwd").send_keys("UITestStudy2024")
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
        self.driver.switch_to.window(original_window)
        self.driver.find_element(By.XPATH, "//span[text()='No thanks']").click()

        # self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div[1]/span[1]/button[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='commonHeader']/div/div/span/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='id-2611']/nav[1]/ul[1]/div[4]/li[3]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Your lists']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Create a list')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='id-2638']/div[2]/div[2]/div[1]/button[1]/div[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Choose a store (Required)']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='id-2639']/div[2]/div[32]/a[1]/span[2]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Walgreens']").click()

        self.driver.find_element(By.ID, "title").clear()
        self.driver.find_element(By.ID, "title").send_keys("Walgreens")

        # self.driver.find_element(By.XPATH, "//div[@id='id-2643']/div[2]/div[1]/div[1]/div[6]/ul[1]/div[1]/li[5]/button[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Add a cover photo to your list']/following-sibling::div//ul//img").click()

        # self.driver.find_element(By.XPATH, "//div[@id='id-2643']/div[2]/div[1]/div[1]/div[7]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='list-sticky-footer-cta-mobile']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/ul[1]/li[8]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='item-search-bar-button']").click()

        # website logic changed, so will rewrite the code based on the task
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//input[@id='search-bar-input']").clear()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//input[@id='search-bar-input']").send_keys("personal care")
        self.driver.find_element(By.ID, "group-0-option-1").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//ul[1]/li[1]/div[1]/div[1]//div[@aria-label='select item']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//ul[1]/li[2]/div[1]/div[1]//div[@aria-label='select item']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//ul[1]/li[3]/div[1]/div[1]//div[@aria-label='select item']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Search for an item']]//ul[1]/li[4]/div[1]/div[1]//div[@aria-label='select item']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Done']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Done editing list']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='optionIcon' and @aria-label='edit list']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='deleteButton']").click()
        # following locator will locate two elements and will lead to timeout for being clickable, so need to refine it
        # self.driver.find_element(By.XPATH, "//span[text()='Delete list']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'id-') and @role='dialog' and .//h1[text()='Delete this list and all its items?']]//span[text()='Delete list']").click()
        # just in case. Wait for the delete action to finish
        time.sleep(2)

        # self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[5]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[5]/div[1]/div[2]/div[1]/div[2]/ul[1]/div[2]/li[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[2]/div[2]/div[2]/div[1]/div[1]/div[6]/div[2]/button[1]/span[1]/div[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//input[@value='on' and @type='checkbox']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='id-2822']/div[2]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/div[4]/li[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[2]/div[2]/div[2]/div[1]/div[1]/div[6]/div[2]/button[1]/span[1]/div[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//input[@value='on' and @type='checkbox']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='id-2924']/div[2]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'View More')]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[2]/ul[1]/li[14]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[2]/div[2]/div[2]/div[1]/div[1]/div[6]/div[2]/button[1]/span[1]/div[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//input[@value='on' and @type='checkbox']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='id-3109']/div[2]/div[1]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/ul[1]/li[8]/ul[1]/li[8]/a[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='store-wrapper']/div[1]/div[1]/div[2]/div[2]/ul[1]/li[23]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[2]/div[2]/div[2]/div[1]/div[1]/div[6]/div[2]/button[1]/span[1]/div[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//input[@value='on' and @type='checkbox']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='id-3274']/div[2]/div[1]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='item_details']/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='store-menu-wrapper']/div[1]/ul[1]/li[4]/a[1]/span[2]").click()
