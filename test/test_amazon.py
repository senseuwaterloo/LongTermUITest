import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestAmazon:
    def test_amazon_1c6bfd10(self):
        self.driver.get("https://www.amazon.com/")
        self.driver.find_element(By.XPATH, "//a[@id='nav-hamburger-menu']/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hmenu-content']/ul[1]/li[3]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='hmenu-content']/ul[3]/li[12]/a").click()
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("roman empire history")
        self.driver.find_element(By.ID, "nav-search-submit-button").click()
        self.driver.find_element(By.XPATH, "//li[@id='n/154606011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_feature_nine_browse-bin/3291437011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='p_n_date/1249101011']/span[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(@id, 'a-autoid-') and contains(@id, '-announce')]/span[2]").click()
        self.driver.find_element(By.ID, "s-result-sort-select_4").click()

        self.driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a/div/img").click()
        self.driver.find_element(By.ID, "wishListMainButton").click()
