"""
Reference:
    - https://docs.python.org/zh-tw/3/library/collections.html
"""
from collections import ChainMap, namedtuple


baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}

# print(baseline)
# print(adjustments)
# print(ChainMap(baseline, adjustments))
# print(list(ChainMap(baseline, adjustments)))


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

c = ChainMap(d1, d2, d3)
print(c, type(c))
# print(dir(c))


class PointA:
    pass


class Point(PointA):
    pass


Point = namedtuple('Point', ['x', 'y'])
print(Point)
p = Point(1, 2)
p2 = Point(5, 3)
print(p.x, p.y)
print(p2.x, p2.y)

print(isinstance(p, Point)) # True
print(isinstance(p2, Point)) # True
print(isinstance(p, PointA)) # False
