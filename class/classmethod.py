from datetime import date

'''
References:
    - https://realpython.com/instance-class-and-static-methods-demystified/
    - https://www.geeksforgeeks.org/classmethod-in-python/
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_ault(age):
        return age > 18


if __name__ == '__main__':
    p = Person.from_birth_year('george', 1984)

    p1 = Person('may', 31)
    p2 = Person('peter', 66)

    print(p.name, p.age)

    print(p1.name, p1.age)
    print(p2.name, p2.age)

    print(Person.is_ault(22))
