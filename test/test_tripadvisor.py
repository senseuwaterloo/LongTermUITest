import pytest
from selenium.webdriver.common.by import By

from browser_helper import calculate_dates_full_month_name


@pytest.mark.usefixtures("setup_class")
class TestTripadvisor:
    def test_tripadvisor_ffc01d9d(self):
        # self.driver.get("https://www.tripadvisor.com/")
        # TODO: Still being blocked by trip advisor, so can't evaluate whether the test can pass. Consider remove trip advisor from out subjects?
        # TODO keep being promoted to verify not being a robot by the time we label the test cases, should remove this subject.
        # self.driver.find_element(By.XPATH, "//div[@id='lithium-root']/main[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[16]/div[1]/button[1]/span[3]/svg[1]/circle[3]").click()
        # self.driver.find_element(By.XPATH, "//a[@id='menu-item-3']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@data-automation='centralNav_flights']").click()

        # page logic changed, click one-way button is moved to below
        # self.driver.find_element(By.XPATH, "//div[@id='component_6']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]").click()

        # self.driver.find_element(By.XPATH, "//input[@name='From' and @value='Columbus (CMH)' and @type='text' and @placeholder='City or Airport']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='From' and @value='Columbus (CMH)' and @type='text' and @placeholder='City or Airport']").send_keys("SAN FRANSISCO")
        # self.driver.find_element(By.XPATH, "//body[@id='BODY_BLOCK_JQUERY_REFLOW']/div[9]/div[1]/div[1]/div[1]/div[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//input[@name='To' and @value='Los Angeles (LAX)' and @type='text' and @placeholder='City or Airport']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='To' and @value='Los Angeles (LAX)' and @type='text' and @placeholder='City or Airport']").send_keys("SAN DIEGO")
        # self.driver.find_element(By.XPATH, "//body[@id='BODY_BLOCK_JQUERY_REFLOW']/div[9]/div[1]/div[1]/div[1]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Origin']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Origin']").send_keys("SAN FRANSISCO")
        self.driver.find_element(By.XPATH, "//div[text()='SFO International Airport (SFO)']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Destination']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @type='search' and @placeholder='Destination']").send_keys("SAN DIEGO")
        self.driver.find_element(By.XPATH, "//div[text()='San Diego International Airport (SAN)']").click()

        # time select logic changed, have to select depart time and return time at first then change to one way
        # self.driver.find_element(By.XPATH, "//div[@id='component_6']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]").click()
        # self.driver.find_element(By.XPATH, "//body[@id='BODY_BLOCK_JQUERY_REFLOW']/div[9]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[7]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and contains(@aria-label, 'Enter the date range.')]").click()
        start_date_str, end_date_str = calculate_dates_full_month_name(14, 21)
        self.driver.find_element(By.XPATH, f"//div[@aria-label='{start_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//div[@aria-label='{end_date_str}']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Apply']").click()

        # self.driver.find_element(By.ID, "OVERLAY").click()
        # self.driver.find_element(By.XPATH, "//body[@id='BODY_BLOCK_JQUERY_REFLOW']/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/span[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//body[@id='BODY_BLOCK_JQUERY_REFLOW']/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/span[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//body[@id='BODY_BLOCK_JQUERY_REFLOW']/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='component_6']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and contains(@aria-label, 'Enter the number of guests.')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Increase']").click()
        self.driver.find_element(By.XPATH, "//div[./div[1]/div[text()='Adults']]/div[2]/button[@title='Increase']").click()
        self.driver.find_element(By.XPATH, "//div[./div[1]/div[text()='Seniors']]/div[2]/button[@title='Increase']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Apply']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='component_6']/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='leftRailFilter']/div[1]/div[1]/div[1]/div[1]/div[9]/div[5]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='leftRailFilter']/div[1]/div[1]/div[1]/div[1]/div[9]/div[8]/div[1]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='leftRailFilter']/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='MAIN']/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='fareOptionsContainerId']/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[7]/td[2]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Search']").click()
        # click on one-way here
        self.driver.find_element(By.XPATH, "//a[text()='One-way']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Prefer nonstop']").click()
        self.driver.find_element(By.XPATH, "//button[@class='ui_button primary fullwidth']/div[text()='Search']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Select all airlines']/following-sibling::div[1]//span[text()='Show more']").click()
        self.driver.find_element(By.XPATH, "//span[text()='United']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Best Value']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Earliest outbound departure']").click()
        self.driver.find_element(By.XPATH, "//div[./div[1]/span[contains(text(), 'Price per person is the average of all passengers')]]/div[2]/div[2]//div[text()='View Deal']").click()
