import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestCvs:
    
    def test_cvs_7acc430a(self):
        # self.driver.get("https://www.cvs.com/")
        # uiteststudy@gmail.com:Pass4John!

        # shadow dom is introduced in the new version
        # self.driver.find_element(By.ID, "Health-menu").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Get Virtual Care')]").click()
        # need to handle shadow dom to click above element
        header_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "body > app-root > app-homepage > cvs-header-component > div > cvs-header > div > cvs-header-desktop")
        sign_in_dropdown = header_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#cvs-desktop-header-container > div > div.header-desktop-top-right.sc-cvs-header-desktop > div > cvs-header-acc-dropdown")
        sign_in_dropdown.click()

        sign_in_content = sign_in_dropdown.shadow_root.find_element(By.CSS_SELECTOR, "div > div > div.acc-dropdown > cvs-header-acc-content")
        sign_in_button = sign_in_content.shadow_root.find_element(By.CSS_SELECTOR, "div > div > div.dropdown-top > a.signin-button.primary.first-link")
        sign_in_button.click()

        self.driver.find_element(By.ID, "emailField").click()
        self.driver.find_element(By.ID, "emailField").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.XPATH, "//div[@id='login-container']/div/div/cvs-email-field/button").click()
        self.driver.find_element(By.ID, "cvs-password-field-input").click()
        self.driver.find_element(By.ID, "cvs-password-field-input").send_keys("Pass4John!")
        self.driver.find_element(By.XPATH, "//div[@id='login-container']/div/div/cvs-password-field/div[1]/div[3]").click()

        header_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "body > app-root > app-homepage > cvs-header-component > div > cvs-header > div > cvs-header-desktop")
        health_menu_button_shadow_root = header_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#cvs-desktop-header-container > div > div.header-desktop-top-left.sc-cvs-header-desktop > nav > cvs-header-desktop-dropdown:nth-child(2)")
        health_menu_button_shadow_root.click()
        health_menu_content_shadow_root = health_menu_button_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#Health-menu-dropdown > div.menu-dropdown-body > cvs-header-menu")
        get_virtual_care_button = health_menu_content_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "nav > ul > li:nth-child(5)")
        get_virtual_care_button.click()
        self.driver.find_element(By.ID, "cta-btn1").click()

        self.driver.find_element(By.XPATH, "//label[@id='patient-0-fullname']/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Select patient and continue')]").click()

        self.driver.find_element(By.ID, "dob").click()
        self.driver.find_element(By.ID, "dob").clear()
        self.driver.find_element(By.ID, "dob").send_keys("01/01/2000")
        self.driver.find_element(By.ID, "gender-male").click()
        self.driver.find_element(By.ID, "aetna_id_no").click()
        self.driver.find_element(By.ID, "phoneNo").clear()
        self.driver.find_element(By.ID, "phoneNo").send_keys("5145778593")
        self.driver.find_element(By.ID, "streetAddress").clear()
        self.driver.find_element(By.ID, "streetAddress").send_keys("123 st")
        self.driver.find_element(By.ID, "city").clear()
        self.driver.find_element(By.ID, "city").send_keys("New York city")

        # self.driver.find_element(By.ID, "state").clear()
        # self.driver.find_element(By.ID, "state").select("New York")
        state_dropdown = self.driver.find_element(By.ID, "state")
        state_select = Select(state_dropdown)
        state_select.select_by_value('NY')

        self.driver.find_element(By.ID, "zipCode").clear()
        self.driver.find_element(By.ID, "zipCode").send_keys("10001")
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    # def test_cvs_0fc202d2(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='' and @value='' and @type='search' and @placeholder='Search products and services']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='' and @value='' and @type='search' and @placeholder='Search products and services']").send_keys("benadryl")
    #     self.driver.find_element(By.ID, "rec-id-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/nav[1]/div[2]/div[1]/div[11]/div[1]/div[1]/div[2]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/nav[1]/div[2]/div[1]/div[11]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/nav[1]/div[2]/div[1]/div[11]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/nav[1]/div[2]/div[1]/div[11]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
    #
    # def test_cvs_0f9dd411(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//a[@id='sec1-link1']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Explore all MinuteClinic health services')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/div[2]/app-mc-services-tiles[1]/div[1]/ul[1]/li[4]/div[1]/div[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/p[1]/span[3]").click()
    #     self.driver.find_element(By.ID, "accordion-cat4").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hair Loss Evaluation & Treatment')]").click()
    #     self.driver.find_element(By.ID, "location").clear()
    #     self.driver.find_element(By.ID, "location").send_keys("45201")
    #     self.driver.find_element(By.XPATH, "//button[@id='find-care-btn']/span[1]").click()
    #
    # def test_cvs_cd8f1f63(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='' and @value='' and @type='search' and @placeholder='Search products and services']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='' and @value='' and @type='search' and @placeholder='Search products and services']").send_keys("dayquil")
    #     self.driver.find_element(By.XPATH, "//button[@id='search-submit-homepage']/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='Vicks-DayQuil-SEVERE-Cough,-Cold-&-Flu-Relief,-24-LiquiCaps---Relieves-Daytime-Sore-Throat,-Fever,-and-Congestion']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='pdp-reviews']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/label[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.ID, "react-select-4-option-5").click()
    #
    # def test_cvs_d29e8a14(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.ID, "Savings & Memberships-menu").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Weekly Ad')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@role='tab' and @title='List View']").click()
    #
    # def test_cvs_e638beb6(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//a[@id='sec1-link1']/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='a1']/div[1]/div[2]/a[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "location").click()
    #     self.driver.find_element(By.ID, "location").clear()
    #     self.driver.find_element(By.ID, "location").send_keys("10003")
    #     self.driver.find_element(By.XPATH, "//button[@id='find-care-btn']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//app-service-clinic-list[@id='clinicResults-overview']/div[1]/div[1]/div[3]/div[2]").click()
    #
    # def test_cvs_53b4ca73(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.ID, "Shop-menu").click()
    #     self.driver.find_element(By.ID, "1-3-10").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Shop-menu-dropdown']/div[1]/cvs-header-menu[1]/template[1]/nav[1]/ul[1]/li[8]/cvs-header-menu-item[1]/template[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vitamin C')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/label[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "react-select-2-option-1").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='product-tile-1010806']/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='large-screen-atc-button']/div[1]/div[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='atc-modal']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/nav[1]/div[1]/div[4]/a[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//nav[@id='vizNavShopbycategory']/div[1]/div[1]/ul[1]/li[4]/div[1]/a[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/label[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "react-select-2-option-1").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='product-tile-1010623']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]").click()
    #
    # def test_cvs_5b433cc4(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//a[@id='sec1-link6']/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/header[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[3]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//section[@id='CVS-Health-At-Home-COVID-19-Test-Kit,-2-CT']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='large-screen-atc-button']/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #
    # def test_cvs_e92cd371(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='' and @value='' and @type='search' and @placeholder='Search products and services']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='' and @value='' and @type='search' and @placeholder='Search products and services']").send_keys("zyrtec")
    #     self.driver.find_element(By.ID, "rec-id-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='product-tile-1070930']/div[1]/div[2]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[2]/div[3]/section[2]/div[2]/button[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text']").send_keys("90028")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[8]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'6201 Hollywood Blvd., Suite 126')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Make this my store')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(@href, '/shop-assets/media/icons.5637b711.svg#xIcon')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='large-screen-atc-button']/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    #
    # def test_cvs_ff6ff6e5(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.ID, "Health-menu").click()
    #     self.driver.find_element(By.ID, "1-2-7").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Skin, Hair & Nails')]").click()
    #     self.driver.find_element(By.ID, "accordion-cat4").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Hair Loss Evaluation & Treatment')]").click()
    #     self.driver.find_element(By.ID, "location").clear()
    #     self.driver.find_element(By.ID, "location").send_keys("10018")
    #     self.driver.find_element(By.ID, "find-care-btn").click()
    #     self.driver.find_element(By.XPATH, "//app-service-clinic-list[@id='clinicResults-overview']/div[1]/div[1]/div[3]/div[2]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Clinic details')]").click()
    #
    # def test_cvs_95499427(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='' and @value='' and @type='search' and @placeholder='Search products and services']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='' and @value='' and @type='search' and @placeholder='Search products and services']").send_keys("cough medicine")
    #     self.driver.find_element(By.ID, "rec-id-0").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/nav[1]/div[2]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/nav[1]/div[2]/div[1]/div[6]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]").click()
    #
    # def test_cvs_2281faf9(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='' and @value='' and @type='search' and @placeholder='Search products and services']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@role='combobox' and @name='' and @value='' and @type='search' and @placeholder='Search products and services']").send_keys("rogaine")
    #     self.driver.find_element(By.XPATH, "//div[@id='product-tile-1013645']/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[4]/div[3]/div[4]/div[1]/h2[1]").click()
    #
    # def test_cvs_27724810(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//button[@id='changeStore']/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("90028")
    #     self.driver.find_element(By.XPATH, "//div[@id='search-container']/div[1]/button[1]").click()
    #
    # def test_cvs_51e85ea8(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.ID, "Shop-menu").click()
    #     self.driver.find_element(By.ID, "1-3-10").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='Shop-menu-dropdown']/div[1]/cvs-header-menu[1]/template[1]/nav[1]/ul[1]/li[8]/cvs-header-menu-item[1]/template[1]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Vitamin D')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@role='checkbox']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/nav[1]/div[2]/div[1]/div[6]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='product-tile-711216']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]").click()
    #
    # def test_cvs_978376c1(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.ID, "Prescriptions-menu").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Pharmacy & Health Rewards')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Join ExtraCare Pharmacy & Health Rewards')]").click()
    #
    # def test_cvs_9a9b1b45(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//a[@id='sec1-link3']/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='uuid2bd27cb9-8426-4450-a100-ab849b3cdabf']/span[1]").click()
    #     self.driver.find_element(By.ID, "state-label").clear()
    #     self.driver.find_element(By.ID, "state-label").send_keys("90028")
    #     self.driver.find_element(By.XPATH, "//div[@id='content']/section[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
    #
    # def test_cvs_bb7c3e38(self):
    #     # self.driver.get("https://www.cvs.com/")
    #     self.driver.find_element(By.XPATH, "//div[@id='cvs-header-util-link']/a[1]").click()
    #     self.driver.find_element(By.ID, "store-search-input").clear()
    #     self.driver.find_element(By.ID, "store-search-input").send_keys("43215")
    #     self.driver.find_element(By.XPATH, "//li[@id='cvs-sl-search-result-item-0']/span[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View weekly deals')]").click()
    