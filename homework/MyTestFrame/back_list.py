# @Time    : 2021/1/8 10:50
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy


class BlackList:

    def __init__(self):
        self.black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    # def __call__(self, *args, **kwargs):
    #     pass

