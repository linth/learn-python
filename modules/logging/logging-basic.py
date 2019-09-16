'''
    Logging modules.

    Reference:
    - https://docs.python.org/zh-cn/3/howto/logging.html
    - https://www.youtube.com/watch?v=-ARI4Cz-awo&t=125s
'''
import logging

def add(x, y):
    logging.debug('The function: add is executing.')
    return x + y

def subtract(x, y):
    logging.debug('The function: subtract is executing.')
    return x - y

def multiply(x, y):
    logging.debug('The function: multiply is executing.')
    return x * y

def divide(x, y):
    logging.debug('The function: divide is executing.')
    return x / y

# example 1: print information based on your setting level.
def example1():
    logging.basicConfig(filename='example1.log', level=logging.DEBUG)

    logging.debug('the message shoild go to the log file.')
    logging.info('So should this')
    logging.warning('And this, too')


def example2():
    logging.basicConfig(filename='example1.log', level=logging.DEBUG)

    num1, num2 = 10, 5
    add_result = add(num1, num2)
    subtract_result = subtract(num1, num2)
    multiply_result = multiply(num1, num2)
    divide_result = divide(num1, num2)

if __name__ == '__main__':
    example1()
    example2()
