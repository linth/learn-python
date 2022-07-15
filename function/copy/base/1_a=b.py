'''
copy 範例 (a = b)
    - [應用情境] 兩者之間完全相同、相依。

TODO: 可以思考一下使用場景

Reference:
    - https://towardsdatascience.com/assignment-shallow-or-deep-a-story-about-pythons-memory-management-b8fad87bfa6c
    - https://www.youtube.com/watch?v=KnirnBi13CE
    - http://foobarnbaz.com/2012/07/08/understanding-python-variables/
'''
from copy import copy, deepcopy


L1 = [1, 2, 3]
L2 = [1, 2, 3]

# L1, L2 記憶體位置不同
print(id(L1))
print(id(L2))

x = 10
y = 10

# x, y 記憶體位置相同
print(id(x))
print(id(y))


A = [1, 2, [10, 11], 3, [20, 21]]
B = A

# A, B 記憶體位置相同
print(id(A), A[3], id(A[3]))
print(id(B), B[3], id(B[3]))

# 修改資料後 (資料記憶體都相同)
A[3] = 5
print(id(A), A[3], id(A[3])) # 2245534992576 5 2245528611248
print(id(B), B[3], id(B[3])) # 2245534992576 5 2245528611248