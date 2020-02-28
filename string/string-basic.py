"""
Goal: use %-format, format method, f-string to provide the parameter insert into the string.

Keyword:
    - f-string
    - string format

Reference:
    - http://openbookproject.net/thinkcs/python/english3e/strings.html
    - https://realpython.com/python-formatted-output/
"""


def use_upper_function():
    ss = "Hello world."
    res = ss.upper()
    print('The string becomes "{}"'.format(res))


def example1():
    """
    example 1: It's for using the function of format to print the string.
    :return:
    """
    fruit = "banana"
    m = fruit[1]
    print('The index 1 of fruit: {} is {}'.format(fruit, m)) # The index 1 of fruit: banana is a

    res = list(fruit)
    print('The list of fruit is {}'.format(res)) # The list of fruit is ['b', 'a', 'n', 'a', 'n', 'a']
    res1 = list(enumerate(fruit))
    print('The list of fruit is {} by enumerate.'.format(res1)) # The list of fruit is [(0, 'b'), (1, 'a'), (2, 'n'), (3, 'a'), (4, 'n'), (5, 'a')] by enumerate.


def example2():
    """
    example 2: It' for using the %-formatting to print the string.
    :return:
    """
    fruit = "banana"
    num = len(fruit)
    print('The length of fruit is %d' % num) # The length of fruit is 6

    i = 0
    while i < len(fruit):
        letter = fruit[i]
        # print(letter)
        i += 1


def example3():
    """
    example 3: It's for using the f-string to print the string.
    :return:
    """
    fruit = ["banana", "apple", "orange"]
    print(f'I love the fruit: {fruit[0]}')


def main():
    # use_upper_function()
    example1()
    example2()
    example3()


if __name__ == '__main__':
    main()
