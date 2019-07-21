

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'this is a point class ({}, {})'.format(self.x, self.y)

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
        self.x2 = x2
        self.y2 = y2

    def the_length_of_line(self):
        return ((self.x - self.x2) ** 2 + (self.y - self.y2) ** 2) ** 0.5


class Point3D(Point):

    def __init__(self, z=0):
        self.z = z


if __name__ == '__main__':
    p = Point() # this is a point class (0, 0)
    print(p) # x = 0, y = 0
    print('x = {}, y = {}'.format(p.x, p.y)) # 10 10

    p.x, p.y = 10, 10
    print(p.distance_from_origin()) # 14.142135623730951

    q = Point()
    r = Point()
    r.x = 10
    r.y = 10
    res = q.midpoint(r)
    print(res.x, res.y) # 5.0 5.0

    s = Point3D()
    s.x, s.y, s.z = 10, 10, 10
    print('({}, {}, {})'.format(s.x, s.y, s.z)) # (10, 10, 10)
