import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("driver_session")
class TestCourseraOrg:
    def test_courseraorg_228fc81a(self):
        self.driver.get("https://www.coursera.org/")

        self.driver.find_element(By.XPATH, "//span[contains(.,'For') and contains(.,' Universities')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Resources')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]").click()

        self.driver.find_element(By.XPATH, "//a[@trackingname='EntWebsiteHow_job_skills_report_button_0']").click()
        self.driver.find_element(By.ID, "FirstName").clear()
        self.driver.find_element(By.ID, "FirstName").send_keys("John")
        self.driver.find_element(By.ID, "LastName").clear()
        self.driver.find_element(By.ID, "LastName").send_keys("Doe")
        self.driver.find_element(By.ID, "Title").clear()
        self.driver.find_element(By.ID, "Title").send_keys("Accounting")
        self.driver.find_element(By.ID, "Email").clear()
        self.driver.find_element(By.ID, "Email").send_keys("Johndoe@gmail.com")

        self.driver.find_element(By.ID, "db_company_name__c").clear()
        self.driver.find_element(By.ID, "db_company_name__c").send_keys("University of Michigan")

        self.driver.find_element(By.ID, "Phone").clear()
        self.driver.find_element(By.ID, "Phone").send_keys("234567890")

        main_industry_dropdown = self.driver.find_element(By.ID, "rentalField9")
        main_industry_select = Select(main_industry_dropdown)
        main_industry_select.select_by_value('Business')

        organization_size_dropdown = self.driver.find_element(By.ID, "Employee_Range__c")
        organization_size_select = Select(organization_size_dropdown)
        organization_size_select.select_by_value('15001+')

        job_function_dropdown = self.driver.find_element(By.ID, "C4C_Job_Title__c")
        job_function_select = Select(job_function_dropdown)
        job_function_select.select_by_value('Finance')

        country_dropdown = self.driver.find_element(By.ID, "Country")
        country_select = Select(country_dropdown)
        country_select.select_by_value('United States')

        state_dropdown = self.driver.find_element(By.ID, "State")
        state_select = Select(state_dropdown)
        state_select.select_by_value('MI')

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    