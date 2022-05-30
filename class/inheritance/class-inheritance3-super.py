'''
References:
    - https://realpython.com/python-super/
'''

class Car:  # first way.
    def __init__(self, wheels, door, passengers):
        self.wheels = wheels
        self.door = door
        self.passengers = passengers

    def __str__(self):
        return '[Car Class] wheels = {}, door = {}, passengers = {}'.format(self.wheels, self.door, self.passengers)


class Car2: # second way.
    def __init__(self):
        self.wheels = 4
        self.door = 4
        self.passengers = 4


class Car3: # third way.
    def __init__(self, wheels=4, door=4, passengers=4):
        self.wheels = wheels
        self.door = door
        self.passengers = passengers


class Toyota(Car):
    def __init__(self, wheels, door, passengers):
        super().__init__(wheels=wheels, door=door, passengers=passengers)

    def __str__(self):
        return '[Toyota Class] wheels = {}, door = {}, passengers = {}'.format(self.wheels, self.door, self.passengers)


class Truk(Car3):
    def __init__(self, door, sunroof):
        super().__init__(wheels=4, door=door, passengers=4)
        self.door = door
        self.sunroof = sunroof

    def __str__(self):
        return '[Truk Class] wheels = {}, door = {}, passengers = {}, sunroof = {}'.format(self.wheels, self.door, self.passengers, self.sunroof)


if __name__ == '__main__':
    c = Car(4, 4, 4)
    print(c) # [Car Class] wheels = 4, door = 4, passengers = 4
    print("the wheel = {0}, the door = {1}, the passengers = {2}".format(c.wheels, c.door, c.passengers)) # the wheel = 4, the door = 4, the passengers = 4

    t = Toyota(4, 4, 4)
    t.door = 5
    t.passengers = 6
    print(t) # [Toyota Class] wheels = 4, door = 5, passengers = 6
    print("the wheel = {0}, the door = {1}, the passengers = {2}".format(t.wheels, t.door, t.passengers)) # the wheel = 4, the door = 5, the passengers = 6

    tr = Truk(3, True)
    print(tr) # [Truk Class] wheels = 4, door = 3, passengers = 4, sunroof = True
    print("the wheel = {0}, the door = {1}, the passengers = {2}, the sunroof = {3}".format(tr.wheels, tr.door, tr.passengers, tr.sunroof)) # the wheel = 4, the door = 3, the passengers = 4, the sunroof = True
