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
        # caps["dontStopAppOnReset"] = "true"
        caps["chromedriverExecutable"] = r"D:\Android\chromedriver83.0.4103.exe"
        caps["chromeOptions"] = {
            'androidProcess': 'com.tencent.mm:appbrand0'
        }
        # caps["adbPort"] = 5038
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_wx(self):
        size = self.driver.get_window_size()
        print(self.driver.contexts)
        sleep(30)
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.3, size['width'] * 0.5, size['height'] * 0.8)
        sleep(10)
        self.driver.find_element(By.XPATH, "//*[@text = '雪球']").click()
        sleep(10)
        print(self.driver.contexts)
        self.driver.find_element(MobileBy.XPATH, '//android.widget.Image').click()
        # self.driver.find_element(By.XPATH, '//wx-image/div').click()
        sleep(5)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="请输入股票名称/代码"]').send_keys("5555")
        # self.driver.find_element(By.XPATH,"//wx-input/div/div[1]").click()
        ActionChains(self.driver).send_keys("alibaba").perform()
        sleep(5)
