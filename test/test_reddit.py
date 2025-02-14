import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestReddit:
    def test_reddit_f83262c3(self):
        # self.driver.get("https://reddit.com")
        # add code to handle shadow root
        reddit_search_large_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "body > shreddit-app > reddit-header-large > reddit-header-action-items > header > nav > div > div > div > search-dynamic-id-cache-controller > reddit-search-large")
        faceplate_search_input_shadow_root = reddit_search_large_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, '#search-input')
        search_input = faceplate_search_input_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, 'input[type="text"][name="q"][placeholder="Search Reddit"]')

        # self.driver.find_element(By.ID, "header-search-bar").clear()
        # self.driver.find_element(By.ID, "header-search-bar").send_keys("r/news")
        search_input.clear()
        search_input.send_keys("r/news")

        # self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/div[1]/a[1]/div[2]/div[1]").click()
        # retrieve shadow root again since the page is updated
        reddit_search_large_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "body > shreddit-app > reddit-header-large > reddit-header-action-items > header > nav > div > div > div > search-dynamic-id-cache-controller > reddit-search-large")
        first_item_in_dropdown = reddit_search_large_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, '#reddit-typeahead-results-partial-container > faceplate-tracker:nth-child(2) > faceplate-tracker > li > a')
        first_item_in_dropdown.click()

        # self.driver.find_element(By.ID, "header-search-bar").clear()
        # self.driver.find_element(By.ID, "header-search-bar").send_keys("football")
        # self.driver.find_element(By.XPATH, "//div[@id='SearchDropdownContent']/button[1]/span[1]").click()
        reddit_search_large_shadow_root = self.driver.find_element(By.CSS_SELECTOR, "body > shreddit-app > reddit-header-large > reddit-header-action-items > header > nav > div > div > div > search-dynamic-id-cache-controller > reddit-search-large")
        faceplate_search_input_shadow_root = reddit_search_large_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, '#search-input')
        news_search_input = faceplate_search_input_shadow_root.shadow_root.find_element(By.CSS_SELECTOR, 'input[type="text"][name="q"][placeholder="Search in r/news"]')
        news_search_input.clear()
        news_search_input.send_keys("football")
        news_search_input.send_keys(Keys.RETURN)

        # self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/button[1]").click()
        self.driver.find_element(By.ID, "search-results-page-tab-comments").click()

        # self.driver.find_element(By.XPATH, "//div[@id='AppRouter-main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Relevance']").click()

        # self.driver.find_element(By.XPATH, "//span[contains(.,'New')]").click()
        self.driver.find_element(By.XPATH, "//div[@slot='dropdown-items']//span[text()=' New ']").click()

        # self.driver.find_element(By.XPATH, "//div[@id='t3_12jvnb0']/div[1]/div[1]/div[2]/div[1]").click()
        self.driver.find_element(By.CSS_SELECTOR, "#main-content > div > reddit-feed > faceplate-tracker:nth-child(1) > div:nth-child(1)").click()

        # self.driver.find_element(By.XPATH, "//div[@id='vote-arrows-t1_jg0oupw']/button[1]/span[1]/i[1]").click()
        shreddit_post = self.driver.find_element(By.CSS_SELECTOR, "#main-content > shreddit-post")
        upvote_button = shreddit_post.shadow_root.find_element(By.CSS_SELECTOR, 'div > span > span > button[class*="text-action-upvote"]')
        upvote_button.click()
