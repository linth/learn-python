

# example 1: add function from x-y axis to x-y-z axis.
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_print(self):
        print('class A: x-axis is {0}; y-axis is {1}'.format(self.x, self.y))

    def get_value(self):
        return "%s, %s" % (self.x, self.y)


class B(A):
    def __init__(self, x, y, z):
        # super(B, self).__init__(x, y) # for python 2.7
        super().__init__(x, y) # for python 3
        self.z = z

    def show_print(self):
        # super(B, self).show_print()
        print('class B: x-axis is {0}; y-axis is {1}; z-axis is {2}'.format(self.x, self.y, self.z))

    def get_value(self):
        return "%s, %s, %s" % (self.x, self.y, self.z)

if __name__ == '__main__':
    a = A(1, 2)
    a.show_print()
    print("(" + a.get_value() + ")")

    b = B(1, 2, 3)
    b.show_print()
    print("(" + b.get_value() + ")")

    c = B(1, 3, 2)
    c.show_print()
    print(c.get_value())
