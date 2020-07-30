"""
References:
    - https://realpython.com/python-exceptions/
"""
import sys


class SameValueError(Exception):
    def __init__(self, message: str):
        self.message = message


def exception_ex1(x: int, y: int) -> int:
    """
    use raise to throw an error when a certain condition occurs.
    :param x:
    :param y:
    :return:
    """
    try:
        if x > y:
            raise Exception(f'x is larger than y, the number is negative.')
        elif x == y:
            raise SameValueError(f'please re-type again, the two numbers are the same.')
        else:
            print(f'[Result]: {y} - {x} = {y-x}')
            return y - x
    except SameValueError as e:
        sv = SameValueError(e)
        print('[Error] SameValueError, ', e)
        print('error message: ', sv.message)
    except ValueError as e:
        print('[Error] ValueError, ', e)
    except Exception as e:
        print('[Error] Exception, ', e)


def is_larger_than_10(num: int):
    """
    use assert to check the condition turn or false.
    :param num:
    :return:
    """
    assert(num > 10)


def sub(a: int, b: int) -> int:
    """

    :param a:
    :param b:
    :return:
    """
    return a - b


def is_negative(a: int, b: int):
    """
    check the sub value between "a" and "b" is negative or not.
    :param a:
    :param b:
    :return:
    """
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
