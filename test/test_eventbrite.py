import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestEventbrite:
    def test_eventbrite_ee22220c(self):
        self.driver.get("https://www.eventbrite.com/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div/div[1]/header/nav/div/div[3]/ul[1]/li[1]/a").click()

        self.driver.find_element(By.ID, "search-autocomplete-input").clear()
        self.driver.find_element(By.ID, "search-autocomplete-input").send_keys("pet festival")

        self.driver.find_element(By.ID, "location-autocomplete").clear()
        self.driver.find_element(By.ID, "location-autocomplete").send_keys("portland")
        self.driver.find_element(By.XPATH, "//div[@data-spec='eds-list-item-contents' and contains(., 'Portland') and contains(., 'OR, USA')]").click()

        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/header/nav/div/div[2]/div/span/div[3]/div/button").click()

        self.driver.find_element(By.XPATH, "//div[@id='view-more-category']/button").click()
        self.driver.find_element(By.XPATH, "//a[contains(@data-testid, 'category-filter-EventbriteCategory') and contains(., 'Home & Lifestyle')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Pets & Animals']").click()

        self.driver.find_element(By.XPATH, "//span[text()='This weekend' and contains(@class, 'ChoiceListItem_label')]").click()

        self.driver.find_element(By.XPATH, "//span[text()='Free' and contains(@class, 'ChoiceListItem_label')]").click()

        self.driver.find_element(By.XPATH, "//span[text()='Festival']").click()

        self.driver.find_element(By.XPATH, "//span[text()='English' and contains(@class, 'ChoiceListItem_label')]").click()
