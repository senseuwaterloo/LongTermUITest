import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_slash_format


@pytest.mark.usefixtures("setup_class")
class TestThetrainline:
    def test_thetrainline_5b37d2e1(self):
        # self.driver.get("https://thetrainline.com")

        # self.driver.find_element(By.ID, "from.search_2023-03-25T10").clear()
        # self.driver.find_element(By.ID, "from.search_2023-03-25T10").send_keys("PARIS")
        # self.driver.find_element(By.XPATH, "//li[@id='selected_option']/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "jsf-origin-input").clear()
        self.driver.find_element(By.ID, "jsf-origin-input").send_keys("PARIS")

        # self.driver.find_element(By.XPATH, "//li[@id='selected_option']/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='jsf-origin-menu']/li[contains(@id, 'jsf-origin-item-') and ./span[text()='Paris'] and ./span[text()='FR']]").click()

        # self.driver.find_element(By.ID, "to.search_2023-03-25T10").clear()
        # self.driver.find_element(By.ID, "to.search_2023-03-25T10").send_keys("MILAN")
        # self.driver.find_element(By.XPATH, "//ul[@id='stations_to']/div[1]/li[2]/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "jsf-destination-input").clear()
        self.driver.find_element(By.ID, "jsf-destination-input").send_keys("MILAN")
        self.driver.find_element(By.XPATH, "//ul[@id='jsf-destination-menu']/li[contains(@id, 'jsf-destination-item-') and ./div/span[text()='Milano'] and ./div/span[text()='Milan'] and ./span[text()='IT']]").click()

        # self.driver.find_element(By.ID, "page.journeySearchForm.outbound.title").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/main[1]/div[1]/div[4]/div[1]/div[1]/div[1]/section[1]/form[1]/div[3]/fieldset[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]/svg[1]/rect[1]").click()
        # self.driver.find_element(By.ID, "page.journeySearchForm.outbound.title3-26").click()n
        self.driver.find_element(By.ID, "jsf-outbound-time-input-toggle").click()
        start_date_str, end_date_str = calculate_dates_slash_format(10, 10)
        if self.driver.find_element(By.XPATH, f"//td[@data-date='{start_date_str}']") is None:
            self.driver.find_element(By.ID, "ChevronRight").click()
        self.driver.find_element(By.XPATH, f"//td[@data-date='{start_date_str}']").click()
        leaving_hour_dropdown = self.driver.find_element(By.ID, "jsf-outbound-time-time-picker-hour")
        leaving_hour_select = Select(leaving_hour_dropdown)
        leaving_hour_select.select_by_value("12")
        leaving_minute_dropdown = self.driver.find_element(By.ID, "jsf-outbound-time-time-picker")
        leaving_minute_select = Select(leaving_minute_dropdown)
        leaving_minute_select.select_by_value("00")

        # self.driver.find_element(By.XPATH, "//button[@id='passenger-summary-btn']/div[1]/div[3]/svg[1]/polyline[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/main[1]/div[1]/div[4]/div[1]/div[1]/div[1]/section[1]/form[1]/div[4]/div[1]/div[4]/div[1]/div[2]/button[1]/div[1]/span[1]").click()
        # self.driver.find_element(By.ID, "58c4c283-ee3e-4922-9179-1cd7d0cc5cea").clear()
        # self.driver.find_element(By.ID, "58c4c283-ee3e-4922-9179-1cd7d0cc5cea").select("16")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/main[1]/div[1]/div[4]/div[1]/div[1]/div[1]/section[1]/form[1]/div[4]/div[1]/div[4]/button[1]").click()
        self.driver.find_element(By.ID, "jsf-passengers-input-toggle").click()
        self.driver.find_element(By.ID, "add-youth-passenger-button").click()
        youth_age_dropdown = self.driver.find_element(By.NAME, "passengers.1.age")
        youth_age_select = Select(youth_age_dropdown)
        youth_age_select.select_by_value("16")

        # already selected time above
        # self.driver.find_element(By.ID, "e438c2ea-2f02-4853-918f-284d88784002").clear()
        # self.driver.find_element(By.ID, "e438c2ea-2f02-4853-918f-284d88784002").select("12")
        # self.driver.find_element(By.ID, "98ee47a2-ed52-42d9-b94d-3c9ec1784da0").clear()
        # self.driver.find_element(By.ID, "98ee47a2-ed52-42d9-b94d-3c9ec1784da0").select("00")

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/main[1]/div[1]/div[4]/div[1]/div[1]/div[1]/section[1]/form[1]/div[5]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='jsf-submit']").click()

        # omit following steps to avoid being blocked
        # self.driver.find_element(By.XPATH, "//div[@id='train']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/button[1]/h3[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='train']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/label[2]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='train']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/label[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/article[14]/button[1]/div[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/article[13]/button[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[5]/div[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='train']/div[1]/div[2]/div[1]/div[2]/button[1]/div[1]").click()
