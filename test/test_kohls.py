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
class TestKohls:
    
    def test_kohls_1d73ad40(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='top-nav-left']/li[1]/a[1]/p[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Women')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Loungewear')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel52432566']/div[4]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Size']/li[7]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "sbSelector_48455586").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low-High')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel52432599']/div[5]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Color']/li[4]/a[1]/span[1]").click()
    
    def test_kohls_a5dd5729(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("spider-man toy")
        self.driver.find_element(By.ID, "K1000_0").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel88579914']/div[9]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='AgeRange']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "sbSelector_44830792").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low-High')]").click()
    
    def test_kohls_d6a40526(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='top-nav-left']/li[1]/a[1]/p[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Women')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Swimwear')]").click()
        self.driver.find_element(By.XPATH, "//article[@id='tce-spotlight']/section[1]/div[1]/ul[1]/li[1]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='vn-box']/ul[1]/li[4]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Color']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "sbSelector_43781700").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low-High')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel24521227']/div[9]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='CustomerRating']/li[1]/a[1]/span[2]").click()
    
    def test_kohls_513f4cef(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//div[@id='open-drawer']/div[1]/div[2]/div[1]/div[1]/div[1]/div[7]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='vn-box']/ul[1]/li[1]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel805803']/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Category']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel805836']/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Gender']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel805856']/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Size']/li[2]/a[1]/span[1]").click()
    
    def test_kohls_5eacf1eb(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Store Locator')]").click()
        self.driver.find_element(By.ID, "rio-browse-by-state").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Ohio')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cincinnati')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Store Info')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Directions')]").click()
    
    def test_kohls_69ed8097(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("coffee maker")
        self.driver.find_element(By.XPATH, "//input[@name='submit-search' and @value='' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel9578290']/div[4]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Rating']/li[1]/a[1]/span[1]").click()
    
    def test_kohls_c37a7e97(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("mens winter coat")
        self.driver.find_element(By.XPATH, "//li[@id='K1000_0']/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel138949620']/div[12]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Promotions']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel138949653']/div[5]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Size']/li[3]/a[1]/span[1]").click()
    
    def test_kohls_150146b2(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='top-nav-left']/li[1]/a[1]/p[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Men')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop by Brand')]").click()
        self.driver.find_element(By.ID, "nfl__state-menu").clear()
        self.driver.find_element(By.ID, "nfl__state-menu").select("Calvin Klein")
    
    def test_kohls_33b57a14(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("shirt")
        self.driver.find_element(By.ID, "search").click()
        self.driver.find_element(By.ID, "sbSelector_11527097").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low-High')]").click()
        self.driver.find_element(By.XPATH, "//img[@title=\"Women's Sonoma Goods For Life® Everyday V-Neck Tee\"]").click()
        self.driver.find_element(By.ID, "panel2045641").clear()
        self.driver.find_element(By.ID, "panel2045641").send_keys("10")
        self.driver.find_element(By.ID, "addtobagID").click()
    
    def test_kohls_47072aee(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("black stroller")
        self.driver.find_element(By.XPATH, "//input[@name='submit-search' and @value='' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel813396']/div[5]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[4]/a[1]/span[1]").click()
    
    def test_kohls_aab91310(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("mens hiking shoes")
        self.driver.find_element(By.XPATH, "//input[@name='submit-search' and @value='' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel454250']/div[10]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel454323']/div[6]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Size']/li[11]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "sbSelector_19359954").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Percent Off')]").click()
        self.driver.find_element(By.XPATH, "//img[@title=\"Eddie Bauer Canyon Men's Waterproof Hiking Shoes\"]").click()
    
    def test_kohls_06309af8(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='top-nav-left']/li[1]/a[1]/p[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Women')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shoes & Sandals')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='vn-box']/ul[1]/li[1]/a[1]/p[1]").click()
        self.driver.find_element(By.ID, "sbSelector_69872894").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Best Sellers')]").click()
    
    def test_kohls_2d92911a(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Store Locator')]").click()
        self.driver.find_element(By.ID, "q").clear()
        self.driver.find_element(By.ID, "q").send_keys("SPRING, TX")
        self.driver.find_element(By.ID, "ui-id-2").click()
        self.driver.find_element(By.XPATH, "//a[@id='search-button']/svg[1]").click()
        self.driver.find_element(By.XPATH, "//li[@id='lid248656']/div[2]/div[1]/a[1]/span[1]/span[1]").click()
    
    def test_kohls_1a16a98f(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("bath towels")
        self.driver.find_element(By.XPATH, "//li[@id='K1000_0']/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='Sonoma Goods For Life® Ultimate Bath Towel with Hygro® Technology']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'BATH TOWEL')]").click()
        self.driver.find_element(By.ID, "addtobagID").click()
        self.driver.find_element(By.ID, "button-panel87432638").click()
        self.driver.find_element(By.ID, "panel1102").clear()
        self.driver.find_element(By.ID, "panel1102").send_keys("FREESHIP3093")
        self.driver.find_element(By.ID, "button-panel1104").click()
    
    def test_kohls_21f5aaaa(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("easter home decor")
        self.driver.find_element(By.XPATH, "//li[@id='K1000_0']/span[1]/span[1]").click()
        self.driver.find_element(By.ID, "sbSelector_16844583").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Arrivals')]").click()
    
    def test_kohls_2b29b7d1(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("mens black hoodie")
        self.driver.find_element(By.XPATH, "//li[@id='K1000_0']/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel21061221']/div[4]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='SizeRange']/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel21061254']/div[4]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "sbSelector_61467700").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Best Sellers')]").click()
    
    def test_kohls_8e1a344d(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='top-nav-left']/li[1]/a[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'For the Home')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rugs')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='vn-box']/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel85002789']/div[3]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Color']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel85002822']/div[5]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Size']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "sbSelector_19054410").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low-High')]").click()
    
    def test_kohls_0c02c193(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("skirt")
        self.driver.find_element(By.ID, "search").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel2083548']/div[2]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Gender']/li[6]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "sbSelector_91383158").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Best Sellers')]").click()
    
    def test_kohls_bf469f30(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='top-nav-left']/li[1]/a[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Pet')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel108587464']/div[2]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='PetType']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel108587497']/div[3]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Category']/li[7]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "sbSelector_11835245").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Highest Rated')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel108587517']/div[6]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[1]/a[1]/span[1]").click()
    
    def test_kohls_4b2030ff(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("wall art")
        self.driver.find_element(By.XPATH, "//input[@name='submit-search' and @value='' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//article[@id='tce-spotlight']/section[1]/section[1]/div[1]/div[1]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel583109']/div[6]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Price']/li[3]/a[1]/span[1]").click()
    
    def test_kohls_4bc70fa1(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='top-nav-left']/li[1]/a[1]/p[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Women')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sweaters & Cardigans')]").click()
        self.driver.find_element(By.ID, "sbSelector_57459950").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low-High')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='4923526_prod_price']/div[3]/p[1]").click()
        self.driver.find_element(By.ID, "addtobagID").click()
    
    def test_kohls_1c8b3d98(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("diamond stud earrings")
        self.driver.find_element(By.XPATH, "//li[@id='K1000_0']/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='10k Gold 1 Carat T.W. Black Diamond Stud Earrings']").click()
        self.driver.find_element(By.ID, "addtobagID").click()
    
    def test_kohls_5a15ea92(self):
        # self.driver.get("https://www.kohls.com/")
        self.driver.find_element(By.XPATH, "//ul[@id='top-nav-left']/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Women')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Swimwear')]").click()
        self.driver.find_element(By.XPATH, "//article[@id='tce-spotlight']/section[1]/div[2]/ul[1]/li[2]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='root_panel24013880']/div[7]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Color']/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.ID, "sbSelector_78498474").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low-High')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='panel24013913']/div[7]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='Occasion']/li[1]/a[1]/span[2]").click()
    