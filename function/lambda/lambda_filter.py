'''
lambda + filter 範例

filter程式撰寫方式：
    - filter(function, iterable(s))
    - 用來過濾序列，過濾掉不符合的元素。
    
Reference:
    - https://www.learncodewithmike.com/2019/12/python-lambda-functions.html
    - https://juejin.cn/post/6988877471500206093
'''

number = [50, 2, 12, 30, 27, 4]

res = filter(lambda x : x > 10, number)
print(list(res)) # [50, 12, 30, 27]


number2 = [1, -2, -1, 2, 3, 4, -3]

def is_positive(num):
    return num > 0

res2 = filter(is_positive, number2)
print(list(res2))

