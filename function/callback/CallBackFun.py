"""
Callback Example:

A callback is a function that is passed as an argument to other function.
This other function is expected to call this callback function in its definition.
The point at which other function calls our callback function depends on the requirement and nature of other function.

Callback Functions are generally used with asynchronous functions.

何謂callback function，在google找到一篇相關的解釋
簡單的說，如果你使用了某個function，那麼你就是『call』了一個function。
如果系統或是函式是要求你給一個function pointer，這個function pointer指到一個實際的函式(多半這個函式是你自己寫的)。
然後它會在適當的時間呼叫此function，則此function就是所謂的 callback function。因為這個function是被『callback』了。


Reference
    - https://pythonexamples.org/python-callback-function/
    - https://ithelp.ithome.com.tw/articles/10006207
"""
import time


def callback_function1(num: int) -> None:
    print(f'callback function 1: length of the text file is : {num}')


def callback_function2(num: int) -> None:
    print(f'callback function 2: length of the text file is : {num}')


def print_file_length(path: str, callback):
    print(f'Go Into print_file_length function....')
    f = open(path, 'r')
    length = len(f.read())
    f.close()
    print(f'close the file....')
    callback(length)


s = [
    {'name': 'george', 'age': 37, 'height': 178, 'weight': 75},
    {'name': 'may', 'age': 22, 'height': 158, 'weight': 45},
]


def callback_search_name(name: str):
    for i in s:
        if i['name'] == name:
            time.sleep(3)
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
    print_file_length('sample.txt', callback_function1)
    print_file_length('sample.txt', callback_function2)

    # small_task('george')
    # small_task('aa') # not found.
