from abc import ABC, abstractmethod


# ################################################
# template 1: for general class template.
# ################################################
class ClassTemplate:
    def method1(self):
        pass

    def method2(self):
        pass


# ################################################
# template 2: for creating ABC class template.
# ################################################
class ABCClassTemplate1(ABC):
    @abstractmethod
    def method1(self):
        pass


class ABCClassTemplate2(ABC):
    @abstractmethod
    def method2(self):
        pass


class ABCClassTemplate3:
    @abstractmethod
    def method3(self):
        pass


class ClassTemplateMix(ABCClassTemplate1,
                       ABCClassTemplate2,
                       ABCClassTemplate3):
    # composition
    pass


# ################################################
# template 3: for inheritance class template
# ################################################
class SubClassA(ClassTemplateMix):
    # ClassTemplateMix -> SubClassA
    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass


class SubClassB(ClassTemplateMix):
    # ClassTemplateMix -> SubClassB
    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass


class SubClassA1(SubClassA):
    # SubClassA -> SubClassA1
    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass


class SubClassA2(SubClassA):
    # SubClassA -> SubClassA2
    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass


