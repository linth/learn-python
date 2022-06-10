'''
遞增法
    - 一個一個動作，沒別的方式。

example:
    - 1~100
    - 2, 4, 6, 8, 10, ...
    - 3, 6, 9, ...

''' 

def incremental_method():
    sum = 0
    
    for i in range(1, 101):
        sum += i

    print(sum)

incremental_method()
