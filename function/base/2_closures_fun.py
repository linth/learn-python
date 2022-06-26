'''
Closure(閉包)
    - 寫法特殊請注意
    - 在 A 函式中再定義一個 B 函式。
    - B 函式使用了 A 函式中的變量。
    - A 函式返回 B 函式名。


閉包的使用時機
    - 閉包避免了全域變數的使用，並可將資料隱藏起來。
    - 當你有一些變數想要定義一個類別封裝起來時，若這個類別內只有一個方法時，使用閉包更為優雅


Reference:
    - https://medium.com/@zhoumax/python-%E9%96%89%E5%8C%85-closure-c98c24e52770
    - https://www.pythontutorial.net/advanced-python/python-closures/
'''
# 使用 class 方式
from tkinter import N


class Animal:
    def __init__(self, name):
        self.name = name
    

# 當使用 function 方式，就可以用閉包方式來處理
def animal(name):
    def inner():
        return name
    return inner


def say():
    
    # closure
    ##########################
    greeting = 'hello'
    
    def display():
        print(greeting)
    ##########################
        
    return display


# def compare(m, n):
#     return m if m > n else n


if __name__ == '__main__':
        
    # # assign function 物件給 fun
    # fun = compare
    
    # print(compare) # <function compare at 0x00000210C126F1F0>
    # print(fun) # <function compare at 0x00000210C126F1F0>
    # print(fun(1,2))
    # print(compare(1, 2))
    
    
    res = say()
    res() # hello
    
    # 使用 class 方式
    a1 = Animal('dog')
    a2 = Animal('cat')
    print(a1.name)
    print(a2.name)
    
    # 當使用 function 方式，就可以用閉包方式來處理
    a3 = animal('frog')
    print(a3())
    a4 = animal('lion')
    print(a4())
    