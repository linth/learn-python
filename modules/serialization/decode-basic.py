'''
Refference:
    - https://www.tutorialspoint.com/How-can-I-convert-a-bytes-array-into-JSON-format-in-Python

Keywords:
    - decode
    - encode

python string and unicode string
    - http://quickteckiteasy.blogspot.com/2009/03/python-string-and-unicode-string.html
'''


def example():
    str_word = b'hello world.'
    print('The type of str_word is {}.'.format(type(str_word))) # The type of str_word is <class 'bytes'>.
    print('This is bytes file: {}.'.format(str_word)) #  is bytes file: b'hello world.'.

    # decode the new_str to string.
    new_str = str_word.decode('utf-8')
    print('The type of new_str is {}.'.format(type(new_str))) # The type of new_str is <class 'str'>.
    print('This is string: {}.'.format(new_str)) # This is string: hello world..


def main():
    example()


if __name__ == '__main__':
    main()
