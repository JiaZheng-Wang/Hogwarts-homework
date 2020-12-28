# @Time    : 2020/12/25 11:27
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWx:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["deviceName"] = "127.0.0.1:62001"
        caps["noReset"] = "true"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        # caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        caps['settings[waitForIdleTimeout]'] = 1  # 设置页面等待空闲状态的超时时间
        # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardwon(self):
        pass
        # self.driver.quit()

    def test_wx(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()

        # 滚动查找
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()

        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'外出打卡')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()

        WebDriverWait(self.driver, 10).until(lambda x: "打卡成功" in x.page_source)
        print(self.driver.page_source)
        assert "打卡成功" in self.driver.page_source
        # //following-sibling::*