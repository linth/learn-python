'''
Reduce 函式
    - 給列表list中所有元素使用相同操作

Reference:
    - https://juejin.cn/post/6988877471500206093
'''

from functools import reduce


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

reduce(lambda a, b : a+b, l) # 55

