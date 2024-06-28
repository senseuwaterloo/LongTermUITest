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
class TestEbay:
    
    def test_ebay_aaade1d2(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.ID, "gh-ac").clear()
        self.driver.find_element(By.ID, "gh-ac").send_keys("trash can automatic lid")
        self.driver.find_element(By.XPATH, "//a[@id='ui-id-153']/b[3]").click()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-endParamValue-textbox").clear()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-endParamValue-textbox").send_keys("60")
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Submit price range']").click()
        self.driver.find_element(By.XPATH, "//div[@id='x-refine__group__4']/ul[1]/li[4]/div[1]/a[1]/div[1]/span[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='x-refine__group__2']/ul[1]/li[1]/div[1]/a[1]/div[1]/span[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-wvq-9']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-wvq-8']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-51-13-5-4[0]-44-2-content-menu']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-khq-3']/button[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-51-13-5-4[0]-40-1-content-menu']/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='srp-river-results']/ul[1]/li[49]/div[1]/div[2]/a[1]/div[1]/span[1]").click()
    
    def test_ebay_a2b1d94b(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Electronics')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Headphones')]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-27_1-9-0-1[1]-0-1[1]-0-12-list']/li[1]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27-9-0-1[0]-0-0-6-5-4[7]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27-9-0-1[0]-0-0-6-5-4[7]-flyout']/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27-9-0-1[0]-0-0-6-5-4[6]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27-9-0-1[0]-0-0-6-5-4[6]-flyout']/div[1]/ul[1]/li[3]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-pkv-1']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-27-9-0-1[0]-0-0-6-4-13-15-content-menu']/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27-9-0-1[0]-0-0-6-5-4[6]-flyout']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27-9-0-1[0]-0-0-6-5-4[6]-flyout']/div[1]/ul[1]/li[8]/a[1]/span[2]").click()
    
    def test_ebay_a3bc6528(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.ID, "gh-ac").clear()
        self.driver.find_element(By.ID, "gh-ac").send_keys("laptop")
        self.driver.find_element(By.ID, "gh-btn").click()
        self.driver.find_element(By.XPATH, "//div[@id='x-refine__group__2']/ul[1]/li[1]/div[1]/a[1]/div[1]/span[1]/input[1]").click()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-beginParamValue-textbox").clear()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-beginParamValue-textbox").send_keys("400")
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-endParamValue-textbox").clear()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-endParamValue-textbox").send_keys("500")
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Submit price range']").click()
        self.driver.find_element(By.XPATH, "//div[@id='x-refine__group__6']/ul[1]/li[1]/div[1]/a[1]/div[1]/span[1]/input[1]").click()
    
    def test_ebay_a8474730(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='acc-skip-content']/div[2]/section[7]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ppc-container[3]/div[1]/a[1]/ppc-content[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='emea']/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/ppc-container[1]/a[1]/div[1]/div[1]/div[1]/div[1]/ppc-container[1]/span[1]/ppc-content[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='FlexibleWorkstylesAccordion']/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='acc-skip-content']/div[2]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/fieldset[1]/ul[1]/li[2]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='CategoryAccordion']/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='acc-skip-content']/div[2]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[3]/div[4]/div[3]/div[1]/div[2]/fieldset[1]/ul[1]/li[1]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "sortselect").clear()
        self.driver.find_element(By.ID, "sortselect").select("Most recent")
    
    def test_ebay_1ced6d51(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Fashion')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\"Men's Shoes\")]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Nike')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[3]-0-0-6-5-4[2]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[3]-0-0-6-5-4[2]-flyout']/div[1]/ul[1]/li[10]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[6]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[6]-flyout']/div[1]/ul[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-jwp-1']/button[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-27_1-9-0-1[0]-0-0-6-4-13-15-content-menu']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[7]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[7]-flyout']/div[1]/ul[1]/li[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[8]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[8]-flyout']/div[1]/ul[1]/li[3]/a[1]/span[2]").click()
    
    def test_ebay_4a0bd619(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Collectibles')]").click()
        self.driver.find_element(By.ID, "s0-16-12-0-1[2]-0-0-27[0]-0-toggle-button").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Furniture')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Chairs')]").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-y88-1']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-27_1-9-0-1[0]-0-0-6-4-13-15-content-menu']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/div[1]/ul[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/div[1]/ul[1]/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[4]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[4]-flyout']/div[1]/ul[1]/li[11]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[0]-0-0-6-5-4[5]-flyout']/div[1]/ul[1]/li[1]/a[1]/span[2]").click()
    
    def test_ebay_4f069a59(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.ID, "gh-ac").click()
        self.driver.find_element(By.ID, "gh-ac").clear()
        self.driver.find_element(By.ID, "gh-ac").send_keys("rare books")
        self.driver.find_element(By.ID, "gh-btn").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-51-13-5-4[0]']/div[2]/div[1]/div[1]/ul[1]/li[3]/a[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-u8c-5']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-51-13-5-4[0]-40-1-content-menu']/li[2]/a[1]/span[1]").click()
    
    def test_ebay_6da08512(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.ID, "gh-ac").click()
        self.driver.find_element(By.ID, "gh-ac").clear()
        self.driver.find_element(By.ID, "gh-ac").send_keys("musical instruments")
        self.driver.find_element(By.ID, "ui-id-35").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-o8x-23']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='nid-o8x-22']/div[1]/span[1]").click()
    
    def test_ebay_7bdebbfa(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.ID, "gh-ac").click()
        self.driver.find_element(By.ID, "gh-ac").clear()
        self.driver.find_element(By.ID, "gh-ac").send_keys("vintage clothing")
        self.driver.find_element(By.ID, "ui-id-43").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-cqn-1']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-51-13-5-4[0]-40-1-content-menu']/li[5]/a[1]/span[1]").click()
    
    def test_ebay_bc45669b(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.ID, "gh-ac").clear()
        self.driver.find_element(By.ID, "gh-ac").send_keys("xbox series x console")
        self.driver.find_element(By.ID, "gh-btn").click()
        self.driver.find_element(By.XPATH, "//div[@id='x-refine__group__2']/ul[1]/li[7]/div[1]/a[1]/div[1]/span[1]/input[1]").click()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-beginParamValue-textbox").clear()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-beginParamValue-textbox").send_keys("200")
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-endParamValue-textbox").clear()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-endParamValue-textbox").send_keys("400")
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Submit price range']").click()
    
    def test_ebay_cf8da12a(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Electronics')]").click()
        self.driver.find_element(By.ID, "s0-16-12-0-1[0]-0-0-27[9]-0-toggle-button").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Video Game Consoles')]").click()
        self.driver.find_element(By.XPATH, "//section[@id='s0-27_1-9-0-1[3]-0-0']/section[1]/ul[1]/li[9]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='c4-mainPanel-Features']/span[1]").click()
        self.driver.find_element(By.ID, "c4-subPanel-Features_Wi-Fi%20Capability_cbx").click()
        self.driver.find_element(By.XPATH, "//form[@id='x-overlay__form']/div[3]/div[2]/button[1]").click()
    
    def test_ebay_df3b7cd4(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Home & Garden')]").click()
        self.driver.find_element(By.ID, "s0-16-12-0-1[0]-0-0-27[5]-0-toggle-button").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Dining Sets')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[2]-0-0-6-5-4[7]-flyout']/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='s0-27_1-9-0-1[2]-0-0-6-5-4[7]-flyout']/div[1]/ul[1]/li[4]/a[1]/span[1]").click()
    
    def test_ebay_8f567f79(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.ID, "gh-ac").clear()
        self.driver.find_element(By.ID, "gh-ac").send_keys("iPhone 12 Pro")
        self.driver.find_element(By.ID, "gh-btn").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-51-12-6-3-4[0]-3-1-1-list']/li[1]/div[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='srp-river-results']/ul[1]/li[2]/div[1]/div[2]/a[1]/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "x-msku__select-box-1000").clear()
        self.driver.find_element(By.ID, "x-msku__select-box-1000").select("Blue")
        self.driver.find_element(By.XPATH, "//div[@id='mainContent']/form[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[2]/div[1]/a[1]").click()
    
    def test_ebay_980d35af(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.ID, "gh-ac").clear()
        self.driver.find_element(By.ID, "gh-ac").send_keys("mens timberland boots")
        self.driver.find_element(By.ID, "gh-btn").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-51-13-6-3-4[0]-3-1-1-list']/li[2]/div[1]/a[1]").click()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-endParamValue-textbox").clear()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-endParamValue-textbox").send_keys("100")
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Submit price range']").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-jt0-1']/button[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-51-13-5-4[0]-40-1-content-menu']/li[4]/a[1]/span[1]").click()
    
    def test_ebay_37c09901(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.ID, "gh-ac").clear()
        self.driver.find_element(By.ID, "gh-ac").send_keys("washing machine")
        self.driver.find_element(By.ID, "gh-btn").click()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-22[1[7]]-1-0-zipcode-validator-2-textbox").clear()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-22[1[7]]-1-0-zipcode-validator-2-textbox").send_keys("90026")
        self.driver.find_element(By.XPATH, "//div[@id='s0-51-13-0-1-2-6-0-22[1[7]]-1-0']/div[2]/div[2]/div[2]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='x-refine__group__7']/ul[1]/li[1]/div[1]/a[1]/div[1]/span[1]/input[1]").click()
    
    def test_ebay_1f128c19(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Toys')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Action Figures')]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-27_1-9-0-1[2]-0-0-12-list']/li[2]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='s0-27_1-9-0-1[0]-0-0']/section[1]/ul[1]/li[9]/button[1]").click()
        self.driver.find_element(By.ID, "c3-mainPanel-Character").click()
        self.driver.find_element(By.ID, "c3-subPanel-Character_Hulk_cbx").click()
        self.driver.find_element(By.XPATH, "//div[@id='c3-mainPanel-Year%20Manufactured']/span[1]").click()
        self.driver.find_element(By.ID, "c3-subPanel-Year%20Manufactured_1990_cbx").click()
        self.driver.find_element(By.XPATH, "//form[@id='x-overlay__form']/div[3]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='x-refine__group_1__2']/ul[1]/li[1]/div[1]/a[1]/div[1]/span[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-i86-3']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-51-12-5-4[0]-40-1-content-menu']/li[4]/a[1]/span[1]").click()
    
    def test_ebay_270c18c6(self):
        # self.driver.get("https://ebay.com")
        self.driver.find_element(By.ID, "gh-ac").clear()
        self.driver.find_element(By.ID, "gh-ac").send_keys("Nintendo Switch Console")
        self.driver.find_element(By.ID, "gh-btn").click()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-endParamValue-textbox").clear()
        self.driver.find_element(By.ID, "s0-51-13-0-1-2-6-0-8[3]-0-textrange-endParamValue-textbox").send_keys("400")
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='Submit price range']").click()
        self.driver.find_element(By.XPATH, "//div[@id='x-refine__group__2']/ul[1]/li[6]/div[1]/a[1]/div[1]/span[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='x-refine__group__4']/ul[1]/li[4]/div[1]/a[1]/div[1]/span[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='nid-ryh-11']/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='s0-51-13-5-4[1]-40-1-content-menu']/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//input[@role='presentation' and @value='on' and @type='checkbox']").click()
    