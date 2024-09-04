import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestTarget:
    
    # def test_target_1a13b675(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.ID, "search").clear()
    #     self.driver.find_element(By.ID, "search").send_keys("bed sheets queen")
    #     self.driver.find_element(By.XPATH, "//ul[@id='typeahead']/li[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "addToCartButtonOrTextIdFor88027887").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Add to cart')]").click()
    #
    # def test_target_1c2baca4(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:Riq97ba6:']/div[1]/div[1]/div[1]/a[19]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:Riq97ba6:']/div[1]/div[1]/div[2]/a[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore All')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[23]/div[1]/div[1]/div[2]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//label[contains(.,'Price-low to high')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[33]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[23]/div[1]/div[1]/div[2]/button[2]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[34]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[34]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[23]/div[1]/div[1]/div[2]/button[4]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[36]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[36]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[23]/div[1]/div[1]/div[2]/button[5]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[37]/div[1]/div[1]/div[2]/div[6]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[37]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[23]/div[1]/div[1]/div[2]/button[6]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[38]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[38]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[23]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[2]").click()
    #     self.driver.find_element(By.ID, "addToCartButtonOrTextIdFor75665848").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'24')]").click()
    #
    # def test_target_cb24d074(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.ID, "search").clear()
    #     self.driver.find_element(By.ID, "search").send_keys("throw pillows")
    #     self.driver.find_element(By.XPATH, "//ul[@id='typeahead']/li[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[5]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[28]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Update')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[6]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[29]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Update')]").click()
    #
    # def test_target_e617d6c6(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='footer']/div[1]/div[1]/a[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "tb-search-submit").click()
    #     self.driver.find_element(By.ID, "category-toggle").click()
    #     self.driver.find_element(By.ID, "category-filter-8").click()
    #     self.driver.find_element(By.ID, "country-toggle").click()
    #     self.driver.find_element(By.ID, "country-filter-1").click()
    #     self.driver.find_element(By.ID, "region-toggle").click()
    #     self.driver.find_element(By.ID, "region-filter-6").click()
    #     self.driver.find_element(By.ID, "city-toggle").click()
    #     self.driver.find_element(By.ID, "city-filter-1").click()
    #
    # def test_target_9a6622b0(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:r5g:']/div[1]/div[1]/div[1]/a[4]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:r5g:']/div[1]/div[1]/div[2]/a[3]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:r5g:']/div[1]/div[1]/div[2]/a[4]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[14]/div[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//label[contains(.,'Price-low to high')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[33]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[14]/div[1]/div[1]/div[2]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Cheese Pizzas')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[34]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[14]/div[1]/div[1]/div[2]/button[7]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[39]/div[1]/div[1]/div[2]/div[3]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[39]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[14]/div[1]/div[1]/div[2]/button[8]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[40]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[40]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[14]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #
    # def test_target_08f78082(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.ID, "utilityNav-findStores").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View store directory')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Texas')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Magnolia')]").click()
    #
    # def test_target_44bde32f(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:Riq97ba6:']/div[1]/div[1]/div[1]/a[3]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:Riq97ba6:']/div[1]/div[1]/div[2]/div[1]/a[4]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]/div[1]/div[1]/div[1]/picture[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[25]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[25]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #
    # def test_target_632bb279(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.ID, "search").clear()
    #     self.driver.find_element(By.ID, "search").send_keys("winter coat")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[24]/div[1]/div[1]/div[2]/div[4]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Update')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[27]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Update')]").click()
    #
    # def test_target_6803cd71(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.ID, "search").clear()
    #     self.driver.find_element(By.ID, "search").send_keys("organic dog food")
    #     self.driver.find_element(By.XPATH, "//ul[@id='typeahead']/li[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tender & True Organic Small Breed Chicken and Liver Recipe Dry Dog Food - 4lb')]").click()
    #     self.driver.find_element(By.ID, "addToCartButtonOrTextIdFor81398282").click()
    #
    # def test_target_80e12375(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:ri0:']/div[1]/div[1]/div[1]/a[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:ri0:']/div[1]/div[1]/div[2]/a[3]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:ri0:']/div[1]/div[1]/div[2]/a[4]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[16]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[16]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[19]/div[1]/div[1]/div[2]/div[12]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[19]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[18]/div[1]/div[1]/div[2]/div[6]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[18]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/div[1]/div[1]/h2[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Self-Rising Crust Uncured Pepperoni Frozen Pizza - 30oz - Good & Gather™')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='select-:rq9:']/span[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(@href, 'link://#')]").click()
    #     self.driver.find_element(By.ID, "addToCartButtonOrTextIdFor79226810").click()
    #
    # def test_target_cc27fdda(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.ID, "utilityNav-findStores").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[2]/div[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "city").click()
    #     self.driver.find_element(By.ID, "city").clear()
    #     self.driver.find_element(By.ID, "city").send_keys("Cincinnati")
    #     self.driver.find_element(By.ID, "state").clear()
    #     self.driver.find_element(By.ID, "state").select("OH")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/form[1]/div[2]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[2]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[3]/div[1]/div[2]/div[3]/div[3]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[2]/div[2]/button[1]").click()
    #
    # def test_target_2c19d467(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:Riq97ba6:']/div[1]/div[1]/div[1]/a[24]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:Riq97ba6:']/div[1]/div[1]/div[2]/a[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[4]/a[1]/div[1]/div[1]/div[1]/div[1]/picture[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[23]/div[1]/div[1]/div[2]/button[7]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[39]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[39]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[23]/div[1]/div[1]/div[2]/button[17]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[49]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[49]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/svg[1]").click()
    #
    # def test_target_2f660153(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Categories')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:rbp:']/div[1]/div[1]/div[1]/a[10]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='overlay-:rbp:']/div[1]/div[1]/div[2]/a[8]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore All')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[15]/div[1]/div[1]/div[2]/div[6]/div[1]/label[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[15]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #
    # def test_target_33064851(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.ID, "utilityNav-registries").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.ID, "RegistrantsName-firstName").click()
    #     self.driver.find_element(By.ID, "RegistrantsName-firstName").clear()
    #     self.driver.find_element(By.ID, "RegistrantsName-firstName").send_keys("SHELDON")
    #     self.driver.find_element(By.ID, "RegistrantsName-lastName").click()
    #     self.driver.find_element(By.ID, "RegistrantsName-lastName").clear()
    #     self.driver.find_element(By.ID, "RegistrantsName-lastName").send_keys("COOPER")
    #     self.driver.find_element(By.XPATH, "//div[@id='true']/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.ID, "sortList3").clear()
    #     self.driver.find_element(By.ID, "sortList3").select("Arizona")
    #     self.driver.find_element(By.ID, "sortList").clear()
    #     self.driver.find_element(By.ID, "sortList").select("Date - latest to soonest")
    #
    # def test_target_eb9995b5(self):
    #     # self.driver.get("https://www.target.com/")
    #     self.driver.find_element(By.ID, "search").clear()
    #     self.driver.find_element(By.ID, "search").send_keys("Nintendo Switch")
    #     self.driver.find_element(By.XPATH, "//ul[@id='typeahead']/li[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h3[1]/div[1]/div[1]/a[1]/div[1]/picture[1]/source[1]/source[1]/source[1]/source[1]/source[1]/source[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/button[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/h3[1]/span[3]/button[1]").click()
    
    def test_target_274571ea(self):
        # self.driver.get("https://www.target.com/")

        # self.driver.find_element(By.XPATH, "//button[@id='web-store-id-msg-btn']/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//button[@id='web-store-id-msg-btn']/div[1]/span[1]").click()

        self.driver.find_element(By.ID, "zip-or-city-state").clear()
        self.driver.find_element(By.ID, "zip-or-city-state").send_keys("25504")
        self.driver.find_element(By.XPATH, "//button[contains(.,'Look up')]").click()
        self.driver.find_element(By.XPATH, "//h4[contains(.,'Barboursville')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'More info')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'More info') and @aria-label='More info about Barboursville store']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[3]/div[1]/div[1]/div[2]/div[1]/div[3]/button[2]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Shop this store']").click()

        # self.driver.find_element(By.XPATH, "//nav[@id='headerPrimary']/a[1]/span[1]/div[1]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[13]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/div[2]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[5]/a[1]/div[1]/div[2]/span[1]").click()
        # since it's not easter now, easter egg is not in the dropdown menu now, so search for easter egg instead
        self.driver.find_element(By.ID, "search").clear()
        self.driver.find_element(By.ID, "search").send_keys("Easter Eggs")
        self.driver.find_element(By.ID, "search").send_keys(Keys.RETURN)

        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@data-test='@web/SlotRenderer']//button[@data-test='facet-button-Type']").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[24]/div[1]/div[1]/div[2]/div[4]/div[1]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Fillable Eggs' and ./parent::span]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Prefilled Eggs' and ./parent::span]").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[24]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Apply']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@data-test='@web/SlotRenderer']//button[@data-test='facet-button-Price']").click()

        # self.driver.find_element(By.ID, "minPriceValue").clear()
        # self.driver.find_element(By.ID, "minPriceValue").send_keys("5")
        # self.driver.find_element(By.ID, "maxPriceValue").clear()
        # self.driver.find_element(By.ID, "maxPriceValue").send_keys("10")
        self.driver.find_element(By.XPATH, "//span[contains(text(), '$5 ') and contains(text(), '–') and contains(text(), ' $9.99') and ./parent::span]").click()

        # self.driver.find_element(By.XPATH, "/html/body[1]/div[25]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Apply']").click()

        # omit the material filter since only one result is returned from above
        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/button[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/div[27]/div[1]/div[1]/div[2]/div[3]/div[1]/label[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/div[27]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[8]/button[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/div[31]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "/html/body[1]/div[31]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='pageBodyContainer']/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[1]/h2[1]").click()
        # self.driver.find_element(By.ID, "addToCartButtonOrTextIdFor83429711").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'View cart & check out')]").click()
        # click on shipping instead of pickup since it is not available for pick up
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@data-test='@web/SlotRenderer']//span[@data-test='facetHeading' and text()='Shipping']").click()
        self.driver.find_element(By.XPATH, "//div[@data-module-type='ProductListGrid']//section[@class]/div[1]/div[1]//button[contains(@id, 'addToCartButtonOrTextIdFor')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    