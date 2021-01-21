# @Time    : 2020/11/26 11:47
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm


# 元祖
a = (1, 2, 3)
print(a)
print(a.count(2))  # 元素出现的次数
print(a.index(3))  # 元素的index

# 集合
b = {1}
c = {1, 3}
print(b.union(c))  # 并集
print(b.intersection(c))  # 交集
print(b.difference(c))  # 差集 b有c没有
print(c.difference(b))  # 差集 c有b没有
print({i for i in "i am your father"})  # 集合推导式

# 字典
a = {"a": 1, "b": 2}  # 定义
b = dict(a=1, b=2)  # 定义
print(a, b)
print(a.popitem())  # 删除
m = {}
n = m.fromkeys([1, 2, 3], "a")  # 定义
print(n)
print({i: i for i in range(4)})  # 字典推导式




a=(1,2)
print(type(a))