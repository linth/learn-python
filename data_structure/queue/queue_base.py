'''
基本的 Queue 使用


Reference:
    - https://www.youtube.com/watch?v=usyg5vbni34
'''
from queue import Queue


if __name__ == '__main__':
    # 基本的 Queue 使用 (先進先出)
    q = Queue()
    
    q.put(1)
    q.put(2)
    q.put(3)
    
    # 3 2 1 ---> [3, 2, 1]
    print(q.get())
    print(q.get())
    print(q.get())
    # print(q.get()) # 阻塞，沒資料可以拿，需等到給我一個值我才繼續走。
    
    # 基本 list 使用 (比較)
    l = []
    
    l.append(1)
    l.append(2)
    l.append(3)
    
    print(l)
    