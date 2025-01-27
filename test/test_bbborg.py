import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestBbbOrg:
    
    # def test_bbborg_bdbc82a2(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/button[1]/span[4]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='content-wrapper']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h1[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'View All Chicago BBB Openings here')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='job_listings']/div[1]/h1[1]").click()
    #
    # def test_bbborg_c1344c8e(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").send_keys("construction services")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/div[1]/div[1]/div[1]/span[1]/b[1]/em[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").send_keys("hollywood")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-1-item-1']/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.ID, ":r1:").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id=':R4l52rl9a:']/svg[1]").click()
    #     self.driver.find_element(By.ID, "distance-10").click()
    #     self.driver.find_element(By.XPATH, "//button[@id=':R5l52rl9a:']/svg[1]").click()
    #     self.driver.find_element(By.ID, "10006-100").click()
    #     self.driver.find_element(By.ID, "10177-101").click()
    #     self.driver.find_element(By.XPATH, "//button[@id=':R5l52rl9a:']/svg[1]").click()
    
    def test_bbborg_c96d460a(self):
        # self.driver.get("https://bbb.org")
        self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div/div/div[2]/form/div/div[2]/div[2]/div/span[1]").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div/div/div[2]/form/div/div[2]/div[2]/ul/li[1]").click()

        self.driver.find_element(By.XPATH, "//main[@id='content']//input[@placeholder='businesses, category']").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']//input[@placeholder='businesses, category']").send_keys("SOLAR")
        time.sleep(2)
        self.driver.find_element(By.ID, "downshift-2-item-0").click()

        # self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div/div/div[2]/form/div/div[2]/button").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']//input[@name='find_loc']").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']//input[@name='find_loc']").send_keys("MIAMI")
        time.sleep(2)
        self.driver.find_element(By.ID, "downshift-3-item-0").click()

        self.driver.find_element(By.XPATH, "//main[@id='content']//button[@type='submit' and text()='Search']").click()
        # self.driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        self.driver.find_element(By.XPATH, "//main[@id='content']/div/div[3]/div/div[1]/div[1]/section/form/details[1]/summary").click()
        # self.driver.find_element(By.XPATH, "//main[@id='content']//input[@id='default']").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH, "//main[@id='content']//input[@id='default']").get_native_element())

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//main[@id='content']/div/div[3]/div/div[1]/div[1]/section/form/details[2]/summary").click()
        # self.driver.find_element(By.ID, "distance-10").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.ID, "distance-10").get_native_element())

        self.driver.find_element(By.XPATH, "//main[@id='content']/div/div[3]/div/div[1]/div[1]/section/form/details[4]/summary").click()
        # self.driver.find_element(By.ID, "C").click()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.ID, "C").get_native_element())

        self.driver.find_element(By.XPATH, "//main[@id='content']/div/div[3]/div/div[1]/div[2]/div[4]/div/div[2]/a").click()
    
    # def test_bbborg_cbc5bf23(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").send_keys("used car dealer")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/div[1]/div[1]/div[1]/span[1]/b[1]/em[1]").click()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").send_keys("new york")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-1-item-1']/div[1]/span[1]/span[1]/span[3]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.ID, ":R4l52rl9a:").click()
    #     self.driver.find_element(By.ID, "distance-5").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/span[2]/svg[1]/path[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@value='Rating']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[3]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/h3[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[1]/header[1]/div[1]/div[1]/div[2]/button[1]").click()
    #
    # def test_bbborg_2b3cafbb(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").send_keys("Mc Donald's")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Read Reviews')]").click()
    #
    # def test_bbborg_36566a2d(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").send_keys("auto repair")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/div[1]/div[1]/div[1]/span[1]/b[1]/em[1]").click()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").send_keys("10002")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-1-item-1']/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//button[@role='switch' and @name='toggle' and @value='on']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/span[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/h3[1]/a[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Read Reviews')]").click()
    #
    # def test_bbborg_54c7bf71(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='main-content']/div[1]/aside[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
    #
    # def test_bbborg_60e7234b(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").send_keys("charity")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/div[1]/div[1]/div[1]/span[1]/b[1]/em[1]").click()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").send_keys("12023")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-1-item-1']/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//button[@role='switch' and @name='toggle' and @value='']").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/span[2]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@value='Rating']").click()
    #
    # def test_bbborg_60e916ed(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").send_keys("hillsborp")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-1-item-1']/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-5']/span[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//button[@id=':R6l52rl9a:']/svg[1]").click()
    #     self.driver.find_element(By.ID, "A").click()
    #     self.driver.find_element(By.XPATH, "//button[@id=':R5l52rl9a:']/svg[1]").click()
    #     self.driver.find_element(By.ID, "10177-101").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/h3[1]").click()
    #
    # def test_bbborg_71266971(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Scam Tracker')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Lookup a Scam')]").click()
    #     self.driver.find_element(By.ID, "demo-simple-select").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-']/div[3]/ul[1]/li[2]").click()
    #     self.driver.find_element(By.ID, ":r4:").click()
    #     self.driver.find_element(By.ID, ":r4:").clear()
    #     self.driver.find_element(By.ID, ":r4:").send_keys("amazon")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[5]/div[3]/div[1]/button[1]/p[1]").click()
    #     self.driver.find_element(By.ID, "demo-simple-select").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-']/div[3]/ul[1]/li[6]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[5]/div[4]/div[1]/div[2]/p[1]").click()
    #
    # def test_bbborg_b47f2eb1(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'File a Complaint')]").click()
    #     self.driver.find_element(By.ID, ":R39qn9l96:").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Report a Scam')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='content-section']/div[3]/button[1]/p[1]").click()
    #
    # def test_bbborg_bb78d72e(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/button[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/a[1]").click()
    #     self.driver.find_element(By.ID, "demo-simple-select").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='menu-']/div[3]/ul[1]/li[5]").click()
    #     self.driver.find_element(By.ID, ":r2:").clear()
    #     self.driver.find_element(By.ID, ":r2:").send_keys("555555555")
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[2]/div[4]/div[3]/div[3]/div[1]/button[1]/p[1]").click()
    #
    # def test_bbborg_bb82ff0a(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[4]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").send_keys("Milwaukee")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-1-item-1']/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").click()
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-9']/span[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id=':R5l52rl9a:']/svg[1]").click()
    #     self.driver.find_element(By.ID, "50260-030").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/h3[1]").click()
    #
    # def test_bbborg_007bd640(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").send_keys("lawyer")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/div[1]/div[1]/div[1]/span[1]/b[1]/em[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").send_keys("new york")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-1-item-1']/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id=':R3l52rl9a:']/svg[1]").click()
    #     self.driver.find_element(By.ID, "742").click()
    #     self.driver.find_element(By.XPATH, "//button[@id=':R5l52rl9a:']/svg[1]").click()
    #     self.driver.find_element(By.ID, "60075-125").click()
    #     self.driver.find_element(By.XPATH, "//button[@id=':R6l52rl9a:']/svg[1]").click()
    #     self.driver.find_element(By.ID, "A").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Request Consultation')]").click()
    #
    # def test_bbborg_215efc73(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rjalal4qa:").send_keys("roofing contractors")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-0-item-0']/div[1]/div[1]/div[1]/span[1]/b[1]/em[1]").click()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").clear()
    #     self.driver.find_element(By.ID, ":Rlalal4qa:").send_keys("10002")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-1-item-1']/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     self.driver.find_element(By.ID, ":r1:").click()
    #     self.driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
    #     self.driver.find_element(By.XPATH, "//button[@id=':R4l52rl9a:']/svg[1]").click()
    #     self.driver.find_element(By.ID, "distance-5").click()
    #
    # def test_bbborg_2720083c(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Get Accredited')]").click()
    #     self.driver.find_element(By.ID, ":R56jl9a:").clear()
    #     self.driver.find_element(By.ID, ":R56jl9a:").send_keys("Vito")
    #     self.driver.find_element(By.ID, ":R76jl9a:").clear()
    #     self.driver.find_element(By.ID, ":R76jl9a:").send_keys("Carlone")
    #     self.driver.find_element(By.ID, ":R96jl9a:").clear()
    #     self.driver.find_element(By.ID, ":R96jl9a:").send_keys("vito.carlone@godfather.com")
    #     self.driver.find_element(By.ID, ":Rb6jl9a:").clear()
    #     self.driver.find_element(By.ID, ":Rb6jl9a:").send_keys("6571572589")
    #     self.driver.find_element(By.ID, ":Rd6jl9a:").clear()
    #     self.driver.find_element(By.ID, ":Rd6jl9a:").send_keys("Mafia Services")
    #     self.driver.find_element(By.ID, ":R2lf6jl9a:").click()
    #     self.driver.find_element(By.ID, ":Rh6jl9a:").clear()
    #     self.driver.find_element(By.ID, ":Rh6jl9a:").send_keys("60068")
    #     self.driver.find_element(By.XPATH, "//form[@id='accreditationInterestForm']/div[8]/button[1]").click()
    #
    # def test_bbborg_f42ec75e(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/button[1]/span[4]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Find Your Local BBB')]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.ID, ":R16laklaa:").clear()
    #     self.driver.find_element(By.ID, ":R16laklaa:").send_keys("Wisconsin")
    #     self.driver.find_element(By.XPATH, "//li[@id='downshift-2-item-1']/div[1]/span[1]/span[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//main[@id='content']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/a[1]").click()
    #
    # def test_bbborg_fa2fb067(self):
    #     # self.driver.get("https://bbb.org")
    #     self.driver.find_element(By.XPATH, "//button[@type='button']").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/a[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='content-section']/div[3]/button[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='__next']/div[5]/div[4]/div[1]/div[4]/p[1]").click()
    