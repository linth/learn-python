'''
References:
    - https://zhuanlan.zhihu.com/p/28010894
    - https://openhome.cc/Gossip/Python/StaticClassMethod.html
    - https://www.geeksforgeeks.org/classmethod-in-python/
'''
from datetime import date


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print('The student name is {}'.format(self.name))

    @classmethod
    def from_birthday_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


class Robot:
    def introduce_self(self):
        print('My name is ' + self.name)


class YmvsStudent(Student):
    def __init__(self, student_id):
        super().__init__()
        self.id = student_id

if __name__ == '__main__':
    # ''' Case 1: you have to create the instance if you want to use the class. '''
    # s = Student('george', 15)
    # s.print_name()
    # g = s.from_birthday_year('george', 1984)
    # print('The age of george is {}-years-old'.format(g.age))
    #
    # ''' Case 2: use class method. '''
    # s1 = Student.from_birthday_year('May', 20)
    # print(s1.age, s1.name)
    #
    # ''' Case 3: use static method. '''
    # print(Student.is_adult(22))
    s = Student('george', 20)
    print(s.name, s.age)
    y = YmvsStudent(1)
    print(y.student_id)


