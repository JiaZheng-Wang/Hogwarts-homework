# @Time    : 2020/12/1 17:01
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import math
import time

print(time.localtime(time.time()))
print(time.strftime("%Y-%m-%d", time.localtime(time.time() - 60 * 60 * 24 * 2)))


print(math.floor(2.2))
print(math.ceil(3.3))
print(math.sqrt(16))