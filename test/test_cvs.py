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
