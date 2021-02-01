# @Time    : 2020/12/1 15:06
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

import json

data = {
    "name": "wjz",
    "age": 15
}
data1 = '{  "name": "wjz",    "age": 15}'
print(type(data))
print(type(json.dumps(data)))
print(type(json.loads))
