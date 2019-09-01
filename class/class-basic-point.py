import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        # print('[Point] x = {}, y = {}'.format(self.x, self.y))

    def __str__(self):
        return '[Point Class]: ({}, {})'.format(self.x, self.y)

    def distance_from_origin(self):
        print(self.x, self.y)
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def midpoint(self, target):
        ''' calculate the middle point between the origin to target. '''
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


class Line(Point):
    def __init__(self, x2=0, y2=0):
        super().__init__()
        self.x2 = x2
        self.y2 = y2
        # print('[Line] x = {}, y = {}, x2 = {}, y2 = {}'.format(self.x, self.y, self.x2, self.y2))

    def __str__(self):
        return '[Line Class]: ({}, {}) to ({}, {})'.format(self.x, self.y, self.x2, self.y2)

    def the_length_of_line(self):
        return ((self.x - self.x2) ** 2 + (self.y - self.y2) ** 2) ** 0.5


class Point3D(Point):
    def __init__(self, z=0):
        super().__init__()
        self.z = z
        # print('[Point3D] x = {}, y = {}, z = {}'.format(self.x, self.y, self.z))

    def __str__(self):
        return '[Point3D Class]: ({}, {}, {})'.format(self.x, self.y, self.z)


def check_the_object_sameness(point1, point2):
    # Sameness
    if point1 is point2:
        print('point1: ({} {}) and point2: ({} {}) are the same.'.format(point1.x, point1.y, point2.x, point2.y))
    else:
        print('point1: ({} {}) and point2: ({} {}) aren\'t the same.'.format(point1.x, point1.y, point2.x, point2.y))


def example_class():
    p = Point()
    l = Line()
    p3 = Point3D()
    print(p)
    print(l)
    print(p3)


if __name__ == '__main__':
    p = Point()     # this is a point class (0, 0)
    print(p)        # x = 0, y = 0
    print('x = {}, y = {}'.format(p.x, p.y))    # 10 10

    p.x, p.y = 10, 10
    print(p.distance_from_origin())     # 14.142135623730951

    q = Point()
    r = Point()
    r.x = 10
    r.y = 10
    res = q.midpoint(r)
    print(res.x, res.y) # 5.0 5.0

    s = Point3D()
    s.x, s.y, s.z = 10, 10, 10
    print('({}, {}, {})'.format(s.x, s.y, s.z)) # (10, 10, 10)

    p1 = Point()
    p2 = p1
    check_the_object_sameness(p1, p2) # point1: (0 0) and point2: (0 0) are the same.
    p1, p2 = Point(), Point()
    check_the_object_sameness(p1, p2) # point1: (0 0) and point2: (0 0) aren't the same.

    # copying.
    p3 = Point(8, 7)
    p4 = copy.copy(p3)
    check_the_object_sameness(p3, p4) # point1: (8 7) and point2: (8 7) aren't the same.

    '''
        Results: 
            [Point Class]: (0, 0)
            [Line Class]: (0, 0) to (0, 0)
            [Point3D Class]: (0, 0, 0)
    '''
    example_class()
