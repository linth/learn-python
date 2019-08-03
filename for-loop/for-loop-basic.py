'''
References:
    - http://openbookproject.net/thinkcs/python/english3e/strings.html
'''

def example1():
    fruit = 'banana'
    for i in fruit:
        print('{}'.format(i))


def example2():
    prefixes = "JKLMNOPQ"
    suffix = 'ack'

    for i in prefixes:
        print('The combination of word is {}'.format(i + suffix))


def example3():
    s = "This is a book."
    print('The string of s is "{}" from {} index to {} index.'.format(s[0:7], 0, 7)) # The string of s is "This is" from 0 index to 7 index.


def example4():
    # Strings are immutable.
    greeting = 'Hello world!'
    # greeting[0] = 'J' # error
    print('The string greeting is {}.'.format(greeting))

def main():
    # example1()
    # example2()
    # example3()
    example4()

if __name__ == '__main__':
    main()
