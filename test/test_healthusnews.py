import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestHealthUsnews:
    
    # def test_healthusnews_fa4b164c(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Doctors')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Dentists')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pediatric Dentists')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[9]/a[1]/span[1]/span[1]").click()
    #
    # def test_healthusnews_72b8fc77(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Diets & Nutrition')]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='sailthru-overlay-container']/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Noom')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Recipes')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Expert Reviews')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Do's & Don'ts\")]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Health & Nutrition')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Overview')]").click()
    #
    # def test_healthusnews_8060e378(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Health & Wellness')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Best Meal Delivery')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Compare Best Meal Kit Services')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ad-in-text-target']/react-trigger[2]/div[1]/div[3]/button[1]/div[1]").click()
    #
    # def test_healthusnews_a8318271(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/nav[1]/div[3]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Senior Living »')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Nursing Home')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='location' and @value='' and @type='text' and @placeholder='Location']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='location' and @value='' and @type='text' and @placeholder='Location']").send_keys("96817")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-home-location-input--item-0']/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[4]/div[1]/div[1]/div[1]/span[3]/label[1]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[1]/div[1]/a[1]").click()
    #
    # def test_healthusnews_04dc6e43(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Senior Living')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Nursing Home')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[4]/div[1]/div[1]/div[1]/span[3]/label[1]/span[1]/svg[1]").click()
    #
    # def test_healthusnews_0cfdd432(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hospitals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Hospital')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='city' and @value='' and @type='text' and @placeholder='']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='city' and @value='' and @type='text' and @placeholder='']").send_keys("Phoenix")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-hospital-location-input--item-0']/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/span[3]/label[1]/span[1]").click()
    #
    # def test_healthusnews_62c3a75c(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Medicare')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Plan')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/fieldset[1]/span[2]/label[1]/span[1]").click()
    #
    # def test_healthusnews_66c46e56(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Doctors')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cardiologists')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]").click()
    #
    # def test_healthusnews_ac9b301e(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Diets & Nutrition')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'All Diets')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/span[3]/label[1]/span[1]/svg[1]").click()
    #
    # def test_healthusnews_bafbd61b(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/nav[1]/div[3]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Doctors »')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Doctors by Location')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Omaha')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Thoracic Surgeons')]").click()
    #     self.driver.find_element(By.ID, "zm_survey-close").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[4]/div[2]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/h2[1]").click()
    #
    # def test_healthusnews_c48248f9(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hospitals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hospital Rankings')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See Full Rankings List')]").click()
    #
    # def test_healthusnews_cf8e4253(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//main[@id='app']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/a[2]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'WeightWatchers')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Recipes')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Fried egg with asparagus-potato hash (5 Points)')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='reset']").click()
    #
    # def test_healthusnews_d7f9e72e(self):
    #     # self.driver.get("https://health.usnews.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Medical Review')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Medical Review Board')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pharmacy')]").click()
    
    def test_healthusnews_de3a4315(self):
        # self.driver.get("https://health.usnews.com")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Doctors')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Doctors' and @data-tracking-id='top_nav']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Cardiology')]").click()
        # need to scroll down a little more to avoid click being blocked by popup ad window
        geriatric_medicine_link = self.driver.find_element(By.XPATH, "//a[text()='Geriatric Medicine']")
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element is not clickable at point (504, 997)
        scroll_to_element(self.driver, geriatric_medicine_link)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cardiology')]").click()

        # self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[4]/div[2]/div[2]/div[1]/form[1]/div[2]/fieldset[1]/div[1]/div[1]/div[1]/span[1]/label[1]/input[1]").clear()
        # self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[4]/div[2]/div[2]/div[1]/form[1]/div[2]/fieldset[1]/div[1]/div[1]/div[1]/span[1]/label[1]/input[1]").send_keys("HOUSTON, TX")
        self.driver.find_element(By.XPATH, "//input[@name='location' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='location' and @type='text']").send_keys("Houston, TX")

        # self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-location-input--item-0']/div[1]/span[1]").click()
        # click coincide by popup of ad window. ad popup when about to click
        # time.sleep(3)
        self.driver.find_element(By.ID, "react-autowhatever-1--item-0").click()

        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//button[@data-tracking-id='search_button']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[4]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[4]/button[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//span[text()='More Filters']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[4]/div[2]/div[2]/div[1]/form[1]/div[2]/fieldset[1]/div[1]/span[1]/label[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[4]/div[2]/div[2]/div[1]/form[1]/div[2]/fieldset[4]/div[1]/span[1]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//main[@id='app']/article[1]/div[1]/div[4]/div[2]/div[2]/div[1]/form[1]/div[2]/fieldset[4]/div[1]/span[1]/label[1]/select[1]").select("Female")
        doctor_gender_dropdown = self.driver.find_element(By.XPATH, "//fieldset[legend[text()='Physician Gender']]//select")
        doctor_gender_select = Select(doctor_gender_dropdown)
        doctor_gender_select.select_by_value('female')

        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @data-tracking-id='doctors_internal']").click()
    