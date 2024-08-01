import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element, scroll_down


@pytest.mark.usefixtures("setup_class")
class TestIndeed:
    
    # def test_indeed_75b3bf74(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "FindSalaries").click()
    #     self.driver.find_element(By.ID, "input-title-autocomplete").clear()
    #     self.driver.find_element(By.ID, "input-title-autocomplete").send_keys("Biostatistician")
    #     self.driver.find_element(By.XPATH, "//div[@id='input-title-autocomplete-suggestion-list']/ul[1]/li[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='what-where-search-btn']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='salaries-page']/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.ID, "cmp-header-follow-button").click()
    #
    # def test_indeed_82c6b348(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "CompanyReviews").click()
    #     self.driver.find_element(By.ID, "ifl-InputFormField-3").clear()
    #     self.driver.find_element(By.ID, "ifl-InputFormField-3").send_keys("burger king")
    #     self.driver.find_element(By.XPATH, "//li[@id=':Rb5:-burger king']/span[1]/b[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//nav[@id='cmp-skip-header-desktop']/div[1]/ul[1]/li[7]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cmp-container']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/ul[1]/li[9]/a[1]").click()
    #
    # def test_indeed_9c508ec3(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "text-input-what").clear()
    #     self.driver.find_element(By.ID, "text-input-what").send_keys("finance")
    #     self.driver.find_element(By.ID, "text-input-where").clear()
    #     self.driver.find_element(By.ID, "text-input-where").send_keys("San Francisco")
    #     self.driver.find_element(By.XPATH, "//div[@id='text-input-where-suggestion-list']/ul[1]/li[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-explvl']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Entry Level (544)')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-edulvl']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Master's Degree (444)\")]").click()
    #
    # def test_indeed_9ee49ba4(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "text-input-what").clear()
    #     self.driver.find_element(By.ID, "text-input-what").send_keys("administrative assistant")
    #     self.driver.find_element(By.ID, "text-input-where").clear()
    #     self.driver.find_element(By.ID, "text-input-where").send_keys("Miami")
    #     self.driver.find_element(By.XPATH, "//div[@id='text-input-where-suggestion-list']/ul[1]/li[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-salary-estimate']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'$40,000+ (335)')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-jobtype']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Part-time (22)')]").click()
    #
    # def test_indeed_b7069c40(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Certifications')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='landing']/div[2]/div[2]/a[2]/span[1]/span[4]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='unified_serp']/div[2]/div[1]/div[1]/button[5]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'30 mins to 1 hour')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='unified_serp']/div[2]/div[1]/div[1]/button[6]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'4.0')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='unified_serp']/div[2]/div[1]/div[1]/button[4]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'(60 courses)')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='unified_serp']/div[2]/div[1]/div[1]/button[3]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Online')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='461599']/div[1]/div[1]/div[1]/div[1]").click()
    #
    # def test_indeed_c4166e68(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "CompanyReviews").click()
    #     self.driver.find_element(By.ID, "ifl-InputFormField-3").clear()
    #     self.driver.find_element(By.ID, "ifl-InputFormField-3").send_keys("Mc Donald's")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Reviews')]").click()
    #
    # def test_indeed_cda8806c(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.XPATH, "//span[@id='jobsearch-HomepageBody']/div[3]/div[5]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='recentSearches']/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]").click()
    #
    # def test_indeed_d21d71f9(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "text-input-what").clear()
    #     self.driver.find_element(By.ID, "text-input-what").send_keys("customer service")
    #     self.driver.find_element(By.ID, "text-input-where").clear()
    #     self.driver.find_element(By.ID, "text-input-where").send_keys("Chicago")
    #     self.driver.find_element(By.XPATH, "//div[@id='text-input-where-suggestion-list']/ul[1]/li[1]/span[1]/span[1]/b[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-salary-estimate']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'$20.00+/hour (788)')]").click()
    #     self.driver.find_element(By.ID, "filter-explvl").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'No Experience Required (11)')]").click()
    #
    # def test_indeed_dd1dc3f9(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "text-input-what").clear()
    #     self.driver.find_element(By.ID, "text-input-what").send_keys("healthcare")
    #     self.driver.find_element(By.ID, "text-input-where").click()
    #     self.driver.find_element(By.ID, "text-input-where").clear()
    #     self.driver.find_element(By.ID, "text-input-where").send_keys("Los Angeles")
    #     self.driver.find_element(By.XPATH, "//li[@role='option']").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-edulvl']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Bachelor's Degree (12318)\")]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-taxo3']/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'No weekends (217)')]").click()
    #
    # def test_indeed_ec54919e(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "text-input-what").clear()
    #     self.driver.find_element(By.ID, "text-input-what").send_keys("home office")
    #     self.driver.find_element(By.XPATH, "//div[@id='text-input-what-suggestion-list']/ul[1]/li[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.ID, "filter-salary-estimate").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'$25,000+ (2390)')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-remotejob']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Remote (158)')]").click()
    #
    # def test_indeed_12f65c16(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Browse Jobs')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Retail')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Grocery Store Cashier jobs')]").click()
    #     self.driver.find_element(By.ID, "text-input-where").clear()
    #     self.driver.find_element(By.ID, "text-input-where").send_keys("Florida")
    #     self.driver.find_element(By.XPATH, "//li[@role='option']").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.ID, "sj_4fd431be482f0c06").click()
    #
    # def test_indeed_1fd666a2(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Browse Companies')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/nav[1]/div[1]/div[1]/ul[1]/li[26]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main']/div[1]/section[1]/ul[1]/li[111]/a[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//nav[@id='cmp-skip-header-desktop']/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "cmp-JobSearchInput-cmp-JobsHeader-what").clear()
    #     self.driver.find_element(By.ID, "cmp-JobSearchInput-cmp-JobsHeader-what").send_keys("human resource")
    #     self.driver.find_element(By.XPATH, "//li[@role='option']").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    # def test_indeed_31a9440b(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "CompanyReviews").click()
    #     self.driver.find_element(By.ID, "ifl-InputFormField-3").clear()
    #     self.driver.find_element(By.ID, "ifl-InputFormField-3").send_keys("Calico")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Reviews')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cmp-container']/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[2]/button[1]").click()
    #
    # def test_indeed_333eca5a(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "text-input-what").clear()
    #     self.driver.find_element(By.ID, "text-input-what").send_keys("software engineer")
    #     self.driver.find_element(By.XPATH, "//div[@id='text-input-what-suggestion-list']/ul[1]/li[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "text-input-where").clear()
    #     self.driver.find_element(By.ID, "text-input-where").send_keys("united states")
    #     self.driver.find_element(By.XPATH, "//div[@id='text-input-where-suggestion-list']/ul[1]/li[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.ID, "filter-remotejob").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Remote (31814)')]").click()
    #
    # def test_indeed_3363038b(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "text-input-what").clear()
    #     self.driver.find_element(By.ID, "text-input-what").send_keys("software engineer")
    #     self.driver.find_element(By.XPATH, "//div[@id='text-input-what-suggestion-list']/ul[1]/li[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-remotejob']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Remote (225)')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-salary-estimate']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'$105,000+ (188)')]").click()
    #
    # def test_indeed_349f5f06(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Countries')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[1]/ul[1]/li[59]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Browse Jobs')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tennessee')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs in Bradley County, TN')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-radius']/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Within 10 miles')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-remotejob']/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Remote (36)')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-explvl']/div[2]/svg[1]/g[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Entry Level (25)')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'date')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-jobtype']/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Part-time (10)')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='indeed-apply-widget']/div[2]/button[1]/div[1]/span[1]").click()
    #
    # def test_indeed_3d8c4d03(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Browse Jobs')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Nagaland')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs in kohima')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Last 7 days')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='filter-taxo3']/div[3]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Bachelor's degree (3)\")]").click()
    #     self.driver.find_element(By.ID, "filter-salary-estimate").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'₹ 25,000.00+/month (2)')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='saveJobButtonContainer']/div[1]/div[1]/button[1]/svg[1]").click()
    #
    # def test_indeed_421c39c0(self):
    #     # self.driver.get("https://indeed.com")
    #     self.driver.find_element(By.ID, "text-input-what").clear()
    #     self.driver.find_element(By.ID, "text-input-what").send_keys("nutritionist")
    #     self.driver.find_element(By.ID, "text-input-where").clear()
    #     self.driver.find_element(By.ID, "text-input-where").send_keys("ohio")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_indeed_4ce51ed5(self):
        # self.driver.get("https://www.indeed.com/worldwide")
        # comment the following step since it is redundant
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Countries')]").click()

        self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[1]/ul[1]/li[58]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Browse Jobs')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'England')]").click()
        # no link for Essex, need to change to Chelmsford
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs in Essex')]").click()
        # scroll to element and scroll down further to avoid being blocked by cookie banner
        chelmsford_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs in Chelmsford')]")
        scroll_to_element(self.driver, chelmsford_link)
        scroll_down(self.driver, 500)
        chelmsford_link.click()

        # self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']/div[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']/div[2]").click()
        # code passed but the dropdown won't open so try to use JS click
        # self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']/div[1]").get_native_element())
        # JS click still not working, try to click on the parent button
        # self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']").click()
        # click on button is also not working so try to use perform method
        # perform method is also not working, try add some sleep time and finally it is working with some sleep time
        time.sleep(3)
        sort_date_button = self.driver.find_element(By.XPATH, "//button[@id='filter-dateposted']/div[1]").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element(sort_date_button)
        action.click().perform()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Last 24 hours')]").click()

        # self.driver.find_element(By.XPATH, "//button[@id='filter-srctype']/div[2]/svg[1]").click()
        # dropdown is not expanding as above so try to add some sleep time to see whether combing typical click and wait time is ok and it seems that it is working so it must sleep
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='filter-srctype']/div[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Employer (724)')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Employer']").click()

        # save as above, add some sleep time otherwise it won't display or maybe some other activity closed the window
        time.sleep(3)
        self.driver.find_element(By.ID, "filter-taxo2").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Healthcare (145)')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Healthcare']").click()
        self.driver.find_element(By.XPATH, "//button[@form='filter-taxo2-menu']").click()

        # self.driver.find_element(By.XPATH, "//button[@id='filter-jobtype']/div[2]/svg[1]").click()
        # save as above, add some sleep time otherwise it won't display or maybe some other activity closed the window
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='filter-jobtype']/div[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Part-time (45)')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Part-time']").click()

        # save as above, add some sleep time otherwise it won't display or maybe some other activity closed the window
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='filter-salary-estimate']/div[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'£20,000+ (42)')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='£20,000+']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'date')]").click()
        self.driver.find_element(By.ID, "dateLabel").click()

        # self.driver.find_element(By.XPATH, "//button[@id='jobActionButton-a722b6770c53079f']/svg[1]/path[1]").click()
        # save as above, add some sleep time otherwise it won't display or maybe some other activity closed the window
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[@id='mosaic-provider-jobcards']/ul/li[1]/div/div/div/div/div/table/tbody/tr/td[2]/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='mosaic-provider-jobcards']/ul[1]/li[1]/div[1]/div[2]/div[1]/button[3]").click()
        self.driver.find_element(By.XPATH, "//div[@data-valuetext='Report job']").click()

        # self.driver.find_element(By.ID, "label-radio-option-1").click()
        self.driver.find_element(By.XPATH, "//span[text()='It seems like a fake job']").click()

        # self.driver.find_element(By.ID, "additional-information-textarea").clear()
        # self.driver.find_element(By.ID, "additional-information-textarea").send_keys("Seems fake")
        self.driver.find_element(By.ID, "ifl-TextAreaFormField-8").clear()
        self.driver.find_element(By.ID, "ifl-TextAreaFormField-8").send_keys("Seems fake")

        # do not really click and submit data to avoid spam
        # self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    