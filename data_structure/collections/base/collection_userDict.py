'''
UserDict in collection.
    - UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects.

Reference:
    - https://www.geeksforgeeks.org/python-collections-module/#ordereddict
'''
from collections import UserDict


class CustomDict(UserDict):   
    def __del__(self):
        raise RuntimeError('deleteion not allowed.')
    
    def pop(self, s=None):
        raise RuntimeError('deletion not allowed.')
    
    def popitem(self, s=None):
        return RuntimeError('deletion not allowed.')
    
    
d = CustomDict({'a':1, 'b': 2, 'c': 3})
print(d)
d.pop(1) # RuntimeError: deleteion not allowed.

