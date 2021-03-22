"""
Goal: using `getattr`, `hasattr`, `setattr`, `delattr`, `__getattribute__`

- getattr(object, attr)
- setattr(object, attr, value)
- delattr(object, attr)
- object.__getattribute__(attr)
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = None


class Woman(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = 'girl'


class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = 'boy'


if __name__ == '__main__':
    m = Man('george', 30)
    print(f"the name of man: {getattr(m, 'name')}, the age of man: , {getattr(m, 'age')}")

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
    
    w = Woman('may', 40)
    print(f'the name of woman: {w.name}, the age: {w.age}, the gender: {w.gender}')
    print(f"we want to get the attribute of w object: {w.__getattribute__('name')}")
