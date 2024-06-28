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
class TestGamestop:
    
    def test_gamestop_a2500e0b(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Polaris Fashion Place Mall - GameStop')]").click()
        self.driver.find_element(By.ID, "store-search-input").clear()
        self.driver.find_element(By.ID, "store-search-input").send_keys("90028")
        self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[3]/form[1]/div[1]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Set as Home Store')]").click()
    
    def test_gamestop_4dceb921(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("Elden Ring")
        self.driver.find_element(By.XPATH, "//div[@id='suggestion-item-0']/a[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='Elden Ring - PlayStation 5']").click()
        self.driver.find_element(By.XPATH, "//button[@id='ratings-summary']/div[3]/div[2]").click()
        self.driver.find_element(By.XPATH, "/html").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-reviews-accordion']/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]").click()
        self.driver.find_element(By.ID, "sortby-dropdown").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Highest to Lowest Rating')]").click()
    
    def test_gamestop_0d56ec88(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("external hard drive")
        self.driver.find_element(By.XPATH, "//div[@id='searchRedesignTemplate']/div[2]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[11]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[11]/div[2]/ul[1]/li[5]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
        self.driver.find_element(By.XPATH, "//button[@id='sortby-dropdown']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low To High')]").click()
    
    def test_gamestop_a34a5ed4(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/div[1]/a[1]/div[1]/div[2]/span[1]").click()
        self.driver.find_element(By.ID, "store-search-input").clear()
        self.driver.find_element(By.ID, "store-search-input").send_keys("21122")
        self.driver.find_element(By.ID, "radius").clear()
        self.driver.find_element(By.ID, "radius").select("50 Miles")
        self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[3]/form[1]/div[1]/div[3]/button[1]").click()
    
    def test_gamestop_757a129b(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("playstation 5 digital edition")
        self.driver.find_element(By.XPATH, "//div[@id='searchRedesignTemplate']/div[2]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='Sony PlayStation 5 Digital Edition Console']").click()
    
    def test_gamestop_000c2828(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='homepage']/div[3]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/div[1]/picture[1]/source[1]/source[1]/source[1]/source[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='catlanding-giftcards']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/picture[1]/source[1]/source[1]/source[1]/source[1]/img[1]").click()
        self.driver.find_element(By.ID, "recipientName").clear()
        self.driver.find_element(By.ID, "recipientName").send_keys("Tim Stebee")
        self.driver.find_element(By.ID, "recipientEmail").clear()
        self.driver.find_element(By.ID, "recipientEmail").send_keys("scisoorbros@gmail.com")
        self.driver.find_element(By.ID, "senderName").clear()
        self.driver.find_element(By.ID, "senderName").send_keys("Jeerimiah Waton")
        self.driver.find_element(By.XPATH, "//div[@id='gift-card-redesign']/div[1]/div[2]/div[3]/div[1]/form[1]/div[4]/button[1]").click()
    
    def test_gamestop_13cf0b14(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("kinect camera")
        self.driver.find_element(By.XPATH, "//div[@id='searchRedesignTemplate']/div[2]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='Microsoft Kinect for Xbox One']").click()
    
    def test_gamestop_1a2befd0(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop all')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[11]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View More')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[11]/div[2]/ul[1]/li[14]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
    
    def test_gamestop_2705de3e(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: Consoles']").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[5]/div[2]/ul[1]/li[1]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[8]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[8]/div[2]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[9]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[9]/div[2]/ul[1]/li[2]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[11]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[11]/div[2]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
        self.driver.find_element(By.XPATH, "//button[@id='sortby-dropdown']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low To High')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/a[1]/div[1]/p[1]").click()
    
    def test_gamestop_a3fc5023(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("resident evil")
        self.driver.find_element(By.XPATH, "//div[@id='suggestion-item-0']/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: Video Games']").click()
        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: Xbox Series X|S']").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/ul[1]/li[1]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[8]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[8]/div[2]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/a[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='primary-details-row']/div[7]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//li[@value='/video-games/products/resident-evil-4-deluxe-edition---xbox-series-x/358039.html']").click()
        self.driver.find_element(By.ID, "add-to-cart").click()
    
    def test_gamestop_716ed90e(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("playstation gift card $10")
        self.driver.find_element(By.XPATH, "//div[@id='searchRedesignTemplate']/div[2]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='PlayStation Store Gift Card $10']").click()
    
    def test_gamestop_7685e8ad(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
        self.driver.find_element(By.XPATH, "//ppc-content[contains(.,'View Jobs')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/span[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='State/ProvinceBody']/div[1]/div[2]/ul[1]/li[5]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/span[1]/button[1]/i[1]").click()
        self.driver.find_element(By.ID, "facetInput_2").clear()
        self.driver.find_element(By.ID, "facetInput_2").send_keys("fre")
        self.driver.find_element(By.XPATH, "//div[@id='CityBody']/div[1]/div[2]/ul[1]/li[2]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[3]/div[4]/div[1]/div[1]/span[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='HiringTypeBody']/div[1]/div[2]/ul[1]/li[2]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "sortselect").clear()
        self.driver.find_element(By.ID, "sortselect").select("Most recent")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply Now')]").click()
    
    def test_gamestop_8a6f2641(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[4]/div[1]/a[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trade']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/a[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: Nintendo Switch']").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[5]/div[2]/ul[1]/li[1]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[8]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[8]/div[2]/ul[1]/li[5]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
        self.driver.find_element(By.XPATH, "//button[@id='sortby-dropdown']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low To High')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Comic Coloring Book - Nintendo Switch')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Print')]").click()
    
    def test_gamestop_a513befc(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("nba2k23")
        self.driver.find_element(By.XPATH, "//div[@id='searchRedesignTemplate']/div[2]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='NBA 2K23 - PlayStation 5']").click()
        self.driver.find_element(By.XPATH, "//div[@id='add-to-cart-buttons']/div[1]/div[1]/button[1]").click()
    
    def test_gamestop_bd4b77db(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("Panini Diamonds Kings Baseball cards")
        self.driver.find_element(By.XPATH, "//div[@id='searchRedesignTemplate']/div[2]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='Panini Diamond Kings Baseball Cards Blaster Box - 2022']").click()
    
    def test_gamestop_c14078dd(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[3]/ul[1]/li[4]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='catlanding-giftcards']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]/picture[1]/source[1]/source[1]/source[1]/source[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//img[@title='PlayStation Store Gift Card $50']").click()
        self.driver.find_element(By.XPATH, "//div[@id='add-to-cart-buttons']/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='addedToCartModal']/div[1]/div[1]/div[1]/button[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='add-to-cart-buttons']/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='presentation']").click()
    
    def test_gamestop_d86d5cc1(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("trade in")
        self.driver.find_element(By.XPATH, "//div[@id='searchRedesignTemplate']/div[2]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trade']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/a[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Find values for games and more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Find values for games and more']").send_keys("Black Ops")
        self.driver.find_element(By.XPATH, "//div[@id='suggestions-wrapper']/div[1]/div[1]/div[2]/div[1]/div[6]/a[1]").click()
    
    def test_gamestop_f52ba76c(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: Consoles']").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[9]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[9]/div[2]/ul[1]/li[2]/a[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
    
    def test_gamestop_5418beec(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("BATMAN")
        self.driver.find_element(By.XPATH, "//div[@id='suggestion-item-0']/a[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: Collectibles']").click()
        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: Figures']").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[5]/div[2]/ul[1]/li[1]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[7]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[7]/div[2]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
    
    def test_gamestop_693ae151(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").send_keys("xbox 360 games")
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Search games, consoles & more']").click()
        self.driver.find_element(By.XPATH, "//p[@id='rightArrow']/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Price Low To High')]").click()
    
    def test_gamestop_f9062def(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[4]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trade']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/a[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Find values for games and more']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Find values for games and more']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='q' and @value='' and @type='search' and @placeholder='Find values for games and more']").send_keys("PS4")
        self.driver.find_element(By.XPATH, "//form[@id='tradeSimpleSearch']/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: Consoles & Hardware']").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[1]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
    
    def test_gamestop_91e18ec8(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='sg-navbar-collapse']/div[1]/div[1]/nav[1]/div[3]/div[1]/ul[2]/li[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/div[1]/div[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='refinementModal']/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/ul[1]/li[1]/a[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
    
    def test_gamestop_9653dc0d(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[4]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trade']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[7]/a[1]/div[1]/div[1]/picture[1]/source[1]/source[1]/source[1]/source[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sony DUALSHOCK 4 Wireless Controller for PlayStation 4')]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[6]/div[6]/div[1]/div[2]/div[2]/div[2]/div[6]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Store')]").click()
        self.driver.find_element(By.ID, "store-search-input").clear()
        self.driver.find_element(By.ID, "store-search-input").send_keys("43240")
        self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[3]/form[1]/div[1]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ae-main-content']/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/img[1]").click()
    
    def test_gamestop_981fdb06(self):
        # self.driver.get("https://gamestop.com")
        self.driver.find_element(By.XPATH, "//div[@id='header-redesign']/div[1]/div[4]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='trade']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/a[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='product-search-results']/div[1]/a[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//span[@title='Refine by Category: PlayStation 4']").click()
        self.driver.find_element(By.XPATH, "//button[@role='button' and @type='button']").click()
    