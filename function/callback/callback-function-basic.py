"""
Reference:
- https://gist.github.com/mchung/76d774879245b355e8bff95f9172f9f8
"""


def add(num, callback):
    """
    callback function as argument.
    :param num:
    :param callback:
    :return:
    """
    res = []
    for i in num:
        res.append(callback(i))
    return res


def add2(num):
    """
    :param num:
    :return:
    """
    return num + 2


def mul2(num):
    """
    :param num:
    :return:
    """
    return num * 2


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4]
    result1 = add(arr1, add2)
    print('result1', result1)

    result2 = add(arr1, mul2)
    print('result2', result2)
