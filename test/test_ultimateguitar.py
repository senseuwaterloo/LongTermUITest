import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestUltimateGuitar:
    
    # def test_ultimateguitar_640e0425(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='' and @type='text' and @placeholder='Enter artist name or song title']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='' and @type='text' and @placeholder='Enter artist name or song title']").send_keys("Rock And Roll Over")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/button[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='reviews']/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'KISS: Rock And Roll Over')]").click()
    #
    # def test_ultimateguitar_2667b421(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='' and @type='text' and @placeholder='Enter artist name or song title']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='' and @type='text' and @placeholder='Enter artist name or song title']").send_keys("kiss")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Relevance')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Kiss Album')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='2079756']/section[1]/section[1]/section[1]/button[1]/svg[1]/path[1]").click()
    #
    # def test_ultimateguitar_1f84888a(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='' and @type='text' and @placeholder='Enter artist name or song title']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='' and @type='text' and @placeholder='Enter artist name or song title']").send_keys("La Bomba")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Chords')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'High rated')]").click()
    #
    # def test_ultimateguitar_4c3b2a4f(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Forums')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Advanced search')]").click()
    #     self.driver.find_element(By.ID, "searchform-search_keyword").clear()
    #     self.driver.find_element(By.ID, "searchform-search_keyword").send_keys("Taylor Swift")
    #     self.driver.find_element(By.ID, "searchform-search_post_from").clear()
    #     self.driver.find_element(By.ID, "searchform-search_post_from").select("1 Months Ago")
    #     self.driver.find_element(By.XPATH, "//form[@id='w0']/footer[1]/button[1]").click()
    
    def test_ultimateguitar_61d28a34(self):
        # self.driver.get("https://www.ultimate-guitar.com/")
        # self.driver.find_element(By.XPATH, "//span[contains(.,'Tabs')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Tabs']").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Beginner')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Beginner']").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Drop C')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Drop C']").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'Rock')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Rock']").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Tab')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Tab']").click()

        # self.driver.find_element(By.XPATH, "//div[contains(.,\"Today's most popular\")]").click()
        self.driver.find_element(By.XPATH, "//div[text()=\"Today's most popular\"]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Most popular of all time')]").click()
        self.driver.find_element(By.XPATH, "//a[text()='Most popular of all time']").click()
        time.sleep(1)

    # def test_ultimateguitar_759a1b1b(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Shots')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'New')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'mauritzwilshusen')]").click()
    #
    # def test_ultimateguitar_928ec908(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Tabs')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Beginner')]").click()
    #
    # def test_ultimateguitar_9326b908(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Tabs')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Non-acoustic')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Intro')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Guitar Pro')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,\"Today's most popular\")]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Recently added')]").click()
    #
    # def test_ultimateguitar_a8de57df(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='' and @type='text' and @placeholder='Enter artist name or song title']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='' and @type='text' and @placeholder='Enter artist name or song title']").send_keys("ukulele")
    #     self.driver.find_element(By.XPATH, "//b[contains(.,'ukulele')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tab')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'High rated')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Far Cry 3 - Ukulele Girl')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Add to Favorites')]").click()
    #
    # def test_ultimateguitar_b332a3c6(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Tabs')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Drop D')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'1990s')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,\"Today's most popular\")]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Rating')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Everlong')]").click()
    #
    # def test_ultimateguitar_d516b2f7(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='' and @type='text' and @placeholder='Enter artist name or song title']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='' and @type='text' and @placeholder='Enter artist name or song title']").send_keys("Ed Sheeran")
    #     self.driver.find_element(By.XPATH, "//b[contains(.,'ed sheeran')]").click()
    #
    # def test_ultimateguitar_da679cfe(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='smith' and @type='text' and @placeholder='Enter artist name or song title']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@name='value' and @value='smith' and @type='text' and @placeholder='Enter artist name or song title']").send_keys("smith")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Search')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Tabs')]").click()
    #     self.driver.find_element(By.XPATH, "//a[@id='band']/div[1]/div[1]/span[1]").click()
    #
    # def test_ultimateguitar_1943febc(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Tabs')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[2]/main[1]/div[2]/div[3]/section[1]/nav[1]/div[2]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Most popular of all time')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Absolute Beginner')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'You Belong With Me (ver 2)')]").click()
    #
    # def test_ultimateguitar_1a35becb(self):
    #     # self.driver.get("https://www.ultimate-guitar.com/")
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Tabs')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Tab')]").click()
    #     self.driver.find_element(By.XPATH, "/html/body[1]/div[1]/div[2]/main[1]/div[2]/div[3]/section[1]/nav[1]/div[2]/div[1]/div[1]/svg[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Most popular of all time')]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Stairway To Heaven')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Add to playlist')]").click()
    