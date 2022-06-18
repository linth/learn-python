'''
建立屬於自己定義的類型
    - NewType
    
    
Reference:
    - https://docs.python.org/zh-tw/3.6/library/typing.html
'''
from typing import NewType

user_id = NewType('user_id', int)
student_id = user_id(1)

print(student_id, type(student_id)) # 1 <class 'int'>
