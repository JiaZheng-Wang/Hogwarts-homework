# @Time    : 2020/12/27 15:27
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["noReset"] = "true"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        caps['settings[waitForIdleTimeout]'] = 1  # 设置页面等待空闲状态的超时时间
        caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=caps)
        self.driver.implicitly_wait(10)

    def teardwon(self):
        pass

    def test_contact(self):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '姓名')]//following-sibling::*").send_keys("asd")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机')]/..//*[@text='手机号']").send_keys("11114444999")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
