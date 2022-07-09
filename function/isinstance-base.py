'''
isinstance 範例
    - isinstance() 與 type() 區別

Reference:
    - https://www.runoob.com/python/python-func-isinstance.html
'''

a = 2


class A:
    pass


class B(A):
    pass


print(isinstance(a, int)) # True
print(isinstance(a, str)) # False
print(isinstance(a, (int, str, list))) # True


print(isinstance(A(), A)) # True
print(type(A()) == A) # True
print(isinstance(B(), A)) # True
print(type(B()) == A) # False
