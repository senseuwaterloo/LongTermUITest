import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_down


@pytest.mark.usefixtures("driver_session")
class TestSixflags:
    def test_sixflags_521d9006(self):
        self.driver.get("https://sixflags.com")

        self.driver.find_element(By.XPATH, "//section[@id='parkselector']//div[@class='sf-dropdown']//button[./div[text()='Browse the Parks Below']]").click()

        self.driver.find_element(By.XPATH, "//section[@id='parkselector']//a[@class='single-park-desktop' and @data-title='Six Flags Magic Mountain' and @data-state='Los Angeles, CA']").click()

        self.driver.find_element(By.XPATH, "//section[@id='parkselector']//div[@class='sf-dropdown']//button[text()='Go!']").click()

        self.driver.find_element(By.XPATH, "//nav[not(@aria-hidden='true')]//a[text()='Groups' and ./span[@aria-label='Menu Toggle' and @role='application'] and ./span[@class='sub-arrow']]").click()
        scroll_down(self.driver, 600)
        self.driver.find_element(By.XPATH, "//button[@class='btn_show_hide card_icon' and ./parent::div/div[1]/h3[text()='Groups of 15 to 99']]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Buy Tickets')]").click()

        override_iframe = self.driver.find_element(By.ID, "override").get_native_element()
        self.driver.switch_to.frame(override_iframe)

        buy_now_button = self.driver.find_element(By.XPATH, "//button[./gap-button-label[text()='Buy Now']]").get_native_element()

        self.driver.execute_script("arguments[0].click()", buy_now_button)

        self.driver.find_element(By.XPATH, "//button[@title='Increase']").click()
        self.driver.find_element(By.XPATH, "//button[@title='Increase']").click()
        self.driver.find_element(By.XPATH, "//button[@title='Increase']").click()
        self.driver.find_element(By.XPATH, "//button[@title='Increase']").click()
        self.driver.find_element(By.XPATH, "//button[@title='Increase']").click()

        self.driver.find_element(By.ID, "next-btn").click()
        self.driver.find_element(By.ID, "groupName").clear()
        self.driver.find_element(By.ID, "groupName").send_keys("Crew")
        self.driver.find_element(By.ID, "firstName").clear()
        self.driver.find_element(By.ID, "firstName").send_keys("James")
        self.driver.find_element(By.ID, "lastName").clear()
        self.driver.find_element(By.ID, "lastName").send_keys("Johnson")
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys("james.john@gmail.com")

        self.driver.find_element(By.ID, "orgType").click()
        self.driver.find_element(By.XPATH, "//span[text()='Family Trip']").click()

        self.driver.find_element(By.ID, "orgName").clear()
        self.driver.find_element(By.ID, "orgName").send_keys("Johnson")

        self.driver.find_element(By.XPATH, "//button[@type='button' and @ng-click='nextView()']").click()
