'''
lambda + reduce 範例

reduce程式撰寫方式：
    - reduce(function, sequence[, initial])
    - 對序列中元素進行累加
    
Reference:
    - https://www.learncodewithmike.com/2019/12/python-lambda-functions.html
'''

from functools import reduce


number = [50, 2, 12, 30, 27, 4]

res = reduce(lambda x, y : x + y, number)
print(res) # 125
