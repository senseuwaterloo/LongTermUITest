import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_weekday_mta_format


@pytest.mark.usefixtures("setup_class")
class TestNewMtaInfo:
    def test_newmtainfo_db203a3a(self):
        # self.driver.get("https://new.mta.info")
        self.driver.find_element(By.ID, "edit-origin").clear()
        self.driver.find_element(By.ID, "edit-origin").send_keys("brooklyn")

        # self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[1]/div[1]/div[1]/ul[1]/div[2]/li[1]").click()
        self.driver.find_element(By.XPATH, "//li[@aria-label='Brooklyn, NY, USA' and @class='ui-menu-item']").click()

        self.driver.find_element(By.ID, "edit-dest").clear()
        self.driver.find_element(By.ID, "edit-dest").send_keys("staten island")

        # self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[2]/div[1]/div[1]/ul[1]/div[2]/li[1]").click()
        self.driver.find_element(By.XPATH, "//li[@aria-label='Staten Island, NY, USA' and @class='ui-menu-item']").click()

        self.driver.find_element(By.XPATH, "//a[@id='link_tp_when']/span[2]").click()
        self.driver.find_element(By.ID, "datePickerId").click()

        # self.driver.find_element(By.XPATH, "//a[@id='datePickerId']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//td[@id='b167910489558825']/span[1]").click()
        leave_date, arrive_date = calculate_dates_weekday_mta_format(7, 8)
        if self.driver.find_element(By.XPATH, f"//td[@aria-label='{leave_date}']") is None:
            self.driver.find_element(By.XPATH, "//td[@aria-label='Next Month' and @title='Next Month']").click()
        self.driver.find_element(By.XPATH, f"//td[@aria-label='{leave_date}']").click()

        self.driver.find_element(By.XPATH, "//div[./label[@for='edit-leave-arr-a']]").click()

        # self.driver.find_element(By.XPATH, "//select[@type='number']").clear()
        # self.driver.find_element(By.XPATH, "//select[@type='number']").select("9")
        # self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[2]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[2]/select[1]").select("45")
        # self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[3]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[3]/select[1]").select("AM")
        # self.driver.find_element(By.XPATH, "//a[@id='datePickerId']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//td[@id='b167910497122625']/span[1]").click()
        # click to opening the calendar is not responding, possibly because the page was loading after click on Arrive by. So we need some sleep time
        time.sleep(2)
        self.driver.find_element(By.ID, "datePickerId").click()
        if self.driver.find_element(By.XPATH, f"//td[@aria-label='{arrive_date}']") is None:
            self.driver.find_element(By.XPATH, "//td[@aria-label='Next Month' and @title='Next Month']").click()
        self.driver.find_element(By.XPATH, f"//td[@aria-label='{arrive_date}']").click()
        hour_dropdown = self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div/div[1]/select")
        hour_select = Select(hour_dropdown)
        hour_select.select_by_visible_text("9")
        minute_dropdown = self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div/div[2]/select")
        minute_select = Select(minute_dropdown)
        minute_select.select_by_visible_text("45")
        am_pm_dropdown = self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div/div[3]/select")
        am_pm_select = Select(am_pm_dropdown)
        am_pm_select.select_by_visible_text("AM")

        self.driver.find_element(By.ID, "linkPreferencesModal").click()

        # self.driver.find_element(By.XPATH, "//div[@id='edit-transport-mode']/div[4]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='edit-transport-mode']/div[3]/label[1]").click()
        # all travel ways are selected by default, just need to deselect Rail
        self.driver.find_element(By.XPATH, "//div[@id='edit-transport-mode']/div[4]/label[1]").click()

        self.driver.find_element(By.XPATH, "//button[@role='button']").click()
        self.driver.find_element(By.ID, "edit-submit").click()
    