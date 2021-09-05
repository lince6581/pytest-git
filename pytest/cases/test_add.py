import json
import pytest
from jsonpath import jsonpath

from middleware.handle_middle import My_Handle


data = My_Handle.read_excel("cases.xlsx", "add").get_all_case()

@pytest.mark.parametrize("case_data", data)
def test_add(case_data):
    """
    管理员先登录系统，再获取借款人信息创建项目
    :param case_data:
    :return:
    """
    case_data = json.dumps(case_data)
    case_data = My_Handle.replace_data(case_data)
    case_data = json.loads(case_data)

    url = "".join([My_Handle.config["http_request"]["url"], case_data["url"]])
    method = case_data["method"]
    headers = json.loads(case_data["headers"])
    data = json.loads(case_data["data"])

    rqs = My_Handle.Request.request(url=url, method=method, headers=headers, json=data)

    if case_data['extractor']:
        extractors = json.loads(case_data['extractor'])
        for yz_prop, jsonpath_exp in extractors.items():
            value = jsonpath(rqs.json(), jsonpath_exp)[0]
            setattr(My_Handle, yz_prop, value)
            print(My_Handle.investor_user_token)

    # 断言
    expected = json.loads(case_data["expected"])
    try:
        for key in expected.keys():
            expected_data = expected[key]
            real_data = jsonpath(json.loads(rqs.text), key)[0]
            assert expected_data == real_data
        My_Handle.logger.info("测试执行成功")
    except:
        My_Handle.logger.error("测试执行失败")
        raise





if __name__ == '__main__':
    pytest.main(["--html=./report.html","test_add.py"])
