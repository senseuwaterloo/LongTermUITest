import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element, scroll_down


@pytest.mark.usefixtures("setup_class")
class TestExtraspace:
    
    # def test_extraspace_69abd425(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").send_keys("birmingham")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='2507_1937']/div[1]/a[1]/div[1]/div[1]").click()
    #
    # def test_extraspace_6b2acd86(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'RV Storage')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Storage Near You')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/label[3]/span[2]").click()
    #
    # def test_extraspace_6c86186f(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").send_keys("New York")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "3").click()
    #     self.driver.find_element(By.ID, "0").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/a[1]/div[1]").click()
    #
    # def test_extraspace_6cb93639(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Packing Supplies')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'ORDER ONLINE')]").click()
    #     self.driver.find_element(By.ID, "head_grdCategories_lnkCategories_3").click()
    #     self.driver.find_element(By.ID, "head_grdProducts_hypurl2_0").click()
    #     self.driver.find_element(By.ID, "head_txtQuantity").clear()
    #     self.driver.find_element(By.ID, "head_txtQuantity").send_keys("2")
    #     self.driver.find_element(By.ID, "head_lnkAddToCart").click()
    #     self.driver.find_element(By.ID, "head_btnContinueShoppingDown").click()
    #
    # def test_extraspace_89150730(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").send_keys("atlanta")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "1").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "1").click()
    #     self.driver.find_element(By.ID, "2").click()
    #     self.driver.find_element(By.ID, "0").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    #     self.driver.find_element(By.ID, "searchButton").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-2']/div[1]/div[2]/div[3]/button[1]").click()
    #
    # def test_extraspace_8add2f40(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").send_keys("32541")
    #     self.driver.find_element(By.XPATH, "//input[@value='32541' and @placeholder='Enter Zip, City, or State']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='32541' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='32541' and @placeholder='Enter Zip, City, or State']").send_keys("32541")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "searchButton").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/label[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-1']/a[1]/div[2]/span[2]").click()
    #
    # def test_extraspace_dad2eaae(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Employment')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search All Jobs')]").click()
    #
    # def test_extraspace_e4a29d60(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vehicle Storage')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.ID, "react-select-years-option-3").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "react-select-makes-option-4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.ID, "react-select-models-option-12").click()
    #     self.driver.find_element(By.ID, "vehicle-size-estimator-submit-btn").click()
    #
    # def test_extraspace_e5c83ccd(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Packing Supplies')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'ORDER ONLINE')]").click()
    #     self.driver.find_element(By.ID, "head_grdCategories_lnkCategories_0").click()
    #     self.driver.find_element(By.ID, "head_grdProducts_btnAdd2_1").click()
    #     self.driver.find_element(By.ID, "head_btnContinueShoppingDown").click()
    #
    # def test_extraspace_f82b4d57(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='atlanta' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='atlanta' and @placeholder='Enter Zip, City, or State']").send_keys("90028")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/a[1]/div[2]/div[1]/div[1]/span[2]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='11842_7291']/div[1]/div[4]/button[1]").click()
    
    def test_extraspace_8fb3e11e(self):
        # self.driver.get("https://extraspace.com")
        # logic changed
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").send_keys("colorado springs")

        # self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @data-qa='navbar-search-button']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/div/main/div[3]/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/div/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/label[1]").click()

        # the cookie window will intercept the click of this checkbox, and the close button of the cookie window is in a shadow dom... need to scroll to an element below it...
        # scroll_to_element(self.driver, self.driver.find_element(By.XPATH, "//label[text()='RV Parking']"))
        # need to scroll down for a specific distance since scroll to element is not working
        scroll_down(self.driver, 500)
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted:
        time.sleep(2)
        enclosed_driver_up_checkbox = self.driver.find_element(By.XPATH, "//label[text()='Enclosed Drive-Up']")
        enclosed_driver_up_checkbox.click()

        # self.driver.find_element(By.XPATH, "//label[text()='Outdoor Covered']").click()
        # self.driver.find_element(By.XPATH, "//label[text()='Outdoor Uncovered']").click()
        # self.driver.find_element(By.XPATH, "//label[text()='RV Parking']").click()

        self.driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/div/main/div[3]/div[2]/div[1]/div[1]/div[3]/div/div/div/div[1]/div/div/div/div[2]/div[3]/a").click()
        self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/div/div/a/div[1]/img").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
        # self.driver.find_element(By.ID, "1").click()
        # self.driver.find_element(By.ID, "2").click()
        # self.driver.find_element(By.ID, "3").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.ID, "searchButton").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[5]").click()
        # self.driver.find_element(By.ID, "4").click()
        # self.driver.find_element(By.ID, "0").click()
        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-2']/div[1]/div[1]/div[1]/ul[1]/li[2]").click()
    
    # def test_extraspace_9118212c(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='32541' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='32541' and @placeholder='Enter Zip, City, or State']").send_keys("32541")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "1").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/label[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/a[1]/div[1]/span[1]/img[1]").click()
    #
    # def test_extraspace_37ced294(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").send_keys("60538")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "1").click()
    #     self.driver.find_element(By.ID, "2").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
    #
    # def test_extraspace_3ddb35d1(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='90028' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='90028' and @placeholder='Enter Zip, City, or State']").send_keys("10019")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/a[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
    #
    # def test_extraspace_4f811227(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='michigan' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='michigan' and @placeholder='Enter Zip, City, or State']").send_keys("Michigan")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/label[1]").click()
    #     self.driver.find_element(By.ID, "searchButton").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[12]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/div[1]/div[2]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'RENT NOW!')]").click()
    #
    # def test_extraspace_00eace8c(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").send_keys("Berkley Ca")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/label[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/a[1]/div[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[4]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='facility-details-container']/div[1]/h3[7]").click()
    #
    # def test_extraspace_18c84c8e(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Enter Zip, City, or State']").send_keys("Chicago")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "4").click()
    #     self.driver.find_element(By.ID, "0").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/div[1]/div[1]").click()
    #
    # def test_extraspace_35563fe5(self):
    #     # self.driver.get("https://extraspace.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/header[1]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='state-District of Columbia']/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='state-District of Columbia']/div[2]/div[2]/div[1]/div[1]/div[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Elevator Access Storage in Washington')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maplist-location-card-0']/div[1]/div[1]/img[1]").click()
    