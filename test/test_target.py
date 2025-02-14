import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestTarget:
    def test_target_274571ea(self):
        # self.driver.get("https://www.target.com/")

        # self.driver.find_element(By.XPATH, "//button[@id='web-store-id-msg-btn']/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//button[@id='web-store-id-msg-btn']/div[1]/span[1]").click()

        self.driver.find_element(By.ID, "zip-or-city-state").clear()
        self.driver.find_element(By.ID, "zip-or-city-state").send_keys("25504")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Look up')]").click()
        self.driver.find_element(By.XPATH, "//h4[contains(.,'Barboursville')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'More info')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'More info') and @aria-label='More info about Barboursville store']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[1]/div[2]/div[1]/div[3]/button[2]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Shop this store']").click()

        # self.driver.find_element(By.XPATH, "//nav[@id='headerPrimary']/a[1]/span[1]/div[1]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[13]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/div[2]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[5]/a[1]/div[1]/div[2]/span[1]").click()
        # since it's not easter now, easter egg is not in the dropdown menu now, so search for easter egg instead
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("Easter Eggs")
        self.driver.find_element(By.ID, "search").send_keys(Keys.RETURN)

        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test='@web/SlotRenderer']//button[@data-test='facet-button-Type']").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[24]/div[1]/div[1]/div[2]/div[4]/div[1]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Fillable Eggs' and ./parent::span]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Prefilled Eggs' and ./parent::span]").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[24]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Apply']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@data-test='@web/SlotRenderer']//button[@data-test='facet-button-Price']").click()

        # self.driver.find_element(By.ID, "minPriceValue").clear()
        # self.driver.find_element(By.ID, "minPriceValue").send_keys("5")
        # self.driver.find_element(By.ID, "maxPriceValue").clear()
        # self.driver.find_element(By.ID, "maxPriceValue").send_keys("10")
        self.driver.find_element(By.XPATH, "//span[contains(text(), '$5 ') and contains(text(), '–') and contains(text(), ' $9.99') and ./parent::span]").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[25]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Apply']").click()

        # omit the material filter since only one result is returned from above
        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/button[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/div[27]/div[1]/div[1]/div[2]/div[3]/div[1]/label[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/div[27]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[8]/button[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/div[31]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/div[31]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/h2[1]").click()
        # self.driver.find_element(By.ID, "addToCartButtonOrTextIdFor83429711").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'View cart & check out')]").click()
        # click on shipping instead of pickup since it is not available for pick up
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@data-test='@web/SlotRenderer']//span[@data-test='facetHeading' and text()='Shipping']").click()
        self.driver.find_element(By.XPATH, "//div[@data-module-type='ProductListGrid']//section[@class]/div[1]/div[1]//button[contains(@id, 'addToCartButtonOrTextIdFor')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    