'''
Zip 函式
    - 將數據中不同列的數據提取出來，使用tuple包裝起來。

Reference:
    - https://juejin.cn/post/6988877471500206093
'''

user_name = ['george', 'peter', 'may']
user_id = [1, 2, 3]
user_age = [20, 21, 22]


print(list(zip(user_age, user_id, user_name))) # [(20, 1, 'george'), (21, 2, 'peter'), (22, 3, 'may')]

