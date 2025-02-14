import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_helper import scroll_to_element


@pytest.mark.usefixtures("setup_class")
class TestImdb:
    def test_imdb_db53ba89(self):
        # self.driver.get("https://imdb.com")

        # self.driver.find_element(By.XPATH, "//svg[@id='iconContext-menu']/path[2]").click()
        self.driver.find_element(By.ID, "imdbHeader-navDrawerOpen").click()

        self.driver.find_element(By.XPATH, "//nav[@id='imdbHeader']/div[2]/aside[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/ul[1]/a[4]/span[1]").click()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Superhero')]").click()
        superhero_link = self.driver.find_element(By.XPATH, "//div[text()='Superhero']")
        scroll_to_element(self.driver, superhero_link)
        superhero_link.click()

        # add one extra step
        self.driver.find_element(By.XPATH, "//a[@data-testid='chip-see-all-movies']").click()

        # filter logic changed
        # self.driver.find_element(By.XPATH, "//input[@name='superhero-sci-fi' and @value='on' and @type='checkbox']").click()
        # self.driver.find_element(By.XPATH, "//input[@name='based-on-comic-book' and @value='on' and @type='checkbox']").click()
        # need to scroll to element first due to the display of advertisement and make the location of element changed
        keywords_div = self.driver.find_element(By.XPATH, "//div[text()='Keywords']")
        scroll_to_element(self.driver, keywords_div)
        keywords_div.click()

        self.driver.find_element(By.XPATH, "//button[text()='See more keywords']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='test-chip-id-superhero-sci-fi']").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='test-chip-id-based-on-comic-book']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Keywords']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/strong[1]").click()
        # self.driver.find_element(By.XPATH, "//div[text()='IMDb ratings']").click()
        imdb_ratings_div = self.driver.find_element(By.XPATH, "//div[text()='IMDb ratings']")
        scroll_to_element(self.driver, imdb_ratings_div)
        imdb_ratings_div.click()

        # self.driver.find_element(By.XPATH, "//select[@name='min' and @value='0.0']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='min' and @value='0.0']").select("7.0")
        # self.driver.find_element(By.XPATH, "//select[@name='max' and @value='10.0']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='max' and @value='10.0']").select("9.0")
        # max and min is inverse in the website
        self.driver.find_element(By.XPATH, "//input[@name='imdb-ratings-max-input']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='imdb-ratings-max-input']").send_keys("7.0")
        self.driver.find_element(By.XPATH, "//input[@name='imdb-ratings-min-input']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='imdb-ratings-min-input']").send_keys("9.0")
        self.driver.find_element(By.XPATH, "//div[text()='IMDb ratings']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='main']/div[1]/div[1]/div[1]/span[1]/strong[1]").click()
        # self.driver.find_element(By.XPATH, "//select[@name='sort']").clear()
        # self.driver.find_element(By.XPATH, "//select[@name='sort']").select("Number of Votes")
        popularity_dropdown = self.driver.find_element(By.ID, "adv-srch-sort-by")
        popularity_select = Select(popularity_dropdown)
        popularity_select.select_by_value('USER_RATING_COUNT')
        self.driver.find_element(By.ID, "adv-srch-sort-order").click()

        # self.driver.find_element(By.XPATH, "//span[@title='Compact view']").click()
        # self.driver.find_element(By.XPATH, "//div[@title='Click to add to watchlist']").click()
        # self.driver.find_element(By.XPATH, "//div[@title='Click to add to watchlist']").click()
        # self.driver.find_element(By.XPATH, "//div[@title='Click to add to watchlist']").click()
        # now only add one to watch list to avoid login
        self.driver.find_element(By.XPATH, "//div[@id='__next']/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[1]/div/div/div/div[1]/div[1]/div/div[1]").click()
