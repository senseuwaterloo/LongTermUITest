import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestMayoclinicOrg:
    
    # def test_mayoclinicorg_847788e5(self):
    #     # self.driver.get("https://www.mayoclinic.org/")
    #     self.driver.find_element(By.ID, "et_globalNavigationButton_3CF3C3A8").click()
    #     self.driver.find_element(By.ID, "et_globalNavigation_6A0B2DB9").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Neuroscience')]").click()
    #     self.driver.find_element(By.ID, "parentLink-{137CB0CC-B73B-4C0D-9E0C-AE348467C79B}").click()
    #
    # def test_mayoclinicorg_9967fe53(self):
    #     # self.driver.get("https://www.mayoclinic.org/")
    #     self.driver.find_element(By.XPATH, "//button[@id='et_globalNavigationButton_AD5A3E3B']/span[1]").click()
    #     self.driver.find_element(By.ID, "et_globalNavigation_AD5A3E3B").click()
    #     self.driver.find_element(By.ID, "location").clear()
    #     self.driver.find_element(By.ID, "location").select("Florida")
    #     self.driver.find_element(By.ID, "type").clear()
    #     self.driver.find_element(By.ID, "type").select("Internship")
    #     self.driver.find_element(By.XPATH, "//form[@id='program-search-form']/div[2]/button[1]").click()
    #
    # def test_mayoclinicorg_a124c6e6(self):
    #     # self.driver.get("https://www.mayoclinic.org/")
    #     self.driver.find_element(By.XPATH, "//button[@id='et_globalNavigationButton_E098AB76']/span[1]").click()
    #     self.driver.find_element(By.ID, "et_globalNavigation_BF86A6C6").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Check on one or more symptoms to find possible causes.')]").click()
    #     self.driver.find_element(By.ID, "main_0_maincontent_1_SympTomRepeater_AdultSymptom_2").click()
    #     self.driver.find_element(By.ID, "main_0_maincontent_1_QualifierRepeater_FactorRepeater_0_CheckBoxQualifier_3").click()
    #     self.driver.find_element(By.ID, "main_0_maincontent_1_QualifierRepeater_FactorRepeater_1_CheckboxText_0").click()
    #     self.driver.find_element(By.ID, "main_0_maincontent_1_QualifierRepeater_FactorRepeater2_2_CheckBoxQualifier_3").click()
    #     self.driver.find_element(By.ID, "main_0_maincontent_1_QualifierRepeater_FactorRepeater_4_CheckboxText_0").click()
    #     self.driver.find_element(By.ID, "FindCause").click()
    #
    # def test_mayoclinicorg_a1b343fd(self):
    #     # self.driver.get("https://www.mayoclinic.org/")
    #     self.driver.find_element(By.ID, "et_globalNavigationButton_AD5A3E3B").click()
    #     self.driver.find_element(By.ID, "et_globalNavigation_F27762FF").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'M.D. Program')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tuition and Aid')]").click()
    #
    # def test_mayoclinicorg_b278b6ca(self):
    #     # self.driver.get("https://www.mayoclinic.org/")
    #     self.driver.find_element(By.ID, "searchTerm").clear()
    #     self.driver.find_element(By.ID, "searchTerm").send_keys("female infertility")
    #     self.driver.find_element(By.XPATH, "//div[@id='ui-id-2']/b[1]").click()
    #     self.driver.find_element(By.ID, "searchTerm").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='b7b1c41a35e845c7afa0570b78c9ea93']/div[1]/ol[1]/li[2]/h3[1]/a[1]").click()
    
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
    
    # def test_mayoclinicorg_ce8dfc6b(self):
    #     # self.driver.get("https://www.mayoclinic.org/")
    #     self.driver.find_element(By.ID, "searchTerm").clear()
    #     self.driver.find_element(By.ID, "searchTerm").send_keys("fever")
    #     self.driver.find_element(By.ID, "searchTerm").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='b7b1c41a35e845c7afa0570b78c9ea93']/div[1]/ol[1]/li[1]/h3[1]/a[1]").click()
    #
    # def test_mayoclinicorg_e4f179c3(self):
    #     # self.driver.get("https://www.mayoclinic.org/")
    #     self.driver.find_element(By.XPATH, "//button[@id='et_globalNavigationButton_3CF3C3A8']/span[1]").click()
    #     self.driver.find_element(By.ID, "et_globalNavigation_44C1CC47").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Airway Biology: Christina M. Pabelick')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Faculty and Staff')]").click()
    #
    # def test_mayoclinicorg_2354e344(self):
    #     # self.driver.get("https://www.mayoclinic.org/")
    #     self.driver.find_element(By.XPATH, "//button[@id='et_globalNavigationButton_0B9BEADC']/span[1]").click()
    #     self.driver.find_element(By.ID, "et_globalNavigation_D8E2EEA7").click()
    #     self.driver.find_element(By.ID, "SearchLocation").clear()
    #     self.driver.find_element(By.ID, "SearchLocation").select("Rochester, MN")
    #     self.driver.find_element(By.ID, "azureSearchTerm").clear()
    #     self.driver.find_element(By.ID, "azureSearchTerm").send_keys("back pain")
    #     self.driver.find_element(By.XPATH, "//div[@id='ui-id-3']/b[1]").click()
    #     self.driver.find_element(By.ID, "searchBtn").click()
    