'''
lambda + map 範例

map程式撰寫方式：
    - map(function, iterable(s))
    - 抓取符合的元素。
    
Reference:
    - https://www.learncodewithmike.com/2019/12/python-lambda-functions.html
    - https://juejin.cn/post/6988877471500206093
'''

number = [50, 2, 12, 30, 27, 4]

res = map(lambda x : x*2, number)
print(list(res)) # [100, 4, 24, 60, 54, 8]


a = [1, 2, 3]
b = [4, 5, 6]

def add(a, b):
    return a+b

res2 = map(lambda a, b : a+b, a, b)
res3 = map(add, a, a)
print(list(res2)) # [5, 7, 9]
print(list(res3)) # [2, 4, 6]