import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import calculate_dates_weekday_mta_format


@pytest.mark.usefixtures("setup_class")
class TestNewMtaInfo:
    
    # def test_newmtainfo_961e4feb(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Planned Work')]").click()
    #     self.driver.find_element(By.ID, "edit-search").clear()
    #     self.driver.find_element(By.ID, "edit-search").send_keys("S92")
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
    #
    # def test_newmtainfo_a29533ef(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//div[@id='blockHeader']/label[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Projects')]").click()
    #     self.driver.find_element(By.ID, "edit-search-api-fulltext").clear()
    #     self.driver.find_element(By.ID, "edit-search-api-fulltext").send_keys("jamaica bus depot expansion")
    #     self.driver.find_element(By.ID, "edit-search-api-fulltext").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[4]/article[1]/div[2]/div[2]/div[1]/div[4]/div[1]/a[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[4]/article[1]/section[1]/div[1]/div[2]/div[1]/div[1]/details[2]/summary[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Volume 2: FEIS Report')]").click()
    #
    # def test_newmtainfo_c52fcdf7(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.ID, "edit-origin").click()
    #     self.driver.find_element(By.ID, "edit-origin").clear()
    #     self.driver.find_element(By.ID, "edit-origin").send_keys("Central park")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[1]/div[1]/div[1]/ul[1]/div[2]/li[1]").click()
    #     self.driver.find_element(By.ID, "edit-dest").click()
    #     self.driver.find_element(By.ID, "edit-dest").clear()
    #     self.driver.find_element(By.ID, "edit-dest").send_keys("JFK")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[2]/div[1]/div[1]/ul[1]/div[2]/li[1]").click()
    #     self.driver.find_element(By.ID, "link_tp_when").click()
    #     self.driver.find_element(By.ID, "edit-leave-arr-a").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='datePickerId']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//td[@id='b168079836671712']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//select[@type='number']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@type='number']").select("11")
    #     self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[2]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[2]/select[1]").select("00")
    #     self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[3]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[3]/select[1]").select("AM")
    #     self.driver.find_element(By.ID, "edit-submit").click()
    #
    # def test_newmtainfo_24bbf21c(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Maps')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]/span[1]/span[1]").click()
    #
    # def test_newmtainfo_7f78da3a(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//div[@id='blockHeader']/label[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See all open MTA positions')]").click()
    #     self.driver.find_element(By.ID, "#ICSetFieldHRS_APP_SCHJOB.TREECTLEVENT.S11").click()
    #     self.driver.find_element(By.ID, "HRS_SCH_WRK_HRS_SORT_RSLTS_BY").clear()
    #     self.driver.find_element(By.ID, "HRS_SCH_WRK_HRS_SORT_RSLTS_BY").select("Department")
    #
    # def test_newmtainfo_1ec300ff(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//div[@id='blockHeader']/label[1]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Planned Service Changes')]").click()
    #     self.driver.find_element(By.ID, "edit-search").clear()
    #     self.driver.find_element(By.ID, "edit-search").send_keys("4")
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
    #     self.driver.find_element(By.ID, "datePickerId").click()
    #     self.driver.find_element(By.XPATH, "//td[@id='b1681312968701n']/span[1]").click()
    #     self.driver.find_element(By.ID, "b16813129770733").click()
    #
    # def test_newmtainfo_26a20a7b(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Fares & Tolls')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[2]/div[1]/div[1]/details[2]/summary[1]/div[1]/div[1]").click()
    #
    # def test_newmtainfo_351568c6(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.ID, "edit-origin").clear()
    #     self.driver.find_element(By.ID, "edit-origin").send_keys("Queensboro plaza")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[1]/div[1]/div[1]/ul[1]/div[1]/li[1]").click()
    #     self.driver.find_element(By.ID, "edit-dest").clear()
    #     self.driver.find_element(By.ID, "edit-dest").send_keys("Grand Central, NY")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[2]/div[1]/div[1]/ul[1]/div[1]/li[1]").click()
    #     self.driver.find_element(By.ID, "linkPreferencesModal").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-transport-mode']/div[2]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-transport-mode']/div[3]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-transport-mode']/div[4]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@role='button']").click()
    #     self.driver.find_element(By.ID, "edit-submit").click()
    #
    # def test_newmtainfo_3a85b415(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//div[@id='blockHeader']/label[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Accessibility')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Download a PDF short list of accessible stations.')]").click()
    #
    # def test_newmtainfo_3e9d6144(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.ID, "edit-origin").clear()
    #     self.driver.find_element(By.ID, "edit-origin").send_keys("Greenport")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[1]/div[1]/div[1]/ul[1]/div[2]/li[1]").click()
    #     self.driver.find_element(By.ID, "edit-dest").clear()
    #     self.driver.find_element(By.ID, "edit-dest").send_keys("Oyster Bay")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[2]/div[1]/div[1]/ul[1]/div[2]/li[1]").click()
    #     self.driver.find_element(By.ID, "linkPreferencesModal").click()
    #     self.driver.find_element(By.ID, "edit-start-service").clear()
    #     self.driver.find_element(By.ID, "edit-start-service").select("Train")
    #     self.driver.find_element(By.ID, "edit-end-service").clear()
    #     self.driver.find_element(By.ID, "edit-end-service").select("Bus")
    #     self.driver.find_element(By.XPATH, "//button[@role='button']").click()
    #     self.driver.find_element(By.ID, "edit-submit").click()
    #
    # def test_newmtainfo_50f1e384(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedules')]").click()
    #     self.driver.find_element(By.ID, "lirr-from").clear()
    #     self.driver.find_element(By.ID, "lirr-from").send_keys("Bay Shore")
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/div[1]/li[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "lirr-to").clear()
    #     self.driver.find_element(By.ID, "lirr-to").send_keys("Breakneck ridge")
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/div[1]/li[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='datePickerId-lirr']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//td[@id='b167910755173623']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//select[@type='number']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@type='number']").select("8")
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[3]/div[2]/div[1]/div[2]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[3]/div[2]/div[1]/div[2]/select[1]").select("37")
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[3]/div[2]/div[1]/div[3]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[3]/div[2]/div[1]/div[3]/select[1]").select("AM")
    #     self.driver.find_element(By.XPATH, "//button[@role='link' and @type='submit']").click()
    #
    # def test_newmtainfo_62c5067e(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.ID, "edit-origin").clear()
    #     self.driver.find_element(By.ID, "edit-origin").send_keys("52nd street, brooklyn")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[1]/div[1]/div[1]/ul[1]/div[2]/li[1]").click()
    #     self.driver.find_element(By.ID, "edit-dest").clear()
    #     self.driver.find_element(By.ID, "edit-dest").send_keys("74th street, brooklyn")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[2]/div[1]/div[1]/ul[1]/div[2]/li[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='default-form-container']/div[4]/label[1]").click()
    #     self.driver.find_element(By.ID, "edit-submit").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Fastest')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Fastest')]").click()
    #
    # def test_newmtainfo_e5c228ff(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Nearby Stations & Stops')]").click()
    #     self.driver.find_element(By.ID, "current-location").click()
    #     self.driver.find_element(By.ID, "current-location").clear()
    #     self.driver.find_element(By.ID, "current-location").send_keys("07055")
    #     self.driver.find_element(By.XPATH, "//li[contains(.,'Passaic, NJ 07055, USA')]").click()
    #
    # def test_newmtainfo_92ba0696(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.ID, "edit-origin").click()
    #     self.driver.find_element(By.ID, "edit-origin").clear()
    #     self.driver.find_element(By.ID, "edit-origin").send_keys("empire state building")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[1]/div[1]/div[1]/ul[1]/div[1]/li[1]").click()
    #     self.driver.find_element(By.ID, "edit-dest").click()
    #     self.driver.find_element(By.ID, "edit-dest").clear()
    #     self.driver.find_element(By.ID, "edit-dest").send_keys("little caribbean")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[2]/div[1]/div[1]/ul[1]/div[1]/li[1]").click()
    #     self.driver.find_element(By.ID, "linkPreferencesModal").click()
    #     self.driver.find_element(By.ID, "edit-minimize").clear()
    #     self.driver.find_element(By.ID, "edit-minimize").select("Walking")
    #     self.driver.find_element(By.XPATH, "//button[@role='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='default-form-container']/div[4]/label[1]").click()
    #     self.driver.find_element(By.ID, "edit-submit").click()
    #
    # def test_newmtainfo_00deddc4(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Special events')]").click()
    #     self.driver.find_element(By.XPATH, "//details[@id='location-filter']/summary[1]").click()
    #     self.driver.find_element(By.XPATH, "//details[@id='location-filter']/ul[1]/li[5]").click()
    #     self.driver.find_element(By.XPATH, "//details[@id='category-filter']/summary[1]").click()
    #     self.driver.find_element(By.XPATH, "//details[@id='category-filter']/ul[1]/li[4]").click()
    #     self.driver.find_element(By.XPATH, "//details[@id='timeframe-filter']/summary[1]").click()
    #     self.driver.find_element(By.XPATH, "//details[@id='timeframe-filter']/ul[1]/li[7]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    #
    # def test_newmtainfo_0cbdfafd(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//div[@id='blockHeader']/label[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='blockHeader']/section[1]/div[1]/ul[1]/li[9]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Bridges & Tunnels')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]").click()
    #
    # def test_newmtainfo_13a676be(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See all open MTA positions.')]").click()
    #     self.driver.find_element(By.ID, "search__location").clear()
    #     self.driver.find_element(By.ID, "search__location").send_keys("brooklyn")
    #     self.driver.find_element(By.XPATH, "//form[@id='search_form---']/fieldset[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//body[@id='search-jobs']/div[4]/div[4]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/span[2]").click()
    #
    # def test_newmtainfo_1a038b20(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Fares & Tolls')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'See railroad fare details.')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Plan a trip to see fares.')]").click()
    #     self.driver.find_element(By.ID, "lirr-from").clear()
    #     self.driver.find_element(By.ID, "lirr-from").send_keys("grand central")
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/div[1]/li[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, "lirr-to").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.ID, "lirr-to").clear()
    #     self.driver.find_element(By.ID, "lirr-to").send_keys("stoney brook")
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/div[1]/li[4]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//select[@type='number']").clear()
    #     self.driver.find_element(By.XPATH, "//select[@type='number']").select("10")
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[3]/div[2]/div[1]/div[2]/select[1]").clear()
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[1]/fieldset[1]/div[1]/div[3]/div[2]/div[1]/div[2]/select[1]").select("00")
    #     self.driver.find_element(By.XPATH, "//button[@role='link' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='datePickerId-lirr']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//td[@id='b168125707291912']/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@role='link' and @type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[2]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='lirr-results']/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='fares-tab']/a[1]").click()
    #
    # def test_newmtainfo_1a833106(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.ID, "edit-origin").clear()
    #     self.driver.find_element(By.ID, "edit-origin").send_keys("central park zoo")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[1]/div[1]/div[1]/ul[1]/div[1]/li[1]").click()
    #     self.driver.find_element(By.ID, "edit-dest").click()
    #     self.driver.find_element(By.ID, "edit-dest").clear()
    #     self.driver.find_element(By.ID, "edit-dest").send_keys("broadway")
    #     self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[2]/div[1]/div[1]/ul[1]/div[2]/li[4]").click()
    #     self.driver.find_element(By.ID, "linkPreferencesModal").click()
    #     self.driver.find_element(By.ID, "edit-minimize").clear()
    #     self.driver.find_element(By.ID, "edit-minimize").select("Walking")
    #     self.driver.find_element(By.XPATH, "//button[@role='button']").click()
    #     self.driver.find_element(By.ID, "edit-submit").click()
    #
    # def test_newmtainfo_ab989f1e(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Schedules')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='schedules-column']/div[1]/div[1]/h2[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Far Rockaway Branch')]").click()
    #
    # def test_newmtainfo_d7c3103a(self):
    #     # self.driver.get("https://new.mta.info")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Fares & Tolls')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[11]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[3]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/section[1]/div[4]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h3[1]").click()
    
    def test_newmtainfo_db203a3a(self):
        # self.driver.get("https://new.mta.info")
        self.driver.find_element(By.ID, "edit-origin").clear()
        self.driver.find_element(By.ID, "edit-origin").send_keys("brooklyn")

        # self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[1]/div[1]/div[1]/ul[1]/div[2]/li[1]").click()
        self.driver.find_element(By.XPATH, "//li[@aria-label='Brooklyn, NY, USA' and @class='ui-menu-item']").click()

        self.driver.find_element(By.ID, "edit-dest").clear()
        self.driver.find_element(By.ID, "edit-dest").send_keys("staten island")

        # self.driver.find_element(By.XPATH, "//div[@id='edit-address-container']/div[2]/div[1]/div[1]/ul[1]/div[2]/li[1]").click()
        self.driver.find_element(By.XPATH, "//li[@aria-label='Staten Island, NY, USA' and @class='ui-menu-item']").click()

        self.driver.find_element(By.XPATH, "//a[@id='link_tp_when']/span[2]").click()
        self.driver.find_element(By.ID, "datePickerId").click()

        # self.driver.find_element(By.XPATH, "//a[@id='datePickerId']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//td[@id='b167910489558825']/span[1]").click()
        leave_date, arrive_date = calculate_dates_weekday_mta_format(7, 8)
        if self.driver.find_element(By.XPATH, f"//td[@aria-label='{leave_date}']") is None:
            self.driver.find_element(By.XPATH, "//td[@aria-label='Next Month' and @title='Next Month']").click()
        self.driver.find_element(By.XPATH, f"//td[@aria-label='{leave_date}']").click()

        self.driver.find_element(By.XPATH, "//div[./label[@for='edit-leave-arr-a']]").click()

        # self.driver.find_element(By.XPATH, "//select[@type='number']").clear()
        # self.driver.find_element(By.XPATH, "//select[@type='number']").select("9")
        # self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[2]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[2]/select[1]").select("45")
        # self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[3]/select[1]").clear()
        # self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div[1]/div[3]/select[1]").select("AM")
        # self.driver.find_element(By.XPATH, "//a[@id='datePickerId']/span[1]").click()
        # self.driver.find_element(By.XPATH, "//td[@id='b167910497122625']/span[1]").click()
        # click to opening the calendar is not responding, possibly because the page was loading after click on Arrive by. So we need some sleep time
        time.sleep(2)
        self.driver.find_element(By.ID, "datePickerId").click()
        if self.driver.find_element(By.XPATH, f"//td[@aria-label='{arrive_date}']") is None:
            self.driver.find_element(By.XPATH, "//td[@aria-label='Next Month' and @title='Next Month']").click()
        self.driver.find_element(By.XPATH, f"//td[@aria-label='{arrive_date}']").click()
        hour_dropdown = self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div/div[1]/select")
        hour_select = Select(hour_dropdown)
        hour_select.select_by_visible_text("9")
        minute_dropdown = self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div/div[2]/select")
        minute_select = Select(minute_dropdown)
        minute_select.select_by_visible_text("45")
        am_pm_dropdown = self.driver.find_element(By.XPATH, "//div[@id='container_tp_when']/div[3]/div/div[3]/select")
        am_pm_select = Select(am_pm_dropdown)
        am_pm_select.select_by_visible_text("AM")

        self.driver.find_element(By.ID, "linkPreferencesModal").click()

        # self.driver.find_element(By.XPATH, "//div[@id='edit-transport-mode']/div[4]/label[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='edit-transport-mode']/div[3]/label[1]").click()
        # all travel ways are selected by default, just need to deselect Rail
        self.driver.find_element(By.XPATH, "//div[@id='edit-transport-mode']/div[4]/label[1]").click()

        self.driver.find_element(By.XPATH, "//button[@role='button']").click()
        self.driver.find_element(By.ID, "edit-submit").click()
    