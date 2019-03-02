# basic concept
# set like dictionary
set = {"apple", "banana", "cherry"}
print(set)
print("banana" in set) # True

'''
    Once a set is created, you cannot change its items, but you can add new items.
'''
set.add("orange")
print(set)
print(len(set))

set.remove("banana") # If the item to remove does not exist, remove() will raise an error.
print(set) # {'cherry', 'apple', 'orange'}

set.discard("banana") # If the item to remove does not exist, discard() will NOT raise an error.
print(set) # {'cherry', 'apple', 'orange'}

set.pop() # remove the lastest one.
print(set)

set.clear() # empties the set
print(set)

del set # delete the set completely
print(set)

t3 = set(("apple", "banana", "cherry"))
print(t3)
