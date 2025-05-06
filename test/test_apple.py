import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestApple:
    def test_apple_a10e6232(self):
        self.driver.get("https://apple.com")
        self.driver.find_element(By.XPATH, "//ul[@id='globalnav-list']/li[2]/div[1]/div[1]/div[3]/ul[1]/li[1]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//nav[@id='chapternav']/div/ul/li[3]/a").click()
        self.driver.find_element(By.XPATH, "//nav[@id='ac-localnav']/div/div[2]/div[2]/div[2]/div[2]/a").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[2]/div[2]/div/div[1]/fieldset/div/div[1]").click()

        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[2]/div[2]/div/div[2]/fieldset/div/div[1]/label").click()
        time.sleep(1.5)
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[2]/div[2]/div/div[3]/fieldset/div/div[1]/label").click()
        time.sleep(1.5)

        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//input[@data-autom='addEngraving-app']").get_native_element())

        time.sleep(1.5)
        self.driver.find_element(By.XPATH, "//input[@data-autom='Engraveline1']").click()
        self.driver.find_element(By.XPATH, "//input[@data-autom='Engraveline1']").send_keys("Hello World")
        save_button = self.driver.find_element(By.XPATH, "//div[@id='portal']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]")
        scroll_to_element(self.driver, save_button)
        save_button.click()
        time.sleep(1.5)
        self.driver.find_element(By.XPATH, "//button[@data-autom='acc_pencil_first_section_noaccessory']").click()
        time.sleep(1.5)
        self.driver.find_element(By.XPATH, "//button[@data-autom='acc_magic_keyboard_section_noaccessory']").click()
        time.sleep(1.5)
        self.driver.find_element(By.XPATH, "//span[text()='No trade-in']").click()
        time.sleep(1.5)
        self.driver.find_element(By.XPATH, "//span[@data-autom='purchaseGroupOptionfullprice_price']").click()
        time.sleep(1.5)
        self.driver.find_element(By.ID, "applecareplus_noapplecare_label").click()
        time.sleep(1.5)
        self.driver.find_element(By.XPATH, "//button[@data-autom='add-to-cart']").click()
    