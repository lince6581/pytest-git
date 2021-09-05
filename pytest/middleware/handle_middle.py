import os
import re
import json
from faker import Faker

from common.handle_log import Loging
from config.handle_filepath import log_file_path, config_path
from common.handle_yaml import get_yaml,write_yaml
from common.handle_request import Http_Request
from common.handle_DB import Mysql
from common.handle_excel import HandleExcel

class DBHandle(Mysql):
    def __init__(self):
        super().__init__(host= get_yaml(My_Handle.config_file)["db_mysql"]["host"],
                 user=get_yaml(My_Handle.config_file)["db_mysql"]["user"],
                 password=get_yaml(My_Handle.config_file)["db_mysql"]["password"],
                 port=get_yaml(My_Handle.config_file)["db_mysql"]["port"],
                 charset=get_yaml(My_Handle.config_file)["db_mysql"]["charset"],
                 database=get_yaml(My_Handle.config_file)["db_mysql"]["database"])



class My_Handle:
    """
    中间件
    """
    #配置文件
    config_file = os.path.join(config_path, "config.yaml")
    config = get_yaml(config_file)

    user_path = os.path.join(config_path, "user.yaml")
    user_config = get_yaml(user_path)

    #正则表达式待替换的数据
    new_phone = ''
    investor_phone = user_config['investor_user']['mobile_phone']
    investor_pwd = user_config['investor_user']['pwd']
    investor_user_token = ''
    investor_user_id = ''

    #日志
    logger = Loging(name = config["logger"]["name"],file= log_file_path).get_log()

    #http接口请求
    Request = Http_Request()

    #mysql数据库执行sql
    db_class = DBHandle

    #读取excel文件
    read_excel = HandleExcel

    #随机生成未注册手机号码
    @classmethod
    def Creat_new_phone(cls):
        # Faker随机生成手机号码，也可以配置成国外
        fk = Faker(locale='zh_CN')
        phone = fk.phone_number()
        sql = "select mobile_phone from member where mobile_phone=" + phone + ";"
        phone_db = My_Handle.db_class().query(sql=sql)
        if not phone_db:
            cls.new_phone = phone
            return phone

    #注册新用户，保存至配置文件
    @classmethod
    def Creat_user(cls, *arg):
        """
         "创建新用户，并保存至配置文件"
        :param arg: ([用户名，类型],[用户名，类型]),类型0：管理员，类型1：普通会员
        :return:
        """
        for name in arg:
            phone = cls.Creat_new_phone()
            try:
                rqs = cls.Request.request(url="http://api.lemonban.com/futureloan/member/register", method="post",
                                          headers={"X-Lemonban-Media-Type":"lemonban.v2"},
                                          json={"mobile_phone": phone, "pwd": "12345678", "type":name[1]})
                if json.loads(rqs.text)["code"] == 0:
                    user = {name[0]: {"id": eval(rqs.text)["data"]["id"], "mobile_phone": phone, "pwd": "12345678"}}
                    write_yaml(My_Handle.user_path, user)
            except:
                My_Handle.logger.error("注册失败")

    #待替换的数据

    #正则表达式
    @classmethod
    def replace_data(cls, string, pattern='#(.*?)#'):
        results = re.finditer(pattern=pattern, string=string)
        for result in results:
            old = result.group()
            key = result.group(1)
            new = str(getattr(cls, key, ''))
            string = string.replace(old, new)
        return string


if __name__ == '__main__':
    # a = My_Handle.replace_data('{"mobile_phone":"#investor_phone#","pwd":"#investor_pwd#"}')
    a = My_Handle.replace_data('{"case_id": 2, "title": "\u65b0\u589e\u9879\u76ee\uff0c\u501f\u6b3e1\u6708", "url": "/loan/add", "data": "{\"member_id\":#investor_user_id#, \"title\":\"\u65b0\u589e\u9879\u76ee\u6210\u529f\",\"amount\":\"6000\",\"loan_rate\":\"20.0\",\"loan_term\":\"1\",\"loan_date_type\":\"1\",\"bidding_days\":\"1\"}", "method": "post", "headers": "{\"X-Lemonban-Media-Type\":\"lemonban.v2\",\"Authorization\":#investor_user_token#}", "expected": "{\"$..code\":0,\"$..msg\":\"OK\"}", "extractor": null, "result": null}')
    # a = My_Handle.Creat_user(["admin", 0],["投资人", 1], ["借款人", 1])
    print(a)
    pass