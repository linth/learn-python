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
    - https://www.runoob.com/python/python-func-filter.html
"""

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even(l):
    if l % 2 == 0:
        return True
    else:
        return False
    
def is_larger_then_five(l):
    if l > 5:
        return True
    else:
        return False

# ##################
# 過濾掉不符合的元素
# ##################
res = filter(is_even, a)
print(list(res)) # [2, 4, 6, 8]

res2 = filter(is_larger_then_five, a)
print(list(res2)) # [6, 7, 8, 9]

# ###################################
# 使用 lambda function + filter 方式
# ###################################
res3 = filter(lambda l : True if l % 2 == 0 else False, a)
print(list(res3)) # [2, 4, 6, 8]

res4 = filter(lambda l : True if l > 5 else False, a)
print(list(res4)) # [6, 7, 8, 9]