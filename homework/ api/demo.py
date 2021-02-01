# @Time    : 2021/1/27 17:45
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import requests

r = requests.get("https://httpbin.ceshiren.com/get", params={"name": "wjz"},verify=False)
print(r.text)
print(r.status_code)
# print(r.json())

# rr = requests.post("https://httpbin.ceshiren.com/post",json={"name":"wjz"})
rr = requests.post("https://httpbin.ceshiren.com/post", data={"name": "wjz"},verify=False)
print(rr.text)
print(rr.status_code)
# print(rr.json())


rr2 = requests.post("https://httpbin.ceshiren.com/post", json={"name": "wjz", "age": 1}, verify=False,headers={"count": "12"},
                    cookies={})
# rr = requests.post("https://httpbin.ceshiren.com/post",data={"name":"wjz"})
print(rr2.text)
print(rr2.status_code)
print(rr2.json())
print("=======")

from jsonpath import jsonpath

print(jsonpath(rr2.json(), '$..Count'))

from hamcrest import assert_that, equal_to

assert_that("123", equal_to("123"))
