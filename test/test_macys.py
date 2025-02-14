import time

import pytest
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from browser_helper import scroll_to_element, switch_to_new_tab, switch_to_new_tab_and_close_old


@pytest.mark.usefixtures("setup_class")
class TestMacys:
    def test_macys_c3a97f15(self):
        # self.driver.get("https://www.macys.com/")
        # self.driver.find_element(By.XPATH, "//li[@id='flexid_324256']/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "fob-Trending").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Wear to Work')]").click()
        wear_to_work_link = self.driver.find_element(By.XPATH, "//div[text()='Wear-To-Work']")
        scroll_to_element(self.driver, wear_to_work_link)
        wear_to_work_link.click()

        # handle potential popup
        time.sleep(2)
        try:
            frame = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "kampyleInvite")))
            self.driver.switch_to.frame(frame.get_native_element())
            self.driver.find_element(By.ID, "kplDeclineButton").click()
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            error_message = f"handle popup in iframe error, check stack trace and screenshot for more details"
            self.driver.error_messages.append(error_message)
        finally:
            self.driver.switch_to.default_content()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop The Trend')]").click()
        # page logic changed, directly click on Tops link
        self.driver.find_element(By.XPATH, "//p[text()='Tops']").click()

        # self.driver.find_element(By.XPATH, "//li[@id='COLOR_NORMAL']/h2[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Black (16)']").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Brown (2)']").click()
        # filter the expected color
        self.driver.find_element(By.ID, "m-filter").click()
        self.driver.find_element(By.XPATH, "//li[@id='COLOR_NORMAL']/h2[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(@title, 'Black') and @class='item_icon ']").click()
        # self.driver.find_element(By.XPATH, "//span[contains(@title, 'Brown') and @class='item_icon ']").click()

        # self.driver.find_element(By.XPATH, "//h2[@title='Collapse Category']").click()
        self.driver.find_element(By.ID, "m-apply-facets").click()

        # self.driver.find_element(By.XPATH, "//li[@id='PRODUCT_DEPARTMENT']/div[1]/ul[1]/li[3]/a[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='region_1_child_2']/div[1]/div[1]/div[6]/ul[1]/li[1]/div[1]/div[1]").click()
        switch_to_new_tab(self.driver)

        # self.driver.find_element(By.XPATH, "//li[@id='SIZE_TYPE']/h2[1]/span[1]").click()
        # self.driver.find_element(By.ID, "sizeSelection").clear()
        # self.driver.find_element(By.ID, "sizeSelection").select("Women's Regular")
        # self.driver.find_element(By.XPATH, "//li[@id='WOMEN_REGULAR_SIZE_T']/div[1]/ul[1]/li[5]/a[1]/span[2]/div[1]").click()
        # self.driver.find_element(By.ID, "img_15453234").click()
        # self.driver.find_element(By.XPATH, "//div[@id='mainCont']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[2]/div[1]/picture[1]/source[1]/img[1]").click()
        # self.driver.find_element(By.ID, "bag-add-15453234").click()
        # self.driver.find_element(By.ID, "atbIntContinueShopping").click()
        # self.driver.find_element(By.XPATH, "//div[@id='mainCont']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[3]/div[1]/picture[1]/source[1]/img[1]").click()
        # self.driver.find_element(By.ID, "bag-add-15453234").click()
        # somehow need some sleep to avoid TimeoutException: Elements not found: xpath = //button[contains(@name, 'cta-sizes-')]//span[text()='S']. Seems like caused by layout shift
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(@name, 'cta-sizes-')]//span[text()='S']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Add To Bag']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Continue shopping']").click()
        switch_to_new_tab_and_close_old(self.driver)
        self.driver.find_element(By.ID, "m-filter").click()
        self.driver.find_element(By.XPATH, "//li[@id='COLOR_NORMAL']/h2[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(@title, 'Black') and @class='item_icon ']").click()
        # need some sleep time to avoid: selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//li[@id='COLOR_NORMAL']/h2[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(@title, 'Brown') and @class='item_icon ']").click()
        self.driver.find_element(By.ID, "m-apply-facets").click()
        # StaleElementReferenceException: Element became stale: xpath = //li[@id='region_1_child_2']/div[1]/div[1]/div[6]/ul[1]/li[1]/div[1]/div[1] - Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//li[@id='region_1_child_2']/div[1]/div[1]/div[6]/ul[1]/li[1]/div[1]/div[1]").click()
        switch_to_new_tab(self.driver)
        # already some sleep in the switch tab function, that's why we don't need sleep before this size selection action
        self.driver.find_element(By.XPATH, "//button[contains(@name, 'cta-sizes-')]//span[text()='XL']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Add To Bag']").click()
