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
class TestCoinmarketcap:
    
    def test_coinmarketcap_5b224de7(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search coin, pair, contract address or exchange']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search coin, pair, contract address or exchange']").send_keys("xrp")
        self.driver.find_element(By.XPATH, "//div[@id='tippy-20']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]").click()
        self.driver.find_element(By.ID, "react-tabs-8").click()
    
    def test_coinmarketcap_5f0c4ebf(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[5]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[7]/button[1]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$0']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$0']").send_keys("100000000")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$999,999,999,999']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$999,999,999,999']").send_keys("1000000000")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[4]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='-100%']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='-100%']").send_keys("0")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='1,000%']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='1,000%']").send_keys("100")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[5]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$0']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='$0']").send_keys("10000000")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[6]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[2]/button[1]").click()
    
    def test_coinmarketcap_6f607b20(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[10]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("Dogecoin")
        self.driver.find_element(By.XPATH, "//p[contains(.,'Dogecoin')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Select 1 Coin')]").click()
    
    def test_coinmarketcap_73fff879(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/table[1]/tbody[1]/tr[5]/td[3]/div[1]/a[1]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[6]/div[1]/div[2]/div[1]/button[1]").click()
    
    def test_coinmarketcap_7de52c01(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/a[2]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Category']").click()
        self.driver.find_element(By.XPATH, "//div[@id='tippy-1']/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Platform']").click()
        self.driver.find_element(By.XPATH, "//div[@id='tippy-2']/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[3]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/p[1]/span[1]").click()
    
    def test_coinmarketcap_8247d9aa(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/table[1]/tbody[1]/tr[3]/td[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[6]/a[1]/div[1]").click()
    
    def test_coinmarketcap_85675087(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Exchanges')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[4]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@value='BSC']").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/thead[1]/tr[1]/th[7]/div[1]/div[1]/p[1]").click()
    
    def test_coinmarketcap_95638e8c(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search coin, pair, contract address or exchange']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search coin, pair, contract address or exchange']").send_keys("dogecoin")
        self.driver.find_element(By.XPATH, "//div[@id='tippy-15']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[1]/p[2]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Compare with']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Compare with']").send_keys("bitcoin")
        self.driver.find_element(By.XPATH, "//div[@id='tippy-3']/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.ID, "react-tabs-8").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tippy-4']/div[1]/div[1]/div[1]/div[1]/button[2]").click()
    
    def test_coinmarketcap_f6aced06(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/table[1]/tbody[1]/tr[13]/td[3]/div[1]/a[1]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Historical Data')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tippy-7']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tippy-7']/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/button[1]").click()
    
    def test_coinmarketcap_fb29f0cf(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/div[1]/div[2]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[2]/button[1]").click()
    
    def test_coinmarketcap_993878c1(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/div[1]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "react-select-cmc-select__from-option-2-7").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/button[1]/span[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='1' and @type='number' and @placeholder='Enter Amount to Convert']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='1' and @type='number' and @placeholder='Enter Amount to Convert']").send_keys("50")
    
    def test_coinmarketcap_a131cdc0(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Exchanges')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/thead[1]/tr[1]/th[4]/div[1]/div[1]/p[1]").click()
    
    def test_coinmarketcap_bdcdfd3f(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/span[1]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tippy-55']/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[18]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/a[1]/div[1]/div[1]/p[1]").click()
    
    def test_coinmarketcap_c328ad54(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[5]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[5]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='tippy-31']/div[1]/div[1]/div[1]/div[1]/button[2]").click()
    
    def test_coinmarketcap_12e66aec(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search coin, pair, contract address or exchange']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search coin, pair, contract address or exchange']").send_keys("cardano")
        self.driver.find_element(By.XPATH, "//div[@id='tippy-27']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[2]/button[1]/span[1]").click()
    
    def test_coinmarketcap_14cb7409(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/div[1]/div[3]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[3]").click()
    
    def test_coinmarketcap_281bb2ae(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search coin, pair, contract address or exchange']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search coin, pair, contract address or exchange']").send_keys("Bitcoin")
        self.driver.find_element(By.XPATH, "//div[@id='tippy-15']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[1]/p[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[3]/span[1]").click()
    
    def test_coinmarketcap_4cd31a67(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/a[3]").click()
    
    def test_coinmarketcap_4d8bd0d3(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/div[1]/div[3]/div[1]/a[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[3]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]").click()
    
    def test_coinmarketcap_54a41fe8(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/div[1]/div[1]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "react-select-cmc-select__from-option-2-1").click()
    
    def test_coinmarketcap_566d826e(self):
        # self.driver.get("https://coinmarketcap.com")
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/table[1]/tbody[1]/tr[3]/td[3]/div[1]/a[1]/div[1]/div[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/button[1]/span[1]").click()
    