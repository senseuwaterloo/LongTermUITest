import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestTravelzoo:
    def test_travelzoo_b770af80(self):
        # self.driver.get("https://travelzoo.com")
        self.driver.find_element(By.ID, "what-field-1").click()

        # self.driver.find_element(By.ID, "ui-id-66").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'ui-id-') and text()='Hotels']").click()

        # self.driver.find_element(By.ID, "ui-id-81").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'ui-id-') and text()='Anywhere']").click()

        self.driver.find_element(By.ID, "when-field-1").click()

        # self.driver.find_element(By.ID, "ui-id-6").click()
        self.driver.find_element(By.XPATH, "//h3[contains(@id, 'ui-id-') and text()='Select a Month']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='ui-id-7']/ul[1]/li[5]").click()
        self.driver.find_element(By.XPATH, "//li[@data-date-type='SpecificMonth' and @data-month='5' and text()='May']").click()

        # self.driver.find_element(By.ID, "guests-field-1").clear()
        # self.driver.find_element(By.ID, "guests-field-1").select("1 Guest")
        guest_number_dropdown = self.driver.find_element(By.ID, "guests-field-1")
        guest_number_select = Select(guest_number_dropdown)
        guest_number_select.select_by_value("1")

        self.driver.find_element(By.ID, "search-button-1").click()
        self.driver.find_element(By.ID, "refine-search-toggle").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[21]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[25]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[15]").click()
        # US is using different format. e.g., US: Pet-Friendly CA: Pet-friendly
        self.driver.find_element(By.XPATH, "//button[@type='button' and (text()='Pet-Friendly' or text()='Pet-friendly')]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[25]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and (text()='Last-Minute' or text()='Last Minute')]").click()
        # no Road Trips filter in the new version, and can only select two filters in the new version so remove one filter
        # self.driver.find_element(By.XPATH, "//div[@id='filter-container']/div[1]/div[1]/div[1]/div[1]/button[15]").click()

        self.driver.find_element(By.XPATH, "//div[@id='sort-container']/div[1]/div[1]/div[1]/div[1]/div[3]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refine-search-container']/div[6]/button[1]").click()

        # self.driver.find_element(By.XPATH, "//li[@id='51574']/div[1]/a[1]/div[1]/h2[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@class='result-group-content']/ul[1]/li[2]//h2[@class='deal-headline']").click()

        # different from the original task, do not book to avoid sending spam data
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'CHECK DATES')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'$189')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'$259')]").click()
        # self.driver.find_element(By.ID, "btnContinueToRoomRates").click()
        # self.driver.find_element(By.XPATH, "//div[@id='ui-id-21']/div[4]/div[1]/div[3]/div[2]/div[1]/div[2]/button[1]/h3[1]").click()
