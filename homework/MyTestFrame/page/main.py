# @Time    : 2021/1/7 20:29
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import time

from selenium.webdriver.common.by import By

from homework.MyTestFrame.base_page import BasePage
from homework.MyTestFrame.page.market import Market


class Main(BasePage):
    def goto_market(self):
        time.sleep(5)
        # self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        # self.find_and_click(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
        self.load("..//page//main.yaml")
        return Market(self.driver)