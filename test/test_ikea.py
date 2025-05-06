import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestIkea:
    def test_ikea_813e47ec(self):
        self.driver.get("https://www.ikea.com/us/en/")

        self.driver.find_element(By.XPATH, "//span[contains(text(),'Kitchenware & tableware')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Flatware & cutlery')]").click()

        self.driver.find_element(By.XPATH, "//div[@id='geo-ingka-navigation-desktop']/div[1]/div[1]/div/span").click()

        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by ZIP code or city, state']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by ZIP code or city, state']").send_keys("san diego")

        self.driver.find_element(By.XPATH, "//div[@id='geo-ingka-navigation-desktop']/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/button/span").click()

        self.driver.find_element(By.XPATH, "//button[@id='geo-market' and @aria-label='Set San Diego as my store and close modal']/span[1]/span[1]").click()

        self.driver.find_element(By.XPATH, "//span[text()='Flatware']").click()

        self.driver.find_element(By.XPATH, "//button[.//span[text()='All filters']]").click()

        self.driver.find_element(By.XPATH, "//li[@id='sort']/div[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='SEC_sort']/div/fieldset/label[2]/span[2]").click()

        self.driver.find_element(By.XPATH, "//li[@id='sort']/div[1]/button[1]").click()

        self.driver.find_element(By.XPATH, "//input[@id='plp-AVAILABLE_IN_STORE']/following-sibling::span").click()

        self.driver.find_element(By.XPATH, "//li[@id='MATERIAL']/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='filter-MATERIAL']/label[1]/span[2]/span[1]").click()

        self.driver.find_element(By.XPATH, "//li[@id='TYPE']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='filter-TYPE']/label[2]/span[2]/span[1]").click()

        self.driver.find_element(By.XPATH, "//button[@type='button' and @aria-label='Close']/span").click()
