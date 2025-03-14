# @Time    : 2020/12/27 17:06
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import logging
import time

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from homework.MyTestFrame.black_handle import black_wrapper


class BasePage:
    FIND = 'find'
    SEND = 'send'
    CONTENT = 'content'
    FIND_AND_CLICK = 'find_and_click'
    LOCATOR='location'
    ACTION='action'

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by=by, value=locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by=by, value=locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def find_by_swip(self, by, locator):
        self.driver.implicitly_wait(1)
        elements = self.driver.find_elements(by, locator)
        while len(elements) == 0:
            self.driver.swipe(0, 0, 0, 20)
            elements = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)

    @staticmethod
    def find_by_swip2(driver: WebDriver, by, locator) -> WebElement:
        driver.implicitly_wait(1)
        elements = driver.find_elements(by, locator)
        while len(elements) == 0:
            driver.swipe(0, 600, 0, 400)
            elements = driver.find_elements(by, locator)
        driver.implicitly_wait(5)
        return elements[0]

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result

    def load(self, path):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        for step in data:
            # element=self.find(step['location'])
            if step.get(self.ACTION) == self.FIND_AND_CLICK:
                self.find_and_click(by=MobileBy.XPATH, locator=step.get(self.LOCATOR))
            if step.get(self.ACTION) == self.FIND:
                self.find(step['location']).send_keys(step['content'])

    def screen_png(self):
        self.driver.save_screenshot("tmp.png")


    def record_screen(self):
        self.driver.start_recording_screen()
        time.sleep(5)
        self.driver.stop_recording_screen()