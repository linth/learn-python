'''
ChainMap in collection.
    - chainMap就是封裝許多dictionaries 到一個簡單的 unit，並return 一個list的dictoraries。
    
    
Reference:
    - https://www.geeksforgeeks.org/python-collections-module/

'''
from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}


c = ChainMap(d1, d2, d3)
print(c)


# Accessing Keys and Values from ChainMap
print(c['a'])
print(c.values())
print(c.keys())

for i in c:
    print(i) # e f c d a b
    
for i in c.values():
    print(i) # 5 6  3 4 1 2
        
for i in c.keys():
    print(i) # e f c d a b
    