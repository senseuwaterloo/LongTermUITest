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
class TestAdoptapet:
    
    def test_adoptapet_0114ee6c(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//h5[contains(.,'Shelters/Rescues')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[1]/div[1]/label[1]/span[2]").click()
        self.driver.find_element(By.ID, "location-4").clear()
        self.driver.find_element(By.ID, "location-4").send_keys("90011")
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/button[1]").click()
    
    def test_adoptapet_8cd3c1a2(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//h5[contains(.,'Shelters/Rescues')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[1]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("10012")
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[2]/div[1]/ul[1]/div[1]/div[2]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[2]/div[1]/ul[1]/div[2]/li[7]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[2]/div[2]/ul[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[2]/div[2]/ul[1]/div[2]/li[4]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'More')]").click()
    
    def test_adoptapet_95d4b13f(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//span[@title='Find a pet']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a cat')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[1]/div[1]/label[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[1]/div[1]/label[1]").send_keys("75209")
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[2]/ul[2]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[2]/ul[2]/div[2]/div[2]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pet-card-85']/a[1]/div[1]/div[1]/div[1]/img[1]").click()
    
    def test_adoptapet_4fbcf13b(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Blog')]").click()
        self.driver.find_element(By.ID, "s").clear()
        self.driver.find_element(By.ID, "s").send_keys("hypoallergenic")
        self.driver.find_element(By.ID, "searchsubmit").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Read More...')]").click()
    
    def test_adoptapet_6d5baec8(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//span[@title='Find a pet']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/header[1]/div[3]/div[1]/nav[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a shelter/rescue')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[1]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("21122")
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/button[1]").click()
    
    def test_adoptapet_44531ae3(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("33109")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Young')]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Male')]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Private owner')]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Spayed/Neutered')]").click()
    
    def test_adoptapet_b49c669d(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/header[1]/div[3]/div[1]/nav[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a dog')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("10019")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[1]/input[1]").send_keys("jack russell")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[2]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]/span[1]").send_keys("buckeye.foobar@gmail.com")
        self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/button[1]").click()
    
    def test_adoptapet_c740e976(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//h5[contains(.,'Cats')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[1]/div[1]/label[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[1]/div[1]/label[1]").send_keys("77494")
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[2]/ul[1]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[2]/ul[1]/div[2]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[2]/ul[2]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[2]/ul[2]/div[2]/div[1]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/ul[1]/div[1]/div[2]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'35 miles or less')]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'White')]").click()
    
    def test_adoptapet_d8707876(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("90028")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[1]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[1]/div[2]/div[4]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Spayed/Neutered')]").click()
    
    def test_adoptapet_c0420a0e(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//span[@title='Find a pet']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a dog')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("90028")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[1]/input[1]").send_keys("bulldog")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[2]/div[80]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Private owner')]").click()
    
    def test_adoptapet_247ed1e9(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("78613")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/div[1]/div[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'German Shepherd Dog')]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Young')]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Male')]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'White')]").click()
    
    def test_adoptapet_2a97a198(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//span[@title='Find a pet']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a dog')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("10019")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[1]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[1]/div[2]/div[3]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[1]/input[1]").send_keys("husky")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[2]/div[116]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_adoptapet_444b0e86(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//span[@title='Find a pet']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/header[1]/div[3]/div[1]/nav[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a cat')]").click()
        self.driver.find_element(By.XPATH, "/html").click()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[1]/div[1]/label[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[1]/div[1]/label[1]").send_keys("21122")
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='livewire-ui-modal']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "/html").click()
        self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder=' ']").click()
        self.driver.find_element(By.XPATH, "/html/body[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/div[2]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Maine Coon')]").click()
    
    def test_adoptapet_03dfedcb(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Learn more')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content-main']/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='text']").click()
        self.driver.find_element(By.XPATH, "//div[@id='content-main']/div[1]/div[1]/div[1]/div[3]/div[2]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='text' and @type='search']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='text' and @type='search']").send_keys("10017")
        self.driver.find_element(By.XPATH, "//div[@id='content-main']/div[1]/div[1]/div[1]/div[5]/div[2]/div[3]/div[1]/input[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content-main']/div[1]/div[1]/div[1]/div[5]/div[2]/div[3]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//div[@id='content-main']/div[1]/div[1]/div[1]/div[5]/div[2]/div[3]/div[1]/input[1]").send_keys("Belgian Shepherd")
        self.driver.find_element(By.XPATH, "//div[@id='content-main']/div[1]/div[1]/div[1]/div[5]/div[2]/div[3]/div[2]/ul[1]/li[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='content-main']/div[1]/div[1]/div[1]/div[5]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='email' and @type='text']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='email' and @type='text']").send_keys("abc@abc.com")
        self.driver.find_element(By.XPATH, "//div[@id='content-main']/div[1]/div[1]/div[1]/button[1]").click()
    
    def test_adoptapet_233c9a3e(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//span[@title='Find a pet']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a dog')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[1]/div[1]/label[1]").send_keys("90028")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[1]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[1]/div[2]/div[4]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[1]/input[1]").send_keys("boxer")
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/div[2]/ul[2]/div[2]/div[42]/div[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='dog-search']/div[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Male')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='pet-card-25']/a[1]/div[1]/div[1]/div[1]/img[1]").click()
    
    def test_adoptapet_7168a307(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//h5[contains(.,'Shelters/Rescues')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[1]/div[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("77084")
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[2]/div[1]/ul[1]/div[1]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[2]/div[1]/ul[1]/div[2]/li[4]/span[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[2]/div[2]/ul[1]/div[1]/div[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/div[2]/div[2]/ul[1]/div[2]/li[3]").click()
        self.driver.find_element(By.XPATH, "//form[@id='shelter-search']/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Small Animals')]").click()
    
    def test_adoptapet_7a91546b(self):
        # self.driver.get("https://adoptapet.com")
        self.driver.find_element(By.XPATH, "//h5[contains(.,'Cats')]").click()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[1]/div[1]/label[1]").clear()
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/div[1]/div[1]/label[1]").send_keys("90028")
        self.driver.find_element(By.XPATH, "//form[@id='cat-search']/div[1]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//label[contains(.,'Siamese')]").click()
    