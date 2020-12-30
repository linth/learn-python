"""
Reference:
    - https://blog.techbridge.cc/2018/06/15/python-decorator-%E5%85%A5%E9%96%80%E6%95%99%E5%AD%B8/
    - https://foofish.net/python-decorator.html
"""


def my_decorator(func):
    print('裝飾器加點料')
    return func


@my_decorator
def my_function():
    print('my_function 被裝飾函式執行')


def my_function2():
    print('my_function2 被裝飾函式執行')


my_function()

# *******************************************************************************
# please note three kinds of method and think about what's different between them.
# *******************************************************************************
# Method 1:
my_decorator(my_function2)
# 裝飾器加點料


# Method 2:
my_decorator(my_function2())
# my_function2 被裝飾函式執行
# 裝飾器加點料


# Method 3:
o = my_decorator(my_function2)
o()
# 裝飾器加點料
# my_function2 被裝飾函式執行
