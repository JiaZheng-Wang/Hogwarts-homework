# @Time    : 2021/1/4 10:07
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from mitmproxy import http


class AddHeader:

    def __init__(self):
        self.num = 0

    def response(self, flow: http.HTTPFlow):
        self.num += 1
        flow.response.headers["count"] = str(self.num)

    def request(self, flow: http.HTTPFlow):
        # if flow.request.pretty_url == "https://www.baidu.com":
        if 'baidu' in flow.request.pretty_url :
            flow.response = http.HTTPResponse.make(
                200,
                b"hello baidu",
                {'content-type': 'text/html'}
            )


addons = [
    AddHeader()
]
