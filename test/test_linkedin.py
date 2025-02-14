import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestLinkedin:
    def test_linkedin_20bc1709(self):
        # self.driver.get("https://www.linkedin.com/")
        # trying to implement this test case without login, so logic is changed
        # self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").clear()
        # self.driver.find_element(By.XPATH, "//input[@role='combobox' and @type='text' and @placeholder='Search']").send_keys("Bioinformatician")
        # self.driver.find_element(By.XPATH, "//div[@id='basic-result-x8t5c']/div[1]/span[1]/span[1]/strong[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='search-reusables__filters-bar']/ul[1]/li[1]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='ember518']/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='artdeco-hoverable-artdeco-gen-61']/div[1]/div[1]/form[1]/fieldset[1]/div[1]/ul[1]/li[3]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='ember709']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='search-reusables__filters-bar']/div[1]/div[1]/button[1]").click()
        # self.driver.find_element(By.ID, "ember981").click()
        # self.driver.find_element(By.XPATH, "//button[@id='ember974']/li-icon[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), '   Jobs')]").click()
        self.driver.find_element(By.ID, "job-search-bar-keywords").clear()
        self.driver.find_element(By.ID, "job-search-bar-keywords").send_keys("Bioinformatician")
        self.driver.find_element(By.XPATH, "//button[@data-tracking-control-name='public_jobs_jobs-search-bar_base-search-bar-search-submit']").click()
        self.driver.find_element(By.XPATH, "//button[@data-tracking-control-name='public_jobs_f_WT' and @type='button']").click()
        self.driver.find_element(By.ID, "f_WT-1").click()
        self.driver.find_element(By.XPATH, "//button[@data-tracking-control-name='public_jobs_f_WT' and @type='submit']").click()
        # remove the following step to avoid login
        # self.driver.find_element(By.XPATH, "//main[@id='main-content']//ul[@class='jobs-search__results-list']/li[1]/div[1]").click()
    