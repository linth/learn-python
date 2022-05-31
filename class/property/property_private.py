'''
@property 函數
    - 作用是在class中返回屬性值。

Reference:
    - https://www.maxlist.xyz/2019/12/25/python-property/
'''

class Student:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @property
    def name(self):
        ''' I'm the `name` property. '''
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @name.deleter
    def name(self):
        del self._name
        
if __name__ == '__main__':
    s = Student('george', 34)
    print('name: ', s._name, '; age: ', s._age)
        
    s._age = 11
    print(s._age)