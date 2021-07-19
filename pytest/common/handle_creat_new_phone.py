import json
from faker import Faker

from common.handle_request import request
from common.handle_yaml import write_yaml
from config.handle_filepath import user_config_file_path
from common.handle_log import logger
from common.handle_DB import Mysql


def Creat_new_phone():
    #Faker随机生成手机号码，也可以配置成国外
    fk = Faker(locale='zh_CN')
    phone = fk.phone_number()
    sql = "select mobile_phone from member where mobile_phone=" + phone + ";"
    do_mysql = Mysql()
    phone_db = do_mysql.query(sql=sql)
    if not phone_db:
        return phone


def Creat_TZR():
    "创建投资人，并保存至配置文件"
    phone = Creat_new_phone()
    data = {"url": "/member/register", "method": "post", "headers": '{"X-Lemonban-Media-Type":"lemonban.v2"}',
                 "data": {"mobile_phone":phone,"pwd":"12345678"}}
    try:
        rqs = request(data, data["data"])
        if json.loads(rqs.text)["code"] == 0:
            tzr = {"investor_user":{"id": eval(rqs.text)["data"]["id"],"mobile_phone":phone, "pwd":"12345678"}}
            write_yaml(user_config_file_path, tzr)
    except:
        logger.error("注册失败")

def Creat_JKR():
    "创建借款人，并保存至配置文件"
    phone = Creat_new_phone()
    data = {"url": "/member/register", "method": "post", "headers": '{"X-Lemonban-Media-Type":"lemonban.v2"}',
                 "data": {"mobile_phone":phone,"pwd":"12345678"}}
    try:
        rqs = request(data, data["data"])
        if json.loads(rqs.text)["code"] == 0:
            jkr = {"borrower_user":{"id": eval(rqs.text)["data"]["id"],"mobile_phone":phone, "pwd":"12345678"}}
            write_yaml(user_config_file_path, jkr)
    except:
        logger.error("注册失败")

def Creat_SPR():
    "创建审批人，并保存至配置文件"
    phone = Creat_new_phone()
    data = {"url": "/member/register", "method": "post", "headers": '{"X-Lemonban-Media-Type":"lemonban.v2"}',
                 "data": {"mobile_phone":phone,"pwd":"12345678"}}
    try:
        rqs = request(data, data["data"])
        if json.loads(rqs.text)["code"] == 0:
            spr = {"approval_user":{"id": eval(rqs.text)["data"]["id"],"mobile_phone":phone, "pwd":"12345678"}}
            write_yaml(user_config_file_path, spr)
    except:
        logger.error("注册失败")


if __name__ == '__main__':
    # a = Creat_new_phone()
    # print(a)
    Creat_JKR()
    Creat_SPR()
    Creat_TZR()
