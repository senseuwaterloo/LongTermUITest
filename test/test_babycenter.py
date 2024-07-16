import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestBabycenter:
    
    def test_babycenter_6c3bb227(self):
        # self.driver.get("https://www.babycenter.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Registry Builder')]").click()
        take_quiz_button = self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[1]/button[1]/span[1]")
        scroll_to_element(self.driver, take_quiz_button)
        self.driver.execute_script("arguments[0].click()", take_quiz_button.get_native_element())

        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_200']/div[2]/div[1]/button[1]/div[1]/div[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_200']/div[3]/div[1]/button[1]/span[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_intermediary_continue']/button[1]/span[1]").get_native_element())

        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_203']/div[2]/div[1]/button[1]/div[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_203']/div[3]/div[1]/button[1]/span[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_201']/ul[1]/li[2]/button[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_201']/div[2]/div[1]/button[1]/span[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_202']/ul[1]/li[2]/button[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_202']/div[2]/div[1]/button[1]/span[1]").get_native_element())

        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_205']/ul[1]/li[5]/button[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_205']/ul[1]/li[6]/button[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_205']/div[2]/div[1]/button[1]/span[1]").get_native_element())

        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_intermediary_continue']/button[1]/span[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_204']/ul[1]/li[4]/button[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_204']/ul[1]/li[5]/button[1]").get_native_element())
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='rm_quiz_question_204']/div[2]/div[1]/button[1]/span[1]").get_native_element())

    # def test_babycenter_4a27bf45(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Names')]").click()
    #     self.driver.find_element(By.ID, "gender1").click()
    #     self.driver.find_element(By.ID, "includeExclude2").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='sort' and @title='sort']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='sort' and @title='sort']").select("A-Z")
    #
    # def test_babycenter_50e258e8(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Community')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='tab-4']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Search group name or keyword']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Search group name or keyword']").send_keys("getting pregnant")
    #     self.driver.find_element(By.XPATH, "//input[@value='getting pregnant' and @type='search' and @placeholder='Search group name or keyword']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[3]/div[1]/div[1]/main[1]/div[3]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='daysSinceCreationFilter' and @value='1' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Apply')]").click()
    #
    # def test_babycenter_616843f8(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Getting Pregnant')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/a[1]/figure[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[8]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[5]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'OK')]").click()
    #     self.driver.find_element(By.ID, "duration").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-How long was your last cycle']/div[3]/ul[1]/li[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/button[2]/span[1]").click()
    #
    # def test_babycenter_631b0391(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Groups')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Search group name or keyword']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Search group name or keyword']").send_keys("diabetes")
    #     self.driver.find_element(By.XPATH, "//input[@value='diabetes' and @type='search' and @placeholder='Search group name or keyword']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[3]/div[1]/div[1]/main[1]/div[3]/div[3]/div[1]/a[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/button[2]/span[1]").click()
    #
    # def test_babycenter_68ce1cf5(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Names')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Search a name']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Search a name']").send_keys("Carl")
    #     self.driver.find_element(By.XPATH, "//input[@value='Carl' and @type='search' and @placeholder='Search a name']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Similar names to Carl')]").click()
    #
    # def test_babycenter_6ba15234(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='How can we help?']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='How can we help?']").send_keys("pregnancy fever")
    #     self.driver.find_element(By.XPATH, "//input[@value='pregnancy fever' and @type='search' and @placeholder='How can we help?']").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='tab-1']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[3]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "postFilter").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='daysSinceCreationFilter' and @value='30' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Apply')]").click()
    #
    # def test_babycenter_2e620aae(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Names')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='gender' and @value='Female' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[3]/div[3]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[1]/button[2]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@role='menuitem']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[4]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Emma name popularity')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-']/div[3]/ul[1]/li[9]").click()
    #
    # def test_babycenter_0d465553(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pregnancy')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[2]/div[5]/a[1]/figure[1]/figcaption[1]").click()
    #     self.driver.find_element(By.ID, "age").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-Select age']/div[3]/ul[1]/li[5]").click()
    #     self.driver.find_element(By.ID, "month").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-Select month']/div[3]/ul[1]/li[5]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #
    # def test_babycenter_873c898e(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Names')]").click()
    #     self.driver.find_element(By.ID, "gender1").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Meaning, origin, theme...')]").click()
    #     self.driver.find_element(By.ID, "origin").clear()
    #     self.driver.find_element(By.ID, "origin").select("Hebrew")
    #     self.driver.find_element(By.ID, "theme").clear()
    #     self.driver.find_element(By.ID, "theme").select("Biblical")
    #     self.driver.find_element(By.ID, "startsWith").clear()
    #     self.driver.find_element(By.ID, "startsWith").send_keys("J")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    # def test_babycenter_8f09efa2(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Names')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='popularity' and @value='hideTopNames' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[3]/div[3]/div[2]/div[1]/button[1]/span[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "startsWith").clear()
    #     self.driver.find_element(By.ID, "startsWith").send_keys("a")
    #     self.driver.find_element(By.ID, "endsWith").clear()
    #     self.driver.find_element(By.ID, "endsWith").send_keys("u")
    #     self.driver.find_element(By.ID, "origin").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-origin']/div[3]/ul[1]/li[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[3]/div[3]/div[2]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[4]/a[1]/div[1]").click()
    #
    # def test_babycenter_909d710b(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Toddler')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/section[1]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[4]/div[2]/ul[1]/li[1]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'What to feed a 2-year-old')]").click()
    #
    # def test_babycenter_cfeb9323(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Products')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/section[1]/div[1]/div[5]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/section[1]/div[1]/div[5]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/section[1]/div[1]/div[4]/div[3]/a[1]/div[1]/div[1]/div[1]/span[1]/img[1]").click()
    #
    # def test_babycenter_d27b1dc3(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Groups')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Search group name or keyword']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Search group name or keyword']").send_keys("Debate Team")
    #     self.driver.find_element(By.XPATH, "//input[@value='Debate Team' and @type='search' and @placeholder='Search group name or keyword']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[3]/div[1]/div[1]/main[1]/div[3]/div[3]/div[1]/a[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[3]/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Community guidelines')]").click()
    #
    # def test_babycenter_d863de59(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Products')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Infant Car Seats')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/section[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/span[1]").click()
    #
    # def test_babycenter_de3a35e1(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Health')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/section[1]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'2023 CDC childhood immunization schedule')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[4]/div[2]/ul[1]/li[2]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'immunization schedule')]").click()
    #     self.driver.find_element(By.XPATH, "//strong[contains(.,'Table 1. By age')]").click()
    #
    # def test_babycenter_ee142be5(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Child')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[2]/div[2]/a[1]/figure[1]/figcaption[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='gender-radio-group' and @value='male' and @type='radio']").click()
    #     self.driver.find_element(By.ID, "age").click()
    #     self.driver.find_element(By.XPATH, "//div[@id=\"menu-Child's age\"]/div[3]/ul[1]/li[13]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='number' and @placeholder='0']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='number' and @placeholder='0']").send_keys("4")
    #     self.driver.find_element(By.ID, "childWeight").clear()
    #     self.driver.find_element(By.ID, "childWeight").send_keys("50")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("5")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("6")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #
    # def test_babycenter_a53a33a2(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Toddler')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[3]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/section[1]/div[1]/div[8]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/section[1]/div[1]/div[8]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/section[1]/div[1]/div[4]/div[4]/a[1]/div[1]/div[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Good sources of potassium')]").click()
    #
    # def test_babycenter_b5d4bddd(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Products')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/section[1]/div[1]/div[2]/div[3]/a[1]/div[1]/div[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/main[1]/div[1]/div[4]/div[2]/ul[1]/li[4]/a[1]/img[1]").click()
    #
    # def test_babycenter_c1dc7085(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Names')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='gender' and @value='Male' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='popularity' and @value='onlyTopNames' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[3]/div[3]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
    #
    # def test_babycenter_f101ef7d(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Courses')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[2]/div[1]/article[1]/ul[1]/li[3]/a[1]/div[3]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[9]/div[1]/article[1]/ol[1]/li[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[9]/div[1]/article[1]/ol[1]/li[2]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[9]/div[1]/article[1]/ol[1]/li[3]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[9]/div[1]/article[1]/ol[1]/li[4]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[9]/div[1]/article[1]/ol[1]/li[5]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/section[9]/div[1]/article[1]/ol[1]/li[6]/div[1]/button[1]").click()
    #
    # def test_babycenter_fcdad63b(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pregnancy')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/a[1]/figure[1]/figcaption[1]").click()
    #     self.driver.find_element(By.ID, "calculationMethod").click()
    #     self.driver.find_element(By.XPATH, "//li[@role='option']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//p[contains(.,'23')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'OK')]").click()
    #     self.driver.find_element(By.ID, "duration").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-Cycle length']/div[3]/ul[1]/li[12]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
    #
    # def test_babycenter_74af19eb(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pregnancy')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[2]/div[3]/a[1]/figure[1]/figcaption[1]").click()
    #     self.driver.find_element(By.ID, "pregnancyWeek").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-pregnancyWeek']/div[3]/ul[1]/li[3]").click()
    #     self.driver.find_element(By.ID, "left-prePregnancyWeight").clear()
    #     self.driver.find_element(By.ID, "left-prePregnancyWeight").send_keys("169")
    #     self.driver.find_element(By.ID, "left-weightNow").clear()
    #     self.driver.find_element(By.ID, "left-weightNow").send_keys("175")
    #     self.driver.find_element(By.ID, "left-height").clear()
    #     self.driver.find_element(By.ID, "left-height").send_keys("5")
    #     self.driver.find_element(By.ID, "right-height").clear()
    #     self.driver.find_element(By.ID, "right-height").send_keys("6")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]/span[1]").click()
    #
    # def test_babycenter_81593c29(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='How can we help?']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='How can we help?']").send_keys("baby bathing")
    #     self.driver.find_element(By.XPATH, "//input[@value='baby bathing' and @type='search' and @placeholder='How can we help?']").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='tab-1']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[3]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "commentFilter").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='daysSinceCreationFilter' and @value='365' and @type='radio']").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[3]/div[3]/div[1]/a[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='comment-2612313474']/div[4]/div[2]/button[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[3]/div[1]/button[1]").click()
    #
    # def test_babycenter_a212f2cc(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Products')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sleep Must Haves')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/section[1]/div[1]/div[2]/div[4]/a[1]/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/main[1]/div[1]/div[4]/div[2]/ul[1]/li[4]/a[1]/span[1]/strong[1]/strong[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='articleFeedbackModule']/div[1]/div[2]/div[1]/img[1]").click()
    #
    # def test_babycenter_a50c0d43(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Child')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[2]/div[2]/a[1]/figure[1]/figcaption[1]").click()
    #     self.driver.find_element(By.ID, "age").click()
    #     self.driver.find_element(By.XPATH, "//div[@id=\"menu-Child's age\"]/div[3]/ul[1]/li[11]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='number' and @placeholder='0']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='number' and @placeholder='0']").send_keys("4")
    #     self.driver.find_element(By.ID, "childWeight").clear()
    #     self.driver.find_element(By.ID, "childWeight").send_keys("55")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("5")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[2]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("2")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("5")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[2]/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("8")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #
    # def test_babycenter_1af30743(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Getting Pregnant')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/a[1]/figure[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//p[contains(.,'8')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'OK')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
    #
    # def test_babycenter_2b79e756(self):
    #     # self.driver.get("https://www.babycenter.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Getting Pregnant')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/a[1]/figure[1]/figcaption[1]").click()
    #     self.driver.find_element(By.ID, "duration").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-How long was your last cycle']/div[3]/ul[1]/li[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//p[contains(.,'3')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'OK')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[5]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
    