# @Time    : 2020/12/4 16:16
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

import requests

r =requests.get("http://www.baidu.com")
print(r.raw.read(10))