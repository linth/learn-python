'''
shallow copy 範例 (淺拷貝，即複製最外層的容器)
    - [應用情境] 需要複製東西，但是兩者之間節省記憶體空間會共用、共享。


TODO: 可以思考一下使用場景
#! 如果有兩層數據資料就要考慮拷貝的深淺

Reference:
    - https://towardsdatascience.com/assignment-shallow-or-deep-a-story-about-pythons-memory-management-b8fad87bfa6c
    - https://www.youtube.com/watch?v=KnirnBi13CE
    - http://foobarnbaz.com/2012/07/08/understanding-python-variables/
    - https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
    - https://blog.csdn.net/CHERISHGF/article/details/105196871
'''
from copy import copy, deepcopy

A = [1, 2, [10, 11], 3, [20, 21]]

# -------------------------------------------
# 重要觀念與範例 - shallow copy
# -------------------------------------------
print('---------- shallow copy -------------')
C = copy(A)

# A, C 記憶體位置不同，但是 list 內的 element 是相同的
print(id(A), A[3], id(A[3])) # 2468053327488 3 2468051183984
print(id(C), C[3], id(C[3])) # 2468053324992 3 2468051183984


# 但是修改資料後 (資料記憶體就會變動，變動的值會給予新的記憶體位址)
A[3] = 5
print(id(A), A[3], id(A[3])) # 2468053327488 5 2468051184048
print(id(C), C[3], id(C[3])) # 2468053324992 3 2468051183984

C[3] = 5
print(id(A), A[3], id(A[3])) # 2468053327488 5 2468051184048
print(id(C), C[3], id(C[3])) # 2468053324992 3 2468051183984

print('----------------------------------------------------')

print(id(A), A[2], id(A[2])) # 2468053327488 3 2468051183984
print(id(C), C[2], id(C[2])) # 2468053324992 3 2468051183984


A[2] = [22, 33]
print(id(A), A[2], id(A[2])) # 2468053327488 5 2468051184048
print(id(C), C[2], id(C[2])) # 2468053324992 3 2468051183984

C[2] = [22, 33]
print(id(A), A[2], id(A[2])) # 2468053327488 5 2468051184048
print(id(C), C[2], id(C[2])) # 2468053324992 3 2468051183984

