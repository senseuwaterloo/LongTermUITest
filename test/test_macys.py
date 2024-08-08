import time

import pytest
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from browser_helper import scroll_to_element, switch_to_new_tab, switch_to_new_tab_and_close_old


@pytest.mark.usefixtures("setup_class")
class TestMacys:
    
    # def test_macys_5a08f2d9(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_1']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shirts')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='row_0']/ul[1]/li[2]/div[1]/div[1]/a[1]/div[2]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.ID, "sortBy").clear()
    #     self.driver.find_element(By.ID, "sortBy").select("Best Sellers")
    #     self.driver.find_element(By.ID, "img_15400615").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mainCont']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/ul[1]/li[3]").click()
    #     self.driver.find_element(By.ID, "bag-add-15400615").click()
    #
    # def test_macys_5cd6189f(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_13247']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sandals')]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='BRAND']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='all_brands_list']/li[86]/a[1]").click()
    #     self.driver.find_element(By.ID, "sortBy").clear()
    #     self.driver.find_element(By.ID, "sortBy").select("Customers' Top Rated")
    #     self.driver.find_element(By.XPATH, "//h2[@title='Collapse Brand']").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title='Size']").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='WOMEN_SHOE_SIZE_T']/div[2]/ul[1]/li[1]/a[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='BRAND']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title='Expand Price']").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRICE']/div[1]/ul[1]/li[2]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRICE']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='FABRIC']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='FABRIC']/div[1]/ul[1]/li[2]/a[1]").click()
    #
    # def test_macys_0f2d0bb0(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_13247']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Baby Shoes')]").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title=\"Expand Customer's Top Rated\"]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='CUSTRATINGS']/div[1]/ul[1]/li[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title='Collapse Price']").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRICE']/div[1]/ul[1]/li[1]/a[1]").click()
    #
    # def test_macys_24e104ae(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Order Lookup')]").click()
    #     self.driver.find_element(By.ID, "js-order-no").clear()
    #     self.driver.find_element(By.ID, "js-order-no").send_keys("12345")
    #     self.driver.find_element(By.ID, "js-order-email").clear()
    #     self.driver.find_element(By.ID, "js-order-email").send_keys("12345@gmail.com")
    #     self.driver.find_element(By.ID, "js-lookup-btn").click()
    #
    # def test_macys_f75f526f(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.ID, "registry-link").click()
    #     self.driver.find_element(By.ID, "registrySearch").clear()
    #     self.driver.find_element(By.ID, "registrySearch").send_keys("Jane Doe")
    #     self.driver.find_element(By.XPATH, "//div[@id='registry-container']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[2]/button[1]").click()
    #
    # def test_macys_b4fc8b29(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_3536']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Sale & Clearance')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='visual-navigation']/div[1]/div[6]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title='Expand Category']").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRODUCT_DEPARTMENT']/div[1]/ul[1]/li[2]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title='Collapse Price']").click()
    #     self.driver.find_element(By.ID, "fromValue").clear()
    #     self.driver.find_element(By.ID, "fromValue").send_keys("0")
    #     self.driver.find_element(By.ID, "toValue").clear()
    #     self.driver.find_element(By.ID, "toValue").send_keys("10")
    #     self.driver.find_element(By.ID, "submitCustomPrice").click()
    #     self.driver.find_element(By.ID, "sortBy").clear()
    #     self.driver.find_element(By.ID, "sortBy").select("Price  Low to High")
    #     self.driver.find_element(By.ID, "img_16011651").click()
    #     self.driver.find_element(By.ID, "bag-add-16011651").click()
    #
    # def test_macys_b83d8b14(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_1']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Jeans')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='row_0']/ul[1]/li[1]/div[1]/div[1]/a[1]/div[2]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='1103208']/div[3]/div[2]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mainCont']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/ul[1]/li[1]").click()
    #     self.driver.find_element(By.ID, "bag-add-1103208").click()
    #
    # def test_macys_0c470ef9(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_5991']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pajamas')]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='GENDER']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='GENDER']/div[1]/ul[1]/li[2]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='GENDER']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='AGE_CATEGORY']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='AGE_CATEGORY']/div[1]/ul[1]/li[2]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='AGE_CATEGORY']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRICE']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRICE']/div[1]/ul[1]/li[2]/a[1]").click()
    #
    # def test_macys_2f096936(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_26846']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='categoryTree']/div[1]/ul[1]/li[4]/div[2]/h5[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Clutches & Evening Bags')]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='COLOR_NORMAL']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Blue (56)']").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='HANDBAG_MATERIAL']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='HANDBAG_MATERIAL']/div[1]/ul[1]/li[2]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRICE']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRICE']/div[1]/ul[1]/li[1]/a[1]").click()
    #
    # def test_macys_b8428fcc(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_260274']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Building Toys')]").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title='Expand Toys Age Range']").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='AGE_RANGE_TOYS']/div[1]/ul[1]/li[5]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title='Collapse Toy Type']").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='TOY_TYPE']/div[1]/ul[1]/li[3]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title='Collapse Gender']").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='GENDER']/div[1]/ul[1]/li[4]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title=\"Collapse Customer's Top Rated\"]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='CUSTRATINGS']/div[1]/ul[1]/li[1]/a[1]").click()
    #     self.driver.find_element(By.ID, "sortBy").clear()
    #     self.driver.find_element(By.ID, "sortBy").select("Best Sellers")
    #     self.driver.find_element(By.XPATH, "//div[@id='14124938']/div[2]/div[1]/a[1]").click()
    
    def test_macys_c3a97f15(self):
        # self.driver.get("https://www.macys.com/")
        # self.driver.find_element(By.XPATH, "//li[@id='flexid_324256']/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "fob-Trending").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Wear to Work')]").click()
        wear_to_work_link = self.driver.find_element(By.XPATH, "//div[text()='Wear-To-Work']")
        scroll_to_element(self.driver, wear_to_work_link)
        wear_to_work_link.click()

        # handle potential popup
        time.sleep(2)
        try:
            frame = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "kampyleInvite")))
            self.driver.switch_to.frame(frame.get_native_element())
            self.driver.find_element(By.ID, "kplDeclineButton").click()
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            error_message = f"handle popup in iframe error, check stack trace and screenshot for more details"
            self.driver.error_messages.append(error_message)
        finally:
            self.driver.switch_to.default_content()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop The Trend')]").click()
        # page logic changed, directly click on Tops link
        self.driver.find_element(By.XPATH, "//p[text()='Tops']").click()

        # self.driver.find_element(By.XPATH, "//li[@id='COLOR_NORMAL']/h2[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Black (16)']").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Brown (2)']").click()
        # filter the expected color
        self.driver.find_element(By.ID, "m-filter").click()
        self.driver.find_element(By.XPATH, "//li[@id='COLOR_NORMAL']/h2[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(@title, 'Black') and @class='item_icon ']").click()
        # self.driver.find_element(By.XPATH, "//span[contains(@title, 'Brown') and @class='item_icon ']").click()

        # self.driver.find_element(By.XPATH, "//h2[@title='Collapse Category']").click()
        self.driver.find_element(By.ID, "m-apply-facets").click()

        # self.driver.find_element(By.XPATH, "//li[@id='PRODUCT_DEPARTMENT']/div[1]/ul[1]/li[3]/a[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='region_1_child_2']/div[1]/div[1]/div[6]/ul[1]/li[1]/div[1]/div[1]").click()
        switch_to_new_tab(self.driver)

        # self.driver.find_element(By.XPATH, "//li[@id='SIZE_TYPE']/h2[1]/span[1]").click()
        # self.driver.find_element(By.ID, "sizeSelection").clear()
        # self.driver.find_element(By.ID, "sizeSelection").select("Women's Regular")
        # self.driver.find_element(By.XPATH, "//li[@id='WOMEN_REGULAR_SIZE_T']/div[1]/ul[1]/li[5]/a[1]/span[2]/div[1]").click()
        # self.driver.find_element(By.ID, "img_15453234").click()
        # self.driver.find_element(By.XPATH, "//div[@id='mainCont']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[2]/div[1]/picture[1]/source[1]/img[1]").click()
        # self.driver.find_element(By.ID, "bag-add-15453234").click()
        # self.driver.find_element(By.ID, "atbIntContinueShopping").click()
        # self.driver.find_element(By.XPATH, "//div[@id='mainCont']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[3]/div[1]/picture[1]/source[1]/img[1]").click()
        # self.driver.find_element(By.ID, "bag-add-15453234").click()
        # somehow need some sleep to avoid TimeoutException: Elements not found: xpath = //button[contains(@name, 'cta-sizes-')]//span[text()='S']. Seems like caused by layout shift
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(@name, 'cta-sizes-')]//span[text()='S']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Add To Bag']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Continue shopping']").click()
        switch_to_new_tab_and_close_old(self.driver)
        self.driver.find_element(By.ID, "m-filter").click()
        self.driver.find_element(By.XPATH, "//li[@id='COLOR_NORMAL']/h2[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(@title, 'Black') and @class='item_icon ']").click()
        # need some sleep time to avoid: selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//li[@id='COLOR_NORMAL']/h2[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(@title, 'Brown') and @class='item_icon ']").click()
        self.driver.find_element(By.ID, "m-apply-facets").click()
        # StaleElementReferenceException: Element became stale: xpath = //li[@id='region_1_child_2']/div[1]/div[1]/div[6]/ul[1]/li[1]/div[1]/div[1] - Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//li[@id='region_1_child_2']/div[1]/div[1]/div[6]/ul[1]/li[1]/div[1]/div[1]").click()
        switch_to_new_tab(self.driver)
        # already some sleep in the switch tab function, that's why we don't need sleep before this size selection action
        self.driver.find_element(By.XPATH, "//button[contains(@name, 'cta-sizes-')]//span[text()='XL']").click()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Add To Bag']").click()


    
    # def test_macys_baf8a9d8(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='myRewardsLabel-container']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Lists')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='listsHeaderView']/section[1]/div[3]/div[1]/div[1]/div[2]/u[1]/li[1]").click()
    #     self.driver.find_element(By.ID, "newListName").clear()
    #     self.driver.find_element(By.ID, "newListName").send_keys("New Home")
    #     self.driver.find_element(By.ID, "listSearchable").click()
    #     self.driver.find_element(By.ID, "btnCreateList").click()
    #     self.driver.find_element(By.ID, "globalSearchInputField").clear()
    #     self.driver.find_element(By.ID, "globalSearchInputField").send_keys("chair")
    #     self.driver.find_element(By.XPATH, "//ul[@id='autosuggest']/div[1]/li[2]/a[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "sortBy").clear()
    #     self.driver.find_element(By.ID, "sortBy").select("Price  Low to High")
    #     self.driver.find_element(By.XPATH, "//div[@id='15937004']/div[2]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='addToList-15937004']/span[1]").click()
    #
    # def test_macys_316850c0(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_544']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rings')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='row_0']/ul[1]/li[1]/div[1]/a[1]/picture[1]/source[1]/source[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='METAL']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='METAL']/div[1]/ul[1]/li[4]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='STONE_WEIGHT']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='STONE_WEIGHT']/div[1]/ul[1]/li[4]/a[1]").click()
    #
    # def test_macys_4e1e4c8a(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_3536']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Kitchen')]").click()
    #     self.driver.find_element(By.XPATH, "//h2[@title='Expand Material']").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='MATERIAL']/div[1]/ul[1]/li[2]/a[1]").click()
    #
    # def test_macys_6accc593(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//li[@id='flexid_118142']/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='giftsbyprice']/div[1]/div[1]/div[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRODUCT_DEPARTMENT']/h2[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='PRODUCT_DEPARTMENT']/div[1]/ul[1]/li[1]/a[1]/span[3]").click()
    #     self.driver.find_element(By.ID, "img_15444237").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='giftCardForm']/div[2]/div[2]/button[2]").click()
    #     self.driver.find_element(By.ID, "eGiftEmail").clear()
    #     self.driver.find_element(By.ID, "eGiftEmail").send_keys("CHRISTENSON@GMAIL.COM")
    #     self.driver.find_element(By.ID, "giftTo").clear()
    #     self.driver.find_element(By.ID, "giftTo").send_keys("christene")
    #     self.driver.find_element(By.ID, "giftFrom").clear()
    #     self.driver.find_element(By.ID, "giftFrom").send_keys("Shak")
    #     self.driver.find_element(By.ID, "giftMessage").clear()
    #     self.driver.find_element(By.ID, "giftMessage").send_keys("Happy birthday, wish you many more years to com")
    #     self.driver.find_element(By.ID, "giftSubmit").click()
    #
    # def test_macys_924476f8(self):
    #     # self.driver.get("https://www.macys.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),\"Macy's Wine Shop\")]").click()
    #     self.driver.find_element(By.ID, "over-twenty-one").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main-content']/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='filters[properties.sweetness][][]' and @value='on' and @type='checkbox']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[2]/main[1]/div[1]/div[1]/ng-form[1]/accordion[1]/dl[1]/div[3]/dd[1]/div[1]/label[5]/input[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[2]/main[1]/div[1]/div[1]/ng-form[1]/accordion[1]/dl[1]/div[5]/dd[1]/div[1]/label[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[2]/main[1]/div[1]/div[1]/ng-form[1]/accordion[1]/dl[1]/div[6]/dd[1]/a[1]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='filters[properties.vintage][][]' and @value='on' and @type='checkbox']").click()
    #     self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[2]/main[1]/div[2]/div[2]/div[1]/ng-include[1]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[2]/main[1]/div[2]/div[2]/div[1]/ng-include[1]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[2]/main[1]/div[2]/div[2]/div[1]/ng-include[1]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main-content']/div[2]/main[1]/div[2]/div[2]/div[1]/ng-include[1]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    