import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_down


@pytest.mark.usefixtures("driver_session")
class TestStudent:
    def test_student_a36836fd(self):
        self.driver.get("https://student.com")

        self.driver.find_element(By.XPATH, "//span[text()='Oceania']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Sydney']").click()

        self.driver.find_element(By.XPATH, "//span[@role='presentation' and text()='Rentals']").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Group booking')]").click()

        if self.driver.find_element(By.XPATH, "//div[@class='download-banner__close-content' and @role='presentation']") is not None:
            self.driver.find_element(By.XPATH, "//div[@class='download-banner__close-content' and @role='presentation']").click()

        self.driver.find_element(By.XPATH, "//input[@name='groupSize' and @value='' and @placeholder='Select group size']").click()
        self.driver.find_element(By.XPATH, "//li[@value='FIVE_TO_TEN']").click()
        self.driver.find_element(By.XPATH, "//input[@name='preciseGroupSize' and @value='' and @type='text' and @placeholder='Input precise group size']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='preciseGroupSize' and @value='' and @type='text' and @placeholder='Input precise group size']").send_keys("10")
        self.driver.find_element(By.XPATH, "//input[@name='city' and @value='' and @placeholder='Search destination city']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='city' and @value='' and @placeholder='Search destination city']").send_keys("sydney")
        self.driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/ul[1]/li[3]/div[1]/div[1]/ul[1]/div[2]/li[1]/p[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='university' and @value='' and @placeholder='Input destination university']").click()
        self.driver.find_element(By.XPATH, "//li[@value='17']").click()
        self.driver.find_element(By.XPATH, "//input[@name='interestedProperty' and @value='' and @type='text' and @placeholder='Input Interested Property']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='interestedProperty' and @value='' and @type='text' and @placeholder='Input Interested Property']").send_keys("apartment")

        scroll_down(self.driver, 500)
        self.driver.find_element(By.XPATH, "//input[@name='moveInDate' and @value='' and @type='text' and @placeholder='Desired move-in date']").click()

        self.driver.find_element(By.XPATH, "//select[@name='year']").click()
        move_in_year_dropdown = self.driver.find_element(By.XPATH, "//select[@name='year']")
        move_in_year_select = Select(move_in_year_dropdown)
        move_in_year_select.select_by_value("2025")
        move_in_month_dropdown = self.driver.find_element(By.XPATH, "//select[@name='month']")
        move_in_month_select = Select(move_in_month_dropdown)
        move_in_month_select.select_by_visible_text("Apr")
        self.driver.find_element(By.XPATH, "//div[@aria-label='Tue Apr 01 2025']").click()

        self.driver.find_element(By.XPATH, "//input[@name='moveOutDate' and @value='' and @type='text' and @placeholder='Desired move-out date']").click()

        self.driver.find_element(By.XPATH, "//select[@name='year']").click()
        move_out_year_dropdown = self.driver.find_element(By.XPATH, "//select[@name='year']")
        move_out_year_select = Select(move_out_year_dropdown)
        move_out_year_select.select_by_value("2026")
        move_out_month_dropdown = self.driver.find_element(By.XPATH, "//select[@name='month']")
        move_out_month_select = Select(move_out_month_dropdown)
        move_out_month_select.select_by_value("2")
        self.driver.find_element(By.XPATH, "//div[@aria-label='Tue Mar 31 2026']").click()

        self.driver.find_element(By.XPATH, "//input[@name='budgetStartValue' and @value='' and @type='text' and @placeholder='e.g. 100']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='budgetStartValue' and @value='' and @type='text' and @placeholder='e.g. 100']").send_keys("100")
        self.driver.find_element(By.XPATH, "//input[@name='budgetEndValue' and @value='' and @type='text' and @placeholder='e.g. 300']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='budgetEndValue' and @value='' and @type='text' and @placeholder='e.g. 300']").send_keys("500")
        self.driver.find_element(By.XPATH, "//input[@name='budgetSelectTime' and @value='Per Week' and @placeholder='']").click()
        self.driver.find_element(By.XPATH, "//li[@value='MONTHLY']").click()
        self.driver.find_element(By.XPATH, "//input[@name='name' and @value='' and @type='text' and @placeholder='Input your name']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='name' and @value='' and @type='text' and @placeholder='Input your name']").send_keys("John Brown")
        self.driver.find_element(By.XPATH, "//input[@name='emailAddress' and @value='' and @type='text' and @placeholder='Input email address']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='emailAddress' and @value='' and @type='text' and @placeholder='Input email address']").send_keys("Johnbrown@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@name='phone-input' and @value='' and @type='phone' and @placeholder='Phone number']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='phone-input' and @value='' and @type='phone' and @placeholder='Phone number']").send_keys("3324456543")
