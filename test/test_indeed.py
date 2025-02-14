import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element, scroll_down


@pytest.mark.usefixtures("setup_class")
class TestIndeed:
    def test_indeed_4ce51ed5(self):
        # self.driver.get("https://www.indeed.com/worldwide")
        # comment the following step since it is redundant
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Countries')]").click()

        self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[1]/ul[1]/li[58]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Browse Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'England')]").click()
        # no link for Essex, need to change to Chelmsford
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs in Essex')]").click()
        # scroll to element and scroll down further to avoid being blocked by cookie banner
        chelmsford_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs in Chelmsford')]")
        scroll_to_element(self.driver, chelmsford_link)
        scroll_down(self.driver, 500)
        chelmsford_link.click()

        # self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']/div[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']/div[2]").click()
        # code passed but the dropdown won't open so try to use JS click
        # self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']/div[1]").get_native_element())
        # JS click still not working, try to click on the parent button
        # self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']").click()
        # click on button is also not working so try to use perform method
        # perform method is also not working, try add some sleep time and finally it is working with some sleep time
        time.sleep(3)
        sort_date_button = self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']/div[1]").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element(sort_date_button)
        action.click().perform()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Last 24 hours')]").click()

        # self.driver.find_element(By.XPATH, "//button[@id='filter-srctype']/div[2]/svg[1]").click()
        # dropdown is not expanding as above so try to add some sleep time to see whether combing typical click and wait time is ok and it seems that it is working so it must sleep
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='filter-srctype']/div[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Employer (724)')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Employer']").click()

        # save as above, add some sleep time otherwise it won't display or maybe some other activity closed the window
        time.sleep(3)
        self.driver.find_element(By.ID, "filter-taxo2").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Healthcare (145)')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Healthcare']").click()
        self.driver.find_element(By.XPATH, "//button[@form='filter-taxo2-menu']").click()

        # self.driver.find_element(By.XPATH, "//button[@id='filter-jobtype']/div[2]/svg[1]").click()
        # save as above, add some sleep time otherwise it won't display or maybe some other activity closed the window
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='filter-jobtype']/div[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Part-time (45)')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Part-time']").click()

        # save as above, add some sleep time otherwise it won't display or maybe some other activity closed the window
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='filter-salary-estimate']/div[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'£20,000+ (42)')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='£20,000+']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'date')]").click()
        self.driver.find_element(By.ID, "dateLabel").click()

        # self.driver.find_element(By.XPATH, "//button[@id='jobActionButton-a722b6770c53079f']/svg[1]/path[1]").click()
        # save as above, add some sleep time otherwise it won't display or maybe some other activity closed the window
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[@id='mosaic-provider-jobcards']/ul/li[1]/div/div/div/div/div/table/tbody/tr/td[2]/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='mosaic-provider-jobcards']/ul[1]/li[1]/div[1]/div[2]/div[1]/button[3]").click()
        self.driver.find_element(By.XPATH, "//div[@data-valuetext='Report job']").click()

        # self.driver.find_element(By.ID, "label-radio-option-1").click()
        self.driver.find_element(By.XPATH, "//span[text()='It seems like a fake job']").click()

        # self.driver.find_element(By.ID, "additional-information-textarea").clear()
        # self.driver.find_element(By.ID, "additional-information-textarea").send_keys("Seems fake")
        self.driver.find_element(By.ID, "ifl-TextAreaFormField-8").clear()
        self.driver.find_element(By.ID, "ifl-TextAreaFormField-8").send_keys("Seems fake")

        # do not really click and submit data to avoid spam
        # self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    