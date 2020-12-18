# @Time    : 2020/12/18 11:00
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from selenium.webdriver.remote.webdriver import WebDriver


class PageBase(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)


