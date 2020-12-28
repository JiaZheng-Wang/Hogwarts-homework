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
        caps["deviceName"] = "127.0.0.1:62001"
        caps["noReset"] = True
        caps["dontStopAppOnReset"] = "true"
        # caps["browserName"] = "Chrome"
        caps["browserName"] = "Browser"
        caps["chromedriverExecutable"] = r"D:\Android\chromedriver.exe"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        pass

    def test_app(self):
        print("==========")
        self.driver.get("https://m.baidu.com")
        self.driver.find_element_by_xpath("//*[@id='index-kw']").click()
        self.driver.find_element_by_xpath("//*[@id='index-kw']").send_keys("appium")
        sleep(5)
        print(self.driver.contexts)
