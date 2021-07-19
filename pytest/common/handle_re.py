import re
import json

from common.handle_creat_new_phone import Creat_new_phone


#替换未注册号码
def not_existed_tel(data):
    json_data = json.loads(re.sub(r'\${not_existed_tel}', Creat_new_phone(), data))
    return json_data

def tzr_tel(data):
    json_data = json.loads(re.sub(r'\${tzr_tel}', Creat_new_phone(), data))
    return json_data


if __name__ == '__main__':
    a = not_existed_tel('{"mobile_phone":"${not_existed_tel}","pwd":"12345678"}')
    print(a)