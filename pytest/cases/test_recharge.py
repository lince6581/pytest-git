import json
import pytest
import requests

from common.handle_excel import HandleExcel
from common.handle_log import logger
from common.handle_yaml import config, user_config

data = HandleExcel("cases.xlsx", "recharge").get_all_case()

@pytest.mark.parametrize("case_data", data)
def test_recharge(case_data, login_token, db_mysql):
    #获取充值前金额
    sql = "select leave_amount from member where mobile_phone={}".format(user_config["investor_user"]["mobile_phone"])
    money_before = db_mysql.query(sql)

    url = "".join([config["url"], case_data["url"]])
    method = case_data["method"]
    header = json.loads(case_data["headers"])
    Authorization = {"Authorization": "Bearer " + login_token}
    Authorization.update(header)
    json_data = json.loads(case_data["data"])

    rqs = requests.request(url=url,method=method,headers=Authorization,json=json_data)

    if json.loads(rqs.text)["code"] == 0:
        #获取充值后金额
        sql = "select leave_amount from member where mobile_phone={}".format(user_config["investor_user"]["mobile_phone"])
        money_after = db_mysql.query(sql)

        #断言
        except_data = json.loads(case_data["expected"])["code"]
        real_data = json.loads(rqs.text)["code"]
        try:
            assert except_data == real_data
            assert money_before == money_after
            logger.info("测试执行成功")
        except:
            logger.error("测试执行失败")
            raise





if __name__ == '__main__':
    pytest.main(["--html=./report.html","test_recharge.py"])
