"""
Goal: using `getattr`, `hasattr`, `setattr`, `delattr`, `__getattribute__`

- getattr(object, attr)
- setattr(object, attr, value)
- delattr(object, attr)
- object.__getattribute__(attr)
"""


class Person:
    def __init__(self, name, age, h, w):
        self.name = name
        self.age = age
        self.gender = None
        self.height = h
        self.weight = w

    def bmi(self):
        return self.weight / ((self.height/100) ** 2)


class Woman(Person):
    def __init__(self, name, age, h, w):
        super().__init__(name, age, h, w)
        self.gender = 'girl'

    def bmi(self):
        return f"woman cannot provide the value of bmi."


class Man(Person):
    def __init__(self, name, age, h, w):
        super().__init__(name, age, h, w)
        self.gender = 'boy'
        

if __name__ == '__main__':
    m = Man('george', 30, 178, 75)
    print(f"the name of man: {getattr(m, 'name')}, the age of man: , {getattr(m, 'age')}, bmi: {m.bmi()}")

    # hasattr
    print('hasattr: ', hasattr(m, 'name'), hasattr(m, 'gender'), hasattr(m, 'age'))
    # setattr
    print('setattr: ', setattr(m, 'name', 'JJ'), setattr(m, 'age', 80))
    print('name change to: ', m.name, 'age change to: ', m.age)
    # delattr
    print(delattr(m, 'name'))
    try:
        print(m.name)
    except Exception as e:
        print('error: ', e)
    
    try:
        # try to find a not existed attribute.
        print(f"the gender of man: {getattr(m, 'gender')}")
    except Exception as e:
        print(f'the error: ', e)
    
    w = Woman('may', 40, 155, 48)
    print(f'the name of woman: {w.name}, the age: {w.age}, the gender: {w.gender}, bmi: {w.bmi()}')
    print(f"we want to get the attribute of w object: {w.__getattribute__('name')}")
