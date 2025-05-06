import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestRedfin:
    def test_redfin_3e4283d1(self):
        self.driver.get("https://www.redfin.com/")

        self.driver.find_element(By.XPATH, "//a[text()='Rent' and @role='tab']").click()

        self.driver.find_element(By.ID, "search-box-input").clear()
        self.driver.find_element(By.ID, "search-box-input").send_keys("Koreatown, Los Angeles")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Wilshire Center-Koreatown')]").click()

        self.driver.find_element(By.XPATH, "//p[text()='Beds/baths']").click()

        self.driver.find_element(By.XPATH, "//div[@aria-label='Number of bedrooms']/div[@role='cell' and @data-text='2']").click()

        self.driver.find_element(By.XPATH, "//span[@data-dd-action-name='bedsAndBaths_doneBtn']/button").click()

        self.driver.find_element(By.XPATH, "//p[text()='Price']").click()

        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").send_keys("3000")

        self.driver.find_element(By.XPATH, "//span[@data-dd-action-name='price_doneBtn']/button").click()

        sort_dropdown = self.driver.find_element(By.XPATH, "//select[@class='Select__nativeSelect' and @role='combobox']")
        sort_select = Select(sort_dropdown)
        sort_select.select_by_value("list_price_asc")

        self.driver.find_element(By.XPATH, "//div[@id='MapHomeCard_0']/div/div/div[1]/div").click()
