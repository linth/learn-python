"""
iterable
    - iterable 定義是：能用來產生迭代器的物件，所以通常會實作 `__iter__()` 和 `__next__()` 這兩個方法，使得該物件同時是可迭代及迭代器。
    - iterator 就是疊代器，即物件實作了 `__next__()`
    - 產生器是一種特別的迭代器，讓你不用實作 `__iter__()` 和 `__next__()` 也能建立迭代器。


重要結論:
    - iterable中有__iter__方法，調用它會產生一個對應的iterator。
    - iterator中有__next__方法，調用它會返回對應iterable序列中的內容。
    - iterator中也有__iter__方法，調用它會返回自己，由於iterator有iterable中的__iter__方法，所以說iterator也是iterable的。


Reference:
    - https://www.notion.so/container-iterator-iterable-generator-0e2982e6c61f4f38811e0a305d0f6fe8
    - https://vivi.emmphysics.com/%E6%90%9E%E6%B8%85%E6%A5%9Apython%E4%B8%AD%E7%9A%84iterable%E3%80%81iterator%E5%92%8Cgenerator%EF%BC%88%E4%B8%80%EF%BC%89/
"""
if __name__ == '__main__':
    # container -> 屬於 iterable object.
    items = [1, 2, 3, 4]
    
    # 妳可以使用 __iter__(), __next__() 來進行疊代，但不代表 container 一定會是 iterator。
    # 換句話說，iterable是沒有 __next__() 的方法的。
    # print('->', next(items)) # 會有問題
    for i in items:
        print(i)
        
    print(dir(items))
    
    # 所以你需要讓 iterable object 可以返回序列內容，則需要使用 iterator 的 __next__
    item_iter = iter(items)
    print(next(item_iter))
    print(next(item_iter))
    print(next(item_iter))
    print(next(item_iter))
    
    