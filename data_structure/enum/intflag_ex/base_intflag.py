'''
IntFlag 範例:
    - 

enum 範例
    - 總共定義4個枚舉類: enum, intenum, flag, intflag
    - 定義一個裝飾器: unique()
    - 定義一個輔助類: auto


Reference:
    - https://docs.python.org/zh-tw/3/library/enum.html
'''
from enum import IntFlag


class Box(IntFlag):
    L = 1
    B = 2
    H = 3
    W = 4
    LBHW = 10
    BH = 5
    

print(Box.L)

    
# 可以進行組合
print(Box.LBHW)
print(Box.BH)


# 如果沒有設置任何 flag，則為 0, boo=False.
print(Box.B & Box.L)

