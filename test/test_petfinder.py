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
class TestPetfinder:
    
    def test_petfinder_9d61cd44(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/ul[1]/li[2]/a[1]").click()
        self.driver.find_element(By.ID, "breed-autosuggest_List_Box_Btn").click()
        self.driver.find_element(By.XPATH, "//ul[@id='breed-autosuggest_List_Box']/li[1]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//pfdc-breed-autosuggest[@id='breed-autosuggest']/div[1]/div[1]/pf-focus-manager[1]/div[1]/div[1]/div[3]/span[1]/svg[1]").click()
        self.driver.find_element(By.ID, "gender-select_List_Box_Btn").click()
        self.driver.find_element(By.XPATH, "//ul[@id='gender-select_List_Box']/li[2]/label[1]/div[1]").click()
        self.driver.find_element(By.ID, "gender-select_List_Box_Btn").click()
    
    def test_petfinder_aa254179(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/ul[1]/li[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("94587")
        self.driver.find_element(By.XPATH, "//li[@id='location-suggestion-1']/label[1]/div[1]").click()
        self.driver.find_element(By.ID, "distanceOption-list").click()
        self.driver.find_element(By.XPATH, "//li[@id='10 miles']/label[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='age-select_List_Box_Btn']/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='age-select_List_Box']/li[2]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='age-select_List_Box']/li[3]/label[1]/div[1]").click()
        self.driver.find_element(By.ID, "sort-select_6_nativeSelect").clear()
        self.driver.find_element(By.ID, "sort-select_6_nativeSelect").select("Oldest addition")
    
    def test_petfinder_acb41370(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/ul[1]/li[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/ul[1]/li[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("NEW YORK")
        self.driver.find_element(By.XPATH, "//label[@role='presentation']").click()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/button[1]").click()
        self.driver.find_element(By.ID, "breed-autosuggest_List_Box_Btn").click()
        self.driver.find_element(By.XPATH, "//ul[@id='breed-autosuggest_List_Box']/li[1]/label[1]/div[1]/div[2]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//pfdc-breed-autosuggest[@id='breed-autosuggest']/div[1]/div[1]/pf-focus-manager[1]/div[1]/div[1]/div[3]/span[1]/svg[1]").click()
        self.driver.find_element(By.ID, "gender-select_List_Box_Btn").click()
        self.driver.find_element(By.XPATH, "//ul[@id='gender-select_List_Box']/li[1]/label[1]/div[1]/div[2]/div[2]/div[1]").click()
        self.driver.find_element(By.ID, "gender-select_List_Box_Btn").click()
        self.driver.find_element(By.XPATH, "//pfdc-pet-card[@id='petId_60187344']/a[1]/div[1]/div[1]/div[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Site']/div[1]/div[1]/pfdc-sticky[1]/div[1]/div[1]/div[2]/div[2]/pf-element[1]/button[1]").click()
        self.driver.find_element(By.ID, "Petcard_60187344_Copy_Link").click()
    
    def test_petfinder_ce0c4604(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='simpleSearchAnimalType' and @value='' and @type='text' and @placeholder='Search Terrier, Kitten, etc.']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='simpleSearchAnimalType' and @value='' and @type='text' and @placeholder='Search Terrier, Kitten, etc.']").send_keys("Cats")
        self.driver.find_element(By.ID, "simpleSearchLocation").clear()
        self.driver.find_element(By.ID, "simpleSearchLocation").send_keys("Seattle")
        self.driver.find_element(By.XPATH, "//section[@id='pet-search-bar']/div[1]/div[1]/div[4]/button[1]/svg[1]/path[2]").click()
        self.driver.find_element(By.ID, "sort-select_6_nativeSelect").clear()
        self.driver.find_element(By.ID, "sort-select_6_nativeSelect").select("Newest addition")
        self.driver.find_element(By.XPATH, "//div[@id='age-select_List_Box_Btn']/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='age-select_List_Box']/li[2]/label[1]/div[1]").click()
    
    def test_petfinder_e2276e18(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/ul[1]/li[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("94587")
        self.driver.find_element(By.XPATH, "//li[@id='location-suggestion-1']/label[1]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='good-with_List_Box_Btn']/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='good-with_List_Box']/li[1]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='good-with_List_Box']/li[3]/label[1]/div[1]").click()
        self.driver.find_element(By.ID, "good-with_List_Box_Btn").click()
        self.driver.find_element(By.XPATH, "//div[@id='coat-select_List_Box_Btn']/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='coat-select_List_Box']/li[2]/label[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "coat-select_List_Box_Btn").click()
        self.driver.find_element(By.XPATH, "//div[@id='days-on-petfinder_List_Box_Btn']/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='days-on-petfinder_List_Box']/li[5]/label[1]/div[1]/div[1]").click()
    
    def test_petfinder_fac10fd0(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/ul[1]/li[4]/button[1]/svg[1]").click()
        self.driver.find_element(By.ID, "awo-location").clear()
        self.driver.find_element(By.ID, "awo-location").send_keys("Union City, CA")
        self.driver.find_element(By.XPATH, "//input[@value='Search' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Woody Feral Cat Support Group')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='Site']/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/pf-element[1]/button[1]").click()
        self.driver.find_element(By.ID, "Petcard_51658_Copy_Link").click()
    
    def test_petfinder_fc8c0df5(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='simpleSearchAnimalType' and @value='' and @type='text' and @placeholder='Search Terrier, Kitten, etc.']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='simpleSearchAnimalType' and @value='' and @type='text' and @placeholder='Search Terrier, Kitten, etc.']").send_keys("American Bulldog")
        self.driver.find_element(By.XPATH, "//li[@id='animal-suggestion-2']/label[1]").click()
        self.driver.find_element(By.ID, "simpleSearchLocation").clear()
        self.driver.find_element(By.ID, "simpleSearchLocation").send_keys("10001")
        self.driver.find_element(By.XPATH, "//section[@id='pet-search-bar']/div[1]/div[1]/div[4]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='distance-select_List_Box_Btn']/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='distance-select_List_Box']/li[3]/label[1]/div[1]").click()
    
    def test_petfinder_ad282601(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='simpleSearchAnimalType' and @value='' and @type='text' and @placeholder='Search Terrier, Kitten, etc.']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='simpleSearchAnimalType' and @value='' and @type='text' and @placeholder='Search Terrier, Kitten, etc.']").send_keys("dog")
        self.driver.find_element(By.ID, "simpleSearchLocation").clear()
        self.driver.find_element(By.ID, "simpleSearchLocation").send_keys("toronto")
        self.driver.find_element(By.XPATH, "//section[@id='pet-search-bar']/div[1]/div[1]/div[4]/button[1]/svg[1]/path[3]").click()
        self.driver.find_element(By.ID, "animal-size_List_Box_Btn").click()
        self.driver.find_element(By.XPATH, "//ul[@id='animal-size_List_Box']/li[3]/label[1]/div[1]/div[1]").click()
    
    def test_petfinder_c862818d(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.ID, "breed-autosuggest_List_Box_Btn").click()
        self.driver.find_element(By.XPATH, "//ul[@id='breed-autosuggest_List_Box']/li[2]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//pfdc-breed-autosuggest[@id='breed-autosuggest']/div[1]/div[1]/pf-focus-manager[1]/div[1]/div[1]/div[3]/span[1]/svg[1]/use[1]").click()
        self.driver.find_element(By.ID, "age-select_List_Box_Btn").click()
        self.driver.find_element(By.XPATH, "//ul[@id='age-select_List_Box']/li[3]/label[1]/div[1]/div[1]").click()
    
    def test_petfinder_0dc9dc8b(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Dogs & Puppies')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View All')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View All')]").click()
    
    def test_petfinder_432a58b4(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Adopt or Get Involved')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Petfinder Foundation')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Donate')]").click()
        self.driver.find_element(By.ID, "label_3_30_1").click()
        self.driver.find_element(By.ID, "input_3_26").clear()
        self.driver.find_element(By.ID, "input_3_26").send_keys("10")
        self.driver.find_element(By.ID, "gform_next_button_3_1").click()
        self.driver.find_element(By.ID, "gform_next_button_3_3").click()
        self.driver.find_element(By.ID, "input_3_22_1").clear()
        self.driver.find_element(By.ID, "input_3_22_1").send_keys("5555555555555555")
        self.driver.find_element(By.ID, "input_3_22_2_month").clear()
        self.driver.find_element(By.ID, "input_3_22_2_month").select("12")
        self.driver.find_element(By.ID, "input_3_22_2_year").clear()
        self.driver.find_element(By.ID, "input_3_22_2_year").select("2036")
        self.driver.find_element(By.XPATH, "//span[@id='input_3_22_2_cardinfo_right']/label[1]").clear()
        self.driver.find_element(By.XPATH, "//span[@id='input_3_22_2_cardinfo_right']/label[1]").send_keys("555")
        self.driver.find_element(By.ID, "input_3_22_5").clear()
        self.driver.find_element(By.ID, "input_3_22_5").send_keys("Jane Doe")
    
    def test_petfinder_46b1539d(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/ul[1]/li[3]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/ul[1]/li[1]/button[1]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("94587")
        self.driver.find_element(By.XPATH, "//li[@id='location-suggestion-1']/label[1]/div[1]/span[2]").click()
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/div[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//pfdc-pet-card[@id='petId_60756014']/pfdc-favorite-btn[1]/button[1]").click()
    
    def test_petfinder_7571cac4(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//section[@id='quizzle-cards']/div[1]/ul[1]/li[4]/a[1]").click()
        self.driver.find_element(By.ID, "awo-location").clear()
        self.driver.find_element(By.ID, "awo-location").send_keys("California")
        self.driver.find_element(By.ID, "awo_keyword_location").clear()
        self.driver.find_element(By.ID, "awo_keyword_location").send_keys("Kitten Tales Rescue")
        self.driver.find_element(By.XPATH, "//input[@value='Search' and @type='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Kitten Tales Rescue')]").click()
    
    def test_petfinder_7c3b62d9(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='simpleSearchAnimalType' and @value='' and @type='text' and @placeholder='Search Terrier, Kitten, etc.']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='simpleSearchAnimalType' and @value='' and @type='text' and @placeholder='Search Terrier, Kitten, etc.']").send_keys("British Shorthair")
        self.driver.find_element(By.XPATH, "//li[@id='animal-suggestion-2']/label[1]/div[1]/span[1]").click()
        self.driver.find_element(By.ID, "simpleSearchLocation").clear()
        self.driver.find_element(By.ID, "simpleSearchLocation").send_keys("Naperville, IL")
        self.driver.find_element(By.XPATH, "//section[@id='pet-search-bar']/div[1]/div[1]/div[4]/button[1]/svg[1]/path[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='age-select_List_Box']/li[3]/label[1]/div[1]/div[1]").click()
        self.driver.find_element(By.ID, "sort-select_6_nativeSelect").clear()
        self.driver.find_element(By.ID, "sort-select_6_nativeSelect").select("Nearest")
    
    def test_petfinder_9b0e656f(self):
        # self.driver.get("https://petfinder.com")
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='simpleSearchAnimalType' and @value='' and @type='text' and @placeholder='Search Terrier, Kitten, etc.']").clear()
        self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='simpleSearchAnimalType' and @value='' and @type='text' and @placeholder='Search Terrier, Kitten, etc.']").send_keys("Labrador Retriever")
        self.driver.find_element(By.XPATH, "//li[@id='animal-suggestion-2']/label[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='gender-select_List_Box_Btn']/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='gender-select_List_Box']/li[1]/label[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//button[@id='color-autosuggest_List_Box_Btn']/div[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='color-autosuggest_List_Box']/li[3]/label[1]/div[1]/div[1]/div[1]").click()
    