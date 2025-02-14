import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_down


@pytest.mark.usefixtures("setup_class")
class TestSixflags:
    def test_sixflags_521d9006(self):
        # self.driver.get("https://sixflags.com")

        # self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='parkselector']//div[@class='sf-dropdown']//button[./div[text()='Browse the Parks Below']]").click()

        # self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='parkselector']//a[@class='single-park-desktop' and @data-title='Six Flags Magic Mountain' and @data-state='Los Angeles, CA']").click()

        self.driver.find_element(By.XPATH, "//section[@id='parkselector']//div[@class='sf-dropdown']//button[text()='Go!']").click()

        # self.driver.find_element(By.ID, "sm-16807812394218174-1").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Group Tickets')]").click()
        # self.driver.find_element(By.XPATH, "//article[@id='post-113811']/div[1]/div[1]/div[1]/div[1]/section[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//nav[not(@aria-hidden='true')]//a[text()='Groups' and ./span[@aria-label='Menu Toggle' and @role='application'] and ./span[@class='sub-arrow']]").click()
        scroll_down(self.driver, 600)
        self.driver.find_element(By.XPATH, "//button[@class='btn_show_hide card_icon' and ./parent::div/div[1]/h3[text()='Groups of 15 to 99']]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Buy Tickets')]").click()

        # No need to select a time slot, just use the default time slot
        # self.driver.find_element(By.XPATH, "//button[@id='row3-cell30']/span[1]").click()

        # need add switch to frame action
        override_iframe = self.driver.find_element(By.ID, "override").get_native_element()
        self.driver.switch_to.frame(override_iframe)

        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//button[./gap-button-label[text()='Buy Now']]").click()
        # need to use Action class because click will be intercepted by its parent element
        buy_now_button = self.driver.find_element(By.XPATH, "//button[./gap-button-label[text()='Buy Now']]").get_native_element()
        # action = ActionChains(self.driver)
        # action.move_to_element(buy_now_button)
        # action.click().perform()
        # somehow Action class is not working: code passed but no click action triggered, so try to use JS click
        self.driver.execute_script("arguments[0].click()", buy_now_button)

        # self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/ng-form[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/ng-form[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/ng-form[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/ng-form[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/ng-form[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[2]/button[1]/span[1]").click()
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

        # self.driver.find_element(By.XPATH, "//select[@name='orgType' and @title='Organization Type']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='orgType' and @title='Organization Type']").select("Family Trip")
        self.driver.find_element(By.ID, "orgType").click()
        self.driver.find_element(By.XPATH, "//span[text()='Family Trip']").click()

        self.driver.find_element(By.ID, "orgName").clear()
        self.driver.find_element(By.ID, "orgName").send_keys("Johnson")

        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @ng-click='nextView()']").click()
