import json
import pytest
from jsonpath import jsonpath

from middleware.handle_middle import My_Handle


data = My_Handle.read_excel("cases.xlsx", "register").get_all_case()

@pytest.mark.parametrize("case_data", data)
@pytest.mark.run(order = 1)
def test_register(case_data):
    url = "".join([My_Handle.config["http_request"]["url"], case_data["url"]])
    method = case_data["method"]
    headers = eval(case_data["headers"])
    # if 'not_existed_tel' in case_data["data"]:
    #     My_Handle.Creat_new_phone()
    #     data = My_Handle.replace_data(case_data["data"])
    # else:
    #     data = My_Handle.replace_data(case_data["data"])
    data = json.loads(My_Handle.replace_data(case_data))
    rqs = My_Handle.Request.request(url=url, method=method, headers=headers, json=data)

    # 断言
    excepted = json.loads(case_data["expected"])
    try:
        for key in excepted.keys():
            excepted_data = excepted[key]
            real_data = jsonpath(json.loads(rqs.text), key)[0]
            assert excepted_data == real_data
            My_Handle.logger.info("测试执行成功")
    except:
        My_Handle.logger.error("测试执行失败")
        raise





if __name__ == '__main__':
    pytest.main(["--html=./report.html","test_regist.py"])
