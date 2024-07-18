import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestCarnival:
    
    # def test_carnival_6cf8ca9c(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//a[@id='cdc-destinations']/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "cdc-ports").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[16]/button[1]").click()
    #     self.driver.find_element(By.ID, "cdc-dates").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[6]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='cdc-durations']/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    
    def test_carnival_c1b8361d(self):
        # self.driver.get("https://www.carnival.com/")
        self.driver.find_element(By.ID, "cdc-destinations").click()
        # Papua New Guinea chnaged to South Pacific on website
        self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[16]/button[1]").click()
        self.driver.find_element(By.ID, "cdc-ports").click()
        self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[3]/button[1]").click()

        self.driver.find_element(By.XPATH, "//a[@id='cdc-dates']/span[1]/span[1]").click()

        # select November 2025 instead of November 2024
        self.driver.find_element(By.XPATH, "//button[@aria-label='November 2025 ']").click()
        self.driver.find_element(By.ID, "cdc-durations").click()
        self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[3]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/button[1]/div[1]").click()
        # change above locator
        self.driver.find_element(By.XPATH, "//button[@aria-label='Show 1 Date']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]").click()
        # change above locator
        self.driver.find_element(By.XPATH, "//a[@data-testid='selectSailingDateButton']").click()

        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/button[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        # change above locator
        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        # change above locator
        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div/div/div/div/div/div/div[3]/div/div/div[2]/button").click()

        # self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
        # change above locator
        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[3]/button").click()

        self.driver.find_element(By.XPATH, "//div[@id='shell-wrapper']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/button[1]").click()

        # omit the following steps since login will be required and anti-robot mechanism can be easily triggered in login steps
        # self.driver.find_element(By.ID, "ges-submit-btn0").click()
        # self.driver.find_element(By.XPATH, "//li[@id='full']/div[1]").click()
        # self.driver.find_element(By.ID, "opt-option-3").click()
    
    # def test_carnival_453da07e(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[1]/li[4]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[1]/li[4]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/svg[1]/use[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-mainContainer']/div[1]/div[2]/div[1]/div[3]/a[1]/img[1]").click()
    #
    # def test_carnival_6a326478(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[1]/li[4]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[1]/li[4]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/svg[1]/use[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'What to Pack & Bring')]").click()
    #
    # def test_carnival_6d963cc0(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[1]/li[4]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[1]/li[4]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]/svg[1]/use[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-mainContainer']/div[2]/h2[2]/div[1]/select[4]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-mainContainer']/div[2]/h2[2]/div[1]/select[4]").select("2 - 5 Days")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-mainContainer']/div[2]/h2[2]/div[1]/button[1]").click()
    #
    # def test_carnival_7cbd1771(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.ID, "cdc-destinations").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[5]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[2]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/svg[1]/path[2]").click()
    #
    # def test_carnival_9365fba7(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.ID, "cdc-destinations").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[2]/button[1]").click()
    #     self.driver.find_element(By.ID, "cdc-ports").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[9]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #
    # def test_carnival_984f5bdb(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-refresh-homepage']/div[3]/ul[1]/li[3]/a[1]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Caribbean')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Miami, FL')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[3]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Aug')]").click()
    #
    # def test_carnival_eab97f0c(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.ID, "cdc-destinations").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #
    # def test_carnival_fb04bb83(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[1]/li[5]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[1]/li[5]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]/svg[1]/use[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='find-sailing-cta-strip']/div[1]/div[2]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-cruise-deals-root']/section[1]/div[1]/div[3]/div[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'VIFP Club Members-Only Offers (2)')]").click()
    #
    # def test_carnival_d4f7da1f(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//a[@id='cdc-destinations']/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[8]/button[1]").click()
    #     self.driver.find_element(By.ID, "cdc-ports").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[8]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/button[1]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]").click()
    #
    # def test_carnival_e62d1f6c(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Beverage Packages')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='organizerAccessModal']/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Beverage Packages')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[8]/div[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='bbModalDynamicHtmlDiv']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='First Name (Required)']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='First Name (Required)']").send_keys("Joe")
    #     self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Last Name (Required)']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Last Name (Required)']").send_keys("Bloggs")
    #     self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='#Booking Number']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='#Booking Number']").send_keys("101010")
    #     self.driver.find_element(By.ID, "saveButtonOne").click()
    #
    # def test_carnival_a065d3cb(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.ID, "cdc-destinations").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[8]/button[1]").click()
    #     self.driver.find_element(By.ID, "cdc-ports").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[8]/button[1]").click()
    #     self.driver.find_element(By.ID, "cdc-dates").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[2]/li[1]/button[1]").click()
    #     self.driver.find_element(By.ID, "cdc-durations").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[3]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #
    # def test_carnival_bf159a0f(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[2]/li[3]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[2]/li[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/label[1]/input[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[2]/li[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/label[1]/input[1]").send_keys("travel agent")
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[2]/li[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find A Travel Agent | Carnival Cruise Line')]").click()
    #     self.driver.find_element(By.ID, "City").clear()
    #     self.driver.find_element(By.ID, "City").send_keys("Grand Junction")
    #     self.driver.find_element(By.ID, "StateCode").clear()
    #     self.driver.find_element(By.ID, "StateCode").select("Colorado")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[6]/div[1]/button[1]").click()
    #
    # def test_carnival_bf94a193(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.ID, "cdc-destinations").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.ID, "cdc-ports").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[17]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='cdc-dates']/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[9]/button[1]").click()
    #     self.driver.find_element(By.ID, "cdc-durations").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[2]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[2]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[2]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Carnival Luminosa')]").click()
    #
    # def test_carnival_0dc0190c(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//a[@id='cdc-destinations']/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[10]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='cdc-ports']/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ccl-search-bar-expandable-filter[1]/div[1]/ul[1]/li[16]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='cdc-dates']/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[2]/li[10]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-cruise-search']/ccl-cruise-search[1]/div[3]/ccl-cruise-search-bar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/svg[1]/path[2]").click()
    #
    # def test_carnival_329d9ee8(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Weddings & Occasions')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccl-accomodations']/div[3]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/h3[1]").click()
    #
    # def test_carnival_3b74d9cc(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[1]/div[2]/ul[1]/li[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Trending (2)')]").click()
    #
    # def test_carnival_4008118a(self):
    #     # self.driver.get("https://www.carnival.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[1]/li[3]/div[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='cclr-global-header-root']/div[1]/header[1]/div[2]/nav[2]/div[2]/ul[1]/li[3]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//ul[@id='HeroSlidesContainer']/li[4]/a[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "filter-ship-BR").click()
    #     self.driver.find_element(By.ID, "filter-meal-breakfast").click()
    