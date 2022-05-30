from datetime import date

'''
Goal: learn how to use the @classmethod in the class. 

Keyword:
    - class
    - classmethod

References:
    - https://realpython.com/instance-class-and-static-methods-demystified/
    - https://www.geeksforgeeks.org/classmethod-in-python/
    - https://www.youtube.com/watch?v=rq8cL2XMM5M&t=2s
    
Note:
    - 不需要實體化
    - 可以用來調用class的屬性、方法、實體化對象
'''


class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @classmethod
    def from_birth_year(cls, name, year, sex):
        """
        calculate the age of person.
        :param name: person's name.
        :param year: person's age.
        :return:
        """
        return cls(name, date.today().year - year, sex)

    @staticmethod
    def is_adult_with_staticmethod(age: int):
        """
        check the person is adult or not.
        :param age:
        :return:
        """
        return age > 18

    def is_adult_with_self(self):
        """
        check the age is larger than 18 or not.
        :return:
        """
        if self.age > 18:
            return True
        else:
            return False

    # def is_adult(self, a):
    #     print(a)

    @classmethod
    def string_to_obj(cls, person_str):
        """
        create object by using the input of string.
        :param person_str:
        :return:
        """
        name, age, sex = person_str.split('-')
        return cls(name, age, sex)


if __name__ == '__main__':
    p = Person.from_birth_year('george', 1984, 'Boy')

    p1 = Person('may', 31, 'Boy')
    p2 = Person('peter', 66, 'Boy')
    p3 = Person('JJ Lin', 10, 'girl')

    print('p person information: ', p.name, p.age, p.sex)

    print('p1 person information: ', p1.name, p1.age, p1.sex)
    print('p2 person information: ', p2.name, p2.age, p2.sex)

    print('Is adult: ', Person.is_adult_with_staticmethod(22)) # using staticmethod class.
    # print(p3.is_adult(p3.age))

    # print(p3.is_adult('bb'))
    # print(p3.is_adult('aa'))

    person_str_1 = 'King-1999-Boy'
    person_str_2 = 'GG-2005-Girl'
    person_str_3 = 'JJ-1988-Boy'

    pf1 = Person.string_to_obj(person_str_1)
    pf2 = Person.string_to_obj(person_str_2)
    pf3 = Person.string_to_obj(person_str_3)
    print(pf1.name, pf1.age, pf1.sex)
    print(pf2.name, pf2.age, pf2.sex)
    print(pf3.name, pf3.age, pf3.sex)
