# @Time    : 2021/2/1 10:28
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
# from core import api
from copy import copy

import requests


# todo: 根据业务传入session，还未解决统一session
class HttpReq:
    def __init__(self, method='', params=''):
        # self.session = requests.Session()
        self.method = method
        self.params = params

    # 调用时传入url，并返回可调用函数hook
    def __call__(self, url):
        self.url = url
        if self.method == 'get' or self.method == 'post':
            return self.hook
        # 处理session
        else:
            pass

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value

    # 实际初始化被装饰函数
    def hook(self, func):
        # 被装饰函数调用
        def decorator(*args, **kwargs):
            # 函数的返回值->dict
            req_data = func(*args, **kwargs)
            # 处理param,获取base的self
            base = args[0]
            print("req_data:", req_data)
            # 根据方法名生成requests的方法
            session = getattr(base.session, self.method)
            # 调用requests
            r = session(url=self.url, **req_data)
            print(r.text)
            if r.json():
                return r.json()
            else:
                return r.text
        return decorator


class Http:
    post = ''
    get = ''
    add = ''

    # 设置方法名
    def __getattribute__(self, item):
        if item == 'post' or item == 'get':
            return HttpReq(method=item)
        else:
            return HttpReq(params=item)


#
# class Mark:
#     def __init__(self, http):
#         self.http = http
#
#     def __call__(self, func):
#

class Api:
    http = Http()
    # mark = Mark(http)


api = Api()


