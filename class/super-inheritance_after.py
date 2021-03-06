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
        return 2 * (self.length + self.width)


# TODO: Here we declare that the square class inherits from the Rectangle class.
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Cube(Square):
    def surface_are(self):
        face_are = super().area()
        return face_are * 6

    def volume(self):
        return self.length**3


# TODO: multiple inheritance example:
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


if __name__ == '__main__':
    r = Rectangle(3, 10)
    print('The area of rectangle is {}'.format(r.area()))
    print('The perimeter of rectangle is {}'.format(r.perimeter()))

    s = Square(7)
    print('The area of square is {}'.format(s.area()))
    print('The perimeter of square is {}'.format(s.perimeter()))

    c = Cube(3)
    print(c.surface_are())
    print(c.volume())
