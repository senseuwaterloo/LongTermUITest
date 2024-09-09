import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestUnderarmour:
    
    # def test_underarmour_f9a882f7(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/header[1]/div[2]/nav[1]/ul[1]/li[6]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shoes')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Unisex')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/h2[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shoes')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Athletic Shoes')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/main[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[7]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'5.5')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='product-list-sorting']/span[1]").click()
    #     self.driver.find_element(By.ID, "product-list-sorting-option-price-low-high").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Unisex Curry Flow Go Running Shoes')]").click()
    #     self.driver.find_element(By.ID, "native-submit").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View Bag & Checkout')]").click()
    #
    # def test_underarmour_18fc60d7(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "gc-recipient-name").clear()
    #     self.driver.find_element(By.ID, "gc-recipient-name").send_keys("John")
    #     self.driver.find_element(By.ID, "gc-recipient-email").clear()
    #     self.driver.find_element(By.ID, "gc-recipient-email").send_keys("abc@test.com")
    #     self.driver.find_element(By.ID, "gc-from").clear()
    #     self.driver.find_element(By.ID, "gc-from").send_keys("buckeye.foobar@gmail.com")
    #     self.driver.find_element(By.ID, "gc-amount").clear()
    #     self.driver.find_element(By.ID, "gc-amount").send_keys("100")
    #     self.driver.find_element(By.ID, "gc-message").click()
    #     self.driver.find_element(By.ID, "gc-message").clear()
    #     self.driver.find_element(By.ID, "gc-message").send_keys("gift card")
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]").click()
    #
    # def test_underarmour_774f0c2f(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'SHOP NOW')]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='Amount-2']/li[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@role='button' and @title='Select color Red']").click()
    #     self.driver.find_element(By.ID, "quantity-1").clear()
    #     self.driver.find_element(By.ID, "quantity-1").select("5")
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[3]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View Bag & Check Out')]").click()
    #     self.driver.find_element(By.ID, "couponCode").clear()
    #     self.driver.find_element(By.ID, "couponCode").send_keys("100OFF")
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/button[1]/span[1]").click()
    #
    # def test_underarmour_afcc3ff5(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Store Locator')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'New York')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'New York')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Store Details')]").click()
    #
    # def test_underarmour_73cf6eec(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//input[@name='hpEmailSignUp' and @type='email']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='hpEmailSignUp' and @type='email']").send_keys("larryknox@gmail.com")
    #     self.driver.find_element(By.XPATH, "//footer[@id='footercontent']/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
    
    def test_underarmour_90bd64ec(self):
        # self.driver.get("https://www.underarmour.com/en-us/")
        # self.driver.find_element(By.XPATH, "//a[@id='kids']/span[1]").click()
        kids_menu_button = self.driver.find_element(By.XPATH, "//a[@data-testid='nav-link-kids']").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element(kids_menu_button).perform()

        # self.driver.find_element(By.ID, "girls-clothing-bottoms").click()
        self.driver.find_element(By.XPATH, "//div[@id='kids']//a[text()='Pants & Leggings' and contains(@href, 'girls')]").click()

        if self.driver.find_element(By.XPATH, "//dialog[@data-testid='user-action-modal']//button[@data-testid='dialog-close-button']") is not None:
            self.driver.find_element(By.XPATH, "//dialog[@data-testid='user-action-modal']//button[@data-testid='dialog-close-button']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//h3[@data-testid='refinement-option' and text()='Sports']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Training')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//a[text()='Training' and @title='Refine by sports: Training']").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//h3[@data-testid='refinement-option' and contains(text(), 'Sports')]").click()

        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//h3[@data-testid='refinement-option' and text()='Size']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'YXL')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//a[text()='YXL' and @title='Refine by size: YXL']").click()
        # need to wait for a few seconds to let the page refreshed otherwise the following action will not be executed but code will pass and will result in element click intercepted for clicking Fit
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//h3[@data-testid='refinement-option' and contains(text(), 'Size')]").click()

        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]").click()

        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Fitted')]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//h3[@data-testid='refinement-option' and text()='Fit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//a[text()='Fitted' and @title='Refine by fit: Fitted']").click()

        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[6]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Now Trending']").click()
        self.driver.find_element(By.ID, "product-list-sorting-option-newest").click()

        # need to wait for a few seconds for the list to be refreshed so that correct items will be selected
        time.sleep(2)

        # self.driver.find_element(By.XPATH, "//section[@id='1377112']/div[1]/div[1]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//section[@id='1373955']/div[1]/div[1]/div[1]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//section[@id='1373950']/div[1]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'products_list ProductGrid_product-listing__')]/div[1]//div[contains(@class, 'ProductTile_wishlist-toggle__')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'products_list ProductGrid_product-listing__')]/div[2]//div[contains(@class, 'ProductTile_wishlist-toggle__')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'products_list ProductGrid_product-listing__')]/div[3]//div[contains(@class, 'ProductTile_wishlist-toggle__')]").click()
        time.sleep(1)

    
    # def test_underarmour_cdd64586(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[@id='new-arrivals-nav-item']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Womens')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Accessories')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Women's UA Radar Batting Gloves\")]").click()
    #
    # def test_underarmour_eb609e15(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[@id='outlet']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Girls')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Jackets')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Clothing')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Jackets')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Outdoor')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'YMD')]").click()
    #
    # def test_underarmour_ccb7c231(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[@id='men']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shirts & Tops')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Graphic T-shirts')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Football')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Men's UA Football All Over Print Metal Logo Short Sleeve\")]").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='button']").click()
    #
    # def test_underarmour_6e98e331(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[@id='women']/span[1]").click()
    #     self.driver.find_element(By.ID, "women-sport-golf").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Clothing')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Polos')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'M')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[3]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='1377338']/div[1]/div[1]/div[1]/button[1]/span[1]").click()
    #
    # def test_underarmour_46a3683f(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[@id='outlet']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Mens')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Clothing')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Short Sleeves')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[8]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'XL')]").click()
    #     self.driver.find_element(By.XPATH, "//img[@title=\"Men's UA Tech™ 2.0 Short Sleeve, Green\"]").click()
    #     self.driver.find_element(By.XPATH, "//a[@role='button' and @title='Select size XL']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[8]/div[2]/div[6]/div[2]/div[1]/div[1]/button[1]").click()
    #
    # def test_underarmour_6407babe(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[@id='men']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shoes')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Running')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'9')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[3]").click()
    #     self.driver.find_element(By.XPATH, "//img[@title=\"Men's UA Surge 3 Running Shoes, Blue\"]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='size-2']/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[8]/div[2]/div[4]/div[2]/div[1]/div[1]/button[1]").click()
    #
    # def test_underarmour_5e47dc3e(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[@id='women']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports Bras')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'S')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='refinement-size']/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@title='Refine by color: Purple']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[6]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'High Support')]").click()
    #
    # def test_underarmour_ebae9339(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[@id='kids']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shoes')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@title='Refine by color: Black']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'9K')]").click()
    #     self.driver.find_element(By.XPATH, "//img[@title=\"Boys' Infant UA Surge 3 AC Running Shoes, Black\"]").click()
    #
    # def test_underarmour_35cf31d3(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[@id='women']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sports Bras')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@title='Refine by color: Black']").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='1373826']/div[1]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='1374379']/div[1]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='1361034']/div[1]/div[1]/div[1]/button[1]/span[1]").click()
    #
    # def test_underarmour_440273fa(self):
    #     # self.driver.get("https://www.underarmour.com/en-us/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Size Guide')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[1]/div[2]/ul[2]/li[2]/a[1]/span[1]").click()
    