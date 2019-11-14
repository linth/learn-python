

def square(x):
    return x ** 2


def add(x):
    return x + 10


def use_map(fn, lst):
    return list(map(fn, lst))


if __name__ == '__main__':
    arr = [1, 2, 3, 6]

    res = use_map(square, arr)
    print(res)

    res1 = use_map(add, arr)
    print(res1)
