import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from browser_helper import calculate_budget_dates, scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestParking:
    
    # def test_parking_0b342c57(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Boston')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").send_keys("hard rock cafe")
    #     self.driver.find_element(By.XPATH, "//div[@id='option-28468816']/div[1]/em[2]").click()
    #     self.driver.find_element(By.ID, "entranceDateFormatted").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'11')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[3]/strong[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'09:00PM')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[8]/strong[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'11:00PM')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "filter_category_general_1").click()
    #     self.driver.find_element(By.ID, "filter_category_general_4").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='result_35512']/div[1]/div[2]/div[2]/button[1]/span[1]").click()

    def test_parking_1c0acb0e(self):
        # self.driver.get("https://parking.com")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Find your city')]").click()
        self.driver.find_element(By.ID, "state_name").click()
        self.driver.find_element(By.ID, "state_37_item").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Arlington')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").clear()
        self.driver.find_element(By.ID, "txtsearch").clear()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").send_keys("5601 chapin ave")
        self.driver.find_element(By.ID, "txtsearch").send_keys("5601 Chapin Ave, Alexandria")

        # self.driver.find_element(By.XPATH, "//span[contains(.,'5601 Chapin Ave')]").click()
        # not giving searching result as when performed manually. Try add some sleep
        time.sleep(2)
        self.driver.find_element(By.ID, "txtsearch").send_keys(Keys.ENTER)

        # somehow the calendar dropdown is not showing and result in the element not found error, so try to use some sleep. Possibly because the page refreshing progress closed the calendar
        time.sleep(2)
        self.driver.find_element(By.ID, "entranceDateFormatted").click()

        # self.driver.find_element(By.XPATH, "//div[contains(.,'27')]").click()
        (start_date_year, start_date_month_adjusted, start_date_day), (end_date_year, end_date_month_adjusted, end_date_day) = calculate_budget_dates(7, 8)
        if self.driver.find_element(By.XPATH, f"//div[@role='calendar' and not(contains(@style, 'display: none;'))]//td[@year='{start_date_year}' and @month='{start_date_month_adjusted}' and @day='{start_date_day}']") is None:
            self.driver.find_element(By.XPATH, "//div[@role='calendar' and not(contains(@style, 'display: none;'))]//div[@role='navigator']/div[3]/i").click()
        self.driver.find_element(By.XPATH, f"//div[@role='calendar' and not(contains(@style, 'display: none;'))]//td[@year='{start_date_year}' and @month='{start_date_month_adjusted}' and @day='{start_date_day}']").click()

        self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[2]/strong[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'10:00AM')]").click()
        start_time_ele = self.driver.find_element(By.XPATH, "//strong[@data-toggle='dropdown' and @aria-expanded='true']//a[contains(text(),'10:00AM')]")
        scroll_to_element(self.driver, start_time_ele)
        start_time_ele.click()

        self.driver.find_element(By.ID, "exitDateFormatted").click()

        # self.driver.find_element(By.XPATH, "//div[contains(.,'28')]").click()
        if self.driver.find_element(By.XPATH, f"//div[@role='calendar' and not(contains(@style, 'display: none;'))]//td[@year='{end_date_year}' and @month='{end_date_month_adjusted}' and @day='{end_date_day}']") is None:
            self.driver.find_element(By.XPATH, "//div[@role='calendar' and not(contains(@style, 'display: none;'))]//div[@role='navigator']/div[3]/i").click()
        self.driver.find_element(By.XPATH, f"//div[@role='calendar' and not(contains(@style, 'display: none;'))]//td[@year='{end_date_year}' and @month='{end_date_month_adjusted}' and @day='{end_date_day}']").click()

        self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[7]/strong[1]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'10:00AM')]").click()
        end_time_ele = self.driver.find_element(By.XPATH, "//strong[@data-toggle='dropdown' and @aria-expanded='true']//a[contains(text(),'10:00AM')]")
        scroll_to_element(self.driver, end_time_ele)
        end_time_ele.click()

        self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[9]/button[1]").click()

        # need wait for a few seconds for the searching result to be loaded
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/strong[1]").click()

        self.driver.find_element(By.ID, "filter_category_general_3").click()
        self.driver.find_element(By.ID, "filter_category_general_7").click()
        self.driver.find_element(By.ID, "filter_category_facility_2").click()
        self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'View details')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div/span[2]/div/div[2]/ul/li[2]/div/div[1]/div[2]/a").click()

    # def test_parking_292749f0(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").send_keys("10001")
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'New York, NY, USA')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Price')]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='result_32255']/div[1]/div[1]/div[1]/h2[1]").click()
    #
    # def test_parking_aa1a4414(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.ID, "txtsearch").clear()
    #     self.driver.find_element(By.ID, "txtsearch").send_keys("Venice Beach")
    #     self.driver.find_element(By.XPATH, "//div[@id='option-82130558']/div[1]/em[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "filter_category_general_2").click()
    #
    # def test_parking_b1fa9bb3(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").send_keys("Disneyland")
    #     self.driver.find_element(By.ID, "txtsearch").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "filter_category_general_7").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View details')]").click()
    #
    # def test_parking_b9f5dd60(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Support')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='faq-accordion_heading-936']/h5[1]/span[1]").click()
    #
    # def test_parking_cdb6b70d(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cities')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[1]/div[3]/div[1]/div[2]/div[5]/div[1]/a[1]/h4[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[7]/div[2]/div[1]/div[11]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Warner Theatre')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See options')]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='result_16205']/div[1]/div[1]/div[1]/h5[1]").click()
    #
    # def test_parking_fbefeb82(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Add Parking to your Website')]").click()
    #     self.driver.find_element(By.ID, "companyNameInput").clear()
    #     self.driver.find_element(By.ID, "companyNameInput").send_keys("BOSTON LEGAL")
    #     self.driver.find_element(By.ID, "addressInput").clear()
    #     self.driver.find_element(By.ID, "addressInput").send_keys("BOSTON NAVY YARD")
    #     self.driver.find_element(By.XPATH, "//div[@id='option-24826823']/div[1]/em[2]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='msdrpdd21_titleText_title']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='msdrpdd21_titleText_child']/ul[1]/li[3]/span[1]").click()
    #     self.driver.find_element(By.ID, "msdrpdd23_titleText_title").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='msdrpdd23_titleText_child']/ul[1]/li[2]").click()
    #     self.driver.find_element(By.ID, "GetCode").click()
    #
    # def test_parking_50bd08bd(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").send_keys("Shubert Theatre")
    #     self.driver.find_element(By.XPATH, "//div[@id='option-67154966']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[1]/nav[1]/div[1]/a[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Price')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View details')]").click()
    #
    # def test_parking_7f640279(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cities')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[7]/div[2]/div[1]/div[12]/a[1]/img[1]").click()
    #
    # def test_parking_8b743c63(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.ID, "txtsearch").clear()
    #     self.driver.find_element(By.ID, "txtsearch").send_keys("MOMA")
    #     self.driver.find_element(By.XPATH, "//div[@id='option-57176755']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[1]/nav[1]/div[1]/a[2]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='result_10057']/div[1]/div[2]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='confirmPurchaseModal']/div[1]/div[1]/div[3]/button[1]").click()
    #
    # def test_parking_1b74fa2c(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.ID, "txtsearch").clear()
    #     self.driver.find_element(By.ID, "txtsearch").send_keys("sofi stadium")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'SoFi Stadium')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "filter_category_general_3").click()
    #
    # def test_parking_1f28fed3(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.ID, "txtsearch").clear()
    #     self.driver.find_element(By.ID, "txtsearch").send_keys("Thalia Hall")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'South Allport Street, Chicago, IL, USA')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "filter_category_general_1").click()
    #
    # def test_parking_34e13beb(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Cities')]").click()
    #     self.driver.find_element(By.ID, "state_name").click()
    #     self.driver.find_element(By.ID, "state_25_item").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'New York')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").send_keys("66 perry st")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[6]/div[1]/span[2]").click()
    #     self.driver.find_element(By.ID, "entranceDateFormatted").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'20')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[3]/strong[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'05:30PM')]").click()
    #     self.driver.find_element(By.ID, "exitDateFormatted").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'21')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[8]/strong[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'05:30AM')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[10]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Price')]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='result_10023']/div[1]/div[2]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='confirmPurchaseModal']/div[1]/div[1]/div[3]/button[1]").click()
    #
    # def test_parking_8e849b85(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").send_keys("stewart hotel")
    #     self.driver.find_element(By.XPATH, "//div[@id='option-15853044']/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Book Monthly Parking')]").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtFirstName").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtFirstName").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtFirstName").send_keys("James")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtLastName").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtLastName").send_keys("SMith")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtAddress1").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtAddress1").send_keys("133 st avenue")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtAddressCity").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtAddressCity").send_keys("New York")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_cboAddressState").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_cboAddressState").select("New York")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtZipCode").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtZipCode").send_keys("10001")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtPhone").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtPhone").send_keys("888888888")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtEmail").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtEmail").send_keys("buckeye.foobar@gmail.com")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtEmailConfirm").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtEmailConfirm").send_keys("buckeye.foobar@gmail.com")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtEmployerName").click()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtEmployerName").clear()
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtEmployerName").send_keys("Gua AB")
    #     self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnNext").click()
    #
    # def test_parking_9ed8cd2a(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").send_keys("radio city music hall")
    #     self.driver.find_element(By.XPATH, "//div[@id='option-48731160']/div[1]/em[3]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='c_map_sidebar']/div[1]/span[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/strong[1]").click()
    #     self.driver.find_element(By.ID, "filter_category_general_5").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View details')]").click()
    #
    # def test_parking_a31de393(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.ID, "txtsearch").clear()
    #     self.driver.find_element(By.ID, "txtsearch").send_keys("Madison Square Garden")
    #     self.driver.find_element(By.XPATH, "//div[@id='option-26867968']/div[1]/em[1]").click()
    #
    # def test_parking_a5c1095b(self):
    #     # self.driver.get("https://parking.com")
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").clear()
    #     self.driver.find_element(By.XPATH, "//form[@id='homepageSearchForm']/div[1]/div[1]/div[1]/div[1]/span[1]/label[1]/span[1]").send_keys("New York City")
    #     self.driver.find_element(By.XPATH, "//div[@id='option-51131358']/div[1]").click()
    #     self.driver.find_element(By.ID, "entranceDateFormatted").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[3]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[3]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[3]/div[1]/div[1]/div[3]/i[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'5')]").click()
    #     self.driver.find_element(By.ID, "exitDateFormatted").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'9')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='maps']/div[2]/div[3]/div[1]/div[4]/div[2]/div[10]/button[1]").click()
    