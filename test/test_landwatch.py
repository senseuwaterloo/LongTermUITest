import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestLandwatch:
    
    # def test_landwatch_465cb989(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[2]/div[1]/div[2]/div[2]/a[2]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//li[@role='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='expansible1']/div[1]/div[1]/div[17]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Iowa')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Dallas County')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'0 - 10 Acres')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='expansible1']/div[1]/fieldset[1]/div[1]/div[3]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dropdown2']/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "Newest").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='saveSearchForm']/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='modal']/div[1]/div[4]/div[1]/button[1]").click()
    #
    # def test_landwatch_4724612e(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Houses')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='button']").clear()
    #     self.driver.find_element(By.XPATH, "//div[@role='button']").send_keys("Maryland")
    #     self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "priceMax").click()
    #     self.driver.find_element(By.ID, "priceMax").clear()
    #     self.driver.find_element(By.ID, "priceMax").send_keys("60000")
    #     self.driver.find_element(By.XPATH, "//div[@id='expansible1']/div[1]/div[1]/div[9]/button[1]").click()
    #
    # def test_landwatch_5aa92172(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Oklahoma')]").click()
    #     self.driver.find_element(By.XPATH, "//li[@role='button']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Wagoner County')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Auction')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dropdown3']/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "Acres-").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/button[1]").click()
    #
    # def test_landwatch_6f21856c(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@role='button']").clear()
    #     self.driver.find_element(By.XPATH, "//div[@role='button']").send_keys("Wilkes County, NC")
    #     self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='expansible1']/div[1]/fieldset[1]/div[1]/div[7]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dropdown2']/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "Price-").click()
    #
    # def test_landwatch_943458e0(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[2]/div[1]/div[2]/div[2]/a[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='button']").clear()
    #     self.driver.find_element(By.XPATH, "//div[@role='button']").send_keys("California")
    #     self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dropdown2']/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "Newest").click()
    #
    # def test_landwatch_b7373567(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[2]/div[1]/div[2]/div[2]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Georgia')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'4,001+ Sq. Ft.')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='expansible1']/div[1]/fieldset[1]/div[1]/div[3]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dropdown4']/div[1]/span[2]").click()
    #     self.driver.find_element(By.ID, "Newest").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]/i[1]/img[1]").click()
    #
    # def test_landwatch_b93b982d(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[2]/div[1]/div[2]/div[2]/a[3]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.ID, "input-Search").clear()
    #     self.driver.find_element(By.ID, "input-Search").send_keys("PRESHO, SD")
    #     self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'80 acres')]").click()
    #
    # def test_landwatch_15e1e37c(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find an Agent')]").click()
    #     self.driver.find_element(By.ID, "input-BrokerSearch").clear()
    #     self.driver.find_element(By.ID, "input-BrokerSearch").send_keys("Orange County FL")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='name' and @value='' and @type='text' and @placeholder='Name']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='name' and @value='' and @type='text' and @placeholder='Name']").send_keys("James SMith")
    #     self.driver.find_element(By.XPATH, "//input[@name='tel' and @value='' and @type='text' and @placeholder='Phone Number']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='tel' and @value='' and @type='text' and @placeholder='Phone Number']").send_keys("8888888888")
    #     self.driver.find_element(By.XPATH, "//textarea[@name='message' and @placeholder='Message']").clear()
    #     self.driver.find_element(By.XPATH, "//textarea[@name='message' and @placeholder='Message']").send_keys("Appointment")
    #     self.driver.find_element(By.XPATH, "//form[@id='contactBrokerModal']/fieldset[1]/div[1]/div[6]/div[1]/button[1]").click()
    #
    # def test_landwatch_17f7aa69(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@role='button']").click()
    #     self.driver.find_element(By.ID, "input-Search").clear()
    #     self.driver.find_element(By.ID, "input-Search").send_keys("Nashville")
    #     self.driver.find_element(By.ID, "input-Search").clear()
    #     self.driver.find_element(By.ID, "input-Search").send_keys("Nashville, TN")
    #     self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/picture[1]/source[1]/source[1]/img[1]").click()
    #
    # def test_landwatch_24948950(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Owner Financing')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'New Mexico')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Luna County')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='expansible1']/div[1]/fieldset[1]/div[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "Date Listed").clear()
    #     self.driver.find_element(By.ID, "Date Listed").select("Past 30 days")
    #     self.driver.find_element(By.XPATH, "//div[@id='dropdown4']/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "PriceperAcre-").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='contact']/span[1]").click()
    #
    # def test_landwatch_290c13e2(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[2]/div[1]/div[2]/div[2]/a[2]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.ID, "input-Search").clear()
    #     self.driver.find_element(By.ID, "input-Search").send_keys("ROCKSPRINGS, TX")
    #     self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'118 acres')]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='contactBrokerRight']/fieldset[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]").click()
    #
    # def test_landwatch_35eda718(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[2]/div[1]/div[2]/div[2]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Texas')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dropdown5']/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "Price+").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'424,000 acres')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #
    # def test_landwatch_c0338a77(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Home Auctions')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dropdown4']/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "Acres-").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'0')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/button[1]/div[1]/span[2]").click()
    #
    # def test_landwatch_fdeb48ba(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[2]/div[1]/div[2]/div[2]/a[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Georgia')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dropdown3']/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "Price-").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='contact']/span[1]").click()
    #
    # def test_landwatch_9da9c965(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hunting Land')]").click()
    #     self.driver.find_element(By.XPATH, "//li[@role='button']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Kansas')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'High Plains Region')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='portal']/form[1]/section[12]/div[2]/a[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "Date Listed").clear()
    #     self.driver.find_element(By.ID, "Date Listed").select("Past 7 days")
    #     self.driver.find_element(By.XPATH, "//div[@id='dropdown5']/div[1]").click()
    #     self.driver.find_element(By.ID, "Acres+").click()
    #
    # def test_landwatch_a58fab14(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/section[2]/div[1]/div[2]/div[2]/a[1]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.ID, "input-Search").clear()
    #     self.driver.find_element(By.ID, "input-Search").send_keys("CHARLESTON, AR")
    #     self.driver.find_element(By.XPATH, "//div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='search-button']/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'0.21 acres')]").click()
    #
    # def test_landwatch_af422029(self):
    #     # self.driver.get("https://landwatch.com")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[2]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Ohio')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/a[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='name' and @value='' and @type='text' and @placeholder='Name']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='name' and @value='' and @type='text' and @placeholder='Name']").send_keys("James Smith")
    #     self.driver.find_element(By.XPATH, "//input[@name='tel' and @value='' and @type='text' and @placeholder='Phone Number']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='tel' and @value='' and @type='text' and @placeholder='Phone Number']").send_keys("8888888888")
    #     self.driver.find_element(By.XPATH, "//textarea[@name='message' and @placeholder='Message']").clear()
    #     self.driver.find_element(By.XPATH, "//textarea[@name='message' and @placeholder='Message']").send_keys("Visit timings")
    #     self.driver.find_element(By.XPATH, "//form[@id='contactBrokerModal']/fieldset[1]/div[1]/div[7]/div[1]/button[1]").click()
    
    def test_landwatch_b3691435(self):
        # self.driver.get("https://landwatch.com")
        self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Timberland')]").click()
        # somehow Georgia is not clicked, try to add some time
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='Georgia ']").click()
        # somehow follow element is not clicked after add time before Georgia, try to add some time here also.
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'51 - 100 Acres')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='expansible1']/div[1]/fieldset[1]/div[1]/div[1]").click()
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='For Sale ']").click()

        # self.driver.find_element(By.ID, "Date Listed").clear()
        # self.driver.find_element(By.ID, "Date Listed").select("Past 7 days")
        date_listed_dropdown = self.driver.find_element(By.ID, "Date Listed")
        date_listed_select = Select(date_listed_dropdown)
        date_listed_select.select_by_visible_text('Past 7 days')

        # self.driver.find_element(By.XPATH, "//div[@id='dropdown2']/div[1]/span[1]").click()
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted:
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'dropdown')]/div[1]/span[1]").click()

        self.driver.find_element(By.ID, "Price-").click()
        # need to wait for a few seconds for the page to be refreshed
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='name' and @value='' and @type='text' and @placeholder='Name']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='name' and @value='' and @type='text' and @placeholder='Name']").send_keys("James Smith")
        # self.driver.find_element(By.XPATH, "//input[@name='tel' and @value='' and @type='text' and @placeholder='Phone Number']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='tel' and @value='' and @type='text' and @placeholder='Phone Number']").send_keys("52465235214")
        self.driver.find_element(By.XPATH, "//input[@name='tel' and @value='' and @type='tel' and @placeholder='Phone Number']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='tel' and @value='' and @type='tel' and @placeholder='Phone Number']").send_keys("52465235214")
        # remove the following step to avoid sending spam data
        # self.driver.find_element(By.XPATH, "//form[@id='contactBrokerModal']/fieldset[1]/div[1]/div[8]/div[1]/button[1]").click()
    