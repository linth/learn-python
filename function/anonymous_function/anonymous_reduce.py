"""
Anonymous function. (匿名函數)
    - map
    - filter
    - reduce

lambda程式撰寫方式：
    - lambda arguments: expression

map程式撰寫方式：
    - map(function, iterable(s))
    - 抓取符合的元素。

filter程式撰寫方式：
    - filter(function, iterable(s))
    - 用來過濾序列，過濾掉不符合的元素。

reduce程式撰寫方式：
    - reduce(function, sequence[, initial])
    - 對序列中元素進行累加

Reference:
    - https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/
"""
from functools import reduce

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def add(x, y):
    return x + y

def show(x, y):
    print(x, y)

# ##################
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
# ##################
sum2 = reduce(lambda x, y : x+y, a)
sum3 = reduce(add, a)

print('sum2', sum2)
print('sum3', sum3)

sum4 = reduce(show, a)
print('sum4', sum4)

'''
1 2
None 3
None 4
None 5
None 6
None 7
None 8
None 9
sum4 None
'''