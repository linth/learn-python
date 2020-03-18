from datetime import date

'''
Goal: learn how to use the @classmethod in the class. 

Keyword:
    - class
    - classmethod

References:
    - https://realpython.com/instance-class-and-static-methods-demystified/
    - https://www.geeksforgeeks.org/classmethod-in-python/
    
Note:
    - 不需要實體化
    - 可以用來調用class的屬性、方法、實體化對象
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        """
        calculate the age of person.
        :param name: person's name.
        :param year: person's age.
        :return:
        """
        return cls(name, date.today().year - year)

    # @staticmethod
    # def is_adult(age):
    #     """
    #     check the person is adult or not.
    #     :param age:
    #     :return:
    #     """
    #     return age > 18

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False

    # def is_adult(self, a):
    #     print(a)


if __name__ == '__main__':
    p = Person.from_birth_year('george', 1984)

    p1 = Person('may', 31)
    p2 = Person('peter', 66)
    p3 = Person('JJ Lin', 10)

    print(p.name, p.age)

    print(p1.name, p1.age)
    print(p2.name, p2.age)

    # print(Person.is_adult(22))
    # print(p3.is_adult(p3.age))

    # print(p3.is_adult('bb'))
    # print(p3.is_adult('aa'))
