import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestTwitter:
    
    # def test_twitter_d6ecc3ea(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/a[7]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//textarea[@name='description']").clear()
    #     self.driver.find_element(By.XPATH, "//textarea[@name='description']").send_keys("Explorer and Wanderer")
    #     self.driver.find_element(By.XPATH, "//div[@id='layers']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]/span[1]").click()
    #
    # def test_twitter_a1147322(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").send_keys("SpaceX")
    #     self.driver.find_element(By.XPATH, "//div[@id='typeaheadDropdown-3']/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='id__s8km0lwttc']/div[3]/div[1]/div[1]/div[1]/svg[1]/g[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='id__s8km0lwttc']/div[5]/div[1]/div[1]/div[1]/div[1]/svg[1]/g[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='layers']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/span[1]").click()
    #
    # def test_twitter_7d55a077(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").send_keys("@amazon")
    #     self.driver.find_element(By.XPATH, "//div[@id='typeaheadDropdown-7']/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
    #
    # def test_twitter_9495b2d9(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").send_keys("Dallas Cowboys")
    #     self.driver.find_element(By.XPATH, "//div[@id='typeaheadDropdown-4']/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]").click()

    def test_twitter_2e64ac92(self):
        # self.driver.get("https://twitter.com")
        # uiteststudy@gmail.com:Pass4Twitter!
        # add extra login step
        self.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
        self.driver.find_element(By.NAME, "text").clear()
        self.driver.find_element(By.NAME, "text").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("Pass4Twitter!")
        self.driver.find_element(By.XPATH, "//span[text()='Log in']").click()
        time.sleep(3)
        # TODO: Consider removing twitter from the subjects because human verification is needed

        # Following steps are not fixed
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").send_keys("Elon Musk")
        self.driver.find_element(By.XPATH, "//div[@id='typeaheadDropdown-4']/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='layers']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='layers']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='id__m0wp09vxxyg']/div[3]/div[1]/div[1]/div[1]/svg[1]").click()

    # def test_twitter_4bac0990(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").send_keys("super bowl")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='super bowl' and @type='text' and @placeholder='Search Twitter']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='id__nlv5c2v1dx']/div[3]/div[1]/div[1]/div[1]/svg[1]").click()
    #
    # def test_twitter_5c1e0e35(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").send_keys("Football")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='Football' and @type='text' and @placeholder='Search Twitter']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]").click()
    #
    # def test_twitter_60cd970c(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/a[4]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/a[1]/div[1]/span[1]/span[1]").click()
    #
    # def test_twitter_6741baf0(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='typeaheadDropdown-10']/div[1]/div[2]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='layers']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]").click()
    #
    # def test_twitter_753bf34d(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").send_keys("food")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='food' and @type='text' and @placeholder='Search Twitter']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[2]/div[1]/div[5]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='id__sy1rd375gw']/div[2]/div[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='layers']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]").click()
    #
    # def test_twitter_761ba1a1(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/a[2]/div[1]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='id__fy4buvz1678']/div[4]/div[1]/div[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='layers']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]").click()
    #
    # def test_twitter_7c394990(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").send_keys("Bill Gates")
    #     self.driver.find_element(By.XPATH, "//div[@id='typeaheadDropdown-6']/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/nav[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='id__346blir2rg2']/div[3]/div[1]/div[1]/div[1]/svg[1]").click()
    #
    # def test_twitter_060b3811(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").send_keys("AOC")
    #     self.driver.find_element(By.XPATH, "//div[@id='typeaheadDropdown-1']/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='id__6o3kk2wpzgd']/div[2]/div[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='layers']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]").click()
    #
    # def test_twitter_23b37c0f(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[8]/div[1]/a[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='id__7j3jtyvz8mp']/div[4]/div[1]/div[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='layers']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]").click()
    #
    # def test_twitter_26beddfb(self):
    #     # self.driver.get("https://twitter.com")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @value='' and @type='text' and @placeholder='Search Twitter']").send_keys("Elon Musk")
    #     self.driver.find_element(By.XPATH, "//div[@id='typeaheadDropdown-1']/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
    