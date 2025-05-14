import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestTarget:
    def test_target_274571ea(self):
        self.driver.get("https://www.target.com/")

        self.driver.find_element(By.XPATH, "//button[@id='web-store-id-msg-btn']/div[1]/span[1]").click()

        self.driver.find_element(By.ID, "zip-or-city-state").clear()
        self.driver.find_element(By.ID, "zip-or-city-state").send_keys("25504")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Look up')]").click()
        self.driver.find_element(By.XPATH, "//h4[contains(.,'Barboursville')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'More info') and @aria-label='More info about Barboursville store']").click()

        self.driver.find_element(By.XPATH, "//button[text()='Shop this store']").click()

        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("Easter Eggs")
        self.driver.find_element(By.ID, "search").send_keys(Keys.RETURN)

        self.driver.find_element(By.XPATH, "//div[@data-test='@web/SlotRenderer']//button[@data-test='facet-button-Type']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Fillable Eggs' and ./parent::span]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Prefilled Eggs' and ./parent::span]").click()

        self.driver.find_element(By.XPATH, "//button[text()='Apply']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@data-test='@web/SlotRenderer']//button[@data-test='facet-button-Price']").click()

        self.driver.find_element(By.XPATH, "//span[contains(text(), '$5 ') and contains(text(), '–') and contains(text(), ' $9.99') and ./parent::span]").click()

        self.driver.find_element(By.XPATH, "//button[text()='Apply']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@data-test='@web/SlotRenderer']//span[@data-test='facetHeading' and text()='Shipping']").click()
        self.driver.find_element(By.XPATH, "//div[@data-module-type='ProductListGrid']//section[@class]/div[1]/div[1]//button[contains(@id, 'addToCartButtonOrTextIdFor')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    