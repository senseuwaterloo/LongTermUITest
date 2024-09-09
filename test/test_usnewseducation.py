import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_down


@pytest.mark.usefixtures("setup_class")
class TestUsnewsEducation:
    
    # def test_usnewseducation_bdb05ce1(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Grad Schools')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for Graduate Schools')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='program']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='program']").select("Nursing")
    #     self.driver.find_element(By.XPATH, "//input[@name='location' and @value='' and @type='text' and @placeholder='City, State or ZIP']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='location' and @value='' and @type='text' and @placeholder='City, State or ZIP']").send_keys("iowa")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-location-input--item-0']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[4]/div[2]/div[1]/div[3]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[4]/div[2]/div[1]/div[3]/select[1]").select("Enrollment (high to low)")
    #
    # def test_usnewseducation_f004058d(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Colleges')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'All Rankings')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Undergraduate Engineering Programs')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Mechanical')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='location' and @value='' and @type='text' and @placeholder='City, State or ZIP']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='location' and @value='' and @type='text' and @placeholder='City, State or ZIP']").send_keys("Illinois")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-location-input--item-0']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[4]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]").click()
    #
    # def test_usnewseducation_f59b4328(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[2]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
    #
    # def test_usnewseducation_d712a8d1(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/nav[1]/div[3]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "gsc-i-id1").clear()
    #     self.driver.find_element(By.ID, "gsc-i-id1").send_keys("Harvard")
    #     self.driver.find_element(By.XPATH, "//b[contains(.,'university')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='___gcse_1']/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/ol[1]/li[1]/a[1]").click()
    #     self.driver.find_element(By.ID, "admissions-tracking-id").click()
    #
    # def test_usnewseducation_deac960a(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Colleges')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'College Major Quiz')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #
    # def test_usnewseducation_e8ba3458(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Grad Schools')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Engineering')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Engineering Programs, Specialties and Additional Rankings')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Chemical Engineering')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[4]/div[2]/div[1]/div[3]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[4]/div[2]/div[1]/div[3]/select[1]").select("Rank (high to low)")
    #
    # def test_usnewseducation_eecdca22(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rankings')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'High School Rankings')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See Full Rankings List')]").click()
    #
    # def test_usnewseducation_57898eda(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'SkillBuilder')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Health')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[4]/div[2]/div[1]/div[3]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[4]/div[2]/div[1]/div[3]/select[1]").select("Cost (low to high)")
    
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
    
    # def test_usnewseducation_88a83138(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rankings')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Global University Rankings')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='region']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='region']").select("Asia")
    #     self.driver.find_element(By.XPATH, "//select[@name='subject']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='subject']").select("Arts and Humanities")
    #
    # def test_usnewseducation_92b1915f(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/nav[1]/div[3]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "gsc-i-id1").clear()
    #     self.driver.find_element(By.ID, "gsc-i-id1").send_keys("Princeton")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'princeton')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='___gcse_1']/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/ol[1]/li[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[2]/div[3]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #
    # def test_usnewseducation_93228887(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Grad Schools')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for Graduate Schools')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='program']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='program']").select("Business")
    #     self.driver.find_element(By.XPATH, "//select[@name='specialty']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='specialty']").select("Finance")
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[1]/div[1]/div[3]/div[1]/span[1]/label[1]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[2]/div[1]/div[3]/div[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[3]/div[1]/div[3]/div[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sticky-promo-container']/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sticky-promo-container']/div[1]/button[1]/div[2]").click()
    #
    # def test_usnewseducation_06a5e80a(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/nav[1]/div[3]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "gsc-i-id1").clear()
    #     self.driver.find_element(By.ID, "gsc-i-id1").send_keys("UCLA")
    #     self.driver.find_element(By.XPATH, "//div[@id='___gcse_1']/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/ol[1]/li[1]/a[1]").click()
    #
    # def test_usnewseducation_0f55d705(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Grad Schools')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for Graduate Schools')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='program']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='program']").select("Law")
    #     self.driver.find_element(By.XPATH, "//select[@name='specialty']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='specialty']").select("Part-time Law")
    #     self.driver.find_element(By.XPATH, "//input[@name='lsat' and @value='' and @type='text' and @placeholder='ex. 150']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='lsat' and @value='' and @type='text' and @placeholder='ex. 150']").send_keys("140")
    #     self.driver.find_element(By.XPATH, "//input[@name='location' and @value='' and @type='text' and @placeholder='City, State or ZIP']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='location' and @value='' and @type='text' and @placeholder='City, State or ZIP']").send_keys("california")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-location-input--item-0']/div[1]").click()
    #
    # def test_usnewseducation_1e9a0413(self):
    #     # self.driver.get("https://www.usnews.com/education")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Global Universities')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Universities in Asia')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Type to Select']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Type to Select']").send_keys("China")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-0']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='subject']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='subject']").select("Microbiology")
    