'''
deep copy 範例
    - 修改資料時候，有哪些變化呢?
    - [應用情境] 需要複製東西，但是兩者之間不會互相干擾。

TODO: 可以思考一下使用場景
#! 如果有兩層數據資料就要考慮拷貝的深淺

Reference:
    - https://towardsdatascience.com/assignment-shallow-or-deep-a-story-about-pythons-memory-management-b8fad87bfa6c
    - https://www.youtube.com/watch?v=KnirnBi13CE
    - http://foobarnbaz.com/2012/07/08/understanding-python-variables/
    - https://blog.csdn.net/CHERISHGF/article/details/105196871
'''
from copy import copy, deepcopy

A = [1, 2, [10, 11], 3, [20, 21]]


# -------------------------------------------
# 重要觀念與範例 - deep copy
# -------------------------------------------
print('---------- deep copy -------------')
D = deepcopy(A)


print(id(A), A[3], id(A[3])) # 1475086589696 3 1475084446064
print(id(D), D[3], id(D[3])) # 1475086587136 3 1475084446064

# 原先相同記憶體位置後，被修改後會分配新的位址。
A[3] = 4
print(id(A), A[3], id(A[3])) # 1475086589696 4 1475084446096
print(id(D), D[3], id(D[3])) # 1475086587136 3 1475084446064

D[3] = 4
print(id(A), A[3], id(A[3])) # 1475086589696 4 1475084446096
print(id(D), D[3], id(D[3])) # 1475086587136 4 1475084446096

print('-------------------------------------------------------------------')

# A, C 記憶體位置不同，同時 list 內的 element 也是不同的。
print(id(A), A[2], id(A[2])) # 1475086589696 [10, 11] 1475086667008
print(id(D), D[2], id(D[2])) # 1475086587136 [10, 11] 1475086666176

A[2] = [12, 13]
print(id(A), A[2], id(A[2])) # 1475086589696 [12, 13] 1475086666944
print(id(D), D[2], id(D[2])) # 1475086587136 [10, 11] 1475086666176

D[2] = [12, 13]
print(id(A), A[2], id(A[2])) # 1475086589696 [12, 13] 1475086666944
print(id(D), D[2], id(D[2])) # 1475086587136 [12, 13] 1475086667008

