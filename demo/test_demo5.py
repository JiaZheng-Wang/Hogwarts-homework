# @Time    : 2020/11/27 17:26
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import pytest
import yaml

a = yaml.safe_load(open("data.yml"))
print(a)


class TestDemo:

    @pytest.mark.parametrize("key,value", [[1,2],[3,4]])
    def test_demo(self, key, value):
        print(key, "\n")
        print(value, "\n")
