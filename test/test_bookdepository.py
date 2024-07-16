import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestBookdepository:
    
    def test_bookdepository_c1f584e2(self):
        # self.driver.get("https://bookdepository.com")
        # book depository is closing soon, so we revised this test case for https://www.barnesandnoble.com/
        self.driver.find_element(By.XPATH, "//a[contains(., ' My Account')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Sign In')]").click()

        login_iframe = self.driver.find_element(By.XPATH, "//iframe[@title='Sign in or Create an Account']").get_native_element()
        self.driver.switch_to.frame(login_iframe)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("UITestStudy2024")
        self.driver.find_element(By.XPATH, "//button[contains(., 'Sign In & Continue')]").click()
        self.driver.switch_to.default_content()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search by Title, Author, Keyword or ISBN']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search by Title, Author, Keyword or ISBN']").send_keys("game of thrones")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Search button']").click()

        language_filter = self.driver.find_element(By.XPATH, "//div[@aria-label='left-nav']//div[@id='Language_category']")
        scroll_to_element(self.driver, language_filter)
        language_filter.click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='left-nav']//div[@id='Language_category']/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='left-nav']//ul[@id='sidebar-section-0']/li[11]/a").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'filter-section justify-content-md-end')]//a[@id='list-view']/div").click()

        self.driver.find_element(By.XPATH, "//form[@id='addToBagForm_0700304046659']/input[11]").click()
        self.driver.find_element(By.XPATH, "//form[@id='addToBagForm_0810011720022']/input[11]").click()

        self.driver.find_element(By.ID, "cartIcon").click()
        self.driver.find_element(By.XPATH, "//input[@id='continue' and @value='CONTINUE TO CHECKOUT']").click()

    # def test_bookdepository_c472a4fe(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Advanced Search')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchAuthor' and @value='' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchAuthor' and @value='' and @type='text']").send_keys("Stephen King")
    #     self.driver.find_element(By.ID, "filterLang").clear()
    #     self.driver.find_element(By.ID, "filterLang").select("German")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()

    # def test_bookdepository_bd2b5866(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by category')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by category')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[4]/div[1]/ul[1]/li[1]/ul[1]/li[4]/ul[1]/li[3]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Education')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'English Language')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'English Language: Reading & Writing Skills')]").click()
    #     self.driver.find_element(By.ID, "filterAvailability").clear()
    #     self.driver.find_element(By.ID, "filterAvailability").select("In Stock (41,088)")
    #     self.driver.find_element(By.ID, "filterFormat").clear()
    #     self.driver.find_element(By.ID, "filterFormat").select("Hardback (13,067)")
    #     self.driver.find_element(By.ID, "filterPrice").clear()
    #     self.driver.find_element(By.ID, "filterPrice").select("Under US$20")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Refine results')]").click()

    # def test_bookdepository_c1a354a1(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Advanced Search')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchIsbn' and @value='' and @type='text']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchIsbn' and @value='' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchIsbn' and @value='' and @type='text']").send_keys("1648926800")
    #     self.driver.find_element(By.ID, "filterLang").clear()
    #     self.driver.find_element(By.ID, "filterLang").select("Hindi")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    #
    # def test_bookdepository_cf8b2846(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[1]/div[1]/ul[2]/li[1]/a[1]").click()
    #     self.driver.find_element(By.ID, "orderNumber").clear()
    #     self.driver.find_element(By.ID, "orderNumber").send_keys("X123456789")
    #     self.driver.find_element(By.ID, "customerEmail").clear()
    #     self.driver.find_element(By.ID, "customerEmail").send_keys("buckeye.foobar@gmail.com")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'View')]").click()
    #
    # def test_bookdepository_db72bae1(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//input[@name='searchTerm' and @value='' and @type='text' and @placeholder='Search for books by keyword / title / author / ISBN']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchTerm' and @value='' and @type='text' and @placeholder='Search for books by keyword / title / author / ISBN']").send_keys("recipe")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'recipe book')]").click()
    #     self.driver.find_element(By.ID, "filterAvailability").clear()
    #     self.driver.find_element(By.ID, "filterAvailability").select("In Stock (7,640)")
    #     self.driver.find_element(By.ID, "filterLang").clear()
    #     self.driver.find_element(By.ID, "filterLang").select("Spanish (42)")
    #     self.driver.find_element(By.ID, "filterFormat").clear()
    #     self.driver.find_element(By.ID, "filterFormat").select("Paperback (39,356)")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Refine results')]").click()
    #
    # def test_bookdepository_01dcf2f1(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by category')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[4]/div[1]/ul[1]/li[1]/ul[1]/li[1]/ul[2]/ul[1]/li[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Fiction')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Romance')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='searchSortBy']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='searchSortBy']").select("Price, low to high")

    # def test_bookdepository_0a2130e7(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by category')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[4]/div[1]/ul[1]/li[1]/ul[1]/li[1]/ul[1]/ul[1]/li[3]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Non-Fiction')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'History')]").click()
    #     self.driver.find_element(By.ID, "ageRange").clear()
    #     self.driver.find_element(By.ID, "ageRange").select("Ages 9-11 (13,217)")
    #     self.driver.find_element(By.ID, "filterLang").clear()
    #     self.driver.find_element(By.ID, "filterLang").select("Hindi (59)")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Refine results')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Notify me')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Add to wishlist')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='wishlistLabel' and @type='text' and @placeholder='Wishlist name']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='wishlistLabel' and @type='text' and @placeholder='Wishlist name']").send_keys("Must buy")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Add')]").click()

    # def test_bookdepository_690eedad(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bestsellers')]").click()
    #     self.driver.find_element(By.ID, "filterPrice").clear()
    #     self.driver.find_element(By.ID, "filterPrice").select("Under US$20")
    #     self.driver.find_element(By.ID, "filterFormat").clear()
    #     self.driver.find_element(By.ID, "filterFormat").select("Hardback")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Refine results')]").click()
    #
    # def test_bookdepository_712d9d7f(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by category')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[4]/div[1]/ul[1]/li[1]/ul[1]/li[1]/ul[2]/ul[1]/li[9]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Complementary Medicine')]").click()
    #     self.driver.find_element(By.ID, "filterFormat").clear()
    #     self.driver.find_element(By.ID, "filterFormat").select("Audio (376)")
    #     self.driver.find_element(By.ID, "filterPrice").clear()
    #     self.driver.find_element(By.ID, "filterPrice").select("Under US$20")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Refine results')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Add to basket')]").click()
    #
    # def test_bookdepository_8e3c7ad0(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//input[@name='searchTerm' and @value='' and @type='text' and @placeholder='Search for books by keyword / title / author / ISBN']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchTerm' and @value='' and @type='text' and @placeholder='Search for books by keyword / title / author / ISBN']").send_keys("Harry Potter")
    #     self.driver.find_element(By.XPATH, "//form[@id='book-search-form']/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Harry Potter and the Cursed Child - Parts I & II')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Add to wishlist')]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Add')]").click()
    #
    # def test_bookdepository_a2b159c8(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by category')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by category')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[4]/div[1]/ul[1]/li[1]/ul[1]/li[1]/ul[2]/ul[1]/li[9]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Diseases & Disorders')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Add to basket')]").click()
    #
    # def test_bookdepository_31a74ae0(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by category')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[4]/div[1]/ul[1]/li[1]/ul[1]/li[1]/ul[3]/li[1]/div[1]/div[2]/div[1]/div[1]/a[6]/div[1]").click()
    #     self.driver.find_element(By.ID, "filterPrice").clear()
    #     self.driver.find_element(By.ID, "filterPrice").select("US$20 to US$40")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Refine results')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Add to basket')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Close')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Add to basket')]").click()
    #
    # def test_bookdepository_4f14fb44(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//input[@name='searchTerm' and @value='' and @type='text' and @placeholder='Search for books by keyword / title / author / ISBN']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchTerm' and @value='' and @type='text' and @placeholder='Search for books by keyword / title / author / ISBN']").send_keys("Jk rowling")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Jk rowling')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='searchSortBy']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='searchSortBy']").select("Publication date, new to old")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[5]/div[1]/div[1]/div[1]/form[1]/div[2]").click()
    #     self.driver.find_element(By.ID, "ageRange").clear()
    #     self.driver.find_element(By.ID, "ageRange").select("Ages 3-5 (31)")
    #     self.driver.find_element(By.ID, "filterPrice").clear()
    #     self.driver.find_element(By.ID, "filterPrice").select("Under US$20")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Refine results')]").click()
    #
    # def test_bookdepository_dd057bda(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by category')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[4]/div[1]/ul[1]/li[1]/ul[1]/li[1]/ul[2]/ul[1]/li[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Fiction')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='searchSortBy']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='searchSortBy']").select("Price, low to high")
    #
    # def test_bookdepository_f296f6a6(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bestsellers')]").click()
    #     self.driver.find_element(By.ID, "filterPrice").clear()
    #     self.driver.find_element(By.ID, "filterPrice").select("US$20 to US$40")
    #     self.driver.find_element(By.ID, "filterAvailability").clear()
    #     self.driver.find_element(By.ID, "filterAvailability").select("In stock (53476)")
    #     self.driver.find_element(By.ID, "filterFormat").clear()
    #     self.driver.find_element(By.ID, "filterFormat").select("Digital")
    #     self.driver.find_element(By.ID, "filterLang").clear()
    #     self.driver.find_element(By.ID, "filterLang").select("French (299)")
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Refine results')]").click()
    #
    # def test_bookdepository_58f811fd(self):
    #     # self.driver.get("https://bookdepository.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cancel my order')]").click()
    #     self.driver.find_element(By.ID, "fullName").clear()
    #     self.driver.find_element(By.ID, "fullName").send_keys("James Smith")
    #     self.driver.find_element(By.ID, "emailAddress").clear()
    #     self.driver.find_element(By.ID, "emailAddress").send_keys("buckeye.foobar@gmail.com")
    #     self.driver.find_element(By.ID, "orderReference").clear()
    #     self.driver.find_element(By.ID, "orderReference").send_keys("X123456")
    #     self.driver.find_element(By.ID, "orderReceivedDate").clear()
    #     self.driver.find_element(By.ID, "orderReceivedDate").send_keys("08/04/23")
    #     self.driver.find_element(By.ID, "contactMessage").clear()
    #     self.driver.find_element(By.ID, "contactMessage").send_keys("Harry Potter Box Set")
    #     self.driver.find_element(By.ID, "cancelReason").clear()
    #     self.driver.find_element(By.ID, "cancelReason").send_keys("Not available at address")
    #     self.driver.find_element(By.ID, "contactUsSubmit").click()
    