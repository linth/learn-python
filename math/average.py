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

if __name__ == '__main__':
    list = [1, 2, 3]
    s = average(*list)
    print(s)

    print(factorial(6))
