"""
Reference:
    - https://dev.to/aldo/implementing-logging-in-python-via-decorators-1gje
"""
import logging
import functools


def _generate_log(path):
    """
    create logger object.
    :param path:
    :return:
    """
    logger = logging.getLogger('LogError')
    logger.setLevel(logging.ERROR)

    # create log file handler, log format and add the format to file handler.
    file_hander = logging.FileHandler(path)

    log_format = '%(levelname)s %(asctime)s %(message)s'
    formatter = logging.Formatter(log_format)
    file_hander.setFormatter(formatter)

    logger.addHandler(file_hander)
    return logger


def log_error(path='D:\\github_project\\learn-python\\decorator\\log\\log.error.log'):
    """
    create a parent function to take arguments.
    :param path:
    :return:
    """
    def error_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger = _generate_log(path)
                error_msg = 'Add error has occurred at /' + func.__name__ + '\n'
                logger.exception(error_msg)
                return e
        return wrapper
    return error_log


@log_error()
def divide(x, y):
    return x/y


if __name__ == '__main__':
    # res = divide(10, 0)
    # print(res)
    nums = [1, 2, 3, 5, 7]
    vis = [False] * len(nums)
    # print(vis)
    for num in nums:
        # print(num)
        print(vis)
