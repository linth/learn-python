'''
References:
    - https://realpython.com/primer-on-python-decorators/
'''


# TODO: inner function example.
def parent(num):
    print('This is the parent() function.')

    def first_child():
        print('This is the first_child() function.')

    def second_child():
        print('This is the second_child() function.')

    if num == 1:
        return first_child()
    else:
        return second_child()


# TODO: simple decorators.
def my_decorator(func):
    def wrapper():
        print('before the function is called.')
        func()
        print('after the function is called.')
    return wrapper


@my_decorator
def say_whee():
    print('Whee........')


# say_whee = my_decorator(say_whee) # without syntactic sugar.

if __name__ == '__main__':
    # parent(1)

    say_whee()
