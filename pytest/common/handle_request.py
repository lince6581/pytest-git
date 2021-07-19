import requests
from middleware.handle_middle import My_Handle

class Http_Request:
    def __init__(self, url = My_Handle.config["http_request"]["url"],
                method = My_Handle.config["http_request"]["method"],
                 headers = My_Handle.config["http_request"]["headers"],
                 json = None):
        self.url = url
        self.method = method
        self.headers = headers
        self.json = json

    # def request(case_data, json_data):
    #     url = "".join([My_Handle.config["url"], case_data["url"]])
    #     method = case_data["method"]
    #     headers = eval(case_data["headers"])
    #
    #     rqs = requests.request(method=method, url=url,
    #                            headers=headers, json=json_data)
    #       return rqs

    def request(self):
        rqs = requests.request(url=self.url, method=self.method, headers=self.headers, json=self.json)
        return rqs



if __name__ == '__main__':
    rqs = Http_Request(url="/member/login", method="post", headers={"X-Lemonban-Media-Type":"lemonban.v2"},
                       json={"mobile_phone":"15703200672","pwd":"12345678"})
    a = rqs.request()
    # a = request(case_data={"url": "/member/register", "method": "post", "headers": '{"X-Lemonban-Media-Type":"lemonban.v2"}'},
    #             json_data={"mobile_phone":"${not_existed_tel}","pwd":"12345678"})
    print(a)
