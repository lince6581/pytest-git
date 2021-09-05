# import re
#
# import requests

# from common.handle_creat_new_phone import Creat_new_phone
# from common.handle_yaml import config_data
# from config.handle_filepath import yaml_file_path
# import yaml
# import json
# with open(yaml_file_path, encoding="utf-8") as f:
#     print(yaml.load(f))

# with open("comfig1.yaml", encoding="utf-8") as f:
#     data = yaml.safe_load()

# data = '{"code":2,"msg":"账号已存在","data":null,"copyright":"Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"}'
# dic = json.loads(data)
# str = json.dumps(dic)
# print(dic)
# print(type(dic))
# print(str)
# print(type(str))

# import re
#
# a = str({"mobile_phone":"${not_existed_tel}"})
# res = re.sub(r'\${not_existed_tel}', "123", a)
# print(res)

# a = {"a": 1, "b": 2, "c": 3}
# b = a.items()
# c = {}
# for i in b:
#     if i[0] == "a" or i[0] == "c":
#         c[i[0]] = i[1]
#
# print(c)

# from config.handle_filepath import user_config_file_path
# from common.handle_yaml import get_yaml
# import yaml

# user = {"register":{"mobile_phone": "13131313", "pwd": "a傻傻的aaaaa大大说"}}
# with open(user_config_file_path, mode="w") as f:
#     yaml.dump(user, f, encoding="utf-8", allow_unicode=True)


# data = get_yaml(user_config_file_path)
# print(data)


class A:
    a =1
    b =2
    def add(self):
        c = self.a + self.b
        return c

    @classmethod
    def add1(cls):
        c = cls.a + cls.b
        return c

    @staticmethod
    def add2():
        a = 2
        b = 2
        c = a + b
        return c

    @classmethod
    def add3(cls):
        return cls.add2()

    s = add2()
    print(s)


a = A()
