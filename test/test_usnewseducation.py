import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestUsnewsEducation:
    def test_usnewseducation_7d047bb7(self):
        # self.driver.get("https://www.usnews.com/education")
        # uiteststudy@gmail.com:Pass4USNews!

        # add extra login steps
        self.driver.find_element(By.XPATH, "//button[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Sign In to My Account']").click()
        # need to wait a few seconds otherwise the email won't be filled out sometimes
        time.sleep(2)
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("Pass4USNews!")
        self.driver.find_element(By.XPATH, "//button[text()='Continue']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Scholarship Search')]").click()
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text()='Scholarships and Finances']").click()

        # self.driver.find_element(By.XPATH, "//select[@name='state-of-residence']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='state-of-residence']").select("Arizona")
        state_residence_dropdown = self.driver.find_element(By.NAME, "state-of-residence")
        state_residence_select = Select(state_residence_dropdown)
        state_residence_select.select_by_value("AZ")

        # self.driver.find_element(By.XPATH, "//select[@name='state-of-study']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='state-of-study']").select("Arizona")
        state_study_dropdown = self.driver.find_element(By.NAME, "state-of-study")
        state_study_select = Select(state_study_dropdown)
        state_study_select.select_by_value("AZ")

        # self.driver.find_element(By.XPATH, "//div[@name='ethnicity' and @placeholder='Type to Select']").clear()
        # self.driver.find_element(By.XPATH, "//div[@name='ethnicity' and @placeholder='Type to Select']").send_keys("african american")
        # need to wait a few second to avoid the dropdown be close by page loading process
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='ethnicity' and @placeholder='Type to Select']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='ethnicity' and @placeholder='Type to Select']").send_keys("african american")

        self.driver.find_element(By.ID, "react-autowhatever-1--item-0").click()

        # self.driver.find_element(By.XPATH, "//select[@name='gender']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='gender']").select("Female")
        gender_dropdown = self.driver.find_element(By.NAME, "gender")
        gender_select = Select(gender_dropdown)
        gender_select.select_by_value("Female")

        # self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[8]/div[1]/div[1]/span[6]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[10]/div[1]/div[1]/span[2]/label[1]").click()
        need_based_checkbox = self.driver.find_element(By.XPATH, "//span[text()='Need-Based Aid']")
        # use JS click to avoid advertisements
        self.driver.execute_script("arguments[0].click()", need_based_checkbox.get_native_element())

        # need to wait a few second for the layout to be stable otherwise other element will be clicked
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Undergraduate']").click()
