'''
specific method.

Reference:
    - https://www.brilliantcode.net/761/python-3-6-class/
    - https://www.geeksforgeeks.org/python-__repr__-magic-method/?ref=rp
'''

class StudentCompare(object):
    
    def __init__(self, id: str, name: str, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age
    
    def __eq__(self, input) -> bool:
        # 判斷物件是否等於
        return self.age == input.age
    
    def __lt__(self, input) -> bool:
        # 判斷物件是否小於
        return self.age > input.age
    
    def __le__(self, input) -> bool:
        # 判斷物件是否小於等於
        return self.age <= input
    
    def __ne__(self, __o: object) -> bool:
        # 判斷物件是否不等於
        return self.age != __o
    
    def __gt__(self, input) -> bool:
        # 判斷物件是否大於
        return self.age > input.age
    
    def __ge__(self, input) -> bool:
        # 判斷物件是否大於等於
        return self.age >= input.age
        
    def __add__(self, input) -> int:
        return self.age + input.age
    
    def __iadd__(self, num: int) -> int:
        self.age += num
        return self.age
    
    def __sub__(self, num: int) -> int:
        return self.age - num
        
    def __isub__(self, num: int) -> int:
        self.age -= num
        return self.age
    
    def __mul__(self, num: int) -> int:
        return self.age * num
        
    def __imul__(self, num: int) -> int:
        self.age *= num
        return self.age
        
    

if __name__ == '__main__':
    sc = StudentCompare('P001', 'george', 30)
    sc2 = StudentCompare('P002', 'bill', 22)
    
    print(sc.__eq__(sc2)) # False
    print(sc.__lt__(sc2)) # True
    
    print(sc.__iadd__(2)) # 32    
    print(sc.__mul__(2)) # 64
    
    
    