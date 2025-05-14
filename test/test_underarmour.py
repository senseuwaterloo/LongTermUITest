import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestUnderarmour:
    def test_underarmour_90bd64ec(self):
        self.driver.get("https://www.underarmour.com/en-us/")

        kids_menu_button = self.driver.find_element(By.XPATH, "//a[@data-testid='nav-link-kids']").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element(kids_menu_button).perform()

        self.driver.find_element(By.XPATH, "//div[@id='kids']//a[text()='Pants & Leggings' and contains(@href, 'girls')]").click()

        if self.driver.find_element(By.XPATH, "//dialog[@data-testid='user-action-modal']//button[@data-testid='dialog-close-button']") is not None:
            self.driver.find_element(By.XPATH, "//dialog[@data-testid='user-action-modal']//button[@data-testid='dialog-close-button']").click()

        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//h3[@data-testid='refinement-option' and text()='Sports']").click()

        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//a[text()='Training' and @title='Refine by sports: Training']").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//h3[@data-testid='refinement-option' and contains(text(), 'Sports')]").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//h3[@data-testid='refinement-option' and text()='Size']").click()

        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//a[text()='YXL' and @title='Refine by size: YXL']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//h3[@data-testid='refinement-option' and contains(text(), 'Size')]").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//h3[@data-testid='refinement-option' and text()='Fit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-refinements']//a[text()='Fitted' and @title='Refine by fit: Fitted']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Now Trending']").click()
        self.driver.find_element(By.ID, "product-list-sorting-option-newest").click()

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[contains(@class, 'products_list ProductGrid_product-listing__')]/div[1]//div[contains(@class, 'ProductTile_wishlist-toggle__')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'products_list ProductGrid_product-listing__')]/div[2]//div[contains(@class, 'ProductTile_wishlist-toggle__')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'products_list ProductGrid_product-listing__')]/div[3]//div[contains(@class, 'ProductTile_wishlist-toggle__')]").click()
        time.sleep(1)
