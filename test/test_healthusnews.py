import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestHealthUsnews:
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
    