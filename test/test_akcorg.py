import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab, calculate_dates_slash_format, scroll_to_element


@pytest.mark.usefixtures("driver_session")
class TestAkcOrg:
    def test_akcorg_9d42f53a(self):
        self.driver.get("https://www.akc.org/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports & Events')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Event Search')]").click()
        switch_to_new_tab(self.driver)
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//span[contains(text(),'Search near City')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//form[@id='locationName']/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//form[@id='locationName']/input[1]").send_keys("brighton")
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//button[@class='dropdown-item']//span[strong[text()='Brighton'] and contains(text(), 'AL')]").click()
        dropdown_element = self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//select[@name='radius']")
        select = Select(dropdown_element)
        select.select_by_value('100')
        start_date_str, end_date_str = calculate_dates_slash_format(14, 379)

        calendar_element = self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateStart' and @placeholder='MM/DD/YYYY']")
        scroll_to_element(self.driver, calendar_element)
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateStart' and @placeholder='MM/DD/YYYY']").click()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateStart' and @placeholder='MM/DD/YYYY']").clear()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateStart' and @placeholder='MM/DD/YYYY']").send_keys(start_date_str)
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateEnd' and @placeholder='MM/DD/YYYY']").click()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateEnd' and @placeholder='MM/DD/YYYY']").clear()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[contains(@class, 'desktop-view') and @name='dateEnd' and @placeholder='MM/DD/YYYY']").send_keys(end_date_str)

        breed_element = self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//span[contains(text(),'Any AKC Recognized or FSS Breed')]")
        scroll_to_element(self.driver, breed_element)
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//span[contains(text(),'All-American Dogs')]").click()

        conformation_events_element = self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//div[contains(text(),'Conformation Events')]")
        scroll_to_element(self.driver, conformation_events_element)
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//div[contains(text(),'Companion Events')]").click()

        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//span[contains(text(),'Agility (AG)')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//span[contains(text(),'Obedience (O/SO/PO/LO)')]").click()

        submit_button = self.driver.find_element(By.XPATH, "//div[@class='desktop-view row']//input[@value='RETRIEVE EVENTS' and @type='button']")
        scroll_to_element(self.driver, submit_button)
        submit_button.click()
    