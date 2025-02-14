import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_class")
class TestPetfinder:
    def test_petfinder_432a58b4(self):
        # self.driver.get("https://petfinder.com")
        # remove the following actions since we now directly start from the https://petfinderfoundation.org/ website
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Adopt or Get Involved')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Petfinder Foundation')]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Donate')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Donate' and ./following-sibling::a[text()='Apply']]").click()

        # handle shadow dom and iframe
        payment_widget_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#main > div > div > div > givebutter-widget")
        payment_form_shadow_root = payment_widget_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "givebutter-giving-form")
        payment_iframe_shadow_root = payment_form_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "givebutter-iframe")
        payment_inner_iframe = payment_iframe_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "iframe").get_native_element()
        self.driver.switch_to.frame(payment_inner_iframe)

        # self.driver.find_element(By.ID, "label_3_30_1").click()
        self.driver.find_element(By.ID, "frequency_1").click()

        # self.driver.find_element(By.ID, "input_3_26").clear()
        # self.driver.find_element(By.ID, "input_3_26").send_keys("10")
        self.driver.find_element(By.ID, "amountOtherInput").clear()
        self.driver.find_element(By.ID, "amountOtherInput").send_keys("10")

        # self.driver.find_element(By.ID, "gform_next_button_3_1").click()
        # self.driver.find_element(By.ID, "gform_next_button_3_3").click()
        self.driver.find_element(By.XPATH, "//div[@id='__givebutter_flow__main']/div/div[1]/form/div[2]/button").click()
        self.driver.find_element(By.ID, "card").click()

        # self.driver.find_element(By.ID, "input_3_22_1").clear()
        # self.driver.find_element(By.ID, "input_3_22_1").send_keys("5555555555555555")
        # self.driver.find_element(By.ID, "input_3_22_2_month").clear()
        # self.driver.find_element(By.ID, "input_3_22_2_month").select("12")
        # self.driver.find_element(By.ID, "input_3_22_2_year").clear()
        # self.driver.find_element(By.ID, "input_3_22_2_year").select("2036")
        # self.driver.find_element(By.XPATH, "//span[@id='input_3_22_2_cardinfo_right']/label[1]").clear()
        # self.driver.find_element(By.XPATH, "//span[@id='input_3_22_2_cardinfo_right']/label[1]").send_keys("555")
        # self.driver.find_element(By.ID, "input_3_22_5").clear()
        # self.driver.find_element(By.ID, "input_3_22_5").send_keys("Jane Doe")
        self.driver.find_element(By.ID, "label_first_name").send_keys("Jane")
        self.driver.find_element(By.ID, "label_last_name").send_keys("Doe")
        self.driver.find_element(By.ID, "label_email").send_keys("uiteststudy@gmail.com")
        self.driver.find_element(By.ID, "label_phone_raw").send_keys("2028766789")
        self.driver.find_element(By.ID, "label_address_1").send_keys("11 Blair Court")
        self.driver.find_element(By.ID, "label_city").send_keys("Newark")
        self.driver.find_element(By.ID, "label_zipcode").send_keys("19922")

        country_dropdown = self.driver.find_element(By.NAME, "country")
        country_select = Select(country_dropdown)
        country_select.select_by_visible_text("United States")

        state_dropdown = self.driver.find_element(By.NAME, "state")
        state_select = Select(state_dropdown)
        state_select.select_by_visible_text("Georgia")

        payment_inner_inner_iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame']").get_native_element()
        self.driver.switch_to.frame(payment_inner_inner_iframe)

        self.driver.find_element(By.NAME, "cardnumber").send_keys("5555555555555555")
        self.driver.find_element(By.NAME, "exp-date").send_keys("1236")
        self.driver.find_element(By.NAME, "cvc").send_keys("555")
