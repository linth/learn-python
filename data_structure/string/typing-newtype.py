"""
Reference:
    - https://docs.python.org/3/library/typing.html

Note:
    - 可以使用自訂的type來確保引數的類型，以免有錯誤值被帶入。

Keyword:
    - NewType
"""
from typing import NewType
UserId = NewType('UserId', int)


def get_user_name(user_id: UserId) -> str:
    return user_id


some_id = UserId('F00001')
print(some_id) # F00001
print(type(some_id)) # <class 'str'>
print(UserId) # <function NewType.<locals>.new_type at 0x0000022ED36E2EA0>
print(type(UserId)) # <class 'function'>
res = get_user_name(some_id)
print(res, type(res)) # F00001 <class 'str'>

some_id2 = UserId(1111)
res2 = get_user_name(some_id2)
print(res2, type(res2)) # 1111 <class 'int'>
