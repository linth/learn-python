"""
References:
    - https://github.com/30-seconds/30-seconds-of-python
"""
from math import ceil


# all_equal([1, 2, 3, 4, 5, 6]) # False
# all_equal([1, 1, 1, 1]) # True
def all_equal(lst):
    return lst[1:] == lst[:-1]


# x = [1,2,3,4,5,6]
# y = [1,2,2,3,4,5]
# all_unique(x) # True
# all_unique(y) # False
def all_unique(lst):
    return len(lst) == len(set(lst))


# bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True]) # [ ['beep', 'boop', 'bar'], ['foo'] ]
def bifurcate(lst, filter):
    return [
        [x for i, x in enumerate(lst) if filter[i] is True],
        [x for i, x in enumerate(lst) if filter[i] is False]
    ]


# bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b') # [ ['beep', 'boop', 'bar'], ['foo'] ]
def bifurcate_by(lst, fn):
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]


# chunk([1,2,3,4,5],2) # [[1,2],[3,4],5]
def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size))))
    )


def compact(lst):
    return list(filter(bool, lst))


def count_by(arr, fn=lambda x: x):
    key = {}



if __name__ == '__main__':
    res = bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
    print(res)

    res1 = bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
    res2 = bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x in 'boop')
    print(res1)
    print(res2)


