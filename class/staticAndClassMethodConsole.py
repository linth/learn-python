from datetime import date

'''
Explanation:

1) 在OOP概念中，所有的class下的method，都稱為class method。
在python裡，有一個觀念class method是指一個method是帶有class本身作為參數傳入。

2) 使用staticmethod 也可以拉出class外面撰寫，然而寫在class內部主要是：
- 可讀性較佳
- 減少memory使用，因為不使用self帶入屬性
- 可允許使用override去複寫method

References:
    - https://zhuanlan.zhihu.com/p/28010894
    - https://openhome.cc/Gossip/Python/StaticClassMethod.html
    - https://www.geeksforgeeks.org/classmethod-in-python/
    - https://realpython.com/instance-class-and-static-methods-demystified/

Explanation: 
    - https://stackoverflow.com/questions/2438473/what-is-the-advantage-of-using-static-methods-in-python/2438627
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.categories = None

    @staticmethod
    def is_adult(age):
        return age > 18


# example 1: student
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.categories = 'student'

    def print_name(self):
        print('The student name is {}'.format(self.name))

    @classmethod
    def from_birthday_year(cls, name, year):
        return cls(name, date.today().year - year)

    @classmethod
    def get_birthday(cls):
        print('cls: ', cls)
        # return 1911 + int(cls.age)


def is_adult(age: int) -> bool:
    """ 請思考上方使用 @staticmethod 跟 單純使用function處理有什麼不同？ """
    return age > 18


# example 2: teacher.
class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.categories = 'teacher'

    @staticmethod
    def is_adult(age: int):
        """ check the teacher is senior or jounior. """
        return age > 50


class Robot:
    def introduce_self(self):
        print('My name is ' + self.name)


class YmvsStudent(Student):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.id = student_id


class YmvsTeacher(Teacher):
    def __init__(self, name, age):
        super().__init__(name, age)


# example 2: static and class method.
class MyClass:
    def method(self):
        ''' The first method on MyClass, called method, is a regular instance method.'''
        print('MyClass method.')
        return 'instance method called', self

    @classmethod
    def classmthod(cls):
        ''' class methods take a cls parameter that points to the class—and not the object instance—when the method is called.'''
        print('MyClass classmethod.')
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        ''' This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).'''
        print('MyClass staticmethod.')
        return 'static method called'


if __name__ == '__main__':
    # ''' Case 1: you have to create the instance if you want to use the class. '''
    s = Student('george', 15)
    s.print_name()
    g = s.from_birthday_year('george', 1984)
    s.get_birthday()
    # print('res: ', s.get_birthday())
    # print('The age of george is {}-years-old'.format(g.age))
    #
    # ''' Case 2: use class method. '''
    # s1 = Student.from_birthday_year('May', 20)
    # print(s1.age, s1.name)
    #
    # ''' Case 3: use static method. '''
    print(Student.is_adult(22))

    # s = Student('george', 20)
    # print(s.name, s.age)
    # y = YmvsStudent(1)
    # print(y.student_id)

    m = MyClass()
    # print(m, type(m))
    # print(m.method(), type(m.method()))
    # m.method()
    # m.classmthod()
    # m.staticmethod()

    # MyClass.classmthod()
    # MyClass.staticmethod()
    # MyClass.method()    # error.

    ys = YmvsStudent('peter', 18, 'F0001')
    print('name: ', ys.name, '; age: ', ys.age, '; student_id: ', ys.id, '; categories: ', ys.categories)
    print('Is the student adult: ', ys.is_adult(ys.age))

    yt = YmvsTeacher('Mary Chen', 50)
    print('name: ', yt.name, '; age: ', yt.age, '; categories: ', yt.categories)
    print('Is the teacher adult: ', yt.is_adult(yt.age))
