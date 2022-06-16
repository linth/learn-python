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

# 不使用 lambda function
def starts_with_A(s):
    return s[0] == "A"


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]


# ##################
# 抓取符合的元素
# ##################
find_a_fruit = map(starts_with_A, fruit) # return map object.
print(list(find_a_fruit))

# map(function, iterable(s))
find_a_fruit_with_lambda = map(lambda s : s[0] == 'A', fruit)
print(list(find_a_fruit_with_lambda))


def double_words(x: list):
    return x*2

print(list(map(double_words, fruit))) # ['AppleApple', 'BananaBanana', 'PearPear', 'ApricotApricot', 'OrangeOrange']

