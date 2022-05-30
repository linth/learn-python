"""
產生費氏數列的物件

因為 fib 物件具有 __iter__() 和 __next__() 方法，所以它本身既是可迭代物件也是迭代器物件。

Reference:
    - https://medium.com/ai-academy-taiwan/python-%E7%9A%84%E5%8F%AF%E8%BF%AD%E4%BB%A3%E7%89%A9%E4%BB%B6-%E8%BF%AD%E4%BB%A3%E5%99%A8%E5%92%8C%E7%94%A2%E7%94%9F%E5%99%A8-236d19c4051e
"""


from itertools import islice

class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value
    
def fib2(n):
    # Fibonacci sequence
    if n <= 2:
        return 1
    else:
        return fib2(n-2) + fib2(n-1)
    
if __name__ == '__main__':
    f = fib()
    fib_list = list(islice(f, 0, 10))
    print(fib_list) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    
    
    print(fib2(5))