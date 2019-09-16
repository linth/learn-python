'''
Reference:
-   https://foofish.net/python-decorator.html
'''
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

''' [Example 1] This is decorator without parameters. '''

def use_logging(func):

    def wrapper():
        logging.debug('{} is running'.format(func.__name__))
        return func()
    return wrapper

@use_logging
def foo():
    print('This is foo function.')


''' [Example 2] This is decorator with parameters. '''
def use_logging_with_args(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'warn':
                logging.warn('[Warning] {} is running'.format(func.__name__))
            elif level == 'info':
                logging.info('[Info] {} is running'.format(func.__name__))
            elif level == 'debug':
                logging.debug('[Debug] {} is running'.format(func.__name__))

            func()
            # return func(*args)
        return wrapper
    return decorator

@use_logging_with_args(level='debug')
def hoo(name='hoo'):
    print('This is hoo function, and the parameter is {}'.format(name))

if __name__ == '__main__':
    foo()
    hoo()
