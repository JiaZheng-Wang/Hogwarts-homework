from selenium.webdriver.common.by import By

from homework.MyTestFrame.base_page import BasePage
from homework.MyTestFrame.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.find_and_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        return Search(self.driver)