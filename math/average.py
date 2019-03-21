# average
'''
    Reference:
    - http://python.kriadmin.me/
    - https://github.com/30-seconds/30-seconds-of-code?fbclid=IwAR0S37V25YPJCX0k9Kuj7kHZVHMQp3c70Tezvc00XEJYtzmnwsK3lJTiqfw
    - https://github.com/codingforentrepreneurs/30-Days-of-Python
'''


def average(*args):
    return sum(args, 0.0) / len(args)

def factorial(num):
    if not ((num >= 0) and (num % 1 == 0)):
        raise Exception('can\'t be floating point or negative.')
    return 1 if num == 0 else num * factorial(num-1)

def max_n(list, n=1, reverse=True):
    return sorted(list, reverse=reverse)[:n]

from copy import deepcopy

def min_n(list, n=1):
    number = deepcopy(list)
    number.sort()
    return number[:n]

if __name__ == '__main__':
    list = [1, 2, 3]
    s = average(*list)
    print(s)
    print(factorial(6))

    print(max_n([1, 2, 3])) # [3]
    print(max_n([1, 2, 3], 2)) # [3, 2]

    print(min_n([1, 2, 3])) # [3]
    print(min_n([1, 2, 3], 2)) # [3, 2]
