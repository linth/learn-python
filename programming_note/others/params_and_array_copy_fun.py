"""
    Basic concept:
    - Because parameter will be copied and pass into the function, the parameter isn't modified.
    - The array cannot be copied. The array will be modified when the array of function is changed.
    - *arg -> tuple, tuple, 都無法使用支援改動
    - params, array/list, set, tuple, dict, string
"""


def param_fun(n):
    """
    :param n: parameter
    :return:
    """
    n = 0


def str_fun(str):
    """
    :param str: string
    :return:
    """
    str = 'aaa'


def array_fun(m):
    """
    :param m: array
    :return:
    """
    m[0] = 0


def set_fun(s):
    """
    :param s: set
    :return:
    """
    s.add(1)


def dict_fun(d):
    """
    :param d: dict
    :return:
    """
    d['a'] = 44


def main():
    # param
    v = 10
    print(f'Before: the parameter of v = {v}') # Before: the parameter of v = 10
    param_fun(v)
    print(f'After: the parameter of v = {v}') # After: the parameter of v = 10

    # string
    ss = 'bbb'
    print(f'Before: the string of ss = {ss}')
    str_fun(ss)
    print(f'After: the string of ss = {ss}')

    # array/list
    a = [1, 2, 3]
    print(f'Before: the array of a = {a}') # Before: the array of a = [1, 2, 3]
    array_fun(a)
    print(f'After: the array of a = {a}') # After: the array of a = [0, 2, 3]

    # set
    b = {11, 9, 3, 66}
    print(f'Before: the set of b = {b}') # Before: the set of b = {3, 9, 66, 11}
    set_fun(b)
    print(f'After: the set of b = {b}') # After: the set of b = {1, 66, 3, 9, 11}

    # dict
    c = {'a': 1, 'b': 2, 'c': 3}
    print(f'Before: the dict of c = {c}') # Before: the dict of c = {'a': 1, 'b': 2, 'c': 3}
    dict_fun(c)
    print(f'After: the dict of c = {c}') # After: the dict of c = {'a': 44, 'b': 2, 'c': 3}


if __name__ == '__main__':
    main()
