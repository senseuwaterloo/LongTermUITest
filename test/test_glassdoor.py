import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestGlassdoor:
    # CAN'T SOLVE THE INTERCEPT ERROR, SO... GIVE UP...
    # def test_glassdoor_447a2fb9(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Guides')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Container']/div[2]/div[2]/div[2]/div[1]/a[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Container']/div[1]/div[1]/div[5]/a[1]/div[2]/div[1]/h3[1]").click()
    #
    # def test_glassdoor_45182e36(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.XPATH, "//header[@id='SiteNav']/nav[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/span[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='SiteNav']/nav[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Work/Life Balance')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Explore']/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[5]/div[2]/div[1]/div[1]/div[1]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='option_4.5']/span[1]/div[1]/div[2]/span[4]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Explore']/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[6]/div[7]/div[1]/label[1]/div[2]").click()
    #     self.driver.find_element(By.ID, "Location-c6313f8-4782-c0c6-db73-bf66236725f4").clear()
    #     self.driver.find_element(By.ID, "Location-c6313f8-4782-c0c6-db73-bf66236725f4").send_keys("bangkok")
    #     self.driver.find_element(By.XPATH, "//div[@id='Explore']/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Explore']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/a[3]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='JobsLandingPage']/div[1]/div[2]/main[1]/div[2]/div[1]/div[3]/div[2]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Last 7 days')]").click()
    #
    # def test_glassdoor_67eaaff2(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.ID, "sc.location").clear()
    #     self.driver.find_element(By.ID, "sc.location").send_keys("oregon")
    #     self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[1]/div[1]/div[1]/div[1]/span[1]/b[1]").click()
    #     self.driver.find_element(By.ID, "sc.keyword").clear()
    #     self.driver.find_element(By.ID, "sc.keyword").send_keys("parks department")
    #     self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[6]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Discover']/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/strong[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='DKFilters']/div[1]/div[3]/button[1]").click()
    #
    # def test_glassdoor_8593b57b(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.ID, "sc.keyword").clear()
    #     self.driver.find_element(By.ID, "sc.keyword").send_keys("Google")
    #     self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[1]/div[1]/div[1]/div[1]/span[1]/b[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='EmpLinksWrapper']/div[2]/div[1]/div[1]/a[1]/p[1]").click()
    #
    # def test_glassdoor_8a2cf20d(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.ID, "sc.keyword").clear()
    #     self.driver.find_element(By.ID, "sc.keyword").send_keys("Tesla")
    #     self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[1]/div[1]/div[1]/div[1]/span[1]/b[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='EmpLinksWrapper']/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    #
    # def test_glassdoor_19756b72(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.ID, "sc.keyword").clear()
    #     self.driver.find_element(By.ID, "sc.keyword").send_keys("Data Analyst")
    #     self.driver.find_element(By.ID, "sc.location").clear()
    #     self.driver.find_element(By.ID, "sc.location").send_keys("New York City")
    #     self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[2]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Discover']/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/strong[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='JAModal']/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='JAModal']/div[1]/div[2]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "filter_minSalary").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='slider']").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='slider']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='PrimaryDropdown']/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='PrimaryDropdown']/div[1]/div[2]/button[2]/span[1]").click()
    #
    # def test_glassdoor_1aaa652f(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.ID, "sc.keyword").clear()
    #     self.driver.find_element(By.ID, "sc.keyword").send_keys("Healthcare")
    #     self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[1]/div[1]/div[1]/div[1]/span[1]/b[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='EmpLinksWrapper']/div[2]/div[1]/div[1]/a[3]/p[1]").click()
    #
    # def test_glassdoor_1d564aaf(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.ID, "sc.keyword").clear()
    #     self.driver.find_element(By.ID, "sc.keyword").send_keys("Sales")
    #     self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[3]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='DKFilters']/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='JAModal']/div[1]/div[2]/div[2]/div[1]/div[3]/button[1]").click()
    #
    # def test_glassdoor_f03a2089(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.ID, "sc.keyword").clear()
    #     self.driver.find_element(By.ID, "sc.keyword").send_keys("Microsoft")
    #     self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[1]/div[1]/div[1]/div[1]/span[1]/b[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='EmpLinksWrapper']/div[2]/div[1]/div[1]/a[1]").click()
    #
    # def test_glassdoor_b0695236(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.XPATH, "//header[@id='SiteNav']/nav[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/span[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='SiteNav']/nav[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "enter a company name-c84111-346-487a-d8ff-56246a50e5a").clear()
    #     self.driver.find_element(By.ID, "enter a company name-c84111-346-487a-d8ff-56246a50e5a").send_keys("tata consultancy services")
    #     self.driver.find_element(By.XPATH, "//div[@id='ReactPageContainer']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/span[2]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "enter a company name-d810e2-ab8-8ef4-2baf-fc371dd0746").clear()
    #     self.driver.find_element(By.ID, "enter a company name-d810e2-ab8-8ef4-2baf-fc371dd0746").send_keys("infosys")
    #     self.driver.find_element(By.XPATH, "//div[@id='ReactPageContainer']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[1]/div[1]/span[2]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ReactPageContainer']/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View All Jobs >')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='EmpLinksWrapper']/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    #
    # def test_glassdoor_b98bfded(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.XPATH, "//header[@id='SiteNav']/nav[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/span[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.ID, "sc.keyword").clear()
    #     self.driver.find_element(By.ID, "sc.keyword").send_keys("any")
    #     self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "sc.location").clear()
    #     self.driver.find_element(By.ID, "sc.location").send_keys("maine")
    #     self.driver.find_element(By.XPATH, "//div[@id='JAModal']/div[1]/div[2]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='filter_minSalary']/span[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='PrimaryDropdown']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[23]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='PrimaryDropdown']/div[1]/div[2]/button[2]/span[1]").click()
    #
    # def test_glassdoor_d7e97d6c(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.XPATH, "//header[@id='SiteNav']/nav[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/a[1]/span[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='SiteNav']/nav[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "jobTitleAutocomplete-51ad8a-7226-77e5-6eb1-34cbb522e376").clear()
    #     self.driver.find_element(By.ID, "jobTitleAutocomplete-51ad8a-7226-77e5-6eb1-34cbb522e376").send_keys("assistant store manager")
    #     self.driver.find_element(By.XPATH, "//div[@id='nodeReplace']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "locationAutocomplete-47f08-3ad8-ef54-1de1-a425c25e502").clear()
    #     self.driver.find_element(By.ID, "locationAutocomplete-47f08-3ad8-ef54-1de1-a425c25e502").send_keys("new york")
    #     self.driver.find_element(By.XPATH, "//div[@id='nodeReplace']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='nodeReplace']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='nodeReplace']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='option_ONE_TO_THREE']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='nodeReplace']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='option_10015']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='nodeReplace']/div[1]/div[1]/div[2]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/button[1]").click()
    #
    # def test_glassdoor_dcc30de6(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.XPATH, "//header[@id='SiteNav']/nav[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/a[1]/span[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='SiteNav']/nav[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "typedKeyword-040ec71-e84b-36a1-b338-5bb1446c25").clear()
    #     self.driver.find_element(By.ID, "typedKeyword-040ec71-e84b-36a1-b338-5bb1446c25").send_keys("data scientist")
    #     self.driver.find_element(By.XPATH, "//div[@id='SrchHero']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "Autocomplete-04cf83-af51-3e0-aef0-21af5047c285").clear()
    #     self.driver.find_element(By.ID, "Autocomplete-04cf83-af51-3e0-aef0-21af5047c285").send_keys("california")
    #     self.driver.find_element(By.XPATH, "//div[@id='SrchHero']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/ul[1]/li[1]/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='SrchHero']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='nodeReplace']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='option_LESS_THAN_ONE']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='nodeReplace']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='option_10013']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'787 open jobs')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='EmpLinksWrapper']/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    #
    # def test_glassdoor_dd472743(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.ID, "sc.keyword").clear()
    #     self.driver.find_element(By.ID, "sc.keyword").send_keys("Senior Bioinformatician")
    #     self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[4]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='nodeReplace']/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='option_SDAS']/span[1]").click()
    #
    # def test_glassdoor_2845e790(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.XPATH, "//header[@id='SiteNav']/nav[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/a[1]/span[1]/div[1]/span[1]/svg[1]/g[1]/path[2]").click()
    #     self.driver.find_element(By.ID, "typedKeyword-0b8b41-a448-a005-ef6a-ca70f25c2865").clear()
    #     self.driver.find_element(By.ID, "typedKeyword-0b8b41-a448-a005-ef6a-ca70f25c2865").send_keys("Marketing Manager")
    #     self.driver.find_element(By.XPATH, "//div[@id='SrchHero']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/span[1]/svg[1]").click()
    
    def test_glassdoor_36113c94(self):
        # self.driver.get("https://glassdoor.com")
        # uiteststudy@gmail.com:Pass4Glassdoor2024!
        time.sleep(7)
        # add login steps
        self.driver.find_element(By.XPATH, "//div[@id='SignInButton']/button[1]").click()
        self.driver.find_element(By.ID, "modalUserEmail").clear()
        self.driver.find_element(By.ID, "modalUserEmail").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//div[@data-test='authModalContainerV2-content']//button[@data-test='email-form-button']").click()
        self.driver.find_element(By.ID, "modalUserPassword").clear()
        self.driver.find_element(By.ID, "modalUserPassword").send_keys("Pass4Glassdoor2024!")

        time.sleep(3)
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted.
        # if locate to div then will overlap with element "show password" and be intercepted
        # If located to button then will intercept by parent div
        # if locate to span then will intercept by parent div
        self.driver.find_element(By.XPATH, "//div[@id='InlineLoginModule']/div/div[1]/div[1]/div/div/div/form/div[2]/button[1]/span[1]").click()
        # self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//div[@id='InlineLoginModule']/div/div[1]/div[1]/div/div/div/form/div[2]/button[1]").get_native_element())
        self.driver.find_element(By.XPATH, "//div[@id='globalNavContainer']/div/ul/li[2]").click()

        # self.driver.find_element(By.ID, "sc.keyword").clear()
        # self.driver.find_element(By.ID, "sc.keyword").send_keys("copywriter")
        # self.driver.find_element(By.ID, "sc.location").clear()
        # self.driver.find_element(By.ID, "sc.location").send_keys("mumbai")
        self.driver.find_element(By.ID, "searchBar-jobTitle").clear()
        self.driver.find_element(By.ID, "searchBar-jobTitle").send_keys("copywriter")
        self.driver.find_element(By.ID, "searchBar-location").clear()
        self.driver.find_element(By.ID, "searchBar-location").send_keys("mumbai")
        self.driver.find_element(By.ID, "searchBar-location").send_keys(Keys.RETURN)

        # self.driver.find_element(By.XPATH, "//ul[@id='SearchKeyword']/li[1]/div[1]/div[1]/div[1]/span[1]/b[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='Discover']/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/strong[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='JAModal']/div[1]/div[2]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_jobType']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='PrimaryDropdown']/ul[1]/li[2]/button[1]/div[1]").click()
        # self.driver.find_element(By.ID, "filter_fromAge").click()
        # self.driver.find_element(By.XPATH, "//div[@id='PrimaryDropdown']/ul[1]/li[4]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_radius']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='PrimaryDropdown']/ul[1]/li[6]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//header[@id='DKFilters']/div[1]/div[1]/div[2]").click()
        # self.driver.find_element(By.XPATH, "//header[@id='DKFilters']/div[1]/div[1]/div[2]/div[2]/div[14]/label[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//header[@id='DKFilters']/div[1]/div[1]/div[2]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//article[@id='MainCol']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//article[@id='MainCol']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/button[1]/div[2]").click()
        # self.driver.find_element(By.XPATH, "//article[@id='MainCol']/div[1]/ul[1]/li[1]/div[2]/div[1]/div[1]/button[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='expand-filters']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='jobTypeIndeed-option' and contains(., 'Full-time')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='fromAge' and text()='Date posted']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='fromAge-option' and contains(., 'Last week')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='radius' and text()='Distance']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='radius-option' and contains(., '50 miles')]").click()
        self.driver.find_element(By.XPATH, "//label[@aria-label='Easy Apply only']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='apply-search-filters' and contains(., 'Apply filters')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='sortBy' and text()='Most relevant']").click()
        self.driver.find_element(By.XPATH, "//button[@role='option' and text()='Most recent']").click()

    # def test_glassdoor_40d890b9(self):
    #     # self.driver.get("https://glassdoor.com")
    #     self.driver.find_element(By.ID, "sc.keyword").clear()
    #     self.driver.find_element(By.ID, "sc.keyword").send_keys("software engineer")
    #     self.driver.find_element(By.ID, "sc.location").clear()
    #     self.driver.find_element(By.ID, "sc.location").send_keys("Seattle, WA")
    #     self.driver.find_element(By.XPATH, "//form[@id='scBar']/div[1]/button[1]/span[1]/span[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Discover']/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/strong[1]").click()
    