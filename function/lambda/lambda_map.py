'''
lambda + map 範例

map程式撰寫方式：
    - map(function, iterable(s))
    - 抓取符合的元素。
    
Reference:
    - https://www.learncodewithmike.com/2019/12/python-lambda-functions.html
'''

number = [50, 2, 12, 30, 27, 4]

res = map(lambda x : x*2, number)
print(list(res)) # [100, 4, 24, 60, 54, 8]
