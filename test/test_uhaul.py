import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_budget_dates


@pytest.mark.usefixtures("driver_session")
class TestUhaul:
    def test_uhaul_9d8ba96c(self):
        self.driver.get("https://uhaul.com")
        self.driver.find_element(By.ID, "PickupLocation-TruckOnly").clear()
        self.driver.find_element(By.ID, "PickupLocation-TruckOnly").send_keys("Birmingham, Alabama")

        self.driver.find_element(By.XPATH, "//div[text()='Birmingham, AL' and contains(@id, 'ui-id-')]").click()

        self.driver.find_element(By.ID, "DropoffLocation-TruckOnly").clear()

        self.driver.find_element(By.ID, "DropoffLocation-TruckOnly").send_keys("Mobil Alabama")

        self.driver.find_element(By.XPATH, "//form[@id='EquipmentSearch']/div[3]/div[1]/label[1]").click()

        (start_date_year, start_date_month_adjusted, start_date_day), (end_date_year, end_date_month_adjusted, end_date_day) = calculate_budget_dates(7, 14)
        self.driver.find_element(By.XPATH, f"//td[@data-year='{start_date_year}' and @data-month='{start_date_month_adjusted}' and not(contains(@class, 'ui-datepicker-other-month'))]/a[text()='{start_date_day}']").click()

        self.driver.find_element(By.XPATH, "//form[@id='EquipmentSearch']/div[3]/div[2]/button[1]").click()
        self.driver.find_element(By.ID, "submit_DC").click()

        pickup_time_dropdown = self.driver.find_element(By.ID, "SelectedScheduleTime_Row0_Entity775073")
        pickup_time_select = Select(pickup_time_dropdown)
        pickup_time_select.select_by_visible_text("12:00 AM Midnight")

        self.driver.find_element(By.ID, "btnContinue_Row0_Entity775073").click()
        self.driver.find_element(By.XPATH, "//div[@id='sharedRevealContent']/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/button[1]").click()

        self.driver.find_element(By.ID, "btnSelectDropoffNoPreference").click()
        self.driver.find_element(By.ID, "btnContinueSafeTrip").click()

        self.driver.find_element(By.ID, "linkNoSafeTrip").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'No thanks, I do not need these items')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'No thanks, I do not need storage')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'No thanks, I do not need supplies')]").click()

        self.driver.find_element(By.XPATH, "//a[contains(text(),'No thanks, I do not need help in ')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'No thanks, I do not need help in ')]").click()

        self.driver.find_element(By.ID, "hlSaveQuote").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Save Equipment Quote')]").click()
