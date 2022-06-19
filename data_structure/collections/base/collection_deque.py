'''
deque in collection.
    - 可以當作進階版的 list
    - append, appendleft
    - pop, popleft

Reference:
    - https://www.geeksforgeeks.org/python-collections-module/#ordereddict
'''
from collections import deque


queue = deque(['name', 'age', 'id'])    
print(queue)


# inserting elements.
queue.append('sex')
print(queue)
queue.appendleft('school_name')
print(queue)


# remove elements.
queue.pop()
print(queue)
queue.popleft()
print(queue)
