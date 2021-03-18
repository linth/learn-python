"""
Goal: using `getattr`, `hasattr`, `setattr`, `delattr`, 
"""

class Person:
    pass


class Woman(Person):
    pass


class Man(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age


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
    
