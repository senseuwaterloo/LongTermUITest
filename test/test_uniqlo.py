import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.mark.usefixtures("setup_class")
class TestUniqlo:
    
    def test_uniqlo_ef3a7151(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[4]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Color']").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='colorFilterCheckBox']/div[1]/div[2]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Size']").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='sizeFilterCheckBox']/div[1]/div[4]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]/g[1]/polygon[1]").click()
    
    def test_uniqlo_323f1c41(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a[2]").click()
        self.driver.find_element(By.ID, "2").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='sizeFilterCheckBox']/div[1]/div[7]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='sizeFilterCheckBox']/div[1]/div[8]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='3']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='colorFilterCheckBox']/div[1]/div[3]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Category']").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@role='option' and @value='23306']").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[9]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E433109-000']/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.ID, "BLACK-09-1").click()
        self.driver.find_element(By.ID, "3XL-008-6").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[2]/div[9]/div[1]/div[1]/button[1]").click()
    
    def test_uniqlo_29c19896(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/footer[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[3]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'How do I return my online order')]").click()
    
    def test_uniqlo_ccf98191(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Price']").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='priceFilter']/div[2]/div[2]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]/g[1]/polygon[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E455762-000']/div[2]/h3[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[2]/div[9]/div[1]/div[1]/button[1]").click()
    
    def test_uniqlo_ddcbce13(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E453773-000']/div[2]/h3[1]").click()
        self.driver.find_element(By.ID, "ORANGE").click()
        self.driver.find_element(By.ID, "L").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[2]/div[9]/div[1]/div[1]/button[1]").click()
    
    def test_uniqlo_ddd935d4(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a[2]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Category']").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@role='option' and @value='23305']").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Size']").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='sizeFilterCheckBox']/div[1]/div[5]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Color']").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='colorFilterCheckBox']/div[1]/div[3]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[9]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E422989-000']/div[2]/h3[1]").click()
        self.driver.find_element(By.ID, "L-005-5").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[2]/div[9]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[1]/div[13]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='fixed-panel']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/section[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "storeSearch").clear()
        self.driver.find_element(By.ID, "storeSearch").send_keys("10005")
        self.driver.find_element(By.XPATH, "//svg[@role='presentation']").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='storeList']/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='selectedDeliveryMethod']/div[1]/button[2]").click()
    
    def test_uniqlo_cbfa5c92(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[5]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Category']").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@id='option-3']/span[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Size']").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='sizeFilterCheckBox']/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E450442-000']/div[2]/h3[1]").click()
        self.driver.find_element(By.ID, "BROWN-34-4").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[2]/div[8]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[1]/div[11]/div[1]/div[1]/div[2]/div[1]/div[1]/button[2]").click()
        self.driver.find_element(By.ID, "PURPLE-72-5").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[2]/div[8]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[1]/div[11]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    
    def test_uniqlo_f8089c50(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='4']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='priceFilter']/div[2]/div[5]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E460652-000']/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    
    def test_uniqlo_e8637690(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/footer[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.ID, "option-47").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/section[1]/section[3]/section[1]/div[2]/div[2]/ul[1]/li[1]/fieldset[1]/h1[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='undefined-content']/fieldset[1]/div[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='undefined-content']/fieldset[1]/div[3]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/section[1]/section[3]/section[1]/div[2]/div[2]/ul[1]/li[2]/fieldset[1]/h1[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='undefined-content']/fieldset[1]/div[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/section[1]/section[3]/section[2]/div[2]/div[2]/ul[1]/li[1]/button[1]").click()
    
    def test_uniqlo_9c9e89c1(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='2']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='sizeFilterCheckBox']/div[1]/div[5]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[6]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
    
    def test_uniqlo_ad381d87(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[3]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Sort by']").click()
        self.driver.find_element(By.XPATH, "//li[@id='option-2']/span[1]").click()
    
    def test_uniqlo_b30b9f84(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//svg[@role='presentation']").click()
        self.driver.find_element(By.ID, "Search").clear()
        self.driver.find_element(By.ID, "Search").send_keys("sports wear")
        self.driver.find_element(By.XPATH, "//svg[@role='presentation']").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Gender > Category']").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@id='option-1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Size']").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='sizeFilterCheckBox']/div[1]/div[3]/div[1]/label[1]").click()
    
    def test_uniqlo_b5cb859d(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='2']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='sizeFilterCheckBox']/div[1]/div[6]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E457754-000']/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='1']").click()
        self.driver.find_element(By.ID, "option-2").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[2]/div[9]/div[1]/div[1]/button[1]").click()
    
    def test_uniqlo_95619447(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[1]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Category']").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@role='option' and @value='24798']").click()
        self.driver.find_element(By.XPATH, "//span[@title='Sort by']").click()
        self.driver.find_element(By.XPATH, "//li[@id='option-2']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E455595-001']/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E455595-001']/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E455595-001']/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    
    def test_uniqlo_42657330(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html").click()
        self.driver.find_element(By.ID, "Search").clear()
        self.driver.find_element(By.ID, "Search").send_keys("women t-shirts")
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[3]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='2']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='sizeFilterCheckBox']/div[1]/div[3]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='3']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='colorFilterCheckBox']/div[1]/div[9]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='4']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='priceFilter']/div[2]/div[3]/div[1]/div[1]/label[1]").click()
    
    def test_uniqlo_7c28f4e3(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/footer[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Postal code, address, store name']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Postal code, address, store name']").send_keys("10017")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/section[1]/section[2]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[2]/section[1]/section[3]/section[2]/div[2]/div[2]/ul[1]/li[1]/button[1]").click()
    
    def test_uniqlo_7f94386a(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/footer[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@role='option' and @value='13']").click()
    
    def test_uniqlo_84d8a4df(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[3]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E455546-000']/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[2]/div[8]/div[1]/div[1]/button[1]").click()
    
    def test_uniqlo_13f1648c(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='1']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@id='option-4']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E449859-000']/div[2]/h3[1]").click()
        self.driver.find_element(By.ID, "PINK").click()
        self.driver.find_element(By.ID, "XXL").click()
        self.driver.find_element(By.XPATH, "//input[@value='1']").click()
        self.driver.find_element(By.XPATH, "//li[@id='option-1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[2]/div[8]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[1]/div[4]/div[1]/div[18]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    
    def test_uniqlo_08a998f9(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/footer[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Postal code, address, store name']").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Postal code, address, store name']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Postal code, address, store name']").send_keys("Chicago")
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@role='option' and @value='13']").click()
    
    def test_uniqlo_099a9da4(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a[3]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Price']").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='priceFilter']/div[2]/div[2]/div[1]/div[1]/label[1]").click()
    
    def test_uniqlo_122178b3(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//svg[@role='presentation']").click()
        self.driver.find_element(By.ID, "Search").clear()
        self.driver.find_element(By.ID, "Search").send_keys("blazer")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[1]/a[3]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Gender > Category']").click()
        self.driver.find_element(By.XPATH, "//input[@value='All']").click()
        self.driver.find_element(By.XPATH, "//li[@role='option' and @value='22211']").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//h4[@title='Color']").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='colorFilterCheckBox']/div[1]/div[2]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/header[1]/button[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='E448034-000']/div[1]/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[3]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[5]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[3]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/button[1]").click()
    
    def test_uniqlo_f1f4e4f7(self):
        # self.driver.get("https://www.uniqlo.com/us/en/")
        self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[1]/div[1]/nav[1]/div[2]/a[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[3]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='2']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//fieldset[@id='sizeFilterCheckBox']/div[1]/div[7]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root']/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='option-1']/span[1]").click()
    