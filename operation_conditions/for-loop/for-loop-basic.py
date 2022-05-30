'''
References:
    - http://openbookproject.net/thinkcs/python/english3e/strings.html
    - https://kaochenlong.com/2011/10/13/python-module/
'''
from decorator.decorator_class_time import Timer

arr = [1, 2, 6, 10, 5, 2, 6, 22]


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


@Timer
def example5():
    for i in range(10000):
        print(i)


def example6():
    for index, element in enumerate(arr):
        print('The index of arr is {}, and the value of arr is {}'.format(index, element))


class Example:
    def __init__(self, arr):
        self.arr = arr

    def example1(self):
        for index, element in enumerate(self.arr):
            print('The index of arr is {}, and the element of arr is {}'.format(index, element))

    def example2(self):
        arr_length = len(self.arr)
        for i in range(arr_length):
            print('The index of arr is {}, and the element of arr is {}'.format(i, self.arr[i]))


def main():
    # example1()
    # example2()
    # example3()
    # example4()
    # example5() # The executing time = 0.03789877891540527
    # example6()
    e = Example(arr)
    # e.example1()
    e.example2()


if __name__ == '__main__':
    main()
