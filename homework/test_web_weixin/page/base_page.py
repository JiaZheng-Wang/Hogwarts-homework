# @Time    : 2020/12/20 17:33
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, base_driver: WebDriver = None):

        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            self.__cookie_login()
        else:
            self.driver = base_driver

    def __cookie_login(self):
        # 使用cookie登录
        with open("../test_cases/data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for i in yaml_data:
                if "expiry" in i:
                    del i["expiry"]
                self.driver.add_cookie(i)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find(self, by, value=None):
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=value)

    def finds(self, by, value=None):
        if value is None:
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_elements(*by)
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=by, value=value)

    def wait_to_click(self, locator):
        if WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator)):
            self.find(locator).click()

    def wait_to_selected(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_selected(locator))
