# @Time    : 2021/1/28 13:58
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import pytest


def pytest_addoption(parser):
    parser.addoption("--ip_type", action="store", default="loopback",
                     help="ip type includes loopback, domain and local_network")


def pytest_generate_tests(metafunc):
    if 'test_data' in metafunc.fixturenames:
        ip_type = metafunc.config.getoption("ip_type")
        if ip_type == "loopback":
            metafunc.parametrize("test_data", ["127.0.0.1"])
        elif ip_type == "local":
            metafunc.parametrize("test_data", ["192.168.1.1", "192.168.1.2"])


# request是已经实现的fixture，注意与metafunc的区别（用于钩子函数）
@pytest.fixture()
def demo_request(request):
    print("\n=======================request start=================================")
    print(request.module)
    print(request.function)
    print(request.cls)
    print(request.fspath)
    print(request.fixturenames)
    print(request.fixturename)
    print(request.scope)
    print("\n=======================request end=================================")


