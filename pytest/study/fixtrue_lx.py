import pytest


# scop = function
# @pytest.fixture()
# def login():
#     print("登录成功")
#
# def test_regist():
#     print("注册账号，不需要登录")
#
# def test_recharge(login):
#     print("充值接口，需要先登录")

# scop = module
# @pytest.fixture(scope="module")
# def login():
#     print("系统登录成功")

def test_recharge_1(login_token, logger_title):
    print("充值成功")

def test_regist():
    print("注册成功")

def test_recharge_2(login_token):
    print("充值成功{}".format(login_token))

def test_db(db_mysql):
    db_mysql.query("sql")
    print(db_mysql)


if __name__ == '__main__':
    # pytest.main(["--html=./report.html","fixtrue_lx.py"])
    # pytest.main(["fixtrue_lx.py"])
    # db()
    test_regist()
    test_recharge_1()