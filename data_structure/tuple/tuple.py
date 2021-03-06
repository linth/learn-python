

'''
    You cannot add/remove item to a tuple.
'''
# tuple, like list.
t = ("apple", "banana", "cherry", "organe")
print(t)
print(type(t)) # tuple

print(t[0]) # apple
print(t[1]) # banana
print(t[3]) # organe
res = t.count('apple')
print(res) # 1

'''
    count(): Returns the number of times a specified value occurs in a tuple
'''
t2 = (1, 2, 1, 2, 1, 4, 6, 1, 5, 2)
res = t2.count(2)
print(res) # 3

'''
    index(): Searches the tuple for a specified value and returns the position of where it was found
'''
res = t.index('cherry')
print(res) # 2

# example 1:
languages = "python", "js", "go"
p = ["python", "js", "go"]
a = "psss"

print('languages have {}'.format(languages))
print(type(languages))
print(type(p))
print(type(a))
# tuple =
