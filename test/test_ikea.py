import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestIkea:
    
    # def test_ikea_b0bb4740(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Location')]").click()
    #     self.driver.find_element(By.ID, "google-maps-store-select").clear()
    #     self.driver.find_element(By.ID, "google-maps-store-select").select("Tempe, AZ")
    #     self.driver.find_element(By.XPATH, "//div[@id='local-store']/div[1]/div[1]/div[2]/div[4]/div[1]/button[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='local-store']/div[1]/div[1]/div[2]/div[4]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='e3095a30-482a-11ec-947f-d76a3ef77dbc']/pub-hide-empty-link[1]/div[1]/a[1]/span[1]/span[1]").click()
    #
    # def test_ikea_ccb397da(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rooms')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/aside[1]/div[3]/nav[4]/ul[1]/li[1]/a[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='45e221e0-357b-11ec-a8f6-0b949a082dfb']/div[1]/div[1]/div[1]/nav[1]/a[5]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/button[22]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='sort']/div[1]/button[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='SEC_sort']/fieldset[1]/label[5]/span[2]/input[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='sort']/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='MATERIAL']/div[1]/button[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='filter-MATERIAL']/label[3]/span[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='switchname' and @value='on' and @type='checkbox']").click()
    #     self.driver.find_element(By.ID, "plp-compact-compare-checkbox-30492275").click()
    #     self.driver.find_element(By.ID, "plp-compact-compare-checkbox-80485338").click()
    #     self.driver.find_element(By.ID, "plp-compact-compare-checkbox-30500893").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='plp-comparison-bar']/div[2]/button[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Show only differences')]").click()
    #
    # def test_ikea_d78e3aac(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Design')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='showrooms']/div[3]/div[2]/div[1]/div[1]/div[2]/p[1]").click()
    #
    # def test_ikea_f118238f(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Products')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Lighting')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Decorative lighting')]").click()
    #     self.driver.find_element(By.XPATH, "//img[@alt='LED candles']").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/span[2]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pip-buy-module-content']/div[6]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]").click()
    #
    # def test_ikea_ff173880(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Products')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Home décor')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Mirrors')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Wall mirrors')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/button[17]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRICE']/div[1]/button[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='filter-PRICE']/label[1]/span[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'View')]").click()
    
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
    
    # def test_ikea_6b4aa5a9(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Products')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Beds & mattresses')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Mattresses')]").click()
    #     self.driver.find_element(By.XPATH, "//img[@alt='Foam and memory foam mattresses']").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Price: low to high')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='filter-REFERENCE_MEASUREMENTS']/label[3]/span[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/span[2]/img[1]").click()
    #
    # def test_ikea_6ca55141(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.ID, "ikea-search-input").clear()
    #     self.driver.find_element(By.ID, "ikea-search-input").send_keys("mirror")
    #     self.driver.find_element(By.ID, "search-box__searchbutton").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Columbus')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by ZIP code or city, state']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by ZIP code or city, state']").send_keys("atlanta georgia")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/nav[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='geo-market']/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[21]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='sort']/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='SEC_sort']/fieldset[1]/label[2]/span[2]/input[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='sort']/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='SHAPES']/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='filter-SHAPES']/label[2]/span[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='SHAPES']/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[5]/label[1]/span[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRICE']/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='filter-PRICE']/label[1]/span[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/button[1]/span[1]").click()
    #
    # def test_ikea_479bdc82(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Deals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Home Essentials Under $20')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='local-plp']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button[3]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='local-plp']/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/button[3]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='local-plp']/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/button[3]").click()
    #
    # def test_ikea_577ac962(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Customer Service')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='873a51f2-8d6d-11eb-88f1-81af06ac936f']/div[1]/div[4]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Read more')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='3c781e70-f0d8-11ec-b37b-3f5a40425fb5']/pub-hide-empty-link[1]/div[1]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "search-field").clear()
    #     self.driver.find_element(By.ID, "search-field").send_keys("105307")
    #     self.driver.find_element(By.XPATH, "//div[@id='gatsby-focus-wrapper']/div[2]/div[1]/ul[1]/li[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='gatsby-focus-wrapper']/div[2]/div[1]/ul[1]/li[1]/div[2]/div[1]/div[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='gatsby-focus-wrapper']/div[2]/div[1]/ul[1]/li[1]/div[2]/div[1]/div[1]/select[1]").select("2")
    #     self.driver.find_element(By.XPATH, "//div[@id='gatsby-focus-wrapper']/div[2]/div[1]/ul[1]/li[1]/div[2]/div[1]/button[1]/span[1]/span[1]").click()
    #
    # def test_ikea_60383804(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Marketplace')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by Color')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop red')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/button[4]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='filter-CATEGORIES']/label[5]/span[2]/span[1]").click()
    #
    # def test_ikea_618dbd1f(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Deals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Limited Time Offers')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/button[6]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/ul[1]/li[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'+ 11 more')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Furniture sets')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Outdoor dining sets')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/header[1]/div[1]/div[1]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='one-checkout']/main[1]/div[1]/div[1]/div[1]/div[23]/div[1]/div[3]/button[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='one-checkout']/main[1]/div[1]/div[1]/div[1]/div[9]/div[4]/div[1]/div[2]/div[1]/div[1]/button[2]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='CLICK_COLLECT_STORE_STANDARD_TRUCK']/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='920e6d67-94cc-4d39-8275-e7119e918d26']/button[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='CLICK_COLLECT_STORE_STANDARD_TRUCK']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
    #
    # def test_ikea_1d0dcb84(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Products')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bathroom')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bathroom storage')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by ZIP code or city, state']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by ZIP code or city, state']").send_keys("60173")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/nav[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='geo-market']/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "zip").clear()
    #     self.driver.find_element(By.ID, "zip").send_keys("60173")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Update ZIP code')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='a8edcce0-14e0-11ed-bbc8-536417f518da']/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/button[4]").click()
    #     self.driver.find_element(By.ID, "gray").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/button[3]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='filter-MATERIAL']/label[1]/span[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//fieldset[@id='filter-MATERIAL']/label[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
    #     self.driver.find_element(By.NAME, "radioname").click()
    #
    # def test_ikea_2d4b44c7(self):
    #     # self.driver.get("https://ikea.com")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Columbus')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by ZIP code or city, state']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search by ZIP code or city, state']").send_keys("11231")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]/div[1]/nav[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='geo-market']/span[1]").click()
    