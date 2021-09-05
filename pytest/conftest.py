import pytest
import jsonpath

from middleware.handle_middle import My_Handle


@pytest.fixture(scope="session")
def logger_title():
    yield "-----------开始执行-----------"
    "-----------结束执行-----------"

#用户登录
@pytest.fixture(scope="session")
def login_token():
    url = "http://api.lemonban.com/futureloan/member/login"
    method = "post"
    headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    json = {"mobile_phone":My_Handle.user_config["investor_user"]["mobile_phone"],
                "pwd":My_Handle.user_config["investor_user"]["pwd"]}
    res = My_Handle.Request.request(url=url, method=method, headers=headers, json=json)
    token = jsonpath.jsonpath(eval(res.text), "$..token")
    yield token[0]

#管理员登录
@pytest.fixture(scope="session")
def admin_login_token():
    url = "http://api.lemonban.com/futureloan/member/login"
    method = "post"
    headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    json = {"mobile_phone":My_Handle.user_config["admin_user"]["mobile_phone"],
                "pwd":My_Handle.user_config["admin_user"]["pwd"]}
    res = My_Handle.Request.request(url=url, method=method, headers=headers, json=json)
    token = jsonpath.jsonpath(eval(res.text), "$..token")
    yield token[0]



@pytest.fixture(scope="session")
def db_mysql():
    db_cnn = My_Handle.db_class()
    yield db_cnn
    db_cnn.query_close()



if __name__ == '__main__':
    login_token()