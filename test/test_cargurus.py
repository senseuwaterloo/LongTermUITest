import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestCargurus:
    def test_cargurus_e832e1f9(self):
        self.driver.get("https://www.cargurus.com/")
        self.driver.find_element(By.XPATH, "//div[@id='heroSearch']/label[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='smcVinPlateField' and @type='text' and @placeholder='(EX.) C4R 6URU']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='smcVinPlateField' and @type='text' and @placeholder='(EX.) C4R 6URU']").send_keys("YAW639")
        dropdown_element = self.driver.find_element(By.XPATH, "//div[@id='heroSearch-tab-content-1']/section/form/section/fieldset[2]/div/label[2]/div/select")
        select = Select(dropdown_element)
        select.select_by_value('LA')
        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Get your offer')]").click()
        self.driver.find_element(By.ID, "postalCode").clear()
        self.driver.find_element(By.ID, "postalCode").send_keys("70726")
        self.driver.find_element(By.XPATH, "//section[@id='location']/div[1]/div[1]/form[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.ID, "mileage").click()
        self.driver.find_element(By.ID, "mileage").send_keys("222900")
        self.driver.find_element(By.XPATH, "//section[@id='car-details']/div[1]/div[1]/form[1]/button[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='car-features']/div[1]/div[1]/form[1]/fieldset[1]/label[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='car-features']/div[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='car-features']/div[1]/div[1]/form[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='condition']/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/label[3]").click()

        condition_dropdown = self.driver.find_element(By.ID, "CONDITION")
        condition_select = Select(condition_dropdown)
        condition_select.select_by_value('Good')

        tire_dropdown = self.driver.find_element(By.ID, "TIRE_CONDITION")
        tire_select = Select(tire_dropdown)
        tire_select.select_by_value('Good To Go')

        self.driver.find_element(By.XPATH, "//section[@id='condition']/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//section[@id='condition']/div[1]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//section[@id='condition']/div[1]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//section[@id='condition']/div[1]/div[1]/form[1]/div[7]/div[1]/div[1]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//section[@id='condition']/div[1]/div[1]/form[1]/div[8]/div[1]/div[1]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//section[@id='condition']/div[1]/div[1]/form[1]/div[9]/div[1]/div[1]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//section[@id='condition']/div[1]/div[1]/form[1]/div[10]/div[1]/div[1]/div[1]/label[2]").click()
        self.driver.find_element(By.XPATH, "//section[@id='condition']/div[1]/div[1]/form[1]/div[11]/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='condition']/div[1]/div[1]/form[1]/div[12]/button[1]/div[1]").click()
    