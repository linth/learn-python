'''
enum 比較範例
    - 不支援比較排序，enum 成員不屬於整數。

    

enum 範例
    - 總共定義4個枚舉類: enum, intenum, flag, intflag
    - 定義一個裝飾器: unique()
    - 定義一個輔助類: auto


Reference:
    - https://docs.python.org/zh-tw/3/library/enum.html
'''
from enum import Enum


class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    
    
print(Mistake.FOUR is Mistake.FOUR) # True
print(Mistake.FOUR is Mistake.ONE) # False
print(Mistake.FOUR is not Mistake.THREE) # True

print(Mistake.FOUR == Mistake.FOUR) # True
print(Mistake.FOUR == Mistake.ONE) # False
print(Mistake.FOUR != Mistake.THREE) # True

# 需要抓取 value，才可以比較大小。
print('result:', Mistake.ONE.value < 2)