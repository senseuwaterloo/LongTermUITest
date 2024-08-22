import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestRedbox:
    
    # def test_redbox_1a53fb39(self):
    #     # self.driver.get("https://redbox.com")
    #     self.driver.find_element(By.ID, "search-query").clear()
    #     self.driver.find_element(By.ID, "search-query").send_keys("The Whale")
    #     self.driver.find_element(By.ID, "searchinput-results-0").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/div[3]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/div[3]/div[4]/div[1]/div[2]/button[2]").click()
    #
    # def test_redbox_9d8f230b(self):
    #     # self.driver.get("https://redbox.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See More')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='at-the-kiosk-filters']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[2]/div[1]/div[3]/div[3]/div[1]/div[4]/button[1]").click()
    #
    # def test_redbox_c88962c1(self):
    #     # self.driver.get("https://redbox.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'On Demand')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'On Demand')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Supported Devices')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='body']/div[1]/div[6]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='body']/div[1]/div[3]/div[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='body']/div[1]/div[6]").click()
    #
    # def test_redbox_cfcc4105(self):
    #     # self.driver.get("https://redbox.com")
    #     self.driver.find_element(By.ID, "search-query").click()
    #     self.driver.find_element(By.ID, "search-query").clear()
    #     self.driver.find_element(By.ID, "search-query").send_keys("Shawshank Redemption")
    #     self.driver.find_element(By.ID, "searchinput-results-0").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/div[2]/div[2]/div[2]/button[1]/svg[1]").click()
    #
    # def test_redbox_c82bd6d6(self):
    #     # self.driver.get("https://redbox.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/header[1]/div[2]/nav[1]/ul[2]/li[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "address-search-field").clear()
    #     self.driver.find_element(By.ID, "address-search-field").send_keys("Daytona")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[3]/div[1]/form[1]/div[2]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/ul[1]/li[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='at-the-kiosk-filters']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[2]/div[1]/div[3]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[2]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[2]/div[1]/div[1]/button[1]/span[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[2]/div[2]/div[1]/div[2]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[2]/div[2]/div[1]/div[2]/select[1]").select("Newest")
    #
    # def test_redbox_12324b80(self):
    #     # self.driver.get("https://redbox.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Deals')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See More')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[1]/div[2]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/div[3]/div[1]/button[1]/div[1]").click()
    #
    # def test_redbox_2879afa9(self):
    #     # self.driver.get("https://redbox.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'On Demand')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Genres')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[12]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/div[2]/div[2]/div[1]/button[1]/svg[1]/g[1]/path[1]").click()
    #
    # def test_redbox_a63b891b(self):
    #     # self.driver.get("https://redbox.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'On Demand')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Supported Devices')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='body']/div[1]/div[3]/div[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='body']/div[1]/div[9]/div[1]/div[1]/div[1]").click()
    
    def test_redbox_c5871c3f(self):
        # self.driver.get("https://redbox.com")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'At The Kiosk')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'See More')]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[2]/div[3]/div[1]/a[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/div[2]/div[2]/div[2]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'At The Kiosk')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'New')]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[2]/div[4]/div[1]/a[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/div[2]/div[2]/div[2]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'At The Kiosk')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'New')]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[2]/div[5]/div[1]/a[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//main[@id='maincontent']/div[1]/div[2]/div[2]/div[2]/div[2]/button[1]/svg[1]").click()
        # redbox is permanently closed, we should remove it from our subject.
        pass
    