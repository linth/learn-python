'''
Generic function

Referenece:
    - https://www.cnblogs.com/wongbingming/p/13798567.html
'''

from functools import singledispatch

@singledispatch
def age(obj):
    print('Please type argument: ')

@age.register(int)
def _(age):
    print('I had already {} years old.'.format(age))

@age.register(str)
def _(age):
    print('I am {} years old.'.format(age))


age(23)  # int type, I had already 23 years old.
age('twenty three')  # str type, I am twenty three years old.
age(['23'])  # list type, Please type argument: