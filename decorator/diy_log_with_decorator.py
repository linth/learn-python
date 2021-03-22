"""
Reference:
    - https://medium.com/@serge45497/python-%E4%B8%AD%E7%9A%84-decorator-%E8%AA%9E%E6%B3%95%E7%B3%96-3f9279f43d2b
    - https://foofish.net/python-decorator.html

# 裝飾器返回是一個function或class，作用就是為已存在的object添加額外功能
"""


def logger(func):
    """
    implement the logger to print information.
    :param func:
    :return:
    """
    print(f'Executing {func.__name__}...')
    func()
    print(f'Ending the {func.__name__}...')


def f1():
    print(f'run f1()...')


def improve_logger(func):
    def wrapper(*args, **kwargs):
        print(f'Starting the {func.__name__}...')
        func(*args, **kwargs)
        print(f'Ending the {func.__name__}...')
    return wrapper


def f2():
    print(f'run f2()...')


@improve_logger
def f3(*args, **kwargs):
    print(f'run f3()...')
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


def greate_logger(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'starting executing greate_logger()...')
            if level == 'high':
                print(f'the level is high.')
                sum_ = 0
                for i in args[0]:
                    sum_ += i
                print(f'args = {args}, kwargs = {kwargs}, sum = {sum_}')
                func(*args, **kwargs)
            elif level == 'medium':
                print(f'the level is medium.')
                multi = 0
                for i in args[0]:
                    multi *= i
                print(f'args = {args}, kwargs = {kwargs}, Multiplication = {multi}')
                func(*args, **kwargs)
            else:
                print(f'the level is low.')
                nagtive_ = 0
                for i in args[0]:
                    nagtive_ -= i
                print(f'args = {args}, kwargs = {kwargs}, nagtive = {nagtive_}')
            print(f'ending the greate_logger()...')
        return wrapper
    return decorator


@greate_logger(level='high')
def f4(*args, **kwargs):
    print(f'run f4()...')
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


if __name__ == '__main__':
    """ 請確認範例的差異性 """
    # use logger() and argument is a function. (最初原始想法)
    # logger(f1)

    # 建立另個function帶入 (第一階段修改)
    # f2 = improve_logger(f2) # 也可以命名另外的名稱
    # f2()

    # 語法糖 (第二階段修改)
    # f3([1, 2, 3], name='george', age=18)
    #
    arr = [4, 5, 6]
    d = {'name': 'Peter', 'age': 20}
    # f3(*arr, **d)

    # decorator 多階 (第三階段修改)
    f4(arr, **d)




