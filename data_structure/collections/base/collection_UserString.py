'''
UserString in collection.
    

Reference:
    - https://www.geeksforgeeks.org/python-collections-module/#ordereddict
'''
from collections import UserString


class User(UserString):
    def append(self, s):
        self.data += s
        
    def remove(self, s):
        self.data = self.data.replace(s, '')
        
        
user1 = User('George')
print(user1) # George

user1.append(' Lin')
print(user1) # George Lin

# 刪除掉字串內的 'e'
user1.remove('e')
print(user1) # Gorg Lin
