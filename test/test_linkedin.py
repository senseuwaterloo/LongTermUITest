import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestLinkedin:
    def test_linkedin_20bc1709(self):
        self.driver.get("https://www.linkedin.com/")

        self.driver.find_element(By.XPATH, "//span[contains(text(), '   Jobs')]").click()
        self.driver.find_element(By.ID, "job-search-bar-keywords").clear()
        self.driver.find_element(By.ID, "job-search-bar-keywords").send_keys("Bioinformatician")
        self.driver.find_element(By.XPATH, "//button[@data-tracking-control-name='public_jobs_jobs-search-bar_base-search-bar-search-submit']").click()
        self.driver.find_element(By.XPATH, "//button[@data-tracking-control-name='public_jobs_f_WT' and @type='button']").click()
        self.driver.find_element(By.ID, "f_WT-1").click()
        self.driver.find_element(By.XPATH, "//button[@data-tracking-control-name='public_jobs_f_WT' and @type='submit']").click()
    