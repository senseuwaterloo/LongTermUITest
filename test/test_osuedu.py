import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from browser_helper import switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestOsuEdu:
    
    # def test_osuedu_b32fcef3(self):
    #     # self.driver.get("https://osu.edu")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Current Students')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Student Health Services')]").click()
    #     self.driver.find_element(By.ID, "ctl00_Navigation1_RptrNavTier1_ctl03_HypNav").click()
    #     self.driver.find_element(By.ID, "ctl00_Navigation1_RptrNavTier1_ctl03_RptrNavTier2_ctl01_HypNav").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Visit the SHI website for benefit details')]").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentBody_homepagewidget_RptrWidget_ctl01_ctl00_RptrService_ctl01_HypService").click()
    #
    # def test_osuedu_d5df5b52(self):
    #     # self.driver.get("https://osu.edu")
    #     self.driver.find_element(By.XPATH, "//div[@id='nav-menu']/ul[1]/li[3]/button[1]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'For Students')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'New Researchers')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Human and Animal Research Subjects')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='block-wcm-theme-content']/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/details[2]/summary[1]").click()
    #
    # def test_osuedu_e3abe9e7(self):
    #     # self.driver.get("https://osu.edu")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Future Students')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Financial Aid')]").click()
    
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
    
    # def test_osuedu_213178c7(self):
    #     # self.driver.get("https://osu.edu")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Academics')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Libraries')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hours')]").click()
    #
    # def test_osuedu_38405ff5(self):
    #     # self.driver.get("https://osu.edu")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Current Students')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'University Housing')]").click()
    #     self.driver.find_element(By.ID, "ctl00_RptrNavTier1_ctl02_HypNav").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Gallery')]").click()
    #
    # def test_osuedu_3f934fbd(self):
    #     # self.driver.get("https://osu.edu")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Future Students')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    #     self.driver.find_element(By.ID, "accordion-d5ej1l69aq-1-tab").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'applicant center')]").click()
    #
    # def test_osuedu_563152da(self):
    #     # self.driver.get("https://osu.edu")
    #     self.driver.find_element(By.XPATH, "//div[@id='nav-menu']/ul[1]/li[2]/button[1]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Calendar')]").click()
    #
    # def test_osuedu_59b2ccbe(self):
    #     # self.driver.get("https://osu.edu")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Future Students')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Degrees and Programs')]").click()
    #     self.driver.find_element(By.ID, "ProgramsRepeater_DegreesRepeater_25_programURL_0").click()
    #     self.driver.find_element(By.ID, "tabCosts").click()
    #
    # def test_osuedu_9ff58139(self):
    #     # self.driver.get("https://osu.edu")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Research')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'For Entrepreneurs')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Venture Development')]").click()
    