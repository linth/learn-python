'''
References:
    - https://www.geeksforgeeks.org/class-as-decorator-in-python/
'''


class ErrorCheck:
    # checking the error parameter using class decorator.
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        if any([isinstance(i, str) for i in args]):
            raise TypeError('The parameter cannot be a string.')
        else:
            return self.func(*args)


@ErrorCheck
def add_number(*numbers):
    return sum(numbers)


if __name__ == '__main__':

    print(add_number(1, 2, 3))
    print(add_number(1, '2', 3))
