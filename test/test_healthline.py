import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestHealthline:
    def test_healthline_77979435(self):
        # self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Weight Management')]").click()

        # nested in shadow dom. Seems that shadow root find element method only supports CSS selector
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'CONTINUE')]").click()
        main_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > landing-view")
        main_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "div > div > div.bg-bottom > div > div > a").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[1]/label[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(1) > label").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/button[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > button").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > div > div.button-container > a").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[6]/label[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(6) > label").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[7]/label[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(7) > label").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[1]/label[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(1) > label").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/button[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > button").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > div > div.button-container > a.continue-button").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[1]/label[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(1) > label").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/button[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > button").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > div > div.button-container > a.continue-button").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[2]/label[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(2) > label").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/button[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > button").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > div > div.button-container > a.continue-button").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[1]/label[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(1) > label").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/ul[1]/li[5]/label[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(5) > label").click()

        # self.driver.find_element(By.XPATH, "//form[@id='quiz-form']/fieldset[1]/button[1]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > button").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > div > div.button-container > a.continue-button").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Read More')]").click()
        result_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > results-view")
        result_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "section > section.content-wrapper > div > section > article:nth-child(1) > a.cta-button").click()
