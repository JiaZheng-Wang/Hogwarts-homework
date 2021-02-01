# @Time    : 2021/1/25 10:08
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

from mitmproxy import http
from mitmproxy import ctx
import json


class AddHeader():
    """
    http://httpbin.org/get  测试网站
    """

    def __init__(self):
        self.count = 0

    def request(self, flow: http.HTTPFlow):
        self.count += 1
        flow.request.headers["request_count"] = str(self.count)
        # ctx.log(str(flow.request.headers))

    def response(self, flow: http.HTTPFlow):
        self.count += 1
        flow.response.headers["request_count"] = str(self.count)
        # print(flow.request.pretty_url)
        # flow.response = http.HTTPResponse.make(
        #     200,
        #     b"baidu",
        #     {"content-type": "text/html"}
        # )
        resp = {
            "args": {},
            "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "max-age=0",
                "Host": "httpbin.org",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                "X-Amzn-Trace-Id": "Root=1-600e3093-3490e54c7821e57f7f2e919e"
            },
            "origin": "203.110.175.138",
            "url": "http://httpbin.org/get1231312312"
        }
        if "httpbin" in flow.request.pretty_url:
            flow.response = http.HTTPResponse.make(
                200,
                json.dumps(resp),
                {"content-type": "text/html"}

            )


addons = [
    AddHeader()
]
