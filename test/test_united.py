import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_without_space, switch_to_new_tab_and_close_old


@pytest.mark.usefixtures("setup_class")
class TestUnited:
    def test_united_fdf322bd(self):
        # self.driver.get("https://www.united.com/en/us")
        # self.driver.find_element(By.XPATH, "//a[@id='headerNav0']/span[1]").click()
        self.driver.find_element(By.XPATH, "//button/span[text()='Book']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='headerNav0-panel']/div[1]/div[2]/ul[1]/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Vacation packages']").click()
        switch_to_new_tab_and_close_old(self.driver)

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/label[2]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//label[@for='Hotel + Flight + Car']").click()

        self.driver.find_element(By.ID, "Where from?").clear()
        self.driver.find_element(By.ID, "Where from?").send_keys("new york")

        # self.driver.find_element(By.XPATH, "//div[@id='Where from?-dropdown-item-0']/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Where from?-dropdown']//div[@id='undefined-item-0']/div[1]/div[1]").click()

        self.driver.find_element(By.ID, "Where to?").clear()
        self.driver.find_element(By.ID, "Where to?").send_keys("las vegas")

        # self.driver.find_element(By.XPATH, "//div[@id='Where to?-dropdown-item-0']/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Where to?-dropdown']//div[@id='undefined-item-0']/div[1]/div[1]").click()

        # self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Departing - Returning']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[17]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[25]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/label[2]/div[1]/svg[3]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Departing - Returning']").click()
        start_date_str, end_date_str = calculate_dates_without_space(14, 21)
        self.driver.find_element(By.XPATH, f"//div[@data-autobot-element-id='DATEPICKER_DAY_{start_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//div[@data-autobot-element-id='DATEPICKER_DAY_{end_date_str}']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Start Saving']").click()
        switch_to_new_tab_and_close_old(self.driver)

        # self.driver.find_element(By.XPATH, "//div[@id='main-wrapper']/div[1]/div[1]/div[3]/div[2]/div[1]/div[7]/div[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/svg[3]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='main-wrapper']/div[1]/div[1]/div[3]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/button[4]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/reach-portal[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[9]/div[1]/div[1]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//svg[@role='img' and @title='Increase Rooms']").click()
        # self.driver.find_element(By.XPATH, "//svg[@role='img' and @title='Increase Adults']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='popover-description-traveler-selection-popover']/div[3]/div[1]/div[2]/div[2]/button[2]/div[1]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/div[5]").click()
        # self.driver.find_element(By.XPATH, "//button[contains(.,'Update Search')]").click()
        # NEED to wait for the content to be fully loaded then click and select rooms and adults otherwise the changes made will be reset after the content is fully loaded.
        # The attachments shows the screenshot of the page that the selections are RESET after page is fully loaded even though it was set to 2 rooms and 4 adults before.
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text()='1 Room, 2 Adults']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Select traveler information']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Increase Rooms']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Increase Adults']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Increase Adults']").click()
        # Use javascript click to force the click since the Done button is not showed in the screen area and the page is not scrollable. See the attached screenshot.
        # self.driver.find_element(By.XPATH, "//div[text()='Done']").click()
        time.sleep(20)
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[text()='Done']").get_native_element())
        self.driver.find_element(By.XPATH, "//div[text()='Update Search']").click()
        switch_to_new_tab_and_close_old(self.driver)

        # self.driver.find_element(By.XPATH, "//div[@id='main-wrapper']/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Choose Another Hotel')]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='main-wrapper']/div[2]/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='name-and-price']/div[2]/div[2]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='rates-table-50570']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='listingContent']/div[1]/div[3]/section[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[2]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[text()='4 +']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Show 12 more']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@for, 'Amenities-CASINO-checkbox-')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='DROP_DOWN_FIELD_BOX']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Lowest Price']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'undefined listings')]/div[contains(@class, 'Listings__StyledWrapper')]/div[1]//button[@data-testid='price-choosen-button']").click()
        time.sleep(2)
