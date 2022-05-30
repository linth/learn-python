"""
Anonymous function. (匿名函數)
    - map
    - filter
    - reduce

lambda程式撰寫方式：
    - lambda arguments: expression

map程式撰寫方式：
    - map(function, iterable(s))

filter程式撰寫方式：
    - filter(function, iterable(s))

reduce程式撰寫方式：
    - reduce(function, sequence[, initial])

Reference:
    - https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/
"""
from functools import reduce

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def add(x, y):
    return x + y


sum2 = reduce(lambda x, y : x+y, a)
sum3 = reduce(add, a)

print('sum2', sum2)
print('sum3', sum3)