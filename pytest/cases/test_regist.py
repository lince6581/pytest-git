import json
import pytest

from common.handle_excel import HandleExcel
from common.handle_log import logger
from common.handle_re import not_existed_tel
from common.handle_request import request


data = HandleExcel("cases.xlsx", "register").get_all_case()

@pytest.mark.parametrize("case_data", data)
def test_register(case_data):
    json_data = not_existed_tel(case_data["data"])

    rqs = request(case_data, json_data)

    #断言
    except_data = json.loads(case_data["expected"])["code"]
    real_data = json.loads(rqs.text)["code"]
    try:
        assert except_data == real_data
        logger.info("测试执行成功")
    except:
        logger.error("测试执行失败")
        raise





if __name__ == '__main__':
    tes = test_register()