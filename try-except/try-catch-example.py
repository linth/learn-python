"""
References:
    - https://realpython.com/python-exceptions/
"""
import sys


def exception_ex1(x, y):
    """ use raise to throw an error when a certain condition occurs. """
    try:
        if x > y:
            raise Exception(f'x is larger than y, the number is negative.')
        elif x == y:
            raise ValueError(f'please re-type again, the two numbers are the same.')
        else:
            print(f'[Result]: {y} - {x} = {y-x}')
            return y - x
    except Exception as e:
        print('[Error]', e)


def is_larger_than_10(num):
    """ use assert to check the condition turn or false."""
    assert(num > 10)


def sub(a, b):
    return a - b


def is_negative(a, b):
    try:
        res = sub(a, b)
        if res < 0:
            raise Exception('The value is less than 0.')
        elif res == 0:
            print('The two number are equal.')
        else:
            print('The res of sub is {}'.format(res))
    except TypeError as e:
        print('TypeError: ', e)
        raise('TypeError error', e)
    except Exception as e:
        print('is_negative ', e)
        raise ('Exception error: ', e)


if __name__ == '__main__':
    exception_ex1(8, 8)
    is_larger_than_10(11)
    # is_negative(1, []) # error
