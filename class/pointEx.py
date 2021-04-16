"""
Point class example.

Reference:
    - https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-points/
"""
import copy
import math


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y
        # print('[Point] x = {}, y = {}'.format(self.x, self.y))

    def __str__(self):
        return '[Point Class]: ({}, {})'.format(self.x, self.y)

    def distance_from_origin(self) -> float:
        """
        calculate the distance between origin to point.
        :return:
        """
        print(self.x, self.y)
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def midpoint(self, target) -> object:
        """
        calculate the middle point between the origin to target.
        :param target:
        :return:
        """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


class Line(Point):
    def __init__(self, x: int = 0, y: int = 0, x2: int = 0, y2: int = 0):
        super().__init__(x, y)
        self.x2 = x2
        self.y2 = y2
        # print('[Line] x = {}, y = {}, x2 = {}, y2 = {}'.format(self.x, self.y, self.x2, self.y2))

    def __str__(self):
        return '[Line Class]: ({}, {}) to ({}, {})'.format(self.x, self.y, self.x2, self.y2)

    def the_length_of_line(self) -> float:
        """
        calculate the distance between two nodes.
        :return:
        """
        return ((self.x - self.x2) ** 2 + (self.y - self.y2) ** 2) ** 0.5


class Point3D(Point):
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        super().__init__(x, y)
        self.z = z
        # print('[Point3D] x = {}, y = {}, z = {}'.format(self.x, self.y, self.z))

    def __str__(self):
        return '[Point3D Class]: ({}, {}, {})'.format(self.x, self.y, self.z)

    def distance_3d_form_origin(self) -> float:
        """
        calculate the distance between two 3d points.
        :return:
        """
        x = abs(self.x - 0)
        y = abs(self.y - 0)
        z = abs(self.z - 0)
        return math.sqrt(x ** 2 + y ** 2 + z ** 2)

    def is_over_distance(self, dist: int = 3) -> bool:
        """
        calculate the distance is over or not.
        :param dist: the limited values of distance.
        :return:
        """
        if self.distance_3d_form_origin() > dist:
            return True
        return False


def check_the_object_sameness(point1: object, point2: object):
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
    # p = Point()     # this is a point class (0, 0)
    # print(p)        # x = 0, y = 0
    # print('x = {}, y = {}'.format(p.x, p.y))    # 10 10

    # p.x, p.y = 10, 10
    # print(p.distance_from_origin())     # 14.142135623730951
    #
    # q = Point()
    # r = Point()
    # r.x = 10
    # r.y = 10
    # res = q.midpoint(r)
    # print(res.x, res.y) # 5.0 5.0
    #
    # s = Point3D()
    # s.x, s.y, s.z = 10, 10, 10
    # print('({}, {}, {})'.format(s.x, s.y, s.z)) # (10, 10, 10)

    # p1 = Point()
    # p2 = p1
    # check_the_object_sameness(p1, p2) # point1: (0 0) and point2: (0 0) are the same.
    # p1, p2 = Point(), Point()
    # check_the_object_sameness(p1, p2) # point1: (0 0) and point2: (0 0) aren't the same.
    #
    # # copying.
    # p3 = Point(8, 7)
    # p4 = copy.copy(p3)
    # check_the_object_sameness(p3, p4) # point1: (8 7) and point2: (8 7) aren't the same.

    '''
        Results: 
            [Point Class]: (0, 0)
            [Line Class]: (0, 0) to (0, 0)
            [Point3D Class]: (0, 0, 0)
    '''
    # example_class()

    arr = (1, 2, 3)
    p3d = Point3D(1, 2, 3)
    res = p3d.distance_3d_form_origin()
    res2 = p3d.is_over_distance(3)
    print(p3d, res, res2)
