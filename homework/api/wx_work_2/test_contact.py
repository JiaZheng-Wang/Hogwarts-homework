# @Time    : 2021/2/1 15:53
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import pytest

from homework.api.wx_work_2.base import Base


class TestContact:
    def setup(self):
        self.base = Base()

    @pytest.mark.run(step=1)
    def test_add(self):
        add_data = {
            "userid": "zs0002",
            "name": "zhangsan002",
            "department": [1],
            "mobile": "86 18500000003"
        }
        assert self.base.add_contact(add_data)

    @pytest.mark.run(step=2)
    def test_query(self):
        assert self.base.query_contact({"userid": "zs0003"})["errmsg"] == "ok"

    @pytest.mark.run(step=3)
    def test_delete(self):
        add_data = {
            "userid": "zs0001",
            "name": "zhangsan001",
            "department": [1],
            "mobile": "86 18500000002"
        }
        self.base.add_contact(add_data)
        assert self.base.delete_contact({"userid": "zs0001"})["errmsg"] == "deleted"

    def teardown(self):
        self.base.delete_contact({"userid": "zs0001"})
