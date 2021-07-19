import pytest
import jsonpath

from common.handle_request import request
from common.handle_yaml import get_yaml
from config.handle_filepath import user_config_file_path
from common.handle_DB import Mysql


@pytest.fixture(scope="session")
def logger_title():
    yield "-----------开始执行-----------"
    "-----------结束执行-----------"


@pytest.fixture(scope="session")
def login_token():
    request_parameter = {"url": "/member/login", "method": "post", "headers": '{"X-Lemonban-Media-Type":"lemonban.v2"}'}
    json_data ={"mobile_phone":get_yaml(user_config_file_path)["investor_user"]["mobile_phone"],
                "pwd":get_yaml(user_config_file_path)["investor_user"]["pwd"]}
    res = request(case_data = request_parameter, json_data= json_data)
    token = jsonpath.jsonpath(eval(res.text), "$..token")
    yield token[0]

@pytest.fixture(scope="session")
def db_mysql():
    db_cnn = Mysql()
    yield db_cnn
    db_cnn.query_close()



if __name__ == '__main__':
    login_token()