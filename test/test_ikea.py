import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestIkea:
    def test_ikea_813e47ec(self):
        # self.driver.get("https://ikea.com")
        # layout logic changed, no need for this click
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Products')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Kitchenware & tableware')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Kitchenware & tableware')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Flatware & cutlery')]").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Columbus')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='geo-ingka-navigation-desktop']/div[1]/div[1]/div/span").click()

        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by ZIP code or city, state']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by ZIP code or city, state']").send_keys("san diego")

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/nav[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='geo-ingka-navigation-desktop']/div[2]/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/button/span").click()

        # original locator will locate multiple "Select store" button we need to make sure it only locates the first one
        # self.driver.find_element(By.XPATH, "//button[@id='geo-market']/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='geo-market' and @aria-label='Set San Diego as my store and close modal']/span[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Flatware')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Flatware']").click()

        # filter logic changed also need to avoid absolute XPath
        # self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/button[13]").click()
        # element click intercepted: Element <span class="plp-pill__label">...</span> is not clickable at point (1635, 857). Other element would receive the click: <button aria-haspopup="true"
        # self.driver.find_element(By.XPATH, "//span[text()='All filters']").click()
        self.driver.find_element(By.XPATH, "//button[.//span[text()='All filters']]").click()

        # self.driver.find_element(By.XPATH, "//li[@id='sort']/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='sort']/div[1]/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='SEC_sort']/fieldset[1]/label[2]/span[2]/input[1]").click()
        # self.driver.find_element(By.ID, "plp-PRICE_LOW_TO_HIGH").click()
        # element not clickable and timeout when locating to the input element so try to locate to the span below the input
        # self.driver.find_element(By.XPATH, "//div[@id='SEC_sort']/div/fieldset/label[2]/span[2]/span").click()
        # click intercepted by the input however when locating to the span. So try the parent span of both the input and current span
        self.driver.find_element(By.XPATH, "//div[@id='SEC_sort']/div/fieldset/label[2]/span[2]").click()

        # self.driver.find_element(By.XPATH, "//li[@id='sort']/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='sort']/div[1]/button[1]").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[3]/label[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@id='plp-AVAILABLE_IN_STORE']/following-sibling::span").click()

        # self.driver.find_element(By.XPATH, "//li[@id='MATERIAL']/div[1]/button[1]/svg[1]/path[1]").click()
        # code passed but action not performed when locating to button so try to locate further to the span
        self.driver.find_element(By.XPATH, "//li[@id='MATERIAL']/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='filter-MATERIAL']/label[1]/span[2]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//li[@id='TYPE']/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='TYPE']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='filter-TYPE']/label[2]/span[2]/span[1]").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @aria-label='Close']/span").click()
