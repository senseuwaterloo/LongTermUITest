import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab_and_close_old, scroll_down


@pytest.mark.usefixtures("setup_class")
class TestOhioGov:
    
    # def test_ohiogov_84efcb18(self):
    #     # self.driver.get("https://ohio.gov/")
    #     self.driver.find_element(By.XPATH, "//nav[@id='main-nav-container']/ul[1]/li[4]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='js-odx-dynamic-cards-catalog_0']/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/a[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[5]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'hunting seasons')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sectionHeader-0']/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sectionHeader-1']/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sectionHeader-2']/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sectionHeader-3']/h3[1]").click()
    #
    # def test_ohiogov_90e320cd(self):
    #     # self.driver.get("https://ohio.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Coronavirus.Ohio.gov')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Families and')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='covid-top-resources']/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/img[1]").click()
    #
    # def test_ohiogov_a677ac08(self):
    #     # self.driver.get("https://ohio.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='js-odx-dynamic-cards-catalog_3']/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/a[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Athletic Trainer')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dnn_ctr771_HtmlModule_lblContent']/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Continuing Education')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'AT Jurisprudence Exam (Ethics)')]").click()
    #
    # def test_ohiogov_c733437c(self):
    #     # self.driver.get("https://ohio.gov/")
    #     self.driver.find_element(By.XPATH, "//nav[@id='main-nav-container']/ul[1]/li[3]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/section[1]/div[2]/div[1]/div[2]/div[2]/a[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[2]/aside[1]/section[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Paper Application')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'FILL‑IN')]").click()
    #
    # def test_ohiogov_f1c6950b(self):
    #     # self.driver.get("https://ohio.gov/")
    #     self.driver.find_element(By.XPATH, "//nav[@id='main-nav-container']/ul[1]/li[3]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/section[1]/div[2]/div[1]/div[2]/div[3]/a[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[2]/aside[1]/section[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/section[3]/div[1]/div[2]/div[1]/div[2]/article[1]/a[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[2]/aside[1]/section[1]/div[1]/div[1]/span[2]/a[1]/span[1]/i[1]").click()
    #
    # def test_ohiogov_f59b9930(self):
    #     # self.driver.get("https://ohio.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Our state')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/section[2]/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/a[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[2]/aside[1]/section[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@role='button' and @value=\"Let's Get Started\" and @type='button']").click()
    #     self.driver.find_element(By.XPATH, "//input[@role='button' and @value='Continue' and @type='submit']").click()
    #
    # def test_ohiogov_f6d55dac(self):
    #     # self.driver.get("https://ohio.gov/")
    #     self.driver.find_element(By.XPATH, "//nav[@id='main-nav-container']/ul[1]/li[3]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/section[1]/div[2]/div[1]/div[2]/div[3]/a[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[2]/aside[1]/section[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/section[1]/div[1]/div[2]/a[2]/div[2]/p[1]").click()
    #
    # def test_ohiogov_67857faa(self):
    #     # self.driver.get("https://ohio.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tools for')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='js-odx-dynamic-cards-catalog_0']/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/section[1]/a[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[2]/aside[1]/section[1]/div[1]/a[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sectionHeader-0']/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'business information kit')]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='js-odx-content__body']/div[1]/div[2]/article[1]/section[1]/h2[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'hiring your first -- or next -- employee')]").click()

    def test_ohiogov_77269ea5(self):
        # self.driver.get("https://ohio.gov/")
        self.driver.find_element(By.XPATH, "//nav[@id='main-nav-container']/ul[1]/li[3]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/section[1]/div[2]/div[1]/div[2]/div[2]/a[1]/div[2]/h3[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[2]/aside[1]/section[1]/div[1]/a[1]/span[1]").click()

        switch_to_new_tab_and_close_old(self.driver)

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Child Care Program Resources')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Search for Early Care and Education Programs')]").click()
        # page logic changed
        # scroll_down(self.driver, 500)
        # The section that contains the button below is dynamic, sometimes other button will be displayed, so will just remove this action and directly click search for care.
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply for Child Care Assistance')]").click()
        # so first click on the span then click on the link
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Search for Child Care')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Search for Child Care']").click()
        switch_to_new_tab_and_close_old(self.driver)

        # actions performed by the agent is wrong
        # self.driver.find_element(By.ID, "ContentPlaceHolder1_ddlCounty").clear()
        # self.driver.find_element(By.ID, "ContentPlaceHolder1_ddlCounty").select("ALL")
        country_dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_ddlCounty")
        country_select = Select(country_dropdown)
        country_select.select_by_visible_text("Clinton")

        # add extra step about Step Up To Quality Rating that is missed by the agent
        step_up_dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_ddlRating")
        step_up_select = Select(step_up_dropdown)
        step_up_select.select_by_visible_text("ANY")

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtCity").clear()
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtCity").send_keys("Midland")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_chkSaturday").click()
        self.driver.find_element(By.ID, "ContentPlaceHolder1_chkSixNoon").click()
        self.driver.find_element(By.ID, "ContentPlaceHolder1_chkTransportation").click()
        self.driver.find_element(By.XPATH, "//div[@id='formActions']/a[1]/span[1]").click()

        # The actions generated by the agent does not align with the task requirement. Will ignore below actions
        # self.driver.find_element(By.ID, "ContentPlaceHolder1_lnkStartOver").click()
        # self.driver.find_element(By.ID, "ContentPlaceHolder1_txtCity").clear()
        # self.driver.find_element(By.ID, "ContentPlaceHolder1_txtCity").send_keys("Midland")
        # self.driver.find_element(By.ID, "ContentPlaceHolder1_chkMonday").click()
        # self.driver.find_element(By.ID, "ContentPlaceHolder1_chkAfterSchoolCare").click()
        # self.driver.find_element(By.ID, "ContentPlaceHolder1_chkTransportation").click()
        # self.driver.find_element(By.XPATH, "//div[@id='formActions']/a[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='programSearchResults']/a[1]/span[1]/span[1]").click()
        # self.driver.find_element(By.ID, "ContentPlaceHolder1_chkTransportation").click()
        # self.driver.find_element(By.XPATH, "//div[@id='formActions']/a[1]/span[1]").click()

    # access to the questionair is forbidden so use the second longest test case
    # def test_ohiogov_7f19d60c(self):
    #     # self.driver.get("https://ohio.gov/")
    #     self.driver.find_element(By.XPATH, "//nav[@id='main-nav-container']/ul[1]/li[3]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='js-odx-dynamic-cards-catalog_0']/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='js-odx-dynamic-cards-catalog_0']/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/a[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[9]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'simple questionnaire')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/section[1]/div[1]/div[2]/a[3]/div[2]/h3[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "form-check").click()
    #     self.driver.find_element(By.ID, "type-myself").click()
    #     self.driver.find_element(By.ID, "ec_next").click()
    #     self.driver.find_element(By.ID, "familycount").clear()
    #     self.driver.find_element(By.ID, "familycount").select("1")
    #     self.driver.find_element(By.ID, "ec_next").click()
    #     self.driver.find_element(By.ID, "income").clear()
    #     self.driver.find_element(By.ID, "income").send_keys("1000")
    #     self.driver.find_element(By.ID, "zip").clear()
    #     self.driver.find_element(By.ID, "zip").send_keys("32350")
    #     self.driver.find_element(By.ID, "ec_next2").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='pregnant' and @value='No' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='child' and @value='No' and @type='radio']").click()
    #     self.driver.find_element(By.ID, "ltc-yes").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='medicare' and @value='No' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='foster' and @value='No' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='medicare' and @value='No' and @type='radio']").click()
    #     self.driver.find_element(By.ID, "srs-yes").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='military' and @value='No' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='subButton' and @value='Find Out Now' and @type='submit']").click()
    
    # def test_ohiogov_185e4e96(self):
    #     # self.driver.get("https://ohio.gov/")
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/section[1]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[2]/aside[1]/section[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='odx-main-content']/article[1]/div[1]/div[2]/section[2]/div[1]/div[1]/div[2]/div[1]/div[3]/h4[1]/a[1]/strong[1]").click()
    