import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_session")
class TestHealthline:
    def test_healthline_77979435(self):
        self.driver.get("https://healthline.com")
        self.driver.find_element(By.XPATH, "//div[@id='site-header']/div[1]/div[1]/div[3]/ul[1]/li[3]/button[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Weight Management')]").click()

        main_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > landing-view")
        main_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "div > div > div.bg-bottom > div > div > a").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(1) > label").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > button").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > div > div.button-container > a").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(6) > label").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(7) > label").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(1) > label").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > button").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > div > div.button-container > a.continue-button").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(1) > label").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > button").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > div > div.button-container > a.continue-button").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(2) > label").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > button").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > div > div.button-container > a.continue-button").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(1) > label").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > ul > li:nth-child(5) > label").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > button").click()

        quiz_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > quiz-view")
        quiz_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "#quiz-form > fieldset > div > div.button-container > a.continue-button").click()

        result_view_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "#nutrition-quiz > results-view")
        result_view_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, "section > section.content-wrapper > div > section > article:nth-child(1) > a.cta-button").click()
