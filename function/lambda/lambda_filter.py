'''
lambda + filter 範例

filter程式撰寫方式：
    - filter(function, iterable(s))
    - 用來過濾序列，過濾掉不符合的元素。
    
Reference:
    - https://www.learncodewithmike.com/2019/12/python-lambda-functions.html
'''

number = [50, 2, 12, 30, 27, 4]

res = filter(lambda x : x > 10, number)
print(list(res)) # [50, 12, 30, 27]

