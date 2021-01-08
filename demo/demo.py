# @Time    : 2021/1/5 16:37
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

def wrapper(func):
    def run(*args):
        print("==")
        func(*args)

    return run


@wrapper
def a():
    try:
        return 1 / 0
    except Exception as e:
        for i in range(2):
            a()
a()