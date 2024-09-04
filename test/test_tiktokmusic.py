import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestTiktokMusic:
    
    # def test_tiktokmusic_013781df(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Andorra')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[13]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[6]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Input artist name']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Input artist name']").send_keys("BCD Studio")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span[1]/button[1]/div[1]").click()
    #
    # def test_tiktokmusic_47932a9a(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[5]/a[1]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Product categories']").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Computers & Office Equipment')]").click()
    #     self.driver.find_element(By.XPATH, "//span[contains(.,'Desktop Computers, Laptops & Tablets')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Last 30 days')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/div[3]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/span[1]/div[1]").click()
    #
    # def test_tiktokmusic_532cab96(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/div[1]/ul[1]/a[2]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccModuleBannerWrap']/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Canada')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='soundPeriodSelect']/span[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Last 30 days')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/label[2]/span[2]/span[1]").click()
    #
    # def test_tiktokmusic_7a301589(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/a[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[3]/a[14]/div[1]/div[1]/div[1]/img[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/span[1]").click()
    #
    # def test_tiktokmusic_86f52e05(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[9]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span[1]/span[1]/span[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Artist Name')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Input artist name']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Input artist name']").send_keys("BCD Studio")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'Use in TikTok Video Editor')]").click()
    #
    # def test_tiktokmusic_88b53da2(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[3]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Belgium')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span[1]/span[1]/span[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Artist Name')]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Input artist name']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Input artist name']").send_keys("TimTaj")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span[1]/button[1]/div[1]").click()
    #
    # def test_tiktokmusic_92a31dcd(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[1]/div[1]/ul[1]/a[1]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Industry']").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Life Services')]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Exercise & Fitness')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='TopadsVideoItem0']/div[1]/div[3]/div[1]/div[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='bcModalWrapper']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/span[1]").click()
    #
    # def test_tiktokmusic_10b87002(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/div[1]/ul[1]/a[3]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='creatorIndutrySelect']/span[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'>10M')]").click()
    #
    # def test_tiktokmusic_1525b41a(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[1]/div[1]/ul[1]/a[2]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search by keyword']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @placeholder='Search by keyword']").send_keys("Games")
    #     self.driver.find_element(By.XPATH, "//div[@id='ScriptKeywordInput']/div[1]/span[1]/div[1]/span[1]/div[1]/span[2]").click()
    #
    # def test_tiktokmusic_188005ee(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/div[1]/ul[1]/a[3]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccModuleBannerWrap']/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Australia')]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='creatorFansRegionSelect']/span[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Brazil')]").click()
    #
    # def test_tiktokmusic_27ada901(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='TimTaj' and @type='text' and @placeholder='Input artist name']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='TimTaj' and @type='text' and @placeholder='Input artist name']").send_keys("zukisuzuki")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span[1]/button[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]").click()
    #     self.driver.find_element(By.XPATH, "//img[@title='play icon']").click()
    #
    # def test_tiktokmusic_30246bda(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/div[1]/ul[1]/a[2]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='soundPeriodSelect']/span[1]/div[1]/div[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Last 30 days')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[4]/div[4]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/label[2]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/span[1]").click()
    #
    # def test_tiktokmusic_35aae722(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[4]/label[1]/span[1]").click()
    #
    # def test_tiktokmusic_375bd12d(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/a[2]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/span[1]/span[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Brazil')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/span[2]/span[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'TikTok Series')]").click()
    #
    # def test_tiktokmusic_eaa378ef(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Australia')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
    #
    # def test_tiktokmusic_eb35b87a(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[1]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[1]/div[1]/ul[1]/a[4]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/span[1]/span[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Creative Effectiveness')]").click()
    #
    # def test_tiktokmusic_a1b36184(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[5]/a[1]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/div[3]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[13]/a[1]/div[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='productCategoryDetailContainer']/div[3]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
    #
    # def test_tiktokmusic_a4dedb12(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/div[1]/ul[1]/a[1]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//span[@id='hashtagPeriodSelect']/span[1]/div[1]/div[1]/div[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Last 30 days')]").click()
    #
    # def test_tiktokmusic_ad47b9a6(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[5]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[4]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[4]/label[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Input music name']").clear()
    #     self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Input music name']").send_keys("dance")
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span[1]/button[1]/div[1]").click()
    
    def test_tiktokmusic_b6f90850(self):
        # self.driver.get("https://music.tiktok.com/au/")
        # uiteststudy@gmail.com:Pass4Tiktok!
        # TODO: consider removing tiktok test cases since it is not available even with VPN on. Also, it needs verification code and captcha when logging in.
        self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/p[1]").click()
        self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[2]/div[1]/ul[1]/a[1]/p[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ccModuleBannerWrap']/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]/div[1]/span[2]/svg[1]").click()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Start typing or select from the list']").clear()
        self.driver.find_element(By.XPATH, "//input[@value='' and @type='text' and @placeholder='Start typing or select from the list']").send_keys("egypt")
        self.driver.find_element(By.XPATH, "//div[contains(.,'Egypt')]").click()
        self.driver.find_element(By.XPATH, "//span[@id='hashtagPeriodSelect']/span[1]/div[1]/div[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//div[contains(.,'Last 120 days')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]/span[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//div[@id='hashtagItemContainer']/a[1]/div[1]/span[1]/span[1]").click()
    
    # def test_tiktokmusic_c7bf7015(self):
    #     # self.driver.get("https://music.tiktok.com/au/")
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[4]/p[1]").click()
    #     self.driver.find_element(By.XPATH, "//header[@id='HeaderContainerId']/div[1]/ul[1]/li[4]/div[1]/ul[1]/a[1]/p[1]/span[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/span[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[contains(.,'Australia')]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/label[1]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[2]/label[1]/span[2]").click()
    #     self.driver.find_element(By.XPATH, "//div[@id='ccContentContainer']/div[3]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/label[1]").click()
    