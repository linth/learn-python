

class Car:

    # first way.
    def __init__(self, wheels, door, passengers):
        self.wheels = wheels
        self.door = door
        self.passengers = passengers

    # second way.
    def __init__(self):
        self.wheels = 4
        self.door = 4
        self.passengers = 4

    # third way.
    def __init__(self, wheels=4, door=4, passengers=4):
        self.wheels = wheels
        self.door = door
        self.passengers = passengers


class Toyota(Car):

    def __init__(self):
        super().__init__()


class Truk(Car):

    def __init__(self, door, sunroof):
        super().__init__()
        self.door = door
        self.sunroof = sunroof


if __name__ == '__main__':
    c = Car()
    print("the wheel = {0}, the door = {1}, the passengers = {2}".format(c.wheels, c.door, c.passengers)) # the wheel = 4, the door = 4, the passengers = 4

    t = Toyota()
    t.door = 5
    t.passengers = 6
    print("the wheel = {0}, the door = {1}, the passengers = {2}".format(t.wheels, t.door, t.passengers)) # the wheel = 4, the door = 5, the passengers = 6

    tr = Truk(3, True)
    print("the wheel = {0}, the door = {1}, the passengers = {2}, the sunroof = {3}".format(tr.wheels, tr.door, tr.passengers, tr.sunroof)) # the wheel = 4, the door = 3, the passengers = 4, the sunroof = True
