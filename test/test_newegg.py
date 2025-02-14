import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_inside_element


@pytest.mark.usefixtures("setup_class")
class TestNewegg:
    def test_newegg_e483a49f(self):
        # TODO be aware that these actions generated from the agent doesn't really satisfy the requirements of this task
        # self.driver.get("https://newegg.com")
        # self.driver.find_element(By.XPATH, "//a[@id='trendingBanner_671801']/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(@id, 'trendingBanner_')]/span[text()='PC Builder']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[2]/div[1]/div[1]/div[5]/div[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/i[@class='diy-cpu']").click()

        # modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']//div[@class='pc-builder-body']/div[1]").get_native_element()
        # scroll_inside_element(self.driver, modal_dialog_div)
        # modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']//div[@class='pc-builder-body']/div[1]").get_native_element()
        # scroll_inside_element(self.driver, modal_dialog_div)
        # time.sleep(20)

        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-cpu']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/dl[3]/dd[1]/ul[1]/li[5]/div[1]/label[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Intel Core i7']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/dl[3]/dd[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//button[text()=' Apply']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[8]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-motherboard']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")

        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[8]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()
        # need to wait for several seconds for the page to finish loading otherwise it will refresh after the following click action and make that click performed but doesn't give expected result page
        time.sleep(2)
        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/a[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[7]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-memory']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[4]/div[1]/a[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[8]/div[1]/div[2]/div[2]/div[1]/button[1]/i[1]").click()
        # need to wait for several seconds for the page to finish loading otherwise it will refresh after the following click action and make that click performed but doesn't give expected result page
        # or the element click will be intercept by other element dur to the layout is changing
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-gpu']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[5]/div[1]/a[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[8]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        # need to wait for several seconds for the page to finish loading otherwise it will refresh after the following click action and make that click performed but doesn't give expected result page
        # or the element click will be intercept by other element dur to the layout is changing
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-case']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[6]/div[1]/a[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[8]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-psu']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[7]/div[1]/a[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/strong[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[7]/div[1]/div[2]/div[2]/div[1]/button[1]").click()

        # need to wait for a few second otherwise the scroll will not work. Probably because page is still loading, wrong scroll element will be located.
        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-hdd']").click()
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/strong[text()='SSD']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[8]/div[1]/a[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[6]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-cooling']").click()
        self.driver.find_element(By.XPATH, "//a[@class='pc-builder-icon']/strong[text()='Fan & Heatsink']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[9]/div[1]/a[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[5]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        time.sleep(2)
        modal_dialog_div = self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']//div[@class='pc-builder-body']/div[1]").get_native_element()
        scroll_inside_element(self.driver, modal_dialog_div)
        self.driver.find_element(By.XPATH, "//div[@class='pc-builder-icon']/a[1]/i[@class='diy-os']").click()
        sort_by_dropdown = self.driver.find_element(By.XPATH, "//select[ancestor::label[@class='form-select' and preceding-sibling::*[1][self::span and text()='Sort By:']]]")
        sort_by_select = Select(sort_by_dropdown)
        sort_by_select.select_by_visible_text("Lowest Price")
        self.driver.find_element(By.XPATH, "//table[@class='table-vertical']/tbody[1]/tr[2]/td[@class='td-action']//div[@class='item-button-area']/button[1]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[10]/div[1]/a[1]/div[1]/i[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/a[1]/strong[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[8]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        # to avoid overlap with the footer......
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

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[10]/div[1]/a[1]/div[1]/i[3]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[17]/a[1]/strong[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[7]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        # to avoid overlap with the footer......
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

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[10]/div[1]/a[1]/div[1]/i[4]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/a[1]/strong[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[8]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
        # to avoid overlap with the footer......
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

        # self.driver.find_element(By.XPATH, "//div[@id='modal-pc-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[10]/div[1]/a[1]/div[1]/i[2]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[4]/a[1]/strong[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]/select[1]").select("Lowest Price")
        # self.driver.find_element(By.XPATH, "//div[@id='app']/div[3]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[7]/td[8]/div[1]/div[2]/div[2]/div[1]/button[1]").click()

        # to avoid overlap with the footer......
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
