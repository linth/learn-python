'''
泛型(Generic)
    - Mapping
    - Sequence
    - TypeVar

TODO: 確認三種 generic 有什麼作用?

Reference:
    - https://docs.python.org/zh-tw/3.6/library/typing.html
    - https://mypy.readthedocs.io/en/stable/generics.html#generic-functions
'''
from typing import Mapping, Sequence, TypeVar


T = TypeVar('T') # Declare type variable

def first(l: Sequence[T]) -> T:
    return l[0]


print(first([1, 2, 33, 4])) # 1
print(first(['george', 'may', 33, 4])) # george


