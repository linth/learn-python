'''
Defining generic classes 定義一個 generic class
    - Stack 泛型範例
    - TypeVar
    - Generic
    
首先不能使用 Any, 因為這樣無法讓函式可以除錯，return值可以式任何 type。
因此，我們就需要定義好 input/output 的 type，方便我們可以確認。但是直接定義 int, str, ...等，會讓程式變得 scale 很差。
解決的辦法就是使用 type variables:
    - Type variables allow you to link several types together. 
    - This is how you can use a type variable to annotate the identity function:
```
from typing import TypeVar
T = TypeVar('T')
```

可以增加限制某些 type 才可以被允許通過。
```
from typing import TypeVar
T = TypeVar('T', int, float)
```


Reference:
    - https://mypy.readthedocs.io/en/stable/generics.html#generic-functions
    - https://dev.to/decorator_factory/typevars-explained-hmo
'''
from typing import TypeVar, Generic


# Putting constraints on a type variable (可以增加限制只允許某些type: int, float才可以通過)
T = TypeVar('T', int, float)


class Stack(Generic[T]):
    def __init__(self):
        # Create an empty list with items of type T.
        self.items = []
        
    def push(self, item: T):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def empty(self):
        return self.items


# Construct an empty Stack[int] instance
stack = Stack[int]()
stack.push(2)
stack.pop()
# print(stack.push('x')) # Type error

stack.push(2)
stack.push(3)
for i in stack.items:
    print(i)

