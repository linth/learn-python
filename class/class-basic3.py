"""
References:
    - https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/Python1a_OOP.html

You will learn something as follows:
    - class inheritance.
"""


# example 1: add function from x-y axis to x-y-z axis.
class Form:
    info = ''

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.name = None

    def show_info(self):
        self.info = f'length: {self.length}; width: {self.width}; area: {self.area()}.'

    def area(self):
        pass


class Square(Form):
    def __init__(self, length):
        super().__init__(length, length)
        self.name = 'Square'

    def show_info(self):
        super().show_info()
        print(f'name: {self.name}, {self.info}')

    def area(self):
        return self.length ** 2


class Rectangle(Form):
    def __init__(self, length=0, width=0):
        super().__init__(length, width)
        self.name = 'Rectangle'

    def show_info(self):
        super().show_info()
        print(f'name: Rectangle; {self.info}')

    def area(self):
        return self.length * self.width


class Cube(Rectangle):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def show_info(self):
        print(f'name: Cube; lenght: {self.length}; width: {self.width}; high: {self.z}; area: {self.area()}')

    def area(self):
        return self.length * self.width * self.z


if __name__ == '__main__':
    s = Square(2)
    s.show_info()

    r = Rectangle(10, 2)
    r.show_info()

    c = Cube(1, 2, 3)
    c.show_info()
