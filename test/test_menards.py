import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestMenards:
    def test_menards_24de7f7d(self):
        # self.driver.get("https://menards.com")
        # self.driver.find_element(By.XPATH, "//svg[@role='presentation']").click()
        self.driver.find_element(By.XPATH, "//button[@qubit-id='SelectStore']").click()

        # no corresponding action
        # self.driver.find_element(By.XPATH, "//button[@id='679bbee9-5f2c-4469-a6cf-f76711ccb188']/span[1]/svg[1]/path[1]").click()

        self.driver.find_element(By.ID, "header-zip-input").clear()
        self.driver.find_element(By.ID, "header-zip-input").send_keys("60538")

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Store Locator')]").click()
        self.driver.find_element(By.XPATH, "//a[@qubit-id='StoreLocator']").click()
        # 'https://menards.com': [(By.XPATH, "//div[@id='emailBanner']/div[2]/button[1]")],
        if self.driver.find_element(By.XPATH, "//div[@id='emailBanner']/div[2]/button[1]"):
            self.driver.find_element(By.XPATH, "//div[@id='emailBanner']/div[2]/button[1]").click()


        self.driver.find_element(By.ID, "zip-input").clear()
        self.driver.find_element(By.ID, "zip-input").send_keys("60538")
        self.driver.find_element(By.XPATH, "//button[@id='zip-submit']/i[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='store-locator-results']/ul[1]/li[1]/div[2]/div[1]/button[1]").click()

        # self.driver.find_element(By.XPATH, "//input[@name='search' and @type='text' and @placeholder='Enter SKU, Model # or Keyword']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='search' and @type='text' and @placeholder='Enter SKU, Model # or Keyword']").send_keys("Magtag electric dryer")
        # need to wait for several seconds, otherwise the input text will be refreshed by the page loading process
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//nav//input[@name='search' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//nav//input[@name='search' and @type='text' and @placeholder='Search']").send_keys("Magtag electric dryer")

        # self.driver.find_element(By.XPATH, "//div[@id='5593']/div[2]/form[1]/button[1]/small[1]").click()
        self.driver.find_element(By.XPATH, "//nav//button[@data-at-id='searchSubmitBtn']").click()

        # extra step to click on the category link since the capacity option will not display in the search page
        # self.driver.find_element(By.XPATH, "//a[contains(text(), '  Electric Dryers')]").click()

        # extra step to show available electric dryer in the store
        # StaleElementReferenceException: Element became stale: xpath = //label[@for='inStockToday'] - Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@for='inStockToday']").click()
        electric_dryer_link = self.driver.find_element(By.XPATH, "//label[@role='checkbox' and contains(text(), 'Electric Dryers')]")
        scroll_to_element(self.driver, electric_dryer_link)
        electric_dryer_link.click()

        # capacity selection not available in the search result page
        # self.driver.find_element(By.XPATH, "//div[@id='spec_capacity_facetfacetsBody']/div[1]/div[2]/div[1]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='spec_capacity_facetfacetsBody']/div[1]/div[3]/div[1]/label[1]").click()

        # self.driver.find_element(By.ID, "headerpriceFacets").click()
        # self.driver.find_element(By.XPATH, "//div[@id='pricefacets']/button[1]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.ID, "priceMin").clear()
        # self.driver.find_element(By.ID, "priceMin").send_keys("0")
        # self.driver.find_element(By.ID, "priceMax").clear()
        # self.driver.find_element(By.ID, "priceMax").send_keys("1000")
        self.driver.find_element(By.ID, "priceMin").clear()
        self.driver.find_element(By.ID, "priceMin").send_keys("0")
        self.driver.find_element(By.ID, "priceMax").clear()
        self.driver.find_element(By.ID, "priceMax").send_keys("1000")

        self.driver.find_element(By.XPATH, "//input[@value='GO' and @type='button']").click()
    