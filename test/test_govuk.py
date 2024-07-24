import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestGovUk:
    
    # def test_govuk_d9c8afd2(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//button[@id='super-navigation-menu-77caf4b3-toggle']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Visas and immigration')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Work in the UK')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply for the Global Talent visa')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Extend your visa')]").click()
    #
    # def test_govuk_eb0e9fc2(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.ID, "search-main-6455fc37").clear()
    #     self.driver.find_element(By.ID, "search-main-6455fc37").send_keys("covid 19")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='facet-wrapper']/div[1]/div[2]/div[1]/h3[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "level_one_taxon").clear()
    #     self.driver.find_element(By.ID, "level_one_taxon").select("Transport")
    #     self.driver.find_element(By.ID, "level_two_taxon").clear()
    #     self.driver.find_element(By.ID, "level_two_taxon").select("Aviation")
    #     self.driver.find_element(By.ID, "order").clear()
    #     self.driver.find_element(By.ID, "order").select("Updated (newest)")
    #
    # def test_govuk_335e1107(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//button[@id='super-navigation-menu-53fd6ba4-toggle']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Passports, travel and living abroad')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Passports')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Getting your first adult passport')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[1]/aside[1]/nav[1]/ol[1]/li[1]").click()
    #
    # def test_govuk_3e22a7b0(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//button[@id='super-navigation-menu-651d46c3-toggle']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'News')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='keywords']/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='facet-wrapper']/div[1]/div[2]/div[6]/h3[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "public_timestamp[from]").clear()
    #     self.driver.find_element(By.ID, "public_timestamp[from]").send_keys("2023")
    #     self.driver.find_element(By.XPATH, "//div[@id='keywords']/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "order").clear()
    #     self.driver.find_element(By.ID, "order").select("Relevance")
    
    def test_govuk_593f78ad(self):
        # self.driver.get("https://www.gov.uk/")
        # self.driver.find_element(By.ID, "search-main-6ddf766d").clear()
        # self.driver.find_element(By.ID, "search-main-6ddf766d").send_keys("benefits")
        self.driver.find_element(By.XPATH, "//div[@id='wrapper']//input[contains(@id, 'search-main-') and @name='q']").clear()
        self.driver.find_element(By.XPATH, "//div[@id='wrapper']//input[contains(@id, 'search-main-') and @name='q']").send_keys("benefits")

        # self.driver.find_element(By.XPATH, "//main[@id='content']/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='wrapper']//button[@enterkeyhint='search']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Check benefits and financial support you can get')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Check what you can get')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(.,'Check what you can get')]").click()

        # somehow wait for the radio button to be clickable will timeout and therefore we wait for the label
        # self.driver.find_element(By.ID, "response-0").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-0']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
        # self.driver.find_element(By.ID, "response-0").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-0']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
        # self.driver.find_element(By.ID, "response-2").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-2']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
        # self.driver.find_element(By.ID, "response-1").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-1']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
        # self.driver.find_element(By.ID, "response-1").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-1']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
        # self.driver.find_element(By.ID, "response-1").click()
        self.driver.find_element(By.XPATH, "//label[@for='response-1']").click()
        self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
    
    # def test_govuk_6b2885ba(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Visas and immigration')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'What you need to do')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Check if you need a UK visa')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Start now')]").click()
    #     self.driver.find_element(By.ID, "response").clear()
    #     self.driver.find_element(By.ID, "response").select("USA")
    #     self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
    #     self.driver.find_element(By.ID, "response-1").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
    #     self.driver.find_element(By.ID, "response-1").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
    #     self.driver.find_element(By.ID, "response-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='current-question']/button[1]").click()
    #
    # def test_govuk_6dad2b8d(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//button[@id='super-navigation-menu-f7c1b516-toggle']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Passports, travel and living abroad')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Living abroad')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Voting if you move or live abroad')]").click()
    #
    # def test_govuk_884a7c23(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//button[@id='super-navigation-menu-6e8c2f9b-toggle']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Money and tax')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Income Tax')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Check your Income Tax for the current year')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'estimate how much Income Tax you should pay this year')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Start now')]").click()
    #     self.driver.find_element(By.ID, "amount").clear()
    #     self.driver.find_element(By.ID, "amount").send_keys("1000")
    #     self.driver.find_element(By.ID, "period-3").click()
    #     self.driver.find_element(By.ID, "button-continue").click()
    #     self.driver.find_element(By.ID, "overStatePensionAge").click()
    #     self.driver.find_element(By.ID, "button-continue").click()
    #     self.driver.find_element(By.ID, "button-continue").click()
    #     self.driver.find_element(By.ID, "payScottishRate-2").click()
    #     self.driver.find_element(By.ID, "button-continue").click()
    #     self.driver.find_element(By.ID, "button-get-results").click()
    #
    # def test_govuk_958167d8(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//button[@id='super-navigation-menu-609901dd-toggle']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Guidance and regulation')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='facet-wrapper']/div[1]/div[2]/div[1]/h3[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "level_one_taxon").clear()
    #     self.driver.find_element(By.ID, "level_one_taxon").select("Brexit")
    #     self.driver.find_element(By.ID, "order").clear()
    #     self.driver.find_element(By.ID, "order").select("Updated (newest)")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Get a goods movement reference: check service availability and issues')]").click()
    #
    # def test_govuk_02993d95(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//button[@id='super-navigation-menu-77caf4b3-toggle']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Education and learning')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Student finance')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Doctoral Loan')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Eligibility')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"What you'll get\")]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'How to apply')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Further information')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"What you'll get\")]").click()
    #
    # def test_govuk_082601c7(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Disabled people')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Carers')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Carer's Credit\")]").click()
    #
    # def test_govuk_0b3cb995(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Emergency Alerts')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Current alerts')]").click()
    #
    # def test_govuk_17cfd4fe(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Benefits')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Benefits and financial support if you're looking for work\")]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Jobseeker's Allowance (JSA)\")]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Eligibility')]").click()
    #
    # def test_govuk_235fe559(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a job')]").click()
    #     self.driver.find_element(By.ID, "button-id-9c398850").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Manchester')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sales Executive')]").click()
    #
    # def test_govuk_95aaaaf6(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//button[@id='super-navigation-menu-e6d074a4-toggle']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Crime, justice and the law')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Courts, tribunals and appeals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a court or tribunal')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Start now')]").click()
    #
    # def test_govuk_b60cd6a1(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a job')]").click()
    #     self.driver.find_element(By.ID, "button-id-e08ccc89").click()
    #     self.driver.find_element(By.ID, "where").clear()
    #     self.driver.find_element(By.ID, "where").send_keys("London")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[5]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='Search' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Teaching Jobs')]").click()
    #
    # def test_govuk_bf40a88e(self):
    #     # self.driver.get("https://www.gov.uk/")
    #     self.driver.find_element(By.XPATH, "//button[@id='super-navigation-menu-53fd6ba4-toggle']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Benefits')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Benefits and financial support for families')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Child Benefit')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Eligibility')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'How it works')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"What you'll get\")]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'How to claim')]").click()
    