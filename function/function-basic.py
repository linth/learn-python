"""
function
"""


def function():
    print('Hello world.')


def add(x, y):
    return x + y


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def greeting(name: str) -> str:
    return 'Hello ' + name


def new_add(x: int, y: int) -> int:
    """
    sum of two int numbers. please reference the function of add and compare with them.
    :param x:
    :param y:
    :return:
    """
    return x+y


def show_kwargs(**kwargs):
    print(kwargs)


def show_values(**kwargs):
    for key, value in kwargs.items():
        print('the value of {} is {}'.format(key, value))


def example1(args1, args2, *args, **kwargs):
    print('args1', args1)
    print('args2', args2)
    print('args', args)
    print('kwargs', kwargs)


if __name__ == '__main__':
    function()

    z = add(1, 3)
    print('z', z) # 4

    x = add(1, 2, 3, 4, 5)
    print('x', x) # 15

    show_kwargs(name='George', id='F0001', sex='boy')   # {'name': 'George', 'id': 'F0001', 'sex': 'boy'}

    # the value of name is George
    # the value of id is F0001
    # the value of sex is boy
    show_values(name='George', id='F0001', sex='boy')

    # args1 1
    # args2 2
    # args (6, 3, 4, 1) => tuple
    # kwargs {'name': 'George', 'id': '888', 'weight': 66, 'height': 180}
    example1(1, 2, 6, 3, 4, 1, name='George', id='888', weight=66, height=180)

    # the type of argument will be checked first.
    res1 = greeting('george')
    res2 = new_add(11, 1)
    print(res1)
    print(res2)
