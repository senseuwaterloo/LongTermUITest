import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import switch_to_new_tab


@pytest.mark.usefixtures("setup_class")
class TestStubhub:
    
    # def test_stubhub_d9e70643(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Help Center')]").click()
    #     self.driver.find_element(By.XPATH, "//h3[contains(.,'Where are my tickets?')]").click()
    #     self.driver.find_element(By.ID, "61000276824").click()
    #
    # def test_stubhub_dd3ef13f(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("KEVIN HART")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("BRISBANE")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[2]/div[1]/div[2]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[5]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[2]/a[1]/button[1]").click()
    #
    # def test_stubhub_e27fee2b(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("Blackpink")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[8]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
    #
    # def test_stubhub_3b1340a5(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/span[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #
    # def test_stubhub_613e8978(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View All')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Celine Dion')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[10]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[4]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[7]/div[1]/div[2]/div[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[2]/a[1]/button[1]").click()
    #
    # def test_stubhub_662af945(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("TAYLOR SWIFT")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("LAS VEGAS")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[2]/div[1]/div[2]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[2]/a[1]/button[1]").click()
    #
    # def test_stubhub_6f79871b(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/div[3]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("Austin")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/div[4]/div[1]/div[2]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("NOFX")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/button[1]").click()
    #
    # def test_stubhub_77ed39d9(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/button[1]").click()
    #
    # def test_stubhub_7a9212a8(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/div[3]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("Boston")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/div[4]/div[1]/div[2]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("NHL")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
    #
    # def test_stubhub_7eefb724(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("Adele")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[2]/a[1]/button[1]").click()
    #
    # def test_stubhub_8eb3f652(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("Bad Bunny")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]").click()
    #
    # def test_stubhub_abf2e88a(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("Los Angeles Lakers")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
    #
    # def test_stubhub_d4c8f4ae(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("Harry Styles")
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[22]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[27]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/select[1]").select("4")
    #     self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[2]/div[1]/div[4]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/label[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
    
    def test_stubhub_1567bfa7(self):
        # self.driver.get("https://stubhub.com")
        time.sleep(5)
        # self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").clear()
        # self.driver.find_element(By.XPATH, "//input[@value='' and @type='search' and @placeholder='Event, artist or team']").send_keys("MIAMI HEAT")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search events, artists, teams, and more']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search events, artists, teams, and more']").send_keys("MIAMI HEAT")

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/div[1]/a[1]/div[2]/div[1]/em[1]").click()
        self.driver.find_element(By.XPATH, "//p[./em[text()='Miami'] and ./em[text()='Heat'] and not(preceding-sibling::*) and not(following-sibling::*)]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='Filter by location']/div[1]").click()

        # self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").clear()
        # self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Search']").send_keys("NEW YOK")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Country, State, City']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Country, State, City']").send_keys("NEW YORK")

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/div[2]/button[1]/div[2]/div[1]/div[2]/div[2]").click()
        self.driver.find_element(By.XPATH, "//div[text()='New York, NY, USA']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[3]/svg[1]/path[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]").click()
        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text()='Home/Away']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Away games']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[./li[1]/div[1]/div[1]/div[text()='New York']]/li[2]//button[text()='See tickets']").click()
        switch_to_new_tab(self.driver)

        # self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[6]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[10]/label[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        # self.driver.find_element(By.XPATH, "//select[@name='quantity-select']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='quantity-select']").select("6 tickets")
        # self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div[1]/div[2]/div[1]/div[2]/a[1]/button[1]").click()
        tickets_dropdown = self.driver.find_element(By.XPATH, "//div[@id='modal-root']//select[@aria-label='Number of tickets']")
        tickets_select = Select(tickets_dropdown)
        tickets_select.select_by_visible_text("6 tickets")
        self.driver.find_element(By.XPATH, "//button[text()='Continue']").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='filter']/div[text()='Zones']").click()
        # club gold is not available now, click on VIP now
        self.driver.find_element(By.XPATH, "//li[contains(@id, 'picker-') and ./div[1]/div[1]/div[text()='VIP']]/div[2]/div[1]/span[1]").click()
        # wait for the page refreshed and click zone again to avoid the popup intercept clicking sort dropdown
        time.sleep(2)
        # self.driver.find_element(By.XPATH, "//div[@aria-label='filter']/div[text()='Zones']").click()
        # seems that click the zone again will also be intercepted, so click the div under modal-div instead
        self.driver.find_element(By.XPATH, "//div[@id='modal-root']/div").click()

        # stubhub-event-detail-listings-sort-dropdown will intercept its child div. Also need to wait for a few
        self.driver.find_element(By.XPATH, "//div[@id='stubhub-event-detail-listings-sort-dropdown']/div").click()
        self.driver.find_element(By.XPATH, "//ul[@id='stubhub-event-detail-sort-dropdown-options']/li[text()='Price']").click()
    
    # def test_stubhub_18c81087(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Occasion')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Birthday')]").click()
    #     self.driver.find_element(By.ID, "card_b2c_2020_birthday1_virtual").click()
    #     self.driver.find_element(By.ID, "btnChooseNext2").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='mainContent']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "btnPersonalizeForme").click()
    #     self.driver.find_element(By.ID, "btnPersonalizeNext2").click()
    #
    # def test_stubhub_1da50745(self):
    #     # self.driver.get("https://stubhub.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Top Cities')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/a[8]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='theatre']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/img[1]").click()
    