import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestFinanceYahoo:
    def test_financeyahoo_b2fd70cb(self):
        # self.driver.get("https://finance.yahoo.com")
        # uiteststudy@gmail.com:Pass4Yahoo2024
        # add extra login steps
        self.driver.find_element(By.ID, "login-container").click()
        self.driver.find_element(By.ID, "login-username").clear()
        self.driver.find_element(By.ID, "login-username").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.ID, "login-signin").click()
        self.driver.find_element(By.ID, "login-passwd").clear()
        self.driver.find_element(By.ID, "login-passwd").send_keys("Pass4Yahoo2024")
        self.driver.find_element(By.ID, "login-signin").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'My Portfolio')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='My Portfolio']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='Col1-0-Portfolios-Proxy']/main[1]/header[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'acccon')]/div/div/div[6]/div/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='myLightboxContainer']/section[1]/div[1]/div[1]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Portfolio Name']").clear()
        # self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Portfolio Name']").send_keys("Tech")
        self.driver.find_element(By.ID, "new-portfolio-name").clear()
        self.driver.find_element(By.ID, "new-portfolio-name").send_keys("Tech")

        # self.driver.find_element(By.XPATH, "//button[@type='submit' and @title='Submit']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'dialog-')]/div[2]/div/div/div/div/div[3]/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='myLightboxContainer']/div[1]/button[2]/span[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='myLightboxContainer']/div[1]/div[10]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='Lead-3-Portfolios-Proxy']/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Lead-3-Portfolios-Proxy']/main/div/div/div[2]/div/div[2]/div/div").click()

        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='VZ, AAPL, TSLA']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='VZ, AAPL, TSLA']").send_keys("Microsoft")

        # self.driver.find_element(By.XPATH, "//div[@id='dropdown-menu']/div[3]/form[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[2]/span[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@role='option' and @title='Microsoft Corporation' and @data-id='result-quotes-0']").click()

        # delete portfolios for next test run
        self.driver.find_element(By.XPATH, "//div[@id='Lead-3-Portfolios-Proxy']/main/header/div[2]/div/div/div[3]/div").click()
        self.driver.find_element(By.XPATH, "//span[text()='Delete Portfolio']").click()
        self.driver.find_element(By.XPATH, "//div[@id='myLightboxContainer']/section/form/div[2]/button[1]").click()
