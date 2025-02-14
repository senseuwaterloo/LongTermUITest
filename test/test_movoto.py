import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestMovoto:
    def test_movoto_d6fe3275(self):
        # self.driver.get("https://movoto.com")
        # uiteststudy@gmail.com:Pass4Movoto!

        # add login step to avoid popups
        self.driver.find_element(By.XPATH, "//a[@role='button' and text()='Sign In']").click()
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("Pass4Movoto!")
        self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Continue with Email']").click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH, "//a[@class='dialog-close' and @comp='mvtHotleadForm']") is not None:
            self.driver.find_element(By.XPATH, "//a[@class='dialog-close' and @comp='mvtHotleadForm']").click()

        # self.driver.find_element(By.XPATH, "//button[@title='Buy']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Buy']").click()
        time.sleep(2)

        # self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").clear()
        # self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys("huntsville")
        # need to wait for a few seconds for the page to be fully loaded then click on the search area otherwise the dropdown content will not be properly displayed and will close after
        # the page is fully loaded
        # time.sleep(3)
        # now will click on buy then click on search therefore the wait is not needed
        # self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").clear()
        # search_input = self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").get_native_element()
        # self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys(Keys.CONTROL, 'a')
        # self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys(Keys.DELETE)
        # TODO Somehow when input with Selenium webdriver, the dropdown list below the search input is different from that when manually test and therefore the rest test actions will not run
        # TODO as expected.
        # TODO also tried to send "RETURN" key in the input area and click on the search icon to search the location name directly but the search input is not responding to these actions and
        # TODO no error will be thrown either. The only way to make the search input responding or give the correct dropdown is to MANUALLY input the text then perform the actions.
        # self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").clear()
        self.driver.find_element(By.CSS_SELECTOR, ".mvt-searchbox__input > input").clear()
        self.driver.find_element(By.CSS_SELECTOR, ".mvt-searchbox__input > input").send_keys("Huntsville, AL")

        time.sleep(2)
        # self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys(" ")
        # self.driver.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keydown', {'key': ' '}));", search_input)
        # self.driver.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keypress', {'key': ' '}));", search_input)
        # self.driver.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keyup', {'key': ' '}));", search_input)
        # self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys(Keys.BACKSPACE)
        # self.driver.execute_script("arguments[0].value = '';", search_input)
        # self.driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", search_input)
        # self.driver.execute_script("arguments[0].value = 'Huntsville, AL'; arguments[0].dispatchEvent(new Event('input'));", search_input)
        # self.driver.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keydown', {'key': 'Enter'}));", search_input)
        # self.driver.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keyup', {'key': 'Enter'}));", search_input)

        # self.driver.find_element(By.XPATH, "//div[@id='textboxGeo']/div[2]/div[1]/a[1]/div[1]/b[1]").click()
        # self.driver.find_element(By.XPATH, "//div[./b[text()='huntsville'] and ./div[text()='AL']]").click()
        # will directly click on the search icon instead of waiting for the dropdown since the desired list item will not show when running the test code...
        # self.driver.find_element(By.XPATH, "//button[@role='button' and @aria-label='Search']/i[@title='Search']").click()
        # somehow the search doesn't seem to be clicked, use Enter key instead.

        time.sleep(2)
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.XPATH, "//button[@role='button' and @aria-label='Search']/i[@title='Search']").get_native_element())

        # self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='City, ZIP, School, Address, Neighborhood']").send_keys(Keys.RETURN)
        # need to wait for the properties in AL loaded then click on filter
        time.sleep(3)

        # self.driver.find_element(By.XPATH, "//a[@id='btnFilter']/span[1]").click()
        self.driver.find_element(By.ID, "btnFilter").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'$150K - $200K')]").click()
        # logic changed, need to input the price range now
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[1]/input").click()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[1]/input").clear()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[1]/input").send_keys("150000")
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[2]/input").click()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[2]/input").clear()
        self.driver.find_element(By.XPATH, "//div[@id='price']/div/div[1]/div[2]/input").send_keys("300000")

        # self.driver.find_element(By.XPATH, "//div[@id='propertyType']/div[1]/button[4]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyType']/div/label[5]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[1]/div[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='container']/div[5]/div[3]/button[2]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@comp='searchSort']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low')]").click()
        self.driver.find_element(By.XPATH, "//a[@role='button' and ./span[text()='Price Low']]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@comp='searchGrid']/div[1]/div[1]/div[2]/div[1]").click()
        switch_to_new_tab(self.driver)

        self.driver.find_element(By.XPATH, "//section[@id='openHousePanel']/div[1]/ul[1]/li[1]/a[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='container']/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/a[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@class='dialog-body']//div[@class='mvt-shifter-list' and @data-role='scroller']/div[3]/button[@class='btn-canlendar' and ./span[3]]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'9:00 am')]").click()
        # somehow the time elements are not displayed on the page after a while
        # self.driver.find_element(By.XPATH, "//button[text()='9:00 am']").click()

        # skip the submit button to avoid sending spam data
        # self.driver.find_element(By.XPATH, "//div[@id='container']/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/button[1]").click()
