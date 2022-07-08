'''
Defining sub-classes of generic classes
    - 使用者定義的 generic class 或 generic class 可以被定義在 typing 使用。


首先不能使用 Any, 因為這樣無法讓函式可以除錯，return值可以式任何 type。
因此，我們就需要定義好 input/output 的 type，方便我們可以確認。但是直接定義 int, str, ...等，會讓程式變得 scale 很差。
解決的辦法就是使用 type variables:
    - Type variables allow you to link several types together. 
    - This is how you can use a type variable to annotate the identity function:
```
from typing import TypeVar

T = TypeVar('T')
```
    
    
Reference:
    - https://mypy.readthedocs.io/en/stable/generics.html#generic-functions
    - 
'''
from typing import Generic, TypeVar, Mapping, Iterator


KT = TypeVar('KT')
VT = TypeVar('VT')


class MyMap(Mapping[KT, VT]): # This is a generic subclass of Mapping
    
    # def __getitem__(self, k: KT) -> VT:
    #     pass
    
    # def __iter__(self) -> Iterator[KT]:
    #     pass
    
    # def __len__(self) -> int:
    #     pass
    
    pass

