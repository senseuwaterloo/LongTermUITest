import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestCookpad:
    
    def test_cookpad_ceac063d(self):
        # self.driver.get("https://cookpad.com")
        #TODO to run this test after the anti-robot time.sleep(100)
        # changed the locators in this  test case
        self.driver.find_element(By.ID, "navigation_search").clear()
        self.driver.find_element(By.ID, "navigation_search").send_keys("pancake")
        self.driver.find_element(By.XPATH, "//button[@name='button' and @type='submit']").click()

        self.driver.find_element(By.ID, "search_excluded_ingredients").clear()
        self.driver.find_element(By.ID, "search_excluded_ingredients").send_keys("beetroot")
        self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[2]/div[2]/div/form/div[1]/div[3]/div/div[1]/div/div/div/div").click()
        self.driver.find_element(By.ID, "search_included_ingredients").clear()
        self.driver.find_element(By.ID, "search_included_ingredients").send_keys("wheat")
        self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[2]/div[2]/div/form/div[1]/div[2]/div/div[1]/div/div/div/div").click()
    
    # def test_cookpad_d7b3fa4b(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='tips_collection']/div[1]/a[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='tip_45628']/div[1]/div[2]/div[1]/ul[1]/li[2]/form[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='tip_45537']/div[1]/div[2]/div[1]/ul[1]/li[1]/form[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='tip_45268']/div[1]/div[2]/div[1]/ul[1]/li[1]/form[1]/button[1]/span[1]").click()
    #
    # def test_cookpad_e06945d3(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='top_navigation']/ul[1]/li[1]/a[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'We add 1 heaping tablespoon of peanut butter and red pepper flakes to taste!!')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@title='Add Reaction']").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'❤️')]").click()
    #
    # def test_cookpad_e424cce6(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").send_keys("gluten free chocolate chip cookies")
    #     self.driver.find_element(By.XPATH, "//input[@name='commit' and @value='Search' and @type='submit']").click()
    #     self.driver.find_element(By.ID, "search_excluded_ingredients").clear()
    #     self.driver.find_element(By.ID, "search_excluded_ingredients").send_keys("nuts")
    #     self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #
    # def test_cookpad_e4e234e6(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").send_keys("shrimp")
    #     self.driver.find_element(By.XPATH, "//input[@name='commit' and @value='Search' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Mediterranean shrimp pasta')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Print')]").click()
    #
    # def test_cookpad_efa53c36(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='top_navigation']/ul[1]/li[3]/a[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[1]/div[1]/div[3]/div[1]/form[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//h1[@role='textbox']").clear()
    #     self.driver.find_element(By.XPATH, "//h1[@role='textbox']").send_keys("Fry Onions faster")
    #     self.driver.find_element(By.XPATH, "//textarea[@placeholder=\"To dice an onion, use a chef's knife to cut the onion in half from the stem tip, to the bottom root.\"]").clear()
    #     self.driver.find_element(By.XPATH, "//textarea[@placeholder=\"To dice an onion, use a chef's knife to cut the onion in half from the stem tip, to the bottom root.\"]").send_keys("While frying onions adding salt will make it brown faster.")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    # def test_cookpad_efb0acb6(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='top_navigation']/ul[1]/li[2]/a[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "navigation_search").clear()
    #     self.driver.find_element(By.ID, "navigation_search").send_keys("Fried Bombay Duck")
    #     self.driver.find_element(By.XPATH, "//header[@id='header']/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Fried Bombay Duck')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='bookmark_recipe_15024649']/div[1]/span[2]/div[1]/span[1]/form[1]/button[1]/span[1]").click()
    #
    # def test_cookpad_f5da4b14(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").send_keys("hamburger")
    #     self.driver.find_element(By.XPATH, "//input[@name='commit' and @value='Search' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hamburger steak')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='bookmark_recipe_16727230']/div[1]/span[2]/div[1]/span[1]/form[1]/button[1]/span[1]").click()
    #
    # def test_cookpad_fe974654(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").send_keys("pad thai")
    #     self.driver.find_element(By.XPATH, "//input[@name='commit' and @value='Search' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Chicken Pad Thai')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Print')]").click()
    #
    # def test_cookpad_a498c980(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").send_keys("vegetable soup")
    #     self.driver.find_element(By.XPATH, "//input[@name='commit' and @value='Search' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Mom's 🥇Southern Style Green Beans and Potatoes Soup By (Jerr)\")]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='recipe']/div[1]/div[1]/div[10]/div[1]/a[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='follow_user_38839937']/div[1]/span[2]/form[1]/button[1]").click()
    #
    # def test_cookpad_b7f65d4e(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").send_keys("eggplant, mushrooms")
    #     self.driver.find_element(By.XPATH, "//input[@name='commit' and @value='Search' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'California Farm Eggplant Schnitzel in Mushroom Sauce')]").click()
    #
    # def test_cookpad_142ed7d3(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Get the App')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[1]/div[1]/a[2]/img[1]").click()
    #
    # def test_cookpad_297361ad(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").send_keys("chicken parmesan")
    #     self.driver.find_element(By.XPATH, "//input[@name='commit' and @value='Search' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sheet-Pan Chicken Parmesan')]").click()
    #     self.driver.find_element(By.ID, "comment_body").clear()
    #     self.driver.find_element(By.ID, "comment_body").send_keys("Can it be made in an air fryer?")
    #     self.driver.find_element(By.XPATH, "//form[@id='new_comment']/div[1]/button[1]/svg[1]/path[1]").click()
    #
    # def test_cookpad_321c79b1(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Dinner')]").click()
    #     self.driver.find_element(By.ID, "search_included_ingredients").clear()
    #     self.driver.find_element(By.ID, "search_included_ingredients").send_keys("lamb")
    #     self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #
    # def test_cookpad_3694f716(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='search_widget']/div[1]/input[1]").send_keys("chicken")
    #     self.driver.find_element(By.XPATH, "//input[@name='commit' and @value='Search' and @type='submit']").click()
    #     self.driver.find_element(By.ID, "search_excluded_ingredients").clear()
    #     self.driver.find_element(By.ID, "search_excluded_ingredients").send_keys("rice")
    #     self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #
    # def test_cookpad_516ae2e8(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'shrimp')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Orange shrimp skewers')]").click()
    #     self.driver.find_element(By.ID, "comment_body").clear()
    #     self.driver.find_element(By.ID, "comment_body").send_keys("It's good to use orange on shrimps!")
    #     self.driver.find_element(By.XPATH, "//div[@id='sidebar']/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='share-links']/li[4]/form[1]/button[1]/span[1]").click()
    #
    # def test_cookpad_8a1322fc(self):
    #     # self.driver.get("https://cookpad.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[2]/footer[1]/div[1]/div[1]/div[1]/div[2]/p[2]/a[6]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='global_feeds_suggested_feed_item_bmV3OjU4NTcwODYw']/div[1]/h1[1]/a[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[1]/div[1]/div[2]/a[1]/div[1]/div[1]/picture[1]/source[1]/source[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main_contents']/div[1]/section[1]/div[3]/div[2]/div[1]/a[1]/picture[1]/source[1]/source[1]/img[1]").click()
    