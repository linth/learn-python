"""
迭代器物件
    - 迭代器是具有狀態的幫助器物件 (helper)，對它使用 next() 會產出下一個值。當物件實作了 __next__() ，它就是迭代器，至於如何產出值則是另外一回事，不影響迭代器的定義。
    - itertools 提供許多能產生迭代器的工具函式
    
Reference:
    - https://medium.com/ai-academy-taiwan/python-%E7%9A%84%E5%8F%AF%E8%BF%AD%E4%BB%A3%E7%89%A9%E4%BB%B6-%E8%BF%AD%E4%BB%A3%E5%99%A8%E5%92%8C%E7%94%A2%E7%94%9F%E5%99%A8-236d19c4051e
"""

from itertools import count
from itertools import cycle # 從有限可迭代物件生成無窮迭代器
from itertools import islice # 從無窮迭代器產生有限迭代器

# 有限可迭代物件
counter = count(start=13)
print(next(counter))
print(next(counter))
print(next(counter))

# 從有限可迭代物件生成無窮迭代器
colors = cycle(['red', 'white', 'blue'])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))

# 從無窮迭代器產生有限迭代器
print(f'從無窮迭代器產生有限迭代器')
limited = islice(colors, 0, 4)
for x in limited:
    print(x)
    
# 建立一個能產生費氏數列的物件 (請參考 fib.py)