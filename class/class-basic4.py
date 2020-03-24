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


class Dog(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def eat_shit(self):
        return NotImplemented
    

class George:
    pee_length = 10

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    @classmethod
    def pee(cls):
        print('pee' + '.' * cls.pee_length)


if __name__ == '__main__':

    George.pee()

