import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class TestStoreSteampowered:
    def test_storesteampowered_29f639c1(self):
        # self.driver.get("https://store.steampowered.com")
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'COMMUNITY')]").click()
        # hover on the element instead of clicking, just ignore this change
        community_element = self.driver.find_element(By.XPATH, "//a[contains(text(),'COMMUNITY')]").get_native_element()
        action = ActionChains(self.driver)
        action.move_to_element(community_element).perform()

        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Discussions')]").click()
        self.driver.find_element(By.XPATH, "//div[@id='global_header']//a[contains(text(),'Discussions')]").click()

        self.driver.find_element(By.XPATH, "//a[@id='tab_games']/span[1]").click()
        self.driver.find_element(By.ID, "associate_game").clear()
        self.driver.find_element(By.ID, "associate_game").send_keys("Dota 2")
        self.driver.find_element(By.XPATH, "//div[@id='game_select_suggestions']/div[1]").click()

        # clicked on the pinned item instead of the newest item
        # self.driver.find_element(By.XPATH, "//div[@id='forum_General_3703047_1696040635904700731']/a[1]").click()
        # somehow the forum_topic_overlay link element will intercept the forum_topic_name div element
        self.driver.find_element(By.XPATH, "//div[contains(@id, 'forum_General_') and contains(@id, '_topics')]/div[@class='forum_topic  unread' and ./preceding-sibling::div[1][@class='forum_topic  unread locked sticky']]/a[@class='forum_topic_overlay']").click()
