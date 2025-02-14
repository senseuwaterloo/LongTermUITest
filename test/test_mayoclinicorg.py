import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestMayoclinicOrg:
    def test_mayoclinicorg_bf2c6dc7(self):
        # self.driver.get("https://www.mayoclinic.org/")
        # self.driver.find_element(By.ID, "et_globalNavigationButton_0B9BEADC").click()
        self.driver.find_element(By.XPATH, "//ul[@data-testid='cmp-tabs']//span[normalize-space(text())='Care at Mayo Clinic']").click()

        # self.driver.find_element(By.ID, "et_globalNavigation_16C51EF4").click()
        self.driver.find_element(By.XPATH, "//ul[@data-testid='cmp-tabs']//span[text()='Locations']").click()

        # self.driver.find_element(By.XPATH, "//a[@id='et-internalPromo-3F3F0FF3']/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@aria-label='Secondary']//span[@role='text' and text()='Find a doctor']").click()

        self.driver.find_element(By.ID, "azureSearchTerm").clear()
        self.driver.find_element(By.ID, "azureSearchTerm").send_keys("Cardiologist")

        # self.driver.find_element(By.XPATH, "//div[@id='ui-id-3']/b[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'ui-id-') and ./b[text()='Cardiologist']]").click()

        # self.driver.find_element(By.ID, "SearchLocation").clear()
        # self.driver.find_element(By.ID, "SearchLocation").select("Jacksonville, FL")
        location_dropdown = self.driver.find_element(By.ID, "SearchLocation")
        location_select = Select(location_dropdown)
        location_select.select_by_visible_text('Jacksonville, FL')

        self.driver.find_element(By.ID, "searchBtn").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Katia Marisa Bravo Jaimes, M.D.')]").click()
    