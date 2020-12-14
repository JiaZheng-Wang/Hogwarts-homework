# @Time    : 2020/12/10 16:43
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

import pytest
from pythoncode.calculator import Calculator
import yaml

test_data = yaml.safe_load(open("data.yaml"))
ids=test_data["ids"]

class TestCalc:
    # def setup_class(self):
    #     self.calc = Calculator()
    #     print("开始计算")
    #
    # def teardown_class(self):
    #     print("结束计算")

    @pytest.mark.parametrize("a,b,expect", test_data["add"], ids=ids)
    def test_add(self, calc_fixture, a, b, expect):
        assert expect == calc_fixture.add(a, b)

    @pytest.mark.parametrize("a,b,expect",  test_data["sub"], ids=ids)
    def test_sub(self, calc_fixture, a, b, expect):
        assert expect == calc_fixture.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", test_data["mul"], ids=ids)
    def test_mul(self, calc_fixture, a, b, expect):
        assert expect == calc_fixture.mul(a, b)

    @pytest.mark.parametrize("a,b,expect",  test_data["div"], ids=ids)
    def test_div(self, calc_fixture, a, b, expect):
        assert expect == calc_fixture.div(a, b)
