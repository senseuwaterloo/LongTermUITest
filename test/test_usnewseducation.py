import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("driver_session")
class TestUsnewsEducation:
    def test_usnewseducation_7d047bb7(self):
        self.driver.get("https://www.usnews.com/education")

        self.driver.find_element(By.XPATH, "//button[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Sign In to My Account']").click()

        time.sleep(2)
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("Pass4USNews!")
        self.driver.find_element(By.XPATH, "//button[text()='Continue']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text()='Scholarships and Finances']").click()

        state_residence_dropdown = self.driver.find_element(By.NAME, "state-of-residence")
        state_residence_select = Select(state_residence_dropdown)
        state_residence_select.select_by_value("AZ")

        state_study_dropdown = self.driver.find_element(By.NAME, "state-of-study")
        state_study_select = Select(state_study_dropdown)
        state_study_select.select_by_value("AZ")

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='ethnicity' and @placeholder='Type to Select']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='ethnicity' and @placeholder='Type to Select']").send_keys("african american")

        self.driver.find_element(By.ID, "react-autowhatever-1--item-0").click()

        gender_dropdown = self.driver.find_element(By.NAME, "gender")
        gender_select = Select(gender_dropdown)
        gender_select.select_by_value("Female")

        need_based_checkbox = self.driver.find_element(By.XPATH, "//span[text()='Need-Based Aid']")

        self.driver.execute_script("arguments[0].click()", need_based_checkbox.get_native_element())

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Undergraduate']").click()
