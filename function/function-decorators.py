'''
# TODO: keyword is functools.
References:
    - https://realpython.com/primer-on-python-decorators/
'''


''' Reusing decorators. '''
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        # print(args, kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def say_whee():
    print('Whee!')


''' Decorating Functions With Arguments '''
@do_twice
def greet(name):
    print(f'Hello {name}')


''' Returning Values From Decorated Functions. '''
@do_twice
def return_greeting(name):
    print('create greeting.')
    return f"Hi, {name}"


# ==============================================
# TODO: using a example to practice the concept of decorate function.
# ==============================================
def do_twice_add(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        # return func(*args, **kwargs)
    return wrapper


@do_twice_add
def add(x, y):
    print('x+y: {} + {} = {}'.format(x, y, x+y))
    return x + y


if __name__ == '__main__':
    # say_whee()

    # greet('george')
    # TODO: Because the do_twice_wrapper() doesn’t explicitly return a value, the call return_greeting("Adam") ended up returning None.
    # hi_adam = return_greeting('Adam')
    # print(hi_adam)

    add(1, 2)




