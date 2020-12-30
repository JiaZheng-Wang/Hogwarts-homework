# @Time    : 2020/12/29 11:56
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestWX:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersions"] = "6.0"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = ".ui.LauncherUI"
        caps["noReset"] = "true"
        # 输入中文时调用unicode键盘，使用完成后重置键盘,并禁用掉自带键盘
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "true"
        caps["dontStopAppOnReset"] = "true"
        caps["chromedriverExecutable"] = r"D:\Android\chromedriver83.0.4103.exe"
        caps["chromeOptions"] = {
            'androidProcess': 'com.tencent.mm:appbrand0'
        }
        # caps["adbPort"] = 5038
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_wx(self):
        size = self.driver.get_window_size()
        print(self.driver.contexts)
        sleep(5)
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.3, size['width'] * 0.5, size['height'] * 0.8)
        self.driver.find_element(By.XPATH, "//*[@text = '雪球']").click()
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        print("当前上下文：", self.driver.context)
        self.driver.find_element(By.XPATH, '//wx-image/div').click()
        sleep(5)
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        print("当前上下文：", self.driver.context)
        # self.driver.find_element(By.XPATH, '//*[@placeholder="请输入股票名称/代码"]').click()
        # self.driver.find_element(By.XPATH, '//wx-input[@placeholder="请输入股票名称/代码"]').click()
        print("Kaishi")
        # self.driver.hide_keyboard()
        try:
            self.driver.find_element(By.CSS_SELECTOR, '._input').click()
            print("jieshu")
            sleep(5)
        except Exception as e:
            print(e)
        self.driver.switch_to.context("NATIVE_APP")
        # 自带虚拟机不支持直接sendkeys，要用ActionChains来输入，而且要
        ActionChains(self.driver).send_keys("alibaba").perform()
        self.driver.switch_to.context(self.driver.contexts[-1])
        sleep(5)
