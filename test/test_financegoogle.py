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
class TestFinanceGoogle:
    
    def test_financegoogle_9238497a(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("Microsoft")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp2180']/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[2]/div[1]/div[4]/div[1]/main[1]/div[2]/div[1]/div[1]/c-wiz[1]/div[1]/div[2]/div[2]/span[3]/div[1]/button[1]/span[1]").click()
    
    def test_financegoogle_9ccb15ec(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("Bitcoin")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp26910']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='5dayTab']/span[2]").click()
    
    def test_financegoogle_b9f1cc21(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/div[1]/div[1]/c-wiz[1]/div[1]/c-wiz[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "c243").clear()
        self.driver.find_element(By.ID, "c243").send_keys("AI Stocks")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
    
    def test_financegoogle_6a2d982c(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("WWE")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp2050']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='1monthTab']/span[2]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[2]/div[1]/div[4]/div[1]/main[1]/div[2]/div[1]/div[1]/c-wiz[1]/div[1]/div[4]/svg[1]/g[1]/g[5]/rect[1]").click()
    
    def test_financegoogle_6f8b5ff4(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("AMC")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp1240']/div[1]/div[1]/div[1]/div[1]").click()
    
    def test_financegoogle_91dc65f9(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[3]").click()
        self.driver.find_element(By.ID, "market-rundown-heading").click()
        self.driver.find_element(By.XPATH, "//button[@id='1yearTab']/span[2]").click()
    
    def test_financegoogle_4b7571c7(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("Tesla")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp16110']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/span[1]/svg[1]/path[1]").click()
    
    def test_financegoogle_5b20e07c(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("Euro")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp6221']/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/div[1]").click()
    
    def test_financegoogle_5bf46b56(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("Google")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp1940']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[2]/div[1]/div[4]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/div[1]").click()
    
    def test_financegoogle_67240082(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/div[1]/div[2]/c-wiz[2]/div[1]/div[2]/a[3]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/div[1]/div[5]/div[1]/div[1]/span[1]/span[1]/i[1]").click()
    
    def test_financegoogle_d78d07bf(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/div[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[5]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "c236").clear()
        self.driver.find_element(By.ID, "c236").send_keys("AI")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/c-wiz[1]/div[2]/div[1]/div[2]/div[1]/div[1]/c-wiz[1]/div[1]/div[1]/div[1]/div[1]/div[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("Artificial")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp8850']/div[1]/div[1]/div[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/i[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]").click()
    
    def test_financegoogle_c82daba5(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//header[@id='gb']/div[2]/div[1]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//a[@role='menuitem' and @title='Market trends']").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[5]").click()
    
    def test_financegoogle_d1b599ef(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("walt disney")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp2020']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[2]/div[1]/div[4]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/div[1]").click()
    
    def test_financegoogle_d69f6b51(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("testla")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp11580']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/main[1]/div[2]/div[1]/div[1]/c-wiz[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/main[1]/div[2]/div[1]/div[1]/c-wiz[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/main[1]/div[2]/div[1]/div[1]/c-wiz[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[2]").send_keys("Ford")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp14711']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='6monthTab']/span[2]").click()
    
    def test_financegoogle_0057b088(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("netflix")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp17060']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/div[3]").click()
    
    def test_financegoogle_d90d474b(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("]AMC")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp21680']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='1monthTab']/span[2]").click()
    
    def test_financegoogle_f7d74ebf(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[1]/div[1]/div[4]/div[1]/div[1]/div[2]/c-wiz[2]/div[1]/div[2]/a[5]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[2]/div[1]/div[4]/div[1]/div[1]/div[1]/button[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[1]/section[1]/div[2]/div[2]/button[1]/img[1]").click()
    
    def test_financegoogle_04c351a7(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("Ether")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp11230']/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@title='Bitcoin (BTC / USD)']").click()
    
    def test_financegoogle_1f7ceb24(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/div[1]/div[2]/c-wiz[2]/div[1]/div[2]/a[4]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/div[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/main[1]/div[2]/div[1]/div[1]/c-wiz[1]/div[1]/div[2]/div[2]/span[1]/div[1]/button[1]/span[1]").click()
    
    def test_financegoogle_33fc9bc6(self):
        # self.driver.get("https://www.google.com/finance/")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/div[4]/div[1]/div[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
        self.driver.find_element(By.ID, "c837").clear()
        self.driver.find_element(By.ID, "c837").send_keys("Tech Stocks")
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/c-wiz[3]/div[1]/c-wiz[1]/div[2]/div[1]/div[2]/div[1]/div[1]/c-wiz[1]/div[1]/div[1]/div[1]/div[1]/div[4]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[2]").clear()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[2]").send_keys("Microsoft")
        self.driver.find_element(By.XPATH, "//div[@id='nngdp24380']/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/i[1]").click()
        self.driver.find_element(By.XPATH, "//body[@id='yDmH0d']/div[11]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]/div[3]").click()
    