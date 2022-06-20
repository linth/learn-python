'''
enum 跌代範例
    - 枚舉成員跌代不會給出別名
    - __member__: 可被用於對枚舉成員進行比較詳細的程序化訪問，如: 找出所有別名。
    

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
    

for name, member in Color.__members__.items():
    print(name, member)
    

res = [name for name, member in Color.__members__.items() if member.name == 'BLUE']
print(res)