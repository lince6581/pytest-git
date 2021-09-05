import json

from middleware.handle_middle import My_Handle
from common.handle_yaml import write_yaml


def Creat_TZR():
    "创建投资人，并保存至配置文件"
    phone = My_Handle.Creat_new_phone()
    data = {"url": "/member/register", "method": "post", "headers": '{"X-Lemonban-Media-Type":"lemonban.v2"}',
                 "data": {"mobile_phone":phone,"pwd":"12345678"}}
    try:
        rqs = My_Handle.request(data, data["data"])
        if json.loads(rqs.text)["code"] == 0:
            tzr = {"investor_user":{"id": eval(rqs.text)["data"]["id"],"mobile_phone":phone, "pwd":"12345678"}}
            write_yaml(My_Handle.user_path, tzr)
    except:
        My_Handle.logger.error("注册失败")

def Creat_JKR():
    "创建借款人，并保存至配置文件"
    phone = My_Handle.Creat_new_phone()
    data = {"url": "/member/register", "method": "post", "headers": '{"X-Lemonban-Media-Type":"lemonban.v2"}',
                 "data": {"mobile_phone":phone,"pwd":"12345678"}}
    try:
        rqs = My_Handle.request(data, data["data"])
        if json.loads(rqs.text)["code"] == 0:
            jkr = {"borrower_user":{"id": eval(rqs.text)["data"]["id"],"mobile_phone":phone, "pwd":"12345678"}}
            write_yaml(My_Handle.user_path, jkr)
    except:
        My_Handle.logger.error("注册失败")

def Creat_SPR():
    "创建审批人，并保存至配置文件"
    phone = My_Handle.Creat_new_phone()
    data = {"url": "/member/register", "method": "post", "headers": '{"X-Lemonban-Media-Type":"lemonban.v2"}',
                 "data": {"mobile_phone":phone,"pwd":"12345678"}}
    try:
        rqs = My_Handle.request(data, data["data"])
        if json.loads(rqs.text)["code"] == 0:
            spr = {"approval_user":{"id": eval(rqs.text)["data"]["id"],"mobile_phone":phone, "pwd":"12345678"}}
            write_yaml(My_Handle.user_path, spr)
    except:
        My_Handle.logger.error("注册失败")


if __name__ == '__main__':
    # a = Creat_new_phone()
    # print(a)
    Creat_JKR()
    Creat_SPR()
    Creat_TZR()
