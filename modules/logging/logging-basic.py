'''
    Logging modules.

    Reference:
    - https://docs.python.org/zh-cn/3/howto/logging.html
'''


import logging

# example 1: print information based on your setting level.
def example1():
    logging.basicConfig(filename='example1.log', level=logging.DEBUG)

    logging.debug('the message shoild go to the log file.')
    logging.info('So should this')
    logging.warning('And this, too')


if __name__ == '__main__':
    example1()
