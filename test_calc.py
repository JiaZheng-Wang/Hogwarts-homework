# @Time    : 2020/12/10 16:43
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8), (-1, -2, -3), (100, 300, 400)
    ], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, -2), (-1, -2, 1), (100, 300, -200)
    ], ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 15), (-1, -2, 2), (100, 300, 30000)
    ], ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (6, 3, 2), (-1, -2, 0.5), (300, 300, 1)
    ], ids=["int", "minus", "bigint"])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)
