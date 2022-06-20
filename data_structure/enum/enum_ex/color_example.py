'''
enum 範例
    - 總共定義4個枚舉類: enum, intenum, flag, intflag
    - 定義一個裝飾器: unique()
    - 定義一個輔助類: auto


Reference:
    - https://docs.python.org/zh-tw/3/library/enum.html
'''
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    

print(Color.BLUE) # Color.BLUE
print(Color.BLUE.__str__()) # Color.BLUE
print(repr(Color.BLUE)) # <Color.BLUE: 3>


for c in Color:
    print(f'c: {c}, name: {c.name}, value: {c.value}')
    

apple = {}
apple[Color.RED] = 'red apple'
apple[Color.GREEN] = 'green apple'
print(apple) # {<Color.RED: 1>: 'red apple', <Color.GREEN: 2>: 'green apple'}


