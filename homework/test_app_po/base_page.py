# @Time    : 2020/12/27 17:06
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from appium.webdriver.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
