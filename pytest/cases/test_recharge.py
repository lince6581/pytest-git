import json
import pytest
from decimal import Decimal

from middleware.handle_middle import My_Handle

data = My_Handle.read_excle("cases.xlsx", "recharge").get_all_case()

@pytest.mark.parametrize("case_data", data)
def test_recharge(case_data, login_token, db_mysql):
    #获取充值前金额
    sql = "select leave_amount from member where mobile_phone={}".format(My_Handle.user_config["investor_user"]["mobile_phone"])
    money_before = db_mysql.query(sql)["leave_amount"]

    url = "".join([My_Handle.config["http_request"]["url"], case_data["url"]])
    method = case_data["method"]
    header = json.loads(case_data["headers"])
    Authorization = {"Authorization": "Bearer " + login_token}
    Authorization.update(header)
    data = json.loads(case_data["data"])

    rqs = My_Handle.Request.request(url=url,method=method,headers=Authorization,json=data)

    #断言
    except_data = json.loads(case_data["expected"])["code"]
    real_data = json.loads(rqs.text)["code"]
    try:

        assert except_data == real_data
        if json.loads(rqs.text)["code"] == 0:
            # 获取充值后金额
            sql = "select leave_amount from member where mobile_phone={}".format(
                    My_Handle.user_config["investor_user"]["mobile_phone"])
            money_after = db_mysql.query(sql)["leave_amount"]
            assert money_before + Decimal(data["amount"]) == money_after
            My_Handle.logger.info("测试执行成功")
        My_Handle.logger.info("测试执行成功")
    except:
        My_Handle.logger.error("测试执行失败")
        raise





if __name__ == '__main__':
    pytest.main(["--html=./report.html","test_recharge.py"])
