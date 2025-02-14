import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from browser_helper import get_control_key


@pytest.mark.usefixtures("setup_class")
class TestWebmd:
    def test_webmd_b3f27ec6(self):
        # self.driver.get("https://www.webmd.com/")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find a Doctor')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[5]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Botox (Botulinum toxin)')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Rhode Island')]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Bristol')]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/main[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()
        # website logic changed, use the search bar instead
        self.driver.find_element(By.ID, "searchkeywords_desktop").clear()
        self.driver.find_element(By.ID, "searchkeywords_desktop").send_keys('Botox (Botulinum toxin)')
        self.driver.find_element(By.ID, "searchlocation_desktop").send_keys(get_control_key() + "a")
        self.driver.find_element(By.ID, "searchlocation_desktop").send_keys(Keys.DELETE)
        self.driver.find_element(By.ID, "searchlocation_desktop").send_keys('Bristol, RI')
        self.driver.find_element(By.XPATH, "//span[@class='webmd-input-group__append']/button[@aria-label='Search']").click()

        # self.driver.find_element(By.ID, "webmd-collapse-head-186").click()
        # self.driver.find_element(By.XPATH, "//div[@id='webmd-collapse-content-186']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@class='filters-container' and not(@style='display: none;')]//span[text()='Virtual Visit']").click()
        # can't find care credit in the new list, use Aetna instead
        self.driver.find_element(By.XPATH, "//span[text()='Insurance']").click()
        # self.driver.find_element(By.XPATH, "//div[contains(@id, 'webmd-popover-')]//input[@placeholder='Search Insurance Plans']").clear()
        # self.driver.find_element(By.XPATH, "//div[contains(@id, 'webmd-popover-')]//input[@placeholder='Search Insurance Plans']").send_keys("Blue Cross")
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'webmd-popover-')]//span[text()='Aetna']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'webmd-popover-') and @aria-hidden='false']//span[text()=' Apply ']").click()


        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='filters-container' and not(@style='display: none;')]//span[text()=' Accepts New Patients ']").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//span[text()='Request Now']").get_native_element())

        # self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Add a First Preferred Date']").click()
        # self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[4]/div[5]").click()
        # self.driver.find_element(By.XPATH, "//input[@name='first_name' and @value='' and @placeholder='First Name']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='first_name' and @value='' and @placeholder='First Name']").send_keys("James")
        # self.driver.find_element(By.XPATH, "//input[@name='last_name' and @value='' and @placeholder='Last Name']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='last_name' and @value='' and @placeholder='Last Name']").send_keys("Smith")
        # self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/span[1]/img[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/select[1]").select("1990")
        # self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/select[1]").select("June")
        # self.driver.find_element(By.XPATH, "//div[@id='ib-booking-app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[4]/div[4]").click()
        # self.driver.find_element(By.XPATH, "//input[@name='phone' and @value='' and @placeholder='(555) 555-5555']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='phone' and @value='' and @placeholder='(555) 555-5555']").send_keys("456546546")
        # self.driver.find_element(By.XPATH, "//input[@name='email' and @value='' and @placeholder='email@example.com']").clear()
        # self.driver.find_element(By.XPATH, "//input[@name='email' and @value='' and @placeholder='email@example.com']").send_keys("buckeye.foobar@gmail.com")
        # self.driver.find_element(By.XPATH, "//textarea[@name='visit_reason' and @placeholder='']").clear()
        # self.driver.find_element(By.XPATH, "//textarea[@name='visit_reason' and @placeholder='']").send_keys("Consultation")

        # ignore the following steps since form filled out is at an external website which varies across different website
        # self.driver.find_element(By.XPATH, "//span[text()='New Patient']").click()
        # self.driver.find_element(By.XPATH, "//a[text()='Continue']").click()
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Add a First Preferred Date']").click()
        # start_date_str, _ = calculate_dates_with_suffix_webmd(7, 7)
        # if self.driver.find_element(By.XPATH, f"//div[contains(@aria-label, '{start_date_str}')]") is None:
        #     self.driver.find_element(By.XPATH, "//button[@aria-label='Next Month']").click()
        #
        # self.driver.find_element(By.XPATH, f"//div[contains(@aria-label, '{start_date_str}')]").click()
        # self.driver.find_element(By.NAME, "first_name").clear()
        # self.driver.find_element(By.NAME, "first_name").send_keys('James')
        # self.driver.find_element(By.NAME, "last_name").clear()
        # self.driver.find_element(By.NAME, "last_name").send_keys('Smith')
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Date of Birth']").clear()
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Date of Birth']").send_keys('06/20/1990')
        # self.driver.find_element(By.NAME, "last_name").click()
        # self.driver.find_element(By.NAME, "phone").clear()
        # self.driver.find_element(By.NAME, "phone").send_keys('456546546')
        # self.driver.find_element(By.NAME, "email").clear()
        # self.driver.find_element(By.NAME, "email").send_keys('buckeye.foobar@gmail.com')
        # self.driver.find_element(By.NAME, "visit_reason").clear()
        # self.driver.find_element(By.NAME, "visit_reason").send_keys('Consultation')
