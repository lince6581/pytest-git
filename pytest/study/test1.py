import requests
import pytest


# 获取测试数据

# 请求接口
res = requests.request(method="post", url="url", header="header", json="data")

# 获取实际结果
real_data = res.text

# 获取预期结果
export_data = "预期结果"

# 断言
assert real_data == export_data

# 输出报告
if __name__ == '__main__':
    pytest.main(["--html=./report.html","test1.py"])