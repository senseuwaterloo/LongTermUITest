import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from browser_helper import get_control_key


@pytest.mark.usefixtures("setup_class")
class TestYelp:
    def test_yelp_63e3020c(self):
        # self.driver.get("https://yelp.com")
        # TODO: Blocked by yelp, consider remove it from subjects...
        # self.driver.find_element(By.XPATH, "/html/body[1]/yelp-react-root[1]/div[1]/div[2]/div[2]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[2]/div[1]/a[1]/span[2]/span[1]").click()
        home_services_link = self.driver.find_element(By.XPATH, "//span[text()='Home Services']").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element(home_services_link).perform()

        self.driver.find_element(By.XPATH, "//span[contains(.,'Electricians')]").click()

        # self.driver.find_element(By.ID, "search_location").clear()
        self.driver.find_element(By.ID, "search_location").send_keys(get_control_key() + "a")
        self.driver.find_element(By.ID, "search_location").send_keys(Keys.DELETE)
        self.driver.find_element(By.ID, "search_location").send_keys("WESTMINSTER")

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Westminster')]").click()
        self.driver.find_element(By.XPATH, "//div[./span[text()='Westminster'] and ./span[text()=', CA']]").click()
        time.sleep(20)

        # self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[2]/a[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/menu[1]/button[2]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Recommended']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Highest Rated']").click()

        # self.driver.find_element(By.XPATH, "//p[contains(.,'Fast-responding')]").click()
        # self.driver.find_element(By.XPATH, "//p[contains(.,'Open Now')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Fast-responding']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Open Now']").click()

        # self.driver.find_element(By.XPATH, "//p[contains(.,'Request a Quote')]").click()
        self.driver.find_element(By.XPATH, "//li[./div/h2[contains(text(), 'All \"electricians\" results')]]/following-sibling::li[1]//span[text()='Request quote & availability']").click()

        # self.driver.find_element(By.XPATH, "//input[@role='radio' and @name='Job Type' and @value='job_electric_installation' and @type='radio' and @placeholder=' ']").click()
        splash_iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@class, 'iframe__') and contains(@class, 'splash-screen-iframe__')]").get_native_element()
        self.driver.switch_to.frame(splash_iframe)
        self.driver.find_element(By.XPATH, "//span[text()='Installation or replacement']").click()

        # self.driver.find_element(By.NAME, "Items").click()
        self.driver.find_element(By.XPATH, "//span[text()='Light Fixture']").click()

        # add extra steps required in new web app
        self.driver.find_element(By.XPATH, "//span[text()='Residential']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Skip']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Skip']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Skip']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Skip']").click()
        self.driver.find_element(By.XPATH, "//span[text()='As soon as possible']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()

        # logic changed
        # self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/ul[1]/li[5]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]").click()
