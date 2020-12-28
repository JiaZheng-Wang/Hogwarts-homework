# @Time    : 2020/12/27 17:16
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from homework.test_app_po.app import App


class TestCase:

    def test_case(self):
        App().start().goto_main()