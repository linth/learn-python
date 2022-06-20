'''
enum auto 範例
    - 如果確切的值不重要，你可以使用 auto


enum 範例
    - 總共定義4個枚舉類: enum, intenum, flag, intflag
    - 定義一個裝飾器: unique()
    - 定義一個輔助類: auto


Reference:
    - https://docs.python.org/zh-tw/3/library/enum.html
'''
from enum import Enum, auto


class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()


print(list(Color)) # [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
