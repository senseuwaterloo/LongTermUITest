import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestJusticeGov:
    
    # def test_justicegov_028b03fb(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[4]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-4']/div[1]/div[1]/div[3]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='edit_field_component_target_id_chosen']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='edit_field_component_target_id_chosen']/div[1]/ul[1]/li[8]").click()
    #
    # def test_justicegov_5419702c(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[3]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-3']/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "facetapi-link--43--checkbox").click()
    #     self.driver.find_element(By.ID, "facetapi-link--3--checkbox").click()
    #
    # def test_justicegov_c97d3d88(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[6]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-6']/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Why Justice')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Disability Hiring')]").click()
    #
    # def test_justicegov_ce61a8d1(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn More')]").click()
    #
    # def test_justicegov_d71df831(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'U.S. Capitol Violence Cases and Other Wanted Fugitives')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'U.S. Marshals Fugitives')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'U.S. Marshals 15 Most Wanted')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #
    # def test_justicegov_e22ebc9c(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'FOIA')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'FOIA Resources')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Court Decisions')]").click()
    #     self.driver.find_element(By.ID, "edit-topic").clear()
    #     self.driver.find_element(By.ID, "edit-topic").select("Attorney Fees")
    #     self.driver.find_element(By.ID, "edit-date-value-month").clear()
    #     self.driver.find_element(By.ID, "edit-date-value-month").select("Jan")
    #     self.driver.find_element(By.ID, "edit-date-value-year").clear()
    #     self.driver.find_element(By.ID, "edit-date-value-year").select("2023")
    #     self.driver.find_element(By.ID, "edit-submit-court-decisions").click()
    
    def test_justicegov_ec10879f(self):
        # self.driver.get("https://www.justice.gov/")
        self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-4']/div[1]/div[1]/div[3]/div[1]/a[1]/span[1]").click()

        # self.driver.find_element(By.ID, "edit_field_component_target_id_chosen").click()
        # self.driver.find_element(By.XPATH, "//div[@id='edit_field_component_target_id_chosen']/div[1]/ul[1]/li[8]").click()
        agency_dropdown = self.driver.find_element(By.NAME, "field_component_target_id")
        agency_select = Select(agency_dropdown)
        agency_select.select_by_visible_text('Civil Division')

        self.driver.find_element(By.ID, "edit-submit-resources").click()

        # self.driver.find_element(By.ID, "edit-title").clear()
        # self.driver.find_element(By.ID, "edit-title").send_keys("radiation exposure")
        self.driver.find_element(By.NAME, "title").clear()
        self.driver.find_element(By.NAME, "title").send_keys("radiation exposure")

        self.driver.find_element(By.ID, "edit-submit-resources").click()

        # self.driver.find_element(By.ID, "edit-reset").click()
        self.driver.find_element(By.XPATH, "//input[@value='Reset Filters']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='edit_field_component_target_id_chosen']/a[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='edit_field_component_target_id_chosen']/div[1]/ul[1]/li[8]").click()
        agency_dropdown = self.driver.find_element(By.NAME, "field_component_target_id")
        agency_select = Select(agency_dropdown)
        agency_select.select_by_visible_text('Civil Division')
        self.driver.find_element(By.ID, "edit-submit-resources").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Form Title')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'2')]").click()
    
    # def test_justicegov_f09c5fe6(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[6]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-6']/div[1]/div[1]/div[5]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search Jobs')]").click()
    #
    # def test_justicegov_f484bada(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[4]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-4']/div[1]/div[1]/div[3]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='edit_field_component_target_id__2_chosen']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='edit_field_component_target_id__2_chosen']/div[1]/ul[1]/li[7]").click()
    #     self.driver.find_element(By.ID, "edit-items-per-page--2").clear()
    #     self.driver.find_element(By.ID, "edit-items-per-page--2").select("50")
    #     self.driver.find_element(By.ID, "edit-submit-resources").click()
    #
    # def test_justicegov_fd5c0878(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.ID, "search-field-en-small-desktop").clear()
    #     self.driver.find_element(By.ID, "search-field-en-small-desktop").send_keys("Career")
    #     self.driver.find_element(By.XPATH, "//form[@id='search_form']/button[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='result-1']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='result-1']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Attorney')]").click()
    #
    # def test_justicegov_615dada2(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[4]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-4']/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-1']/div[1]/div[1]/div[3]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View by Category')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Office of Tribal Justice (OTJ)')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tracy Toulou')]").click()
    #
    # def test_justicegov_7a8bf304(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[4]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-4']/div[1]/div[1]/div[4]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Office of the Attorney General')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'General Departmental Policies Regarding Charging, Pleas, and Sentencing')]").click()
    #
    # def test_justicegov_947081d2(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[6]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-6']/div[1]/div[1]/div[5]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "edit-position").clear()
    #     self.driver.find_element(By.ID, "edit-position").select("Law Student Volunteer, Summer")
    #     self.driver.find_element(By.ID, "edit-field-va-location-administrative-area").clear()
    #     self.driver.find_element(By.ID, "edit-field-va-location-administrative-area").select("New York")
    #     self.driver.find_element(By.ID, "edit-submit-vacancy-announcements").click()
    #
    # def test_justicegov_9879926c(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-1']/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Learn more about Attorneys General throughout history')]").click()
    #     self.driver.find_element(By.ID, "edit-sort-order").clear()
    #     self.driver.find_element(By.ID, "edit-sort-order").select("Ascending")
    #
    # def test_justicegov_bf76e110(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View Organizational Chart')]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[4]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-4']/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-1']/div[1]/div[1]/div[3]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View by Category')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Oversight')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Special Counsel's Office - Jack Smith\")]").click()
    #
    # def test_justicegov_c5c0b8f7(self):
    #     # self.driver.get("https://www.justice.gov/")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/label[1]/nav[1]/div[1]/ul[1]/li[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='basic-nav-section-_-1']/div[1]/div[1]/div[4]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'FY 2021')]").click()
    