"""
this example is that let us know about abstractmethod.
- two things should be used at the same time. (ABC and abstractmethod)
"""
from abc import ABC, abstractmethod


class A(ABC):
    # ABC isn't work if you use ABC only.
    def show(self):
        print(f'A class - show() function.')


class B(ABC):
    """ 需加入 @abstractmethod才可以確保繼承過的class需要實作method. """
    @abstractmethod
    def show(self):
        raise NotImplementedError('show() should be overridden.')


class C(A):
    pass


class D(B):
    pass


if __name__ == '__main__':
    # a = A()
    # a.show()
    # TODO: please note the different between c and d as follows:
    c = C() # it's work.
    # d = D() # TypeError: Can't instantiate abstract class C with abstract methods show

