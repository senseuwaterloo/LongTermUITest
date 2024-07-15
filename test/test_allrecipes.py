import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestAllrecipes:
    
    # def test_allrecipes_5d596e62(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Ingredients')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Beef')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='taxonomy-nodes__link_1-0-6']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='mntl-card-list-items_1-0']/div[2]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "mntl-recipe-review-bar__comment-count_1-0").click()
    #
    # def test_allrecipes_698f3edc(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'News')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Recalls')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='mntl-card-list-items_1-0']/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Share on Twitter']").click()
    #
    # def test_allrecipes_7e2030f7(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='header-nav_1-0']/div[1]/ul[1]/li[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'30-Minute Meals')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='mntl-save__link_1-0-1']/svg[1]/use[1]").click()
    #
    # def test_allrecipes_834828e1(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Meals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Lunch')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='taxonomy-nodes__link_1-0-3']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='mntl-card-list-items_2-0-2']/div[2]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "mntl-recipe-details__nutrition-link_1-0").click()
    
    def test_allrecipes_87db8a52(self):
        # self.driver.get("https://allrecipes.com")
        self.driver.find_element(By.XPATH, "//nav[@id='mntl-header-nav_1-0']//a[contains(text(),'Ingredients')]").click()
        self.driver.find_element(By.ID, "mntl-search-form--hero__search-input").click()
        self.driver.find_element(By.ID, "mntl-search-form--hero__search-input").clear()
        self.driver.find_element(By.ID, "mntl-search-form--hero__search-input").send_keys("cinnamon")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Click to search' and contains(text(),'GO')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='mntl-card-list-items_1-0']/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//button[@class='mm-recipes-social-share__share-button']/span").click()
    
    # def test_allrecipes_8b28a545(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Occasions')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Easter')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='taxonomy-nodes__link_1-0-3']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='mntl-card-list-items_2-0-1']/div[1]/div[1]/div[1]/img[1]").click()
    #
    # def test_allrecipes_c01036f5(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'News')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Trends')]").click()
    #
    # def test_allrecipes_ccb59263(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Kitchen Tips')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Air Fryer')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='card--featured_1-0']/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Share on Pinterest']").click()
    #
    # def test_allrecipes_d31b0344(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//nav[@id='header-nav_1-0']/div[1]/ul[1]/li[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'30-Minute Meals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='taxonomy-nodes__link_1-0-4']/span[1]").click()
    #
    # def test_allrecipes_d9605d02(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Kitchen Tips')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View All')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='taxonomy-nodes__link_1-0-4']/span[1]").click()
    #
    # def test_allrecipes_fa64e4d4(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Ingredients')]").click()
    #     self.driver.find_element(By.ID, "search-box__search-input").clear()
    #     self.driver.find_element(By.ID, "search-box__search-input").send_keys("pumpkin")
    #     self.driver.find_element(By.XPATH, "//div[@id='search-box_1-0']/form[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='mntl-card-list-items_1-0-6']/div[1]/div[1]/div[1]/img[1]").click()
    #
    # def test_allrecipes_03d4147d(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Ingredients')]").click()
    #     self.driver.find_element(By.ID, "search-box__search-input").clear()
    #     self.driver.find_element(By.ID, "search-box__search-input").send_keys("pork")
    #     self.driver.find_element(By.XPATH, "//div[@id='search-box_1-0']/form[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='mntl-card-list-items_1-0']/div[2]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='mntl-save__link_1-0']/svg[1]/use[1]").click()
    #
    # def test_allrecipes_3261eec0(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Meals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'L')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Lemon Bars')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='mntl-card-list-items_1-0']/div[1]/div[1]/div[1]/img[1]").click()
    #
    # def test_allrecipes_3d06adad(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='general-search_1-0']/button[1]/svg[1]/use[1]").click()
    #     self.driver.find_element(By.ID, "general-search__search-input").clear()
    #     self.driver.find_element(By.ID, "general-search__search-input").send_keys("filipino dessert")
    #     self.driver.find_element(By.XPATH, "//div[@id='general-search_1-0']/form[1]/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='mntl-card-list-items_1-0-10']/div[1]/div[1]/div[1]/img[1]").click()
    #
    # def test_allrecipes_5245c1ae(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Ingredients')]").click()
    #     self.driver.find_element(By.ID, "search-box__search-input").clear()
    #     self.driver.find_element(By.ID, "search-box__search-input").send_keys("sweet potatoes")
    #     self.driver.find_element(By.XPATH, "//div[@id='search-box_1-0']/form[1]/div[1]/button[1]").click()
    #
    # def test_allrecipes_547ed17c(self):
    #     # self.driver.get("https://allrecipes.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Meals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Drinks')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='taxonomy-nodes__link_1-0-4']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='taxonomy-nodes__link_1-0-1']/span[1]").click()
    #     self.driver.find_element(By.ID, "mntl-save__link_1-0").click()
    