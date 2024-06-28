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
class TestUdemy:
    
    def test_udemy_28c73a62(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//button[@id='u156-popper-trigger--1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-category-269']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-subcategory-102']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='header-browse-nav-level-three']/ul[1]/li[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[3]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u155-accordion-panel-title--270']/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[2]/svg[1]").click()
        self.driver.find_element(By.ID, "u155-form-group--224").clear()
        self.driver.find_element(By.ID, "u155-form-group--224").select("Highest Rated")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Material Ledger Actual Costing in SAP S4 Hana Controlling')]").click()
        self.driver.find_element(By.XPATH, "//body[@id='udemy']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='udemy']/div[13]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='udemy']/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
    
    def test_udemy_43517267(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//button[@id='u148-popper-trigger--1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-category-269']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-subcategory-116']/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u44-accordion-panel-title--73']/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[2]").click()
        self.driver.find_element(By.ID, "u44-form-group--11").clear()
        self.driver.find_element(By.ID, "u44-form-group--11").select("Newest")
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
    
    def test_udemy_9d5a39ec(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//body[@id='udemy']/div[1]/div[3]/footer[1]/div[1]/div[1]/ul[2]/li[5]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Events & Presentations')]").click()
    
    def test_udemy_ad61cc39(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//body[@id='udemy']/div[1]/div[2]/div[1]/main[1]/section[1]/div[1]/a[4]/div[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Amazon AWS')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Amazon EC2')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='u185-scroll-port--3']/div[1]/a[1]/div[2]/div[1]").click()
    
    def test_udemy_b4279cf6(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.ID, "u36-search-form-autocomplete--3").click()
        self.driver.find_element(By.ID, "u36-search-form-autocomplete--3").clear()
        self.driver.find_element(By.ID, "u36-search-form-autocomplete--3").send_keys("Python courses for beginners")
        self.driver.find_element(By.XPATH, "//svg[@role='img']").click()
        self.driver.find_element(By.ID, "u169-form-group--23").clear()
        self.driver.find_element(By.ID, "u169-form-group--23").select("Highest Rated")
    
    def test_udemy_c35ea9f3(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//button[@id='u284-popper-trigger--1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-category-288']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-subcategory-8']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='header-browse-nav-level-three']/ul[1]/li[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u86-tabs--19-tab-2']/span[1]").click()
    
    def test_udemy_ce14c7e4(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//button[@id='u55-popper-trigger--1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-category-296']/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u105-tabs--30-tab-2']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Excel Deep Dive: Pivot Tables Workshop')]").click()
        self.driver.find_element(By.XPATH, "//body[@id='udemy']/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]/svg[1]").click()
    
    def test_udemy_e782bd39(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//button[@id='u19-popper-trigger--1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-category-268']/div[1]").click()
        self.driver.find_element(By.ID, "u30-form-group--37").clear()
        self.driver.find_element(By.ID, "u30-form-group--37").select("Most Popular")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'The Complete SQL Bootcamp: Go from Zero to Hero')]").click()
        self.driver.find_element(By.XPATH, "//body[@id='udemy']/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[9]/div[1]/div[1]/div[1]/div[3]/div[2]/button[1]").click()
    
    def test_udemy_7e03082e(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Drawing')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Pencil Drawing')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sketching')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.ID, "u105-form-group--164").clear()
        self.driver.find_element(By.ID, "u105-form-group--164").select("Highest Rated")
    
    def test_udemy_80d27032(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.ID, "u183-search-form-autocomplete--3").clear()
        self.driver.find_element(By.ID, "u183-search-form-autocomplete--3").send_keys("java")
        self.driver.find_element(By.ID, "u183-search-form-autocomplete--3").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/svg[1]").click()
        self.driver.find_element(By.ID, "u31-form-group--13").clear()
        self.driver.find_element(By.ID, "u31-form-group--13").select("Highest Rated")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Software Testing Bootcamp (2023): From Beginner to Expert')]").click()
        self.driver.find_element(By.XPATH, "//body[@id='udemy']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]").click()
    
    def test_udemy_8ca49b7b(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//button[@id='u91-popper-trigger--1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-category-288']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-subcategory-14']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='header-browse-nav-level-three']/ul[1]/li[2]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[5]/svg[1]").click()
    
    def test_udemy_949e33a5(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.ID, "u148-search-form-autocomplete--3").clear()
        self.driver.find_element(By.ID, "u148-search-form-autocomplete--3").send_keys("home workout")
        self.driver.find_element(By.XPATH, "//a[@id='u148-search-form-autocomplete--3-0']/div[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u83-accordion-panel-title--239']/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u83-accordion-panel-title--283']/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u83-accordion-panel-title--254']/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[3]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u83-accordion-panel-title--276']/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[2]/svg[1]").click()
        self.driver.find_element(By.ID, "u83-form-group--198").clear()
        self.driver.find_element(By.ID, "u83-form-group--198").select("Newest")
    
    def test_udemy_4712364d(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//button[@id='u156-popper-trigger--1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-category-268']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-subcategory-26']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='header-browse-nav-level-three']/ul[1]/li[6]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u29-tabs--19-tab-2']/span[1]").click()
    
    def test_udemy_4e90dc8a(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//button[@id='u221-popper-trigger--1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-category-268']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-subcategory-28']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='header-browse-nav-level-three']/ul[1]/li[3]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
    
    def test_udemy_4f9997df(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//a[@id='u213-popper-trigger--5']/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='udemy']/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]").click()
    
    def test_udemy_55025267(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//button[@id='u108-popper-trigger--1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-category-294']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-subcategory-138']/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='header-browse-nav-level-three']/ul[1]/li[2]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[5]/svg[1]").click()
        self.driver.find_element(By.ID, "u77-form-group--218").clear()
        self.driver.find_element(By.ID, "u77-form-group--218").select("Newest")
    
    def test_udemy_672ee0b8(self):
        # self.driver.get("https://www.udemy.com/")
        self.driver.find_element(By.XPATH, "//button[@id='u94-popper-trigger--1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-category-276']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='header-browse-nav-subcategory-242']/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sound Therapy')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u119-accordion-panel-title--231']/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='u119-accordion-panel-title--261']/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='filter-form']/div[1]/div[8]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[3]/svg[1]").click()
    