'''


'''
import logging

class MyExampleClass:
  
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        log_file_handler = logging.FileHandler('my_log.log')
        log_file_handler.setLevel(logging.DEBUG)

        log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_file_handler.setFormatter(log_formatter)

        self.logger.addHandler(log_file_handler)

    def do_something(self):
        self.logger.debug('this is a debug information.')
        self.logger.info('this is a info information.')
        self.logger.warning('this is a warnning information.')
        self.logger.error('this is an error information.')


if __name__ == "__main__":
    my_instance = MyExampleClass()
    my_instance.do_something()
