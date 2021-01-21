# @Time    : 2020/11/29 21:53
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm


# 表达式
print("11+22={}".format(11 + 22))
# 指定顺序
print("{1}{1}{0}{0}".format("w", "z"))
# 列表解包，依次传递
list_a = [1, 2, 3]
print("{}{}{}".format(*list_a))
print("{2}{1}{0}".format(*list_a))
# 字典解包，依次传递
dict_a = {"name": "wjz", "age": 12}
print("my name is {name} and my age is {age}".format(**dict_a))
print("my name is {name} and my age is {age}".format(**dict_a))
# 3.6版本
a = "aaa"
print(f"{a}")
print(f"{dict_a}")
print(f"{dict_a['name']}")

print(f"{1 + 2}")
print(f"{a + a}")
