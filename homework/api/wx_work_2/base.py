# @Time    : 2021/2/1 10:21
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import requests

from homework.api.wx_work_2.api import api


class Base:

    def __init__(self):
        self.session = requests.Session()
        token_data = {
            'corpid': 'ww8ee6c3038cdf350f',
            'corpsecret': 'nQbcr1syePgFKO3qpw1OeiahGlxbTGPAUgNTMdALg70'

        }
        self.session.params["access_token"] = self.get_token(token_data).get("access_token")
        print(self.session.params)

    # token
    @api.http.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken")
    def get_token(self, data):
        return dict(params=data, verify=False)

    # 查询
    @api.http.get(url="https://qyapi.weixin.qq.com/cgi-bin/user/get")
    def query_contact(self, data):
        return dict(params=data, verify=False)

    # 添加
    @api.http.post(url="https://qyapi.weixin.qq.com/cgi-bin/user/create")
    def add_contact(self, data):
        return dict(json=data, verify=False)

    # 删除
    @api.http.get(url="https://qyapi.weixin.qq.com/cgi-bin/user/delete")
    def delete_contact(self, data):
        return dict(params=data, verify=False)


if __name__ == '__main__':
    base = Base()
    add_data = {
        "userid": "zs0003",
        "name": "zhangsan003",
        "department": [1],
        "mobile": "86 18500000004"
    }
    base.add_contact(add_data)
    # base.query_contact({"userid": "zs0001"})
