# @Time    : 2021/2/1 10:11
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

import requests


def get_token():
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8ee6c3038cdf350f&corpsecret=nQbcr1syePgFKO3qpw1OeiahGlxbTGPAUgNTMdALg70')
    return r.json()['access_token']


token = get_token()


def test_add_contract():
    data = {
        "userid": "wangwu",
        "name": "00221",
        "mobile": "+86 13381999999",
        "department": "4",
    }
    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}', json=data)
    print(r.json())


def test_delete_contract():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=wangwu'
    r = requests.get(url=url)
    print(r.json())
