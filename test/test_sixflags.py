import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from browser_helper import scroll_down


@pytest.mark.usefixtures("setup_class")
class TestSixflags:
    
    # def test_sixflags_a52fcf7a(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[9]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-16807824943263699-5']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tickets & Passes')]").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='post-222922']/div[1]/div[1]/div[1]/div[1]/section[7]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[3]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "next-btn").click()
    #     self.driver.find_element(By.ID, "firstName").clear()
    #     self.driver.find_element(By.ID, "firstName").send_keys("Jame")
    #     self.driver.find_element(By.ID, "lastName").clear()
    #     self.driver.find_element(By.ID, "lastName").send_keys("Jones")
    #     self.driver.find_element(By.ID, "email").clear()
    #     self.driver.find_element(By.ID, "email").send_keys("jame_jones@hotmail.com")
    #     self.driver.find_element(By.ID, "zipCode").clear()
    #     self.driver.find_element(By.ID, "zipCode").send_keys("10005")
    #     self.driver.find_element(By.ID, "age").clear()
    #     self.driver.find_element(By.ID, "age").send_keys("35")
    #     self.driver.find_element(By.XPATH, "//div[@id='pass-type-selection-container']/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pass-type-selection-container']/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/div[2]/div[5]/div[1]/div[1]/div[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[2]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.ID, "modal-ok-btn").click()
    #
    # def test_sixflags_02aaea66(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[9]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-16807832506760938-13']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='sm-16807832506760938-14']/li[14]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "dp1680783264218").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'21')]").click()
    #     self.driver.find_element(By.ID, "dp1680783264219").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'24')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.ID, "sbSelector_72125332").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'1')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Themed')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='avCont']/div[2]/div[6]/div[1]/div[3]/div[6]/div[1]/a[1]/span[1]").click()
    #
    # def test_sixflags_19b955ba(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs')]").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='post-354953']/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='post-354953']/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div[3]/a[2]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='post-354953']/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='post-240203']/div[1]/div[1]/div[1]/div[1]/section[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[2]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply now')]").click()
    #
    # def test_sixflags_374f69aa(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[10]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-16813419461804138-9']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Family Rides')]").click()
    #
    # def test_sixflags_ee1e95ab(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-16807820539749233-5']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pass Add-Ons')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Buy Now')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='package-list-item-0-0']/div[2]/div[1]/span[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
    #     self.driver.find_element(By.ID, "next-btn").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cart-view-page-buttons']/div[2]/div[2]/button[1]").click()
    #
    # def test_sixflags_38fb3573(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "sm-1679981237123882-9").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Thrill Rides')]").click()
    #
    # def test_sixflags_f968b06b(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[9]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-1681346329834657-5']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Deals')]").click()
    #
    # def test_sixflags_c3e841d5(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "sm-1679369987310896-1").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tickets & Passes')]").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='post-211203']/div[1]/div[1]/div[1]/div[1]/section[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/button[1]").click()
    #     self.driver.find_element(By.ID, "next-btn").click()
    #     self.driver.find_element(By.XPATH, "//span[@role='button' and @title='']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[2]/div[1]/div[2]/button[1]").click()
    #
    # def test_sixflags_c4538b84(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='page']/div[1]/div[1]/section[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]").click()
    #
    # def test_sixflags_caafd610(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[13]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-16813461625851528-7']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Mapa del Parque')]").click()
    #
    # def test_sixflags_dc1f0824(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[11]/a[2]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-16813418445371646-11']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See all events')]").click()
    #
    # def test_sixflags_df73be67(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[9]/a[2]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-1681346758871876-9']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Shops & Gifts')]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='shop_category']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='shop_category']").select("Gifts")
    #
    # def test_sixflags_e0feee24(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Investors')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='MainWrapper']/div[3]/nav[1]/ul[1]/li[4]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='twocolright']/div[1]/h1[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='tabs-nav-cash-flow-level3']/a[1]/span[1]").click()
    #
    # def test_sixflags_5b56d5b8(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/a[2]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-16793701409299702-9']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tickets & Passes')]").click()
    #
    # def test_sixflags_607cea69(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "sm-16813416023695874-3").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='post-113811']/div[1]/div[1]/div[1]/div[1]/section[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Request Information')]").click()
    #
    # def test_sixflags_b4362dec(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-16813465497178574-5']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='sm-16813465497178574-6']/li[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Buy Now')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='desktop-navigation']/div[6]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='desktop-navigation']/div[6]/ul[1]/li[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='package-list-item-0-0']/div[2]/div[1]/img[1]").click()
    #     self.driver.find_element(By.ID, "next-btn").click()
    #
    # def test_sixflags_5098c679(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[7]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-16813548894703142-13']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='sm-16813548894703142-14']/li[10]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Security')]").click()
    #
    # def test_sixflags_930803d7(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Groups')]").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='post-126775']/div[1]/div[1]/div[1]/div[1]/section[9]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/a[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='row3-cell22']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/button[1]").click()
    #
    # def test_sixflags_a11022ab(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.ID, "form-field-first_name").clear()
    #     self.driver.find_element(By.ID, "form-field-first_name").send_keys("Dick")
    #     self.driver.find_element(By.ID, "form-field-last_name").clear()
    #     self.driver.find_element(By.ID, "form-field-last_name").send_keys("Smith")
    #     self.driver.find_element(By.ID, "form-field-email").clear()
    #     self.driver.find_element(By.ID, "form-field-email").send_keys("smith@gmail.com")
    #     self.driver.find_element(By.ID, "form-field-park_preference").clear()
    #     self.driver.find_element(By.ID, "form-field-park_preference").select("Six Flags Magic Mountain / Los Angeles, CA")
    #     self.driver.find_element(By.XPATH, "//button[@id='news_letter_form_submit']/span[1]").click()
    #
    # def test_sixflags_8f4a020d(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "sm-16807037116655586-5").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='sm-16807037116655586-6']/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@role='button']").click()
    #     self.driver.find_element(By.ID, "next-btn").click()
    #     self.driver.find_element(By.ID, "dynamic-form-field-0").clear()
    #     self.driver.find_element(By.ID, "dynamic-form-field-0").send_keys("Neo")
    #     self.driver.find_element(By.ID, "dynamic-form-field-2").clear()
    #     self.driver.find_element(By.ID, "dynamic-form-field-2").send_keys("Thomas")
    #     self.driver.find_element(By.ID, "dynamic-form-field-4").clear()
    #     self.driver.find_element(By.ID, "dynamic-form-field-4").send_keys("05/05/1995")
    #     self.driver.find_element(By.ID, "dynamic-form-field-6").clear()
    #     self.driver.find_element(By.ID, "dynamic-form-field-6").send_keys("Texas city")
    #     self.driver.find_element(By.ID, "dynamic-form-field-8").clear()
    #     self.driver.find_element(By.ID, "dynamic-form-field-8").send_keys("252-654-5258")
    #     self.driver.find_element(By.ID, "dynamic-form-field-1").clear()
    #     self.driver.find_element(By.ID, "dynamic-form-field-1").send_keys("thomas.neo@gmail.com")
    #     self.driver.find_element(By.ID, "dynamic-form-field-3").clear()
    #     self.driver.find_element(By.ID, "dynamic-form-field-3").send_keys("Anderson")
    #     self.driver.find_element(By.ID, "dynamic-form-field-5").clear()
    #     self.driver.find_element(By.ID, "dynamic-form-field-5").send_keys("po box 2846")
    #     self.driver.find_element(By.ID, "dynamic-form-field-7").clear()
    #     self.driver.find_element(By.ID, "dynamic-form-field-7").send_keys("Texas")
    #     self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cart-view-page-buttons']/div[2]/div[2]/button[1]").click()
    #     self.driver.find_element(By.ID, "next-btn").click()
    #
    # def test_sixflags_0fd460cc(self):
    #     # self.driver.get("https://sixflags.com")
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/a[3]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='sm-16813417254371912-3']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='sm-16813417254371912-4']/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//article[@id='post-298248']/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[9]/div[1]/div[1]/a[1]/span[1]/span[1]").click()

    def test_sixflags_521d9006(self):
        # self.driver.get("https://sixflags.com")

        # self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='parkselector']//div[@class='sf-dropdown']//button[./div[text()='Browse the Parks Below']]").click()

        # self.driver.find_element(By.XPATH, "//section[@id='parkselector']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='parkselector']//a[@class='single-park-desktop' and @data-title='Six Flags Magic Mountain' and @data-state='Los Angeles, CA']").click()

        self.driver.find_element(By.XPATH, "//section[@id='parkselector']//div[@class='sf-dropdown']//button[text()='Go!']").click()

        # self.driver.find_element(By.ID, "sm-16807812394218174-1").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Group Tickets')]").click()
        # self.driver.find_element(By.XPATH, "//article[@id='post-113811']/div[1]/div[1]/div[1]/div[1]/section[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//nav[not(@aria-hidden='true')]//a[text()='Groups' and ./span[@aria-label='Menu Toggle' and @role='application'] and ./span[@class='sub-arrow']]").click()
        scroll_down(self.driver, 600)
        self.driver.find_element(By.XPATH, "//button[@class='btn_show_hide card_icon' and ./parent::div/div[1]/h3[text()='Groups of 15 to 99']]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Buy Tickets')]").click()

        # No need to select a time slot, just use the default time slot
        # self.driver.find_element(By.XPATH, "//button[@id='row3-cell30']/span[1]").click()

        # need add switch to frame action
        override_iframe = self.driver.find_element(By.ID, "override").get_native_element()
        self.driver.switch_to.frame(override_iframe)

        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//button[./gap-button-label[text()='Buy Now']]").click()
        # need to use Action class because click will be intercepted by its parent element
        buy_now_button = self.driver.find_element(By.XPATH, "//button[./gap-button-label[text()='Buy Now']]").get_native_element()
        # action = ActionChains(self.driver)
        # action.move_to_element(buy_now_button)
        # action.click().perform()
        # somehow Action class is not working: code passed but no click action triggered, so try to use JS click
        self.driver.execute_script("arguments[0].click()", buy_now_button)

        # self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
        # self.driver.find_element(By.XPATH, "//span[@title='Increase']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/ng-form[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/ng-form[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/ng-form[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/ng-form[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[2]/button[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[2]/ng-form[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@title='Increase']").click()
        self.driver.find_element(By.XPATH, "//button[@title='Increase']").click()
        self.driver.find_element(By.XPATH, "//button[@title='Increase']").click()
        self.driver.find_element(By.XPATH, "//button[@title='Increase']").click()
        self.driver.find_element(By.XPATH, "//button[@title='Increase']").click()

        self.driver.find_element(By.ID, "next-btn").click()
        self.driver.find_element(By.ID, "groupName").clear()
        self.driver.find_element(By.ID, "groupName").send_keys("Crew")
        self.driver.find_element(By.ID, "firstName").clear()
        self.driver.find_element(By.ID, "firstName").send_keys("James")
        self.driver.find_element(By.ID, "lastName").clear()
        self.driver.find_element(By.ID, "lastName").send_keys("Johnson")
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys("james.john@gmail.com")

        # self.driver.find_element(By.XPATH, "//select[@name='orgType' and @title='Organization Type']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='orgType' and @title='Organization Type']").select("Family Trip")
        self.driver.find_element(By.ID, "orgType").click()
        self.driver.find_element(By.XPATH, "//span[text()='Family Trip']").click()

        self.driver.find_element(By.ID, "orgName").clear()
        self.driver.find_element(By.ID, "orgName").send_keys("Johnson")

        # self.driver.find_element(By.XPATH, "//div[@id='application-view']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @ng-click='nextView()']").click()
