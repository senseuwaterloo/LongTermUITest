import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestShoppingGoogle:
    
    # def test_shoppinggoogle_275a7416(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("Google Pixel 7")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c398']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[11]/div[2]/div[1]/div[1]/div[1]/span[3]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]/span[5]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//g-popup[@id='ow12']/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='lb']/div[1]/g-menu[1]/g-menu-item[3]/div[1]").click()
    #
    # def test_shoppinggoogle_2de30aa3(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("Nest Hello Video Doorbell")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c506']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rso']/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rso']/div[2]/div[2]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/span[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='reviews']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/a[5]/div[1]").click()
    #
    # def test_shoppinggoogle_470ee759(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c248']/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("drip coffee maker")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c457']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[3]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/span[2]/div[1]/a[1]/span[1]").click()
    #
    # def test_shoppinggoogle_51c2f319(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("pokemon go elite trainer box")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c515']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rso']/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rso']/div[2]/div[2]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[4]/div[2]/a[1]").click()
    #
    # def test_shoppinggoogle_09ef065e(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").click()
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("running shoes")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c448']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[8]/div[2]/div[1]/div[1]/div[1]/span[21]/div[1]/a[1]/span[1]").click()
    #
    # def test_shoppinggoogle_1f91de2a(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").click()
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("smart tv")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c362']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/span[3]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/a[1]/span[1]").click()
    
    def test_shoppinggoogle_7349981f(self):
        # self.driver.get("https://shopping.google.com/")

        # self.driver.find_element(By.ID, "REsRA").clear()
        # self.driver.find_element(By.ID, "REsRA").send_keys("computer monitor")
        self.driver.find_element(By.ID, "REsRA").clear()
        self.driver.find_element(By.ID, "REsRA").send_keys("computer monitor")

        # self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c418']/div[1]/div[2]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='computer monitor' and not(./b)]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/span[3]/div[1]/a[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/span[2]/div[1]/a[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[2]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Available nearby']").click()
        self.driver.find_element(By.XPATH, "//span[@title='Samsung']").click()
        self.driver.find_element(By.XPATH, "//span[@title='LG']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/span[2]/div[1]/a[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[1]/span[2]/div[1]/a[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[10]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='4K']").click()
        self.driver.find_element(By.XPATH, "//span[@title='IPS Panel']").click()

        # self.driver.find_element(By.XPATH, "//g-popup[@id='ow12']/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='lb']/div[1]/g-menu[1]/g-menu-item[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Sort by: Relevance']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Review score']").click()
    
    # def test_shoppinggoogle_f8df8406(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("running shoes")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c389']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Black']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/span[4]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/span[10]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[3]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@role='radio']").click()
    #
    # def test_shoppinggoogle_5b0eace3(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("Granitestone Sandwich Maker")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c458']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rso']/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[4]/div[2]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sh-oo__filters-wrapper']/div[3]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//tr[@id='sh-osd__headers']/th[4]").click()
    #
    # def test_shoppinggoogle_705c914c(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("iphone 14")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c348']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/span[2]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//g-popup[@id='ow14']/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='lb']/div[1]/g-menu[1]/g-menu-item[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rso']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rso']/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='reviews']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/a[5]/div[1]").click()
    #
    # def test_shoppinggoogle_d10c0099(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.XPATH, "//c-wiz[@id='kO001e']/div[1]/div[1]/div[1]/c-wiz[1]/div[1]/div[1]/span[1]/button[1]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "//c-wiz[@id='kO001e']/div[1]/div[1]/div[1]/c-wiz[1]/div[1]/div[3]/div[1]/div[1]/div[3]/a[2]").click()
    #     self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]/span[2]/span[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, "c33").clear()
    #     self.driver.find_element(By.ID, "c33").send_keys("Future Birthday Gifts")
    #     self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[5]/div[2]/div[1]/div[2]/div[1]/span[2]/span[1]/div[1]/button[1]/span[1]").click()
    #
    # def test_shoppinggoogle_d57b93a0(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").click()
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("electric coffee grinder")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c513']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]/span[3]/div[1]/a[1]/span[1]").click()
    #
    # def test_shoppinggoogle_ebfe31b3(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("Nike Air")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c322']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/span[2]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[1]/span[2]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/span[5]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[20]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/a[1]/span[1]").click()
    #
    # def test_shoppinggoogle_85d6d6f1(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/section[1]/div[2]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/article[1]/a[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sg-product__pdp-container']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
    #
    # def test_shoppinggoogle_8a1cda91(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").click()
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("earbuds")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c351']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//g-popup[@id='ow14']/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='lb']/div[1]/g-menu[1]/g-menu-item[2]/div[1]").click()
    #
    # def test_shoppinggoogle_8f309c5d(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").click()
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("cat food")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c364']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//g-popup[@id='ow14']/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='lb']/div[1]/g-menu[1]/g-menu-item[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rcnt']/div[3]/div[1]/div[1]/div[13]/div[2]/div[1]/div[1]/div[1]/span[2]/div[1]/a[1]/span[1]").click()
    #
    # def test_shoppinggoogle_99205f1e(self):
    #     # self.driver.get("https://shopping.google.com/")
    #     self.driver.find_element(By.ID, "REsRA").clear()
    #     self.driver.find_element(By.ID, "REsRA").send_keys("Samsung Galaxy S22")
    #     self.driver.find_element(By.XPATH, "//li[@id='core-suggestion-c436']/div[1]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rso']/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='rso']/div[2]/div[2]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[4]/div[2]/a[1]").click()
    