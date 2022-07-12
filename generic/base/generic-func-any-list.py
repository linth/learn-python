'''
可以使用 typing 來使用 generic 限制/確認 引數的類型
    - 讓引數可以限制某些類型

Reference:
    - https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb
'''
from typing import Any, List


def first(container: List[Any]):
    return container[0]


if __name__ == '__main__':
    # list_one: List[int] = ['a', 'b', 'c']
    # print(first(list_one))


    list_two: List[int] = [1, 2, 3]
    print(first(list_two))
