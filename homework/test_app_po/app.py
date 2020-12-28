# @Time    : 2020/12/27 17:06
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from appium import webdriver

from homework.test_app_po.base_page import BasePage


class App(BasePage):

    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.tencent.wework"
            caps["deviceName"] = "127.0.0.1:62001"
            caps["noReset"] = "true"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
            caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
            caps['settings[waitForIdleTimeout]'] = 1  # 设置页面等待空闲状态的超时时间
            # caps['dontStopAppOnReset'] = 'true'  # 启动之前不停止app

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()

        return self

    def goto_main(self):
        return True
