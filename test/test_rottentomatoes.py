import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestRottentomatoes:
    def test_rottentomatoes_d4d4a01e(self):
        # self.driver.get("https://rottentomatoes.com")

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Tv shows')]").click()

        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[1]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Sort: Most popular']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-radio-group[1]/select-label[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//select-label[@data-qa='option-newest']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[2]/span[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Genre' and @slot='label']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[1]/template[1]/div[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//select-label[@data-qa='option-action']").click()
        self.driver.find_element(By.XPATH, "//bottom-sheet-menu[@data-qa='discovery-filter-genres-options']//button[@data-qa='apply-btn']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[4]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[1]/select-checkbox[1]/template[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Audience score' and @slot='label']").click()
        self.driver.find_element(By.XPATH, "//select-label[@data-qa='option-upright']").click()
        self.driver.find_element(By.XPATH, "//bottom-sheet-menu[@data-qa='discovery-filter-audience-options']//button[@data-qa='apply-btn']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/filter-chip[5]/span[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/select-checkbox-group[1]/select-label[1]/select-checkbox[1]/template[1]/div[1]").click()
        # self.driver.find_element(By.XPATH, "//div[@id='main-page-content']/div[1]/div[2]/div[1]/bottom-sheet-menu[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//filter-chip[@data-qa='discovery-filter-critics']//span[text()='Tomatometer' and @slot='label']").click()
        self.driver.find_element(By.XPATH, "//select-label[@data-qa='option-fresh']").click()
        self.driver.find_element(By.XPATH, "//bottom-sheet-menu[@data-qa='discovery-filter-critics-options']//button[@data-qa='apply-btn']").click()
    