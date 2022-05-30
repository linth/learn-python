"""
iterable (可)
    - Lists, tuples, dictionaries, and sets are all iterable objects.
    - list, tuple, dict, set 都是 iterable 的 object。
    - 通常是一個容器
    - iterable實作__iter__方法回傳一個參考到此容器內部的iterator
    
iterator
    - an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
    - iterator 屬於實作iterator protocol 的 object，包含__iter__(), __next()__。
    - 迭代器
    - 

請釐清楚下面幾個的名詞和觀念：(詳細內容可以參考reference)
    - 容器 (container)
    - 迭代器物件 (iterator)：能用來產生迭代器的物件，回傳其包含的所有元素，但它不必是資料結構。
    - 產生器物件 (generator)
    - generator expression
    - list, set, dict comprehension

Reference:
    - https://medium.com/ai-academy-taiwan/python-%E7%9A%84%E5%8F%AF%E8%BF%AD%E4%BB%A3%E7%89%A9%E4%BB%B6-%E8%BF%AD%E4%BB%A3%E5%99%A8%E5%92%8C%E7%94%A2%E7%94%9F%E5%99%A8-236d19c4051e
"""
# list
student = ["george", "may", "peter", "JJ", "Haha"]

# tuple 
fruit = ("apple", "banana", "cherry")

# dict
s = {'name': 'george', 'age': 88, 'sex': 'boy', 'id': 'p0001'}

print(student, type(student))
print(fruit, type(fruit))

for i in s:
    print(i) # name, age, sex, id

x = iter(fruit)
y = iter(fruit) # x 是 tuple 型別的資料結構，但這並非必要條件。
print(f'x =', next(x)) 
print(f'x =', next(x))
print(f'y =', next(y))