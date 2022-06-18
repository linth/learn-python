'''
compare with union and typevar.
    - So, use a TypeVar if multiple types are allowed, but different usages of T within a single scope must match each other. 
    - Use a Union if multiple types are allowed, but different usages of U within a given scope don't need to match each other.

TODO: 需要再確認研讀+測試

Reference:
    - https://jerry-git.github.io/daily-dose-of-python/doses/1/
    - https://stackoverflow.com/questions/58903906/whats-the-difference-between-a-constrained-typevar-and-a-union
'''
from typing import Union, TypeVar

from numpy import var


U = Union[int, str]
T = TypeVar('T', int, str)


def max_1(var1: U, var2: U) -> U:
    print('var1', var1, 'type:', type(var1))
    print('var2', var2, 'type:', type(var2))
    # return max(var1, var2)
    return var1


def max_2(var1: T, var2: T) -> T:
    print('var1', var1, 'type:', type(var1))
    print('var2', var2, 'type:', type(var2))
    return var1


# print(max_1('foo', 1)) # foo
# print(max_1(1, 'foo'))
# print(max_1('foo', 'bar'))
# print(max_1(1, 2))

# print(max_2('foo', 1)) # foo
# print(max_2(1, 'foo'))
print(max_2('foo', 'bar'))
# print(max_2(1, 2))
