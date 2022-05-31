"""
Generator object

產生器的種類，有兩種產生器：
    - 產生器函數 (generator function)：產生器函數就是前面用的例子，在函數裡使用 yield
    - 產生器表示式 (generator expression)


# TODO: 深入了解 yield and generator.
- iterable 定義是：能用來產生迭代器的物件，所以通常會實作 `__iter__()` 和 `__next__()` 這兩個方法，使得該物件同時是可迭代及迭代器。
- iterator 就是疊代器，即物件實作了 `__next__()`
- 產生器是一種特別的迭代器，讓你不用實作 `__iter__()` 和 `__next__()` 也能建立迭代器。


Reference:
    - https://medium.com/ai-academy-taiwan/python-%E7%9A%84%E5%8F%AF%E8%BF%AD%E4%BB%A3%E7%89%A9%E4%BB%B6-%E8%BF%AD%E4%BB%A3%E5%99%A8%E5%92%8C%E7%94%A2%E7%94%9F%E5%99%A8-236d19c4051e
"""

from itertools import islice
   
def fib():
    prev, curr = 0, 1
    while True:
        yield curr # 核心在 yield 這個關鍵字上。
        prev, curr = curr, prev + curr

def list_generator():
    # generator for list.
    numbers = [1, 2, 3, 4, 5, 6]
    return [x * x for x in numbers]

def set_generator():
    # generator for set.
    numbers = {1, 2, 3, 4, 5, 6}
    return {x * x for x in numbers}

def dict_generator():
    # generator for dict.
    numbers = [1, 2, 3, 4, 5, 6]
    return {x: str(x**2) for x in numbers}
        
if __name__ == '__main__':
    print(fib())
    res = fib()
    print(next(res))
    print(next(res))
    print(next(res))
    
    # generator for list.
    print('list generator:', list_generator())
    
    # generator for set.
    print('set generator:', set_generator())
    
    # generator for dict.
    print('dict generator:', dict_generator())
    
    #! 了解並熟悉 yield 