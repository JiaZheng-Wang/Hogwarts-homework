# @Time    : 2021/1/4 10:07
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

class AddHeader:

    def __init__(self):
        self.num = 0

    def response(self, flow):
        self.num += 1
        flow.response.headers["count"]=str(self.num)


addons=[
    AddHeader()
]

