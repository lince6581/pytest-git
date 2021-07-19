#登录接口
class dai:
    def register(self, username, pwd):
        if username == "test" and pwd == "123456":
            return "登录成功"
        return "登录失败"

dai = dai()