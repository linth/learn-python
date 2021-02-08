"""
Learn getattr() and setattr() method to get/set the value of object.
"""


class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.sex = None


class Men(Person):
    def __init__(self, h, w):
        super().__init__(h, w)
        self.sex = 'boy'


class Woman(Person):
    def __init__(self, h, w):
        super().__init__(h, w)
        self.sex = 'girl'


if __name__ == '__main__':
    p = Person(178, 77)
    print(f'height: {p.height}, weight: {p.weight}')

    h = getattr(p, "height")
    w = getattr(p, "weight")
    print(f'height: {h}, weight: {w}')

    setattr(p, "height", 190)
    setattr(p, "weight", 80)
    print(f'height: {p.height}, weight: {p.weight}')

    print(f'the instance of person is {p.__dict__}')
    # get attributes with another way.
    print('height: ', p.__getattribute__('height'), 'weight: ', p.__getattribute__('weight'))

    m = Men(160, 80)
    print(f'men\'s height: {m.height}, weight: {m.weight}, sex: {m.sex}')
    woman = Woman(154, 38)
    print(f'woman\'s height: {woman.height}, weight: {woman.weight}, sex: {woman.sex}')

