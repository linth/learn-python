"""
Reference:
    - https://blog.techbridge.cc/2018/06/15/python-decorator-%E5%85%A5%E9%96%80%E6%95%99%E5%AD%B8/
    - https://foofish.net/python-decorator.html
"""


def my_decorator(func):
    """
    decorator function for printing the logging.
    :param func: a function.
    :return:
    """
    print(f'Starting the programming...')
    print(f'Executing {func.__name__} function...')
    return func


@my_decorator
def f1():
    # TODO: 當發生使用decorator時候，似乎會先暫存執行
    print('f1() 被裝飾函式執行')


@my_decorator
def f2():
    """ with decorator function. """
    print('f2() 被裝飾函式執行')


def f3():
    """ without decorator function. """
    print('f3() 被裝飾函式執行')


if __name__ == '__main__':
    # basic method.
    # f1()

    # *******************************************************************************
    # please note three kinds of method and think about what's different between them.
    # *******************************************************************************
    # Method 1:
    # my_decorator(f1) # 裝飾器加點料

    # Method 2:
    # my_decorator(f2())
    # my_function2 被裝飾函式執行
    # 裝飾器加點料
    # pass

    # Method 3:
    # o = my_decorator(f2())
    # o()
    # 裝飾器加點料
    # my_function2 被裝飾函式執行

    f1()
    f2()
    f3()
