"""
References:
    - https://realpython.com/primer-on-python-decorators/
    - https://foofish.net/python-decorator.html
"""
import time
import logging
import functools

# logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)


def timed(logger, level=None, format='%s: %s sec'):
    if level is None:
        level = logging.DEBUG

    def decorator(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            start = time.time()
            result = fn(*args, **kwargs)
            duration = time.time() - start
            logger.log(level, format, repr(fn), duration)
            return result
        return inner
    return decorator


def timed_without_arg(func):
    def decorator(*args):
        start_time = time.time()
        res = func(*args)
        end_time = time.time()
        print('The executing time = {}'.format(end_time - start_time))
        return res
    return decorator


def decorator_params(fruit):    # outer function
    def timed_with_arg(func):
        def decorator(*args):   # inner function
            print(args, fruit)
        return decorator
    return timed_with_arg


@timed_without_arg
def pow10(x):
    for i in range(x):
        print(i)


@decorator_params('banana')
def pow20(x):
    for i in range(x):
        print(i)


def main():
    pow10(1000) # DEBUG:root:<function pow10 at 0x000001D030F8A400>: 0.003988742828369141 sec
    pow20(2000) # The executing time = 0.0031440258026123047, (2000,) banana


if __name__ == '__main__':
    main()
