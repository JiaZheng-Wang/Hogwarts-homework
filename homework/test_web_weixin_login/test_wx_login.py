# @Time    : 2020/12/18 10:40
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

import yaml
from selenium import webdriver

from homework.test_web_weixin_login.wx_page import PageWx


class TestWx:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        # 复用浏览器，获取cookie，存到本地
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = driver.get_cookies()
        with open("wx_cookies.yaml", "w") as f:
            yaml.dump(cookies, f)

    def teardown_class(self):
        pass

    def test_wx(self):

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("wx_cookies.yaml") as f:
            cookies = yaml.safe_load(f)
            for i in cookies:
                if "expiry" in i:
                    del i["expiry"]
                self.driver.add_cookie(i)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        page = PageWx(self.driver)
        # 断言王小二在列表里
        assert "王小二" in page.add_contacts()

