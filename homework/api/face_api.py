# @Time    : 2021/1/28 16:26
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import time

import requests

header = {
    'Content-Type': 'application/json',
    'mode': 'simple'
}
json={
    "groupId":"0_00000001",
    "dataVer":"",
    "pageNum":1,
    "pageSize": 100
}


r = requests.post(url='https://58.144.147.148:20229/offline/person/all', json=json, headers=header, verify=False)
print(r.text)