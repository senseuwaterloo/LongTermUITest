import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestCourseraOrg:
    
    # def test_courseraorg_5991ba25(self):
    #     # self.driver.get("https://coursera.org")
    #     self.driver.find_element(By.ID, "student-link").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Resources')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//img[@alt='Career Readiness: Secrets to delivering better graduate career outcomes']").click()
    #     self.driver.find_element(By.ID, "question_first_name").clear()
    #     self.driver.find_element(By.ID, "question_first_name").send_keys("Johnn")
    #     self.driver.find_element(By.ID, "question_last_name").clear()
    #     self.driver.find_element(By.ID, "question_last_name").send_keys("Doe")
    #     self.driver.find_element(By.ID, "question_email").clear()
    #     self.driver.find_element(By.ID, "question_email").send_keys("johndoe@gmail.com")
    #     self.driver.find_element(By.ID, "question_confirm_email").clear()
    #     self.driver.find_element(By.ID, "question_confirm_email").send_keys("johndoe@gmail.com")
    #     self.driver.find_element(By.ID, "question_job_title").clear()
    #     self.driver.find_element(By.ID, "question_job_title").send_keys("Accounting")
    #     self.driver.find_element(By.ID, "custom_question_0").clear()
    #     self.driver.find_element(By.ID, "custom_question_0").send_keys("UAI")
    #     self.driver.find_element(By.ID, "btnSubmit").click()
    #
    # def test_courseraorg_733d1e8f(self):
    #     # self.driver.get("https://coursera.org")
    #     self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").send_keys("Psychology")
    #     self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/button[2]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='coursera-onboarding-profile-form']/div[1]/div[3]/div[1]/div[2]/div[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-84").click()
    #
    # def test_courseraorg_d27a6164(self):
    #     # self.driver.get("https://coursera.org")
    #     self.driver.find_element(By.XPATH, "//div[@id='MegamenuWrapperDiv']/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='learning_paths~menu-item']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Data Analyst')]").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-55").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-71").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-163").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-97").click()
    
    def test_courseraorg_228fc81a(self):
        # self.driver.get("https://coursera.org")
        # overall changed the locators
        self.driver.find_element(By.XPATH, "//span[contains(.,'For') and contains(.,' Universities')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Resources')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]").click()
        # add a click button action
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

        # self.driver.find_element(By.ID, "Primary_Discipline__c").clear()
        # self.driver.find_element(By.ID, "Primary_Discipline__c").select("Accounting")
        main_industry_dropdown = self.driver.find_element(By.ID, "rentalField9")
        main_industry_select = Select(main_industry_dropdown)
        main_industry_select.select_by_value('Business')

        organization_size_dropdown = self.driver.find_element(By.ID, "Employee_Range__c")
        organization_size_select = Select(organization_size_dropdown)
        organization_size_select.select_by_value('15001+')

        job_function_dropdown = self.driver.find_element(By.ID, "C4C_Job_Title__c")
        job_function_select = Select(job_function_dropdown)
        job_function_select.select_by_value('Finance')

        # self.driver.find_element(By.ID, "Country").clear()
        # self.driver.find_element(By.ID, "Country").select("United States")
        # self.driver.find_element(By.ID, "State").clear()
        # self.driver.find_element(By.ID, "State").select("MI")
        country_dropdown = self.driver.find_element(By.ID, "Country")
        country_select = Select(country_dropdown)
        country_select.select_by_value('United States')

        state_dropdown = self.driver.find_element(By.ID, "State")
        state_select = Select(state_dropdown)
        state_select.select_by_value('MI')

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    # def test_courseraorg_2776878c(self):
    #     # self.driver.get("https://coursera.org")
    #     self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").send_keys("deeeplearning")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-1-item-0']/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-44").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/a[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]/div[1]/span[1]").click()
    #
    # def test_courseraorg_2bc717a1(self):
    #     # self.driver.get("https://coursera.org")
    #     self.driver.find_element(By.XPATH, "//div[@id='MegamenuWrapperDiv']/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='free~menu-item']/span[1]").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-20-label-text").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-30").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-42").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-52").click()
    #
    # def test_courseraorg_0a060d81(self):
    #     # self.driver.get("https://coursera.org")
    #     self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='textbox' and @value='' and @type='text' and @placeholder='What do you want to learn?']").send_keys("university of london")
    #     self.driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='nav-title~1']/span[1]").click()
    #
    # def test_courseraorg_0cc44161(self):
    #     # self.driver.get("https://coursera.org")
    #     self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='certificates~menu-item']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/div[3]/div[1]/section[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h1[1]").click()
    #
    # def test_courseraorg_efa508bf(self):
    #     # self.driver.get("https://coursera.org")
    #     self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='free~menu-item']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rendered-content']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "cds-react-aria-95").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cds-react-aria-85']/div[3]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
    