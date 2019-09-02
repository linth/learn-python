'''
    reference:
    - https://www.brilliantcode.net/761/python-3-6-class/
'''


class Car:
    def __init__(self, wheels=4, door=4, passengers=4):
        self.wheels = wheels
        self.door = door
        self.passengers = passengers


class Toyota(Car):
    def __init__(self, brand_name='', air_bag=2, sunroof=True):
        super().__init__()
        self.brand_name = brand_name
        self.air_bag = air_bag
        self.sunroof = sunroof

    def __str__(self):
        return '[Toyota Class] wheels = {}, door = {}, passengers = {}, brand_name = {}, air_bag = {}, sunroof = {}'.format(self.wheels, self.door, self.passengers, self.brand_name, self.air_bag, self.sunroof)

    def __gt__(self, other): # greater than.
        return self.door > other.door

    def __lt__(self, other): # less than.
        return self.door < other.door

    def __le__(self, other): # less than, equal to.
        return self.door <= other.door

    def __ge__(self, other): # greater than, equal to.
        return self.door >= other.door

    def __eq__(self, other): # equal.
        return self.door == other.door

    def __nq__(self, other):
        return self.door != other.door

    def __add__(self, other):
        return self.door + other.door


if __name__ == '__main__':
    c = Car()
    print(c.wheels, c.door, c.passengers)
    # print()
    # print()

    t = Toyota()
    t.passengers = 5
    t.door = 7
    print(t.wheels, t.door, t.passengers, t.brand_name, t.air_bag, t.sunroof)
    print(t > c) # True.
    print(t < c) # False.
    print(t >= c) # True.
    print(t != c) # True.

    print(t + c) # 11
