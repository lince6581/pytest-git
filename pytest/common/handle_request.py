import requests

class Http_Request:

    def request(self, url = '',method = '',headers = '',json = None):
        rqs = requests.request(url=url, method=method, headers=headers, json=json)
        return rqs



if __name__ == '__main__':
    Request = Http_Request()
    rqs = Request.request(url="http://api.lemonban.com/futureloan/member/login", method="post",
                           headers={"X-Lemonban-Media-Type":"lemonban.v2"},
                           json={"mobile_phone":"15703200672","pwd":"12345678"})
    print(rqs.text)
