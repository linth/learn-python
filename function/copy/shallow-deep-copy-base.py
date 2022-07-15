'''
(重要!!!) shallow copy & deep copy 範例


Reference:
    - https://towardsdatascience.com/assignment-shallow-or-deep-a-story-about-pythons-memory-management-b8fad87bfa6c
    - https://www.youtube.com/watch?v=KnirnBi13CE
    - http://foobarnbaz.com/2012/07/08/understanding-python-variables/
'''
from copy import copy, deepcopy

A = [1, 2, [10, 11], 3, [20, 21]]

# -------------------------------------------
# 重要觀念與範例 - shallow copy
# -------------------------------------------
print('---------- shallow copy -------------')
C = copy(A)

# A, C 記憶體位置不同，但是 list 內的 element 是相同的
print(id(A), id(A[3])) # 1792384674176 1792377317744
print(id(C), id(C[3])) # 1792384673856 1792377317744


# -------------------------------------------
# 重要觀念與範例 - deep copy
# -------------------------------------------
print('---------- deep copy -------------')
D = deepcopy(A)

# A, C 記憶體位置不同，同時 list 內的 element 也是不同的。
print(id(A), id(A[2])) # 1792212118016 1792212117632
print(id(D), id(D[2])) # 1792212118208 1792212117696


