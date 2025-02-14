import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestEspn:
    def test_espn_be5e5f14(self):
        # self.driver.get("https://espn.com")
        self.driver.find_element(By.XPATH, "//nav[@id='global-nav']/ul[1]/li[1]/a[1]/span[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//nav[@id='global-nav-secondary']/div[1]/ul[1]/li[4]/a[1]/span[1]").click()
        # should click somewhere else to hide the hover window otherwise will have selenium.common.exceptions.ElementClickInterceptedException
        self.driver.find_element(By.ID, "global-search-trigger").click()

        self.driver.find_element(By.XPATH, "//nav[@id='global-nav-secondary']/div[1]/ul[1]/li[3]/a[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Calendar']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]/use[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()
        self.driver.find_element(By.XPATH, "//button[@class='Arrow flex justify-center items-center Arrow--left Arrow--year']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='fittPageContainer']/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[27]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@class='MonthContainer__WeekList__item']//span[text()='Super Bowl']").click()
