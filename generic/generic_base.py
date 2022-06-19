'''
generic base.

Reference:
    - https://docs.python.org/zh-tw/3.6/library/typing.html
'''

def greeting(name: str) -> str:
    return 'Hello ' + name


print(greeting('george'))
# print(greeting(111)) # TypeError: can only concatenate str (not "int") to str
