'''
unique 範例
    - 用來確保枚舉為唯一枚舉值
    - 不允許有相同名稱的屬性
    - 在enum class增加裝飾器 @unique 即可


enum 範例
    - 總共定義4個枚舉類: enum, intenum, flag, intflag
    - 定義一個裝飾器: unique()
    - 定義一個輔助類: auto


Reference:
    - https://docs.python.org/zh-tw/3/library/enum.html
'''
from enum import Enum, unique


@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 3
    

# 有重複，故會產生 ValueError
m = Mistake('THREE')    
print(m) # ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE


