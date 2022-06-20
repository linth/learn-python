'''
UserList in collection.
    

Reference:
    - https://www.geeksforgeeks.org/python-collections-module/#ordereddict
'''
from collections import UserList 


class MyList(UserList):    
    def remove(self, s=None):
        raise RuntimeError('Deletion not allowed')
    
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed") 
    

L = MyList([1, 2, 3, 4])
L.append(5)
print(L) 

# Deleting From List
L.remove() # RuntimeError: Deletion not allowed