import logging

class Loging:
    def __init__(self, name = 'root',
                 logger_level = 'DEBUG',
                 stream_handler_level = 'DEBUG',
                 file = None,
                 file_handler_level = 'INFO',
                 fmt_str = '%(asctime)s - [%(levelname)s] - [msg]:%(message)s - %(name)s - %(lineno)d'
                 ):
        #记录器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logger_level)

        # 格式化日志
        verbose_formatter = logging.Formatter(fmt_str)

        #处理器
        if file:
            logger_file = logging.FileHandler(filename=file, mode="a", encoding="utf-8")
            logger_file.setLevel(file_handler_level)

            logger_file.setFormatter(verbose_formatter)
            self.logger.addHandler(logger_file)

        logger_console = logging.StreamHandler()
        logger_console.setLevel(stream_handler_level)

        logger_console.setFormatter(verbose_formatter)
        self.logger.addHandler(logger_console)


    def get_log(self):
        return self.logger



if __name__ == '__main__':
    logger = Loging().get_log()
    logger.error("wenj")
    logger.info("cons")




