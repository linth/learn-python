"""
References:
    - https://www.runoob.com/python/python-func-filter.html
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017323698112640
    - https://wiki.jikexueyuan.com/project/explore-python/Advanced-Features/iterator.html
"""
import math
from collections import Iterable


# Iterator 判斷一個object是不是可迭代的
def is_iterator(lst):
    return hasattr(lst, '__iter__')
    # hasattr(l{}, '__iter__')
    # hasattr(l'abc '__iter__')


def is_odd(n):
    return n % 2 == 1


def is_even(n):
    return n % 2 == 0


def get_odd_from_list(lst):
    # filter(function, iterable)
    res = filter(is_odd, lst)
    return list(res)


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


# 過濾出1-100中平方根是整數的數
def filter_sqr():
    res = filter(is_sqr, range(1, 101))
    return list(res)


if __name__ == '__main__':
    print(is_even(10))

    arr = [1, 2, 3, 2, 8, 9, 4, 5]
    res = get_odd_from_list(arr)
    print(res, type(res))

    print(is_iterator(123))
    print(isinstance('abc', Iterable))

    print(filter_sqr())
