import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from browser_helper import switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestOsuEdu:
    def test_osuedu_efa85d1d(self):
        # self.driver.get("https://osu.edu")
        # self.driver.find_element(By.XPATH, "//div[@id='nav-menu']/ul[1]/li[2]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//li[@data-submenu='true']/a[contains(text(), ' Academics')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Calendar')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'See the full academic calendar')]").click()

        # self.driver.find_element(By.XPATH, "//font[contains(.,'Course & Class Information')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Student Hub']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search Schedule of Classes')]").click()
        # add switch tab action
        switch_to_new_tab(self.driver)

        # ignore redundant useless actions
        # self.driver.find_element(By.ID, "CLASS_SRCH_WRK2_INSTITUTION$31$").click()
        # self.driver.find_element(By.ID, "CLASS_SRCH_WRK2_STRM$35$").click()

        # add extra step to switch to iframe
        frame = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "ptifrmtgtframe")))
        self.driver.switch_to.frame(frame.get_native_element())

        # self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_CAMPUS$0").clear()
        # self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_CAMPUS$0").select("Columbus")
        campus_dropdown = self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_CAMPUS$0")
        campus_select = Select(campus_dropdown)
        campus_select.select_by_visible_text("Columbus")

        # self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_SUBJECT_SRCH$1").clear()
        # self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_SUBJECT_SRCH$1").select("Animal Sciences")
        subject_dropdown = self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_SUBJECT_SRCH$1")
        subject_select = Select(subject_dropdown)
        time.sleep(1)
        subject_select.select_by_visible_text("Animal Sciences")

        # self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_SSR_EXACT_MATCH1$2").clear()
        # self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_SSR_EXACT_MATCH1$2").select("is exactly")
        course_number_dropdown = self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_SSR_EXACT_MATCH1$2")
        course_number_select = Select(course_number_dropdown)
        time.sleep(1)
        course_number_select.select_by_visible_text("is exactly")

        # self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_ACAD_CAREER$3").clear()
        # self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_ACAD_CAREER$3").select("Medicine")
        course_career_dropdown = self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_ACAD_CAREER$3")
        course_career_select = Select(course_career_dropdown)
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(1)
        course_career_select.select_by_visible_text("Medicine")

        self.driver.find_element(By.ID, "SSR_CLSRCH_WRK_SSR_OPEN_ONLY$4").click()
        self.driver.find_element(By.ID, "CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH").click()
