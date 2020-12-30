# @Time    : 2020/12/28 17:34
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestDemo:

    def test_demo(self):
        caps = {}
        caps["platformName"] = "Android"
        # caps["platformVersions"] = "6.0"
        caps["deviceName"] = "emulator-5554"
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["noReset"] = "true"
        # caps["dontStopAppOnReset"] = "true"
        # caps["skipDeviceInitialization"] = "true"
        caps["browserName"] = "Browser"
        caps["chromedriverExecutable"] = r"D:\Android\chromedriver.exe"
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        driver.implicitly_wait(5)
        driver.make_gsm_call("13300011111", GsmCallActions.CALL)
