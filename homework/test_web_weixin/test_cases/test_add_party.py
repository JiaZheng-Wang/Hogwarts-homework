# @Time    : 2020/12/20 18:37
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import pytest

from homework.test_web_weixin_2.page.main_page import MainPage


class TestAddParty:

    def setup_class(self):
        self.main = MainPage()

    @pytest.mark.parametrize("name", ["自动化测试部门", ])
    def test_add_party(self, name):
        res = self.main.to_contact().to_add_party().add_party(name)
        assert name in res
