import time

import pytest
from selenium.webdriver.common.by import By

from browser_helper import switch_to_new_tab, calculate_dates


@pytest.mark.usefixtures("setup_class")
class TestQatarairways:
    def test_qatarairways_4786982f(self):
        # self.driver.get("https://www.qatarairways.com/en-us/homepage.html")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Book')]").click()
        # Just update the locator to make it locate the element uniquely, doesn't really impact the result since the first element located by the locator is the target element.
        self.driver.find_element(By.XPATH, "//a[normalize-space(text())='Book' and @role='button']").click()

        # self.driver.find_element(By.XPATH, "//ul[@id='planyourtrip']/li[3]/a[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//ul[@id='planyourtrip']/li[3]/a[1]/span[text()='Hotels']").click()
        switch_to_new_tab(self.driver)

        self.driver.find_element(By.ID, "ss").clear()
        self.driver.find_element(By.ID, "ss").send_keys("washington")
        self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/span[2]/span[1]").click()

        start_date_str, end_date_str = calculate_dates(14, 15)

        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/span[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[2]/div[2]/div[1]/div[1]/div[5]/ul[1]/li[1]/label[1]/span[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//form[@id='frm']/div[1]/div[4]/div[2]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, f"//td[@data-date='{start_date_str}']").click()
        self.driver.find_element(By.XPATH, f"//td[@data-date='{end_date_str}']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='left_col_wrapper']/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-sb-id='main' and @type='submit']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='left_col_wrapper']/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='left_col_wrapper']/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='left_col_wrapper']/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='left_col_wrapper']/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='occupancy-config']/span[@data-testid='searchbox-form-button-icon']").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='occupancy-popup']/div/div[1]/div[2]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='occupancy-popup']/div/div[1]/div[2]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='occupancy-popup']/div/div[3]/div[2]/button[2]").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='occupancy-popup']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='filter_group_di_:R44q:']/button[1]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_group_di_:R44q:']/div[9]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_group_hotelfacility_:R3cq:']/button[1]/span[1]/span[1]/svg[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_group_hotelfacility_:R3cq:']/div[17]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='filter_group_class_:R14q:']/div[10]/label[1]/span[2]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='search_results_table']/div[2]/div[1]/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[4]/a[1]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//button[@id='hcta']/span[1]").click()
        # need to wait for a second for the page to be refreshed after selecting each filter otherwise the filters will not be properly selected
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='bodyconstraint']//div[@data-testid='filters-group' and @data-filters-group='di']//div[text()='Downtown D.C.']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='bodyconstraint']//button[contains(@aria-controls, 'filter_group_hotelfacility') and @data-testid='filters-group-expand-collapse']").click()
        self.driver.find_element(By.XPATH, "//div[@data-testid='filters-group' and @data-filters-group='hotelfacility']//div[text()='Free Wifi']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='bodyconstraint']//div[@data-testid='filters-group' and @data-filters-group='class']//div[text()='5 stars']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@data-testid='sorters-dropdown-trigger']").click()
        self.driver.find_element(By.XPATH, "//button[@data-id='price' and @type='button']//span[text()='Price (lowest first)']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='search_results_table']/div[2]/div/div/div[3]/div[3]//a[@data-testid='availability-cta-btn']").click()
    