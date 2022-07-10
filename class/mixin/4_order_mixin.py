'''
繼承上有順序
    - 前面優先繼承

Reference:
    - https://github.com/twtrubiks/python-notes/tree/master/what_is_the_mixin
'''

class HelloMixin:
    
    def display(self):
        print('HelloMixin hello')


class SuperHelloMixin:
    
    def display(self):
        print('SuperHello hello')


class A(SuperHelloMixin, HelloMixin):
    pass


if __name__ == '__main__':
    a = A()
    a.display()