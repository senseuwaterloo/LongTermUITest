import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_inside_element


@pytest.mark.usefixtures("driver_session")
class TestNewegg:
    def test_newegg_e483a49f(self):
        self.driver.get("https://newegg.com")

        self.driver.find_element(By.XPATH, "//a[contains(@id, 'trendingBanner_')]/span[text()='PC Builder']").click()

        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/i[@class='diy-cpu']").click()

        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-cpu']").click()

        self.driver.find_element(By.XPATH, "//span[text()='Intel Core i7']").click()

        self.driver.find_element(By.XPATH, "//button[text()=' Apply']").click()

        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")

        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-motherboard']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")

        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-memory']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-gpu']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-case']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-psu']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-hdd']").click()
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/strong[text()='SSD']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-cooling']").click()
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/strong[text()='Fan & Heatsink']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-os']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-control']/i[contains(@class, 'fa-arrow-circle-right')]").click()
        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='app']/div[@class='pc-builder']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/span[text()='Accessories']").click()
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/strong[text()='LCD / LED Monitors']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-control']/i[contains(@class, 'fa-arrow-circle-right')]").click()
        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='app']/div[@class='pc-builder']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon is-active']/span[text()='Accessories']").click()
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/strong[text()='Keyboards']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-control']/i[contains(@class, 'fa-arrow-circle-right')]").click()
        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='app']/div[@class='pc-builder']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon is-active']/span[text()='Accessories']").click()
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/strong[text()='Gaming Keyboards']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-control']/i[contains(@class, 'fa-arrow-circle-right')]").click()
        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='app']/div[@class='pc-builder']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon is-active']/span[text()='Accessories']").click()
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/strong[text()='Gaming Mice']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()
