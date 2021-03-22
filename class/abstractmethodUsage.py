"""
Goal: learn OOP concept in python.

Keyword:
    - inheritance
    - abstract class
    - abstract method
    - Composition

References:
    - https://realpython.com/inheritance-composition-python/
    - https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-2-static-class-abstract-methods%E4%B9%8B%E5%AF%A6%E7%8F%BE-1e3b3998bccf
"""
import abc
from abc import ABC, abstractmethod


class Animal(ABC):
    """ ABC class: Animal """
    def __init__(self):
        pass

    @abstractmethod
    def eat(self):
        return NotImplementedError('the eat() should be overridden.')

    @abstractmethod
    def run(self):
        return NotImplementedError('the run() should be overridden.')

    @abstractmethod
    def fly(self):
        return NotImplementedError('the fly() should be overridden.')

    def move(self):
        pass


class Dog(Animal):
    def __init__(self, sex: str):
        self.legs = 4
        self.mouth = 1
        self.body = 1
        self.sex = sex

    def eat(self):
        print(f'with {self.mouth} mouth to eat something.')

    def run(self):
        print(f'with {self.legs} legs to run.')

    def fly(self):
        raise NotImplemented
    

class Bird(Animal):
    def __init__(self, sex: str):
        self.legs = 2
        self.wing = 2
        self.mouth = 1
        self.body = 1
        self.sex = sex

    def eat(self):
        print(f'with {self.mouth} mouth to eat something (Bird).')

    def run(self):
        raise NotImplemented

    def fly(self):
        print(f'with {self.wing} wings to fly the sky.')


class Human(Animal):
    def __init__(self, sex):
        self.legs = 2
        self.hands = 2
        self.mouth = 1
        self.body = 1
        self.sex = sex

    def eat(self):
        return f'with {self.mouth} mouth to eat something (Human).'

    def run(self):
        return f'the human uses {self.legs} legs to run.'

    def fly(self):
        return NotImplemented



if __name__ == '__main__':
    d = Dog("boy")
    d.eat()
    print('sex:', d.sex)
    # TODO: if you don't use "@abc.abstractmethod",
    #  which means that you don't need to implement it necessarily.
    d.move()

    b = Bird("girl")
    b.fly()
    print('sex:', b.sex)
    # TODO: if you don't use "@abc.abstractmethod",
    #  which means that you don't need to implement it necessarily.
    b.move()

    h = Human('boy')
    print(f"the human: {h.eat()}; {h.run()}")
