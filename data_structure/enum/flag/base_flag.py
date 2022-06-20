'''
Flag 範例:
    - 通常會使用 flag + auto 同時使用

enum 範例
    - 總共定義4個枚舉類: enum, intenum, flag, intflag
    - 定義一個裝飾器: unique()
    - 定義一個輔助類: auto


Reference:
    - https://docs.python.org/zh-tw/3/library/enum.html
'''
from enum import Flag, auto


class Color(Flag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    WHITE = RED | BLUE | GREEN
    


print(Color.RED & Color.GREEN) # Color.0

# 單一標誌的值會是 2^n (1, 2, 4, 8, ...)
print(Color.WHITE.value) # 7