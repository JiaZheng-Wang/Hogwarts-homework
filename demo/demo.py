# @Time    : 2021/1/5 16:37
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import yaml


def demo():
    with open('demo.yaml') as f:
        data = yaml.safe_load(f)
        print(data)


demo()