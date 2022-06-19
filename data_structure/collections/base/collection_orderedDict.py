'''
OrderedDict in collection.
    - 測試看起來好像使用 dict or orderdict 都會按照新增順序去排序。
    
TODO: 需找適當例子來修改!

Reference:
    - https://www.geeksforgeeks.org/python-collections-module/
'''
from collections import OrderedDict


# use general dict
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for k, v in d.items():
    print(f'key: {k}, value: {v}')
    
d.pop('a')
print(d)
d['a'] = 1
print(d)


# use OrderedDict
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for k, v in od.items(): 
    print(f'key: {k}, value: {v}') 

od.pop('a') # deleting element
od['a'] = 1 # Re-inserting the same

for k, v in od.items(): 
    print(f'key: {k}, value: {v}')
