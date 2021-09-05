#处理路径
import os

#可以使用pathlib
#获取根目录路径
root_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#获取测试用例（data）路径
data_dir_path = os.path.join(root_dir_path, "data")
data_file_path = os.path.join(data_dir_path, "cases.xlsx")

#获取配置文件（yaml）路径
config_path = os.path.join(root_dir_path, "config")
config_path_user = os.path.join(config_path, "user.yaml")

#获取日志文件（log）路径
log_file_path = os.path.join(os.path.join(root_dir_path, "logs"), "log.log")

#获取测试报告文件路径
report_file_path = os.path.join(root_dir_path, "report.html")


if __name__ == '__main__':
    print(log_file_path)
