'''
References:
    - https://realpython.com/python-super/
'''


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


if __name__ == '__main__':
    r = Rectangle(3, 10)
    print('The area of rectangle is {}'.format(r.area()))
    print('The perimeter of rectangle is {}'.format(r.perimeter()))

    s = Square(7)
    print('The area of square is {}'.format(s.area()))
    print('The perimeter of square is {}'.format(s.perimeter()))




