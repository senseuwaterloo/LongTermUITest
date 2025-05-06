import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestShoppingGoogle:
    def test_shoppinggoogle_7349981f(self):
        self.driver.get("https://shopping.google.com/")

        self.driver.find_element(By.ID, "REsRA").clear()
        self.driver.find_element(By.ID, "REsRA").send_keys("computer monitor")

        self.driver.find_element(By.XPATH, "//span[text()='computer monitor' and not(./b)]").click()

        self.driver.find_element(By.XPATH, "//span[@title='Available nearby']").click()
        self.driver.find_element(By.XPATH, "//span[@title='Samsung']").click()
        self.driver.find_element(By.XPATH, "//span[@title='LG']").click()

        self.driver.find_element(By.XPATH, "//span[@title='4K']").click()
        self.driver.find_element(By.XPATH, "//span[@title='IPS Panel']").click()

        self.driver.find_element(By.XPATH, "//div[text()='Sort by: Relevance']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Review score']").click()
