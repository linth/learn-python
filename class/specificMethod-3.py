'''
specific method
    - __str__() and __repr__()
    - __repr__() magic method returns a printable representation of the object.
    - The __str__() magic method returns the string

Reference:
    - https://www.geeksforgeeks.org/python-__repr__-magic-method/?ref=rp
'''

class GFG:
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self) -> str:
        return f'Name is {self.name}'
    
    def __repr__(self) -> str:
        return f'GFG(name={self.name})'


if __name__ == '__main__':
    obj = GFG('george')
    
    print(obj.__str__())
    print(obj.__repr__())
