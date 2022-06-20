'''
intenum 範例:
    - 

enum 範例
    - 總共定義4個枚舉類: enum, intenum, flag, intflag
    - 定義一個裝飾器: unique()
    - 定義一個輔助類: auto


Reference:
    - https://docs.python.org/zh-tw/3/library/enum.html
'''
from enum import IntEnum


class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2


class Request(IntEnum):
    POST = 1
    GET = 2


print(Shape.CIRCLE) # Shape.CIRCLE
print(Shape.CIRCLE == 1) # True
print(Shape.CIRCLE == Request.POST) # True

