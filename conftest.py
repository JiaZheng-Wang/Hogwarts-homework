import pytest

from pythoncode.calculator import Calculator


def pytest_collection_modifyitems(session, config, items):
    print(type(items))
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)

@pytest.fixture(scope="module")
def calc_fixture():

    calc = Calculator()
    print("开始计算")
    yield calc
    print("结束计算")
