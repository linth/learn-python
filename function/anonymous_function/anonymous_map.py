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

# 不使用 lambda function
def starts_with_A(s):
    return s[0] == "A"


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

find_a_fruit = map(starts_with_A, fruit) # return map object.
print(list(find_a_fruit))

# map(function, iterable(s))
find_a_fruit_with_lambda = map(lambda s : s[0] == 'A', fruit)
print(list(find_a_fruit_with_lambda))


def double_words(x: list):
    return x*2

print(list(map(double_words, fruit))) # ['AppleApple', 'BananaBanana', 'PearPear', 'ApricotApricot', 'OrangeOrange']

