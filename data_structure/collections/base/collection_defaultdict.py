'''
defaultdict in collection.
    - DefaultDict objects can be initialized using DefaultDict() method by passing the data type as an argument.

Reference:
    - https://www.geeksforgeeks.org/python-collections-module/

'''
from collections import defaultdict

# integer
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]

for i in L:
    d[i] += 1
    
print(d)


# list
d2 = defaultdict(list)

for i in range(5):
    d2[i].append(i)
    
print(d2)