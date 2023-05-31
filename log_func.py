class LogUtil():
    def __init__(self, logger):
        self.logger = logger
    def log_func_start(self, func_name):
        self.logger.info(f'==== {func_name} start ====')
    def log_func_end(self, func_name):
        self.logger.info(f'==== {func_name} end ====')
