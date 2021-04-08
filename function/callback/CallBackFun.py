"""
Callback Example:

A callback is a function that is passed as an argument to other function.
This other function is expected to call this callback function in its definition.
The point at which other function calls our callback function depends on the requirement and nature of other function.

Callback Functions are generally used with asynchronous functions.

Reference
    - https://pythonexamples.org/python-callback-function/
"""
import time


def callback_function(s):
    # time.sleep(2)
    print(f'length of the text file is : {s}')


def print_file_length(path, callback):
    print(f'Go Into print_file_length function....')
    f = open(path, 'r')
    length = len(f.read())
    f.close()
    print(f'close the file....')
    # time.sleep(1)
    callback(length)


s = [
    {'name': 'george', 'age': 37, 'height': 178, 'weight': 75},
    {'name': 'may', 'age': 22, 'height': 158, 'weight': 45},
]


def callback_search_name(name):
    for i in s:
        if i['name'] == name:
            return i
    return None


def small_task(name: str):
    print(f'Go Into do_something function....')
    res = callback_search_name(name)
    if res:
        print(f'find the name: {name}, the age of result: {res}')
    else:
        print(f'not found.')


if __name__ == '__main__':
    # print_file_length('sample.txt', callback_function)

    small_task('george')
