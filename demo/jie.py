# @Time    : 2020/12/20 16:17
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import os

tur = ("123", 45)
print(tur)
print(*tur)


def tmp(*args):
    print(*args)
    print(args)
    # print(a)
    # print(b)

def tmp1(a, b):

    print(a)
    print(b)


# tmp(*tur)
# tmp(tur)
# tmp(1, 2)
# tmp1(1, 2)


def tmp2(*args, **kwargs):
    print(args)
    print(*args)
    print(kwargs)


tmp2((1, 2), a=3, b=4)
