import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestBabycenter:
    
    def test_babycenter_6c3bb227(self):
        # self.driver.get("https://www.babycenter.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Registry Builder')]").click()
        take_quiz_button = self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[1]/div[3]/div[1]/div[1]/main[1]/div[2]/div[1]/button[1]")
        scroll_to_element(self.driver, take_quiz_button)
        time.sleep(2)
        take_quiz_button_native = take_quiz_button.get_native_element()
        take_quiz_button_native.click()
        # self.driver.execute_script("arguments[0].click()", take_quiz_button.get_native_element())

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
    