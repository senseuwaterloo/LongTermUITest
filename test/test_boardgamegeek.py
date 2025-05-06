import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestBoardgamegeek:
    def test_boardgamegeek_d2171cc3(self):
        self.driver.get("https://boardgamegeek.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
        self.driver.find_element(By.ID, "inputUsername").click()
        self.driver.find_element(By.ID, "inputUsername").send_keys("UITestStudy")
        self.driver.find_element(By.ID, "inputPassword").click()
        self.driver.find_element(By.ID, "inputPassword").send_keys("UITestStudy2024")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[contains(.,'GeekLists')]").click()

        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//a[contains(text(),'Hot')]").get_native_element())
        self.driver.find_element(By.XPATH, "/html/body[1]/gg-app[1]/div[1]/gg-header[1]/header[1]/nav[1]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Browse')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Boardgames')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='results_objectname1']/a").click()

        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//button[contains(., 'Add To') and contains(., 'Collection')]").get_native_element())
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/form/div/div/div[3]/button[1]").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[contains(.,'Browse')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'All Boardgames')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='results_objectname3']/a").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//button[contains(., 'Add To') and contains(., 'Collection')]").get_native_element())
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/form/div/div/div[3]/button[1]").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//*[@id='global-header-outer']/header/nav/div/div[2]/div/div[1]/ul/li[8]/button").click()
        self.driver.find_element(By.XPATH, "//*[@id='global-header-outer']/header/nav/div/div[2]/div/div[1]/ul/li[8]/div/ul[1]/li[3]/a").click()
        self.driver.find_element(By.XPATH, "//div[@id='results_objectname1']/a").click()

        time.sleep(2)
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//span[@class='hidden-xs']//button[@id='button-collection']/span[1]").get_native_element())

        self.driver.find_element(By.XPATH, "//*[@id='mainbody']/div[2]/div/div[1]/div[2]/ng-include/div/ng-include/div/div[2]/div[2]/div[4]/span[3]/ng-include/div/div[3]/span/span[2]/span/span/div/div/div[1]/span/button").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/form/div/div/div[2]/div[1]/button/span").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Delete from Collection')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Yes, Delete')]").click()

        self.driver.find_element(By.XPATH, "//*[@id='global-header-outer']/header/nav/div/div[2]/div/div[1]/ul/li[8]/button").click()
        self.driver.find_element(By.XPATH, "//*[@id='global-header-outer']/header/nav/div/div[2]/div/div[1]/ul/li[8]/div/ul[1]/li[3]/a").click()
        self.driver.find_element(By.XPATH, "//div[@id='results_objectname1']/a").click()

        time.sleep(2)
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//span[@class='hidden-xs']//button[@id='button-collection']/span[1]").get_native_element())

        self.driver.find_element(By.XPATH, "//*[@id='mainbody']/div[2]/div/div[1]/div[2]/ng-include/div/ng-include/div/div[2]/div[2]/div[4]/span[3]/ng-include/div/div[3]/span/span[2]/span/span/div/div/div[1]/span/button").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/form/div/div/div[2]/div[1]/button/span").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Delete from Collection')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Yes, Delete')]").click()
    