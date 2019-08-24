'''
References:
    - https://realpython.com/primer-on-python-decorators/
    - https://foofish.net/python-decorator.html
'''
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

@timed(logger)
def pow10(x):
    for i in range(1000):
        print(i)


def main():
    pow10(100000) # DEBUG:root:<function pow10 at 0x000001D030F8A400>: 0.003988742828369141 sec

if __name__ == '__main__':
    main()
