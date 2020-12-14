# @Time    : 2020/12/13 15:45
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

import pytest


@pytest.fixture(params=["123", "345"])
def my_fixture(request):
    print(f"参数是{request.param}")


class TestDemo:

    @pytest.mark.parametrize("a,b", [(1, 1), (2, 2)])
    def test_demo(self, my_fixture,a,b):
        assert a / b == 1
