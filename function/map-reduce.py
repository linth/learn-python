'''
Reference:
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080
'''
from functools import reduce


def f(x):
    return x * x


def add(x, y):
    return x + y


def method1():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []
    for i in arr:
        res.append(f(i))
    print('The res = {}'.format(res)) # The res = [1, 4, 9, 16, 25, 36, 49, 64, 81]


def use_map():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # use the map function
    res = map(f, arr)
    print('The res = {} by using the map function.'.format(list(res))) # The res = [1, 4, 9, 16, 25, 36, 49, 64, 81] by using map function.


def use_reduce():
    # use the reduce function to calcuate the value of sum.
    arr = [1, 3, 5, 7, 9]
    res = reduce(add, arr)
    print('The res = {} by using the reduce function.'.format(res)) # The res = 25 by using the reduce function.

    # you can also use the function of sum.
    res1 = sum(arr)
    print('The res1 = {} by using the sum function.'.format(res1)) # The res1 = 25 by using the sum function.


def main():
    method1()
    use_map()
    use_reduce()


if __name__ == '__main__':
    main()
