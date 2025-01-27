import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestEpicurious:
    
    # def test_epicurious_c9342d63(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("bread")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[3]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[9]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[4]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[5]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[2]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/ul[1]/li[2]/span[1]").click()
    #
    # def test_epicurious_d0a70037(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Go to Main Navigation')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Recipes & Menus')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vegetarian')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[7]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/div[3]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[4]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/ul[1]/li[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View Recipe')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/article[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]").click()
    
    def test_epicurious_d7fb2a4f(self):
        # self.driver.get("https://epicurious.com")
        # self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
        self.driver.find_element(By.ID, "search-form-text-field-q").click()

        # self.driver.find_element(By.ID, "inputTerms").clear()
        # self.driver.find_element(By.ID, "inputTerms").send_keys("CURRY")
        self.driver.find_element(By.ID, "search-form-text-field-q").clear()
        self.driver.find_element(By.ID, "search-form-text-field-q").send_keys("CURRY")

        # self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
        self.driver.find_element(By.ID, "search-form-text-field-q").send_keys(Keys.RETURN)

        # website logic changed, now can only filter dinner and south asian food
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[6]/h3[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[9]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[15]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h3[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/h3[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[9]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[28]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[2]/h3[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'react-select-') and contains(@id, '-placeholder') and text()='Popular']").click()

        # somehow clicking the label element in the div is not working
        # Just tried again, somehow seems fine now.
        self.driver.find_element(By.ID, "react-select-2-option-5").click() # somehow clicking the label element in the div is not working
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'react-select-') and contains(@id, '-placeholder') and text()='Cuisines & Flavors']").click()

        # somehow clicking the label element in the div is not working
        self.driver.find_element(By.ID, "react-select-4-option-7").click()
        # was using the following step to close the dropdown in case click interception happens, also seems unnecessary and fine now.
        # self.driver.find_element(By.XPATH, "//div[contains(@id, 'react-select-') and contains(@id, '-placeholder') and text()='Cuisines & Flavors']").click()
        self.driver.find_element(By.XPATH, "//div[@id='0-Recipes']/div[2]/section/div/div/div/div[1]/div[1]/div[1]/span").click()

    # def test_epicurious_dfdf6de1(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("chicken")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/ul[1]/li[3]/span[1]").click()
    #
    # def test_epicurious_158a1416(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("CHICKEN")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[2]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[4]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[6]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/ul[1]/li[5]/span[1]").click()
    #
    # def test_epicurious_6395ffd7(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("pasta")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[3]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[6]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/ul[1]/li[4]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/article[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]").click()
    #
    # def test_epicurious_8d5e6634(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("chicken soup")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[8]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[8]/div[1]/div[4]/label[1]").click()
    #
    # def test_epicurious_90b7a2d1(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("pizza")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[5]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[4]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[4]/label[1]").click()
    #
    # def test_epicurious_98e767b7(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("Halloween")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/ul[1]/li[3]/span[1]").click()
    #
    # def test_epicurious_9b9bc876(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("pie")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/ul[1]/li[3]/span[1]").click()
    #
    # def test_epicurious_b82327ff(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("burger")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/span[1]").click()
    #
    # def test_epicurious_c3902020(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Go to Main Navigation')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Expert Advice')]").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='essential-guides']/a[1]/h4[1]").click()
    #
    # def test_epicurious_39c7c4fc(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("vegan lasagna")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[2]/ul[1]/li[3]/span[1]").click()
    #
    # def test_epicurious_42d231a6(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//form[@action='https://www.epicurious.com/search/']").click()
    #     self.driver.find_element(By.ID, "inputTerms").clear()
    #     self.driver.find_element(By.ID, "inputTerms").send_keys("gluten-free dessert")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[2]/div[2]/div[1]/ul[1]/li[3]/span[1]").click()
    #
    # def test_epicurious_5ea87c71(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View “17 Easy Scone Recipes for a Bakery-Worthy Breakfast”')]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='6414b4d5abc0a6fbb90a3744']/div[1]/div[1]/figure[1]/figcaption[1]/div[1]/div[3]/div[2]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/article[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]").click()
    #
    # def test_epicurious_f7246831(self):
    #     # self.driver.get("https://epicurious.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Go to Main Navigation')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Recipes & Menus')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Gluten-Free')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='react-app']/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
    