'''
namedtuple in collection.


Reference:
    - https://www.geeksforgeeks.org/python-collections-module/#ordereddict
'''
from collections import namedtuple


Student = namedtuple('Student', ['name', 'age', 'DOB'])

s = Student('george', '33', '20011101')

print(s[1]) # 33
print(s.name) # george
