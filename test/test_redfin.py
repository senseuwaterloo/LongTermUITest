import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestRedfin:
    
    # def test_redfin_23372ead(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Redfin Premier')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchInputBox' and @value='' and @type='search' and @placeholder='Find an agent in your area' and @title='Find an agent in your area']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchInputBox' and @value='' and @type='search' and @placeholder='Find an agent in your area' and @title='Find an agent in your area']").send_keys("St Augustine FL")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'St. Augustine Agents')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/div[7]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
    #
    # def test_redfin_282f29ee(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.ID, "search-box-input").clear()
    #     self.driver.find_element(By.ID, "search-box-input").send_keys("san diego")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'San Diego')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").send_keys("1000000")
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #
    # def test_redfin_39ddfc7b(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rent')]").click()
    #     self.driver.find_element(By.ID, "search-box-input").clear()
    #     self.driver.find_element(By.ID, "search-box-input").send_keys("NEW YORK")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'New York')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[3]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[6]/div[1]").click()
    #
    # def test_redfin_6380770e(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/div[8]/div[1]/div[1]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/div[9]/div[1]/a[1]/div[1]/div[2]/div[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dept-job-list']/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='dept-job-list']/span[1]/span[1]/div[1]/div[1]/div[1]/div[40]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Real Estate Agent - Atlanta (Lawrenceville)')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    #
    # def test_redfin_82fdd257(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.ID, "search-box-input").clear()
    #     self.driver.find_element(By.ID, "search-box-input").send_keys("NEW YORK")
    #     self.driver.find_element(By.XPATH, "//div[@id='tabContentId0']/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[3]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[3]/div[1]").click()
    #
    # def test_redfin_1808ce30(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rent')]").click()
    #     self.driver.find_element(By.ID, "search-box-input").clear()
    #     self.driver.find_element(By.ID, "search-box-input").send_keys("85747")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'85747')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[5]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='filterContent']/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='right-container']/div[5]/div[1]/aside[1]/header[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/div[1]").click()
    
    def test_redfin_3e4283d1(self):
        # self.driver.get("https://www.redfin.com/")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Rent')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Rent' and @role='tab']").click()

        self.driver.find_element(By.ID, "search-box-input").clear()
        self.driver.find_element(By.ID, "search-box-input").send_keys("Koreatown, Los Angeles")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Wilshire Center-Koreatown')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//p[text()='Beds/baths']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='Number of bedrooms']/div[@role='cell' and @data-text='2']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]").click()
        self.driver.find_element(By.XPATH, "//span[@data-dd-action-name='bedsAndBaths_doneBtn']/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//p[text()='Price']").click()

        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").send_keys("3000")

        # self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[@data-dd-action-name='price_doneBtn']/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/div[1]").click()
        sort_dropdown = self.driver.find_element(By.XPATH, "//select[@class='Select__nativeSelect' and @role='combobox']")
        sort_select = Select(sort_dropdown)
        sort_select.select_by_value("list_price_asc")

        # self.driver.find_element(By.XPATH, "//div[@id='MapHomeCard_0']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/img[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='MapHomeCard_0']/div/div/div[1]/div").click()
    
    # def test_redfin_01ac3b25(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Mortgage ▾')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Payment calculator')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='$250,000' and @type='text' and @placeholder=' ']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='$250,000' and @type='text' and @placeholder=' ']").send_keys("500,000")
    #     self.driver.find_element(By.XPATH, "//input[@name='searchInputBox' and @value='' and @type='search' and @placeholder='City, neighborhood, or zip' and @title='City, neighborhood, or zip']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchInputBox' and @value='' and @type='search' and @placeholder='City, neighborhood, or zip' and @title='City, neighborhood, or zip']").send_keys("85747")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'85747')]").click()
    #
    # def test_redfin_1290a124(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rent ▾')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'How much rent can I afford?')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchInputBox' and @value='' and @type='search' and @placeholder='City, neighborhood, or zip code' and @title='City, neighborhood, or zip code']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchInputBox' and @value='' and @type='search' and @placeholder='City, neighborhood, or zip code' and @title='City, neighborhood, or zip code']").send_keys("Chicago")
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/div[7]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='income' and @value='' and @type='text' and @placeholder='Income before taxes']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='income' and @value='' and @type='text' and @placeholder='Income before taxes']").send_keys("130000")
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/div[7]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]/span[1]").click()
    #
    # def test_redfin_1703b236(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='header-content']/header[2]/div[2]/div[5]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Payment calculator')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='$250,000' and @type='text' and @placeholder=' ']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='250000' and @type='text' and @placeholder=' ']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='250000' and @type='text' and @placeholder=' ']").send_keys("500000")
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='$100,000' and @type='text' and @placeholder=' ']").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='100000' and @type='text' and @placeholder=' ']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='100000' and @type='text' and @placeholder=' ']").send_keys("200000")
    #     self.driver.find_element(By.XPATH, "//input[@name='searchInputBox' and @value='' and @type='search' and @placeholder='City, neighborhood, or zip' and @title='City, neighborhood, or zip']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchInputBox' and @value='' and @type='search' and @placeholder='City, neighborhood, or zip' and @title='City, neighborhood, or zip']").send_keys("HOUSTON")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Houston')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/div[7]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/div[7]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    #
    # def test_redfin_879426e8(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.ID, "search-box-input").clear()
    #     self.driver.find_element(By.ID, "search-box-input").send_keys("85747")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'85747')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[3]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[5]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='poolType']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='poolType']").select("Private pool")
    #     self.driver.find_element(By.XPATH, "//div[@id='right-container']/div[5]/div[1]/aside[1]/header[1]/button[1]/svg[1]/svg[1]/g[1]/path[1]").click()
    #
    # def test_redfin_886b485c(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rent ▾')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'How much rent can I afford?')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchInputBox' and @value='' and @type='search' and @placeholder='City, neighborhood, or zip code' and @title='City, neighborhood, or zip code']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='searchInputBox' and @value='' and @type='search' and @placeholder='City, neighborhood, or zip code' and @title='City, neighborhood, or zip code']").send_keys("94587")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'94587')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@name='income' and @value='' and @type='text' and @placeholder='Income before taxes']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='income' and @value='' and @type='text' and @placeholder='Income before taxes']").send_keys("100,000")
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/div[7]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]/span[1]").click()
    #
    # def test_redfin_95b4eb0c(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Buy ▾')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Homes for sale')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='right-container']/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").send_keys("10000")
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//img[@title='1825 Merriweather Dr, Columbus, OH 43221']").click()
    #
    # def test_redfin_84601e79(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rent')]").click()
    #     self.driver.find_element(By.ID, "search-box-input").clear()
    #     self.driver.find_element(By.ID, "search-box-input").send_keys("HOUSTON")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Houston')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/svg[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter min']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter min']").send_keys("1750")
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").send_keys("2750")
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[5]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[2]/button[2]/span[1]").click()
    #
    # def test_redfin_a2a888e7(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.ID, "search-box-input").clear()
    #     self.driver.find_element(By.ID, "search-box-input").send_keys("10017")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'10017')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Enter max']").send_keys("300000")
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[3]/div[1]").click()
    #
    # def test_redfin_ab2f0102(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.ID, "search-box-input").clear()
    #     self.driver.find_element(By.ID, "search-box-input").send_keys("Bluff, UT")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bluff')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[5]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='filterContent']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]").click()
    #     self.driver.find_element(By.XPATH, "//select[@name='solds']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@name='solds']").select("Last 1 year")
    #     self.driver.find_element(By.XPATH, "//div[@id='right-container']/div[5]/div[1]/aside[1]/header[1]/button[1]/svg[1]").click()
    #
    # def test_redfin_f73e9a28(self):
    #     # self.driver.get("https://www.redfin.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rent')]").click()
    #     self.driver.find_element(By.ID, "search-box-input").clear()
    #     self.driver.find_element(By.ID, "search-box-input").send_keys("San Francisco")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'San Francisco')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='sidepane-header']/div[1]/div[1]/form[1]/div[5]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='filterContent']/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='filterContent']/div[1]/div[9]/div[2]/div[1]/div[9]/span[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='searchForm']/form[1]/div[2]/div[1]/div[1]/button[1]/span[1]").click()
    