# @Time    : 2021/1/28 11:54
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import pytest

count = 0


@pytest.fixture(autouse=True)
def a_fixture():
    global count
    print(f"i am fixture-{count}")
    yield
    count += 1


class TestCache:

    @pytest.mark.run(order=0)
    def test_cache1(self, cache):
        cache.set("name", "wjzxz1333")

    @pytest.mark.run(order=1)
    def test_cache2(self, cache):
        print(cache.get("name", default=""))

    @pytest.mark.run(order=2)
    def test_cache3(self, cache):
        print(cache.get("name", default=""))