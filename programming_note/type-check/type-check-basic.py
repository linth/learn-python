'''
Reference:
    -  https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/356804/

'''

def check_type():
    a = 1
    b = "1"

    # python對於類型需要注意
    # two parameters are showing the 1, but the type of two parameters is different.
    print('a = {}. The type of a is {}.'.format(a, type(a)))
    print('b = {}. The type of b is {}.'.format(b, type(b)))


if __name__ == '__main__':
    check_type()
