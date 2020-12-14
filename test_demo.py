# @Time    : 2020/12/9 20:40
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import pytest


class TestDemo:

    def setup_class(self):
        print("===setup_class")

    def teardown_class(self):
        print("===teardown_class")

    @pytest.mark.parametrize("a,b", [[1, 2], [3, 4], [5, 6]])
    def test_one(self, a, b):
        assert b - a == 1

    @pytest.mark.demo
    def test_demo1(self):
        assert 1 == 1

    @pytest.mark.demo
    def test_demo2(self):
        assert 2 == 2
