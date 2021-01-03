"""
Goal:
    This sample code is for avoiding the parameters could be changed/updated.
"""
from abc import ABC, abstractmethod


class StudentDelegate(ABC):
    def get_id(self) -> str:
        pass

    def get_name(self) -> str:
        pass

    def get_age(self) -> int:
        pass


class StudentImpl(StudentDelegate):
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age


if __name__ == '__main__':
    # please check the following and understand what's different between thtem.
    student1 = StudentImpl('F0001', 'George', 30)
    student2: StudentDelegate = StudentImpl('F0002', 'May', 20)

    print(f'ID: {student1.id}, Name: {student1.name}, Age: {student1.age}')
    print(f'ID: Name: {student2.name}, Age: {student2.age}')

    # still can be updated/changed, the method cannot be avoid completely.
    print(student2.name)
    student2.name = 'Peter'
    print(student2.name)
