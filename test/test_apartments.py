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
class TestApartments:
    
    def test_apartments_018eb03a(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "quickSearchLookup").clear()
        self.driver.find_element(By.ID, "quickSearchLookup").send_keys("Boston")
        self.driver.find_element(By.ID, "quickSearchLookup_typeahead_0").click()
        self.driver.find_element(By.ID, "bedRangeLink").click()
        self.driver.find_element(By.XPATH, "//span[@id='bedsMinMaxRangeControl']/div[1]/div[1]/ul[1]/li[3]").click()
        self.driver.find_element(By.XPATH, "//span[@id='bedsMinMaxRangeControl']/div[1]/div[1]/ul[2]/li[4]").click()
        self.driver.find_element(By.XPATH, "//a[@id='advancedFiltersIcon']/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='None']").click()
        self.driver.find_element(By.XPATH, "//div[@id='advancedFilters']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='sortSearchIcon']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='searchResultSortMenu']/ul[1]/li[5]/span[1]").click()
    
    def test_apartments_9d891501(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "headerMeunIcon").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Townhomes For Rent')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Spring Townhomes For Rent')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='placardContainer']/ul[1]/li[2]/article[1]/section[1]/div[1]/div[2]/div[1]/div[1]/a[1]/p[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='anchors']/div[1]/div[1]/button[3]").click()
    
    def test_apartments_b6908293(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rent Calculator')]").click()
        self.driver.find_element(By.ID, "monthlyIncome").click()
        self.driver.find_element(By.ID, "monthlyIncome").clear()
        self.driver.find_element(By.ID, "monthlyIncome").send_keys("14000")
        self.driver.find_element(By.ID, "searchBarLookup").clear()
        self.driver.find_element(By.ID, "searchBarLookup").send_keys("Houston, TX")
        self.driver.find_element(By.XPATH, "//li[@id='searchBarLookup_typeahead_0']/span[1]").click()
        self.driver.find_element(By.ID, "searchButton").click()
    
    def test_apartments_c766b1a1(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "quickSearchLookup").clear()
        self.driver.find_element(By.ID, "quickSearchLookup").send_keys("New York")
        self.driver.find_element(By.ID, "quickSearchLookup_typeahead_0").click()
        self.driver.find_element(By.XPATH, "//a[@id='typeSelect']/span[3]/i[1]").click()
        self.driver.find_element(By.ID, "2").click()
        self.driver.find_element(By.XPATH, "//button[@id='sortSearchIcon']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='searchResultSortMenu']/ul[1]/li[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='placardContainer']/ul[1]/li[1]/article[1]/section[1]/div[1]/div[2]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='placardContainer']/ul[1]/li[2]/article[1]/section[1]/div[1]/div[2]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='placardContainer']/ul[1]/li[3]/article[1]/section[1]/div[1]/div[2]/div[1]/a[1]").click()
    
    def test_apartments_d3d5d845(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "headerMeunIcon").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Renter Tools')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Rental Calculator')]").click()
        self.driver.find_element(By.ID, "monthlyIncome").clear()
        self.driver.find_element(By.ID, "monthlyIncome").send_keys("6000")
        self.driver.find_element(By.ID, "sliderInput").click()
        self.driver.find_element(By.ID, "searchBarLookup").clear()
        self.driver.find_element(By.ID, "searchBarLookup").send_keys("90012")
        self.driver.find_element(By.ID, "searchBarLookup_typeahead_0").click()
        self.driver.find_element(By.ID, "searchButton").click()
    
    def test_apartments_e034b288(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "quickSearchLookup").clear()
        self.driver.find_element(By.ID, "quickSearchLookup").send_keys("nyc")
        self.driver.find_element(By.ID, "quickSearchLookup_typeahead_1").click()
        self.driver.find_element(By.ID, "rentRangeLink").click()
        self.driver.find_element(By.ID, "min-input").clear()
        self.driver.find_element(By.ID, "min-input").send_keys("1500")
        self.driver.find_element(By.ID, "max-input").clear()
        self.driver.find_element(By.ID, "max-input").send_keys("2500")
        self.driver.find_element(By.XPATH, "//a[@id='bedRangeLink']/span[2]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='bedRangeLink']/span[2]/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='bedsMinMaxRangeControl']/div[1]/div[1]/ul[1]/li[4]").click()
        self.driver.find_element(By.XPATH, "//span[@id='bedsMinMaxRangeControl']/div[1]/div[1]/ul[2]/li[5]").click()
        self.driver.find_element(By.XPATH, "//a[@id='typeSelect']/span[3]/i[1]").click()
        self.driver.find_element(By.ID, "StyleSmall_4").click()
        self.driver.find_element(By.XPATH, "//a[@id='advancedFiltersIcon']/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='advancedFilterBaths']/li[3]/fieldset[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='advancedFiltersIcon']/span[1]").click()
    
    def test_apartments_e60febbe(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "headerMeunIcon").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Homes For Rent')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Houston Homes For Rent')]").click()
        self.driver.find_element(By.XPATH, "//a[@id='bedRangeLink']/span[2]/i[1]").click()
        self.driver.find_element(By.XPATH, "//span[@id='bedsMinMaxRangeControl']/div[1]/div[1]/ul[1]/li[2]").click()
        self.driver.find_element(By.XPATH, "//span[@id='bedsMinMaxRangeControl']/div[1]/div[1]/ul[2]/li[3]").click()
        self.driver.find_element(By.XPATH, "//a[@id='typeSelect']/span[3]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='placardContainer']/ul[1]/li[1]/article[1]/header[1]/div[1]/a[1]/div[1]/span[1]").click()
    
    def test_apartments_7a65d9c8(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "quickSearchLookup").click()
        self.driver.find_element(By.ID, "quickSearchLookup").clear()
        self.driver.find_element(By.ID, "quickSearchLookup").send_keys("Corning")
        self.driver.find_element(By.XPATH, "//li[@id='quickSearchLookup_typeahead_1']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='rentRangeLink']/span[2]/i[1]").click()
        self.driver.find_element(By.ID, "max-input").click()
        self.driver.find_element(By.XPATH, "//ul[@id='maxRentOptions']/li[3]").click()
    
    def test_apartments_7e24f1bf(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "quickSearchLookup").clear()
        self.driver.find_element(By.ID, "quickSearchLookup").send_keys("Elevate")
        self.driver.find_element(By.ID, "quickSearchLookup_typeahead_4").click()
        self.driver.find_element(By.XPATH, "//div[@id='propertyHeader']/div[2]/div[1]/div[2]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "carouselPillVirtualToursLink").click()
    
    def test_apartments_869c6676(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "quickSearchLookup").clear()
        self.driver.find_element(By.ID, "quickSearchLookup").send_keys("Chicago IL")
        self.driver.find_element(By.ID, "quickSearchLookup_typeahead_0").click()
        self.driver.find_element(By.XPATH, "//a[@id='advancedFiltersIcon']/span[1]/span[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='advancedFilterUnitAmenities']/li[9]/fieldset[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='map-container']/div[1]/div[1]/div[2]/div[2]").click()
    
    def test_apartments_91f092a8(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "quickSearchLookup").clear()
        self.driver.find_element(By.ID, "quickSearchLookup").send_keys("Ohio City")
        self.driver.find_element(By.ID, "quickSearchLookup_typeahead_0").click()
        self.driver.find_element(By.XPATH, "//a[@id='advancedFiltersIcon']/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='advancedFilterUnitAmenities']/li[6]/fieldset[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='advancedFilterUnitAmenities']/li[8]/fieldset[1]/label[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='advancedFilterUnitAmenities']/li[10]/fieldset[1]/label[1]").click()
    
    def test_apartments_96309122(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "headerManageRental").click()
        self.driver.find_element(By.XPATH, "//nav[@id='block-themekit-main-menu']/ul[1]/li[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'State rental laws and regulations')]").click()
        self.driver.find_element(By.ID, "edit-state").clear()
        self.driver.find_element(By.ID, "edit-state").select("Kentucky")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Ky. Rev. Stat. Ann. § 383')]").click()
    
    def test_apartments_f6d10418(self):
        # self.driver.get("https://apartments.com")
        self.driver.find_element(By.ID, "quickSearchLookup").clear()
        self.driver.find_element(By.ID, "quickSearchLookup").send_keys("Detroit")
        self.driver.find_element(By.XPATH, "//li[@id='quickSearchLookup_typeahead_0']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='advancedFiltersIcon']/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button' and @title='None']").click()
        self.driver.find_element(By.XPATH, "//div[@id='advancedFilters']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[@id='typeSelect']/span[3]/i[1]").click()
        self.driver.find_element(By.XPATH, "//label[@id='0']/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='sortSearchIcon']/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='searchResultSortMenu']/ul[1]/li[2]/span[1]").click()
    