import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestEventbrite:
    def test_eventbrite_ee22220c(self):
        # self.driver.get("https://www.eventbrite.com/")
        # self.driver.find_element(By.XPATH, "//header[@id='global-header']/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div/div[1]/header/nav/div/div[3]/ul[1]/li[1]/a").click()

        self.driver.find_element(By.ID, "search-autocomplete-input").clear()
        self.driver.find_element(By.ID, "search-autocomplete-input").send_keys("pet festival")

        self.driver.find_element(By.ID, "location-autocomplete").clear()
        self.driver.find_element(By.ID, "location-autocomplete").send_keys("portland")
        self.driver.find_element(By.XPATH, "//div[@data-spec='eds-list-item-contents' and contains(., 'Portland') and contains(., 'OR, USA')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='edsModalContentChildren']/div[1]/main[1]/header[1]/div[1]/form[1]/div[1]/div[1]/div[1]/span[2]/span[1]/button[1]/i[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/header/nav/div/div[2]/div/span/div[3]/div/button").click()

        # free pet festivals don't exist, so will just select the filters
        self.driver.find_element(By.XPATH, "//div[@id='view-more-category']/button").click()
        self.driver.find_element(By.XPATH, "//a[contains(@data-testid, 'category-filter-EventbriteCategory') and contains(., 'Home & Lifestyle')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Pets & Animals']").click()

        self.driver.find_element(By.XPATH, "//span[text()='This weekend' and contains(@class, 'ChoiceListItem_label')]").click()

        self.driver.find_element(By.XPATH, "//span[text()='Free' and contains(@class, 'ChoiceListItem_label')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='View more Format']/div[3]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Festival']").click()

        self.driver.find_element(By.XPATH, "//span[text()='English' and contains(@class, 'ChoiceListItem_label')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='View more Language']/div[1]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='View more Price']/div[1]/li[1]/label[1]/span[1]/div[1]/label[1]").click()
        # self.driver.find_element(By.ID, "locationPicker").clear()
        # self.driver.find_element(By.ID, "locationPicker").send_keys("portland")
        # self.driver.find_element(By.XPATH, "//li[@id='ChIJJ3SpfQsLlVQRkYXR9ua5Nhw']/div[1]/button[1]/div[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='View more Date']/div[4]/li[1]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='View more Date']/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[7]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='View more Date']/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]/div[1]/div[2]").click()
        # self.driver.find_element(By.ID, "eventbrite-widget-modal-trigger-559262147137").click()
        # self.driver.find_element(By.ID, "ticket-quantity-selector-931865299").clear()
        # self.driver.find_element(By.ID, "ticket-quantity-selector-931865299").select("2")
        # self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]").click()
