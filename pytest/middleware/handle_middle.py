from common.handle_log import Loging
from config.handle_filepath import config_file_path, user_config_file_path,log_file_path
from common.handle_yaml import get_yaml

class My_Handle:
    #读取配置文件
    config = get_yaml(config_file_path)
    user_config = get_yaml(user_config_file_path)

    #http接口请求

    #日志
    logger = Loging(name = config["logger"]["name"],
                    logger_level= config["logger"]["logger_level"],
                    stream_handler_level= config["logger"]["stream_handler_level"],
                    file= log_file_path,
                    file_handler_level= config["logger"]["file_handler_level"]
                    ).get_log()
