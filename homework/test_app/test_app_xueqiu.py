# @Time    : 2020/12/24 14:56
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from time import sleep

from appium import webdriver


class TestApp:

    def setup_class(self):
        """
        启动app
        :return:
        """
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersions"] = "6.0"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = "true"
        # caps["dontStopAppOnReset"] = "true"
        caps["skipDeviceInitialization"] = "true"
        # caps["browserName"] = "Browser"
        caps["chromedriverExecutable"] = r"D:\Android\chromedriver.exe"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def test_app(self):
        print("==========")
        print(self.driver.contexts)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='交易']").click()
        sleep(2)
        print(self.driver.contexts)
        self.driver.find_element_by_xpath("//*[@class='android.view.View' and @content-desc='免费领']").click()
        sleep(5)
        # self.driver

