import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestDrugs:
    def test_drugs_bb78798e(self):
        self.driver.get("https://www.drugs.com/")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/ul[1]/li[2]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Agree and Continue')]").click()
        self.driver.find_element(By.ID, "livesearch-imprint").clear()
        self.driver.find_element(By.ID, "livesearch-imprint").send_keys("894 5")

        color_list = self.driver.find_element(By.ID, "color-select")
        color_select = Select(color_list)
        color_select.select_by_visible_text('Pink')

        shape_list = self.driver.find_element(By.ID, "shape-select")
        shape_select = Select(shape_list)
        shape_select.select_by_visible_text('Oval')

        self.driver.find_element(By.XPATH, "//button[@data-submit='Searching...' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View details')]").click()
