'''
可以使用 typing 來使用 generic 限制/確認 引數的類型
    - 讓引數可以限制某些類型

Reference:
    - https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb
'''
from typing import Dict, Generic, TypeVar

T = TypeVar('T') # 自訂義一個 Type: T


class Registry(Generic[T]):
    
    def __init__(self):
        self._store: Dict[str, T] = {}
        
    def set_item(self, k: str, v: T):
        self._store[k] = v
        
    def get_item(self, k: str):
        return self._store[k]
    
    
if __name__ == '__main__':
    family_name_reg1 = Registry[str]()
    family_name_reg2 = Registry[str]()
    family_age_reg = Registry[int]()
    
    family_name_reg1.set_item('name', 'george')
    family_name_reg2.set_item('name', 'peter')
    
    family_age_reg.set_item('age', 30)
    
    print(family_name_reg1.get_item('name'))
    print(family_name_reg2.get_item('name'))
    print(family_age_reg.get_item('age'))
    