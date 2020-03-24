"""
Reference:
    - https://www.geeksforgeeks.org/class-as-decorator-in-python/
"""
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Student:
    def __init__(self, show_logging_info):
        self.use_logging = show_logging_info

    def __call__(self, *args, **kwargs):
        res = self.use_logging(*args, **kwargs)
        print('The arg = {}, and the kwargs = {}'.format(args, kwargs))
        print('The class: Student')
        return res


@Student
def show_logging_info(*args, **kwargs): # function_name='show_logging_info', message='Hello', name=''
    logging.debug('This is show_logging_info function')
    # print('{}, function: {}'.format(message, function_name))
    print('args = {}, kwargs = {}'.format(args, kwargs))


if __name__ == '__main__':
    '''
        Result:
            DEBUG:root:This is show_logging_info function
            Good morning, function: Show Logging Information
            The class: Student
    '''
    show_logging_info(1, 'Show Logging Information', 'Good morning', name='george')

