import functools
import math
import time

'''
References:
    - https://realpython.com/primer-on-python-decorators/
'''


# The following @debug decorator will print the arguments a function is called with as well as its return value every time the function is called:
# python中每一個對象都會去implement __str__還有__repr__兩個方法，
# 這兩個方法都會回傳一個代表這個對象的字串，而如果調用了print function，
# 其輸出是__str__返回的字串，若是直接輸入變數，輸出則為__repr__返回的字串
#  reference: https://ithelp.ithome.com.tw/articles/10194593
def debug(func):
    # print the function signature and return value.
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug


def slow_down(func):
    ''' Sleep 1 second before calling the function.'''
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


@debug
def make_greeting(name, age=None):
    if age is None:
        return f'Howdy {name}!'
    else:
        return f'Whoa {name}! {age} already, you are growing up!'


@slow_down
def countdown(from_number):
    if from_number < 1:
        print('Liftoff !')
    else:
        print(from_number)
        countdown(from_number - 1)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)


if __name__ == '__main__':
    make_greeting('george', 35)

    make_greeting('Richard', age=112)

    make_greeting(name='Dorrisile', age=116)

    # approximate_e(5)

    countdown(3)
