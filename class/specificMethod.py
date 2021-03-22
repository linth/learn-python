"""
    Reference:
        - https://www.brilliantcode.net/761/python-3-6-class/
        -
"""


class Car:
    def __init__(self, wheels=4, door=4, passengers=4):
        self.wheels = wheels
        self.door = door
        self.passengers = passengers

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

    # add __setattr__() example.


class Audi(Car):
    def __init__(self):
        super().__init__(4, 4, 4)

    def __str__(self):
        return f"[Audi] wheels: {self.wheels}, door: {self.door}, passengers: {self.passengers}"


class Toyota(Car):
    def __init__(self, brand_name='', air_bag=2, sunroof=True):
        super().__init__()
        self.brand_name = brand_name
        self.air_bag = air_bag
        self.sunroof = sunroof

    def __str__(self):
        return '[Toyota Class] wheels = {}, door = {}, passengers = {}, brand_name = {}, air_bag = {}, sunroof = {}'.format(self.wheels, self.door, self.passengers, self.brand_name, self.air_bag, self.sunroof)


if __name__ == '__main__':
    c = Car()
    print('General car: ', c.wheels, c.door, c.passengers)
    
    a = Audi()
    print('Audi\'s car: ', a.wheels, a.door, a.passengers)
    print(a.__str__())
    a.__setattr__('door', 2)

    t = Toyota()
    print('Toyota\'s car: ', t.wheels, t.door, t.passengers)
    print('compare with Audi\'s door and Toyota\'s door: ', a.door, t.door, a >= t, t<a, t==a, t!=a)
    t.passengers = 5
    t.door = 7
    print(t.__dict__)   # use __dict__ can show the dict: key/value.
    print(t.wheels, t.door, t.passengers, t.brand_name, t.air_bag, t.sunroof)
    print(t > c) # True.
    print(t < c) # False.
    print(t >= c) # True.
    print(t != c) # True.

    print(t + c) # 11

