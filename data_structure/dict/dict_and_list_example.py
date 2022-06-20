'''
dict + list 範例


Reference:
    - https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/?ref=gcse
'''

d = dict((val, range(int(val), int(val) + 2)) for val in ['1', '2', '3'])

print([dict(id=v) for v in range(4)]) # [{'a': 0}, {'a': 1}, {'a': 2}, {'a': 3}]


# d2 = dict(a=[1, 2, 3])
# print(d2)
