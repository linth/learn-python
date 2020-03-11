"""
Goal: learn to split the string and do something.

Keyword:
    - split

References:
    - https://www.youtube.com/watch?v=rq8cL2XMM5M (youtube video)
    - https://realpython.com/python-formatted-output/
"""


class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gamil.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


if __name__ == '__main__':
    emp_1 = Employee('george', 'lin', 50000)
    emp_2 = Employee('may', 'chen', 88888)

    emp_str_1 = 'John-Doe-700000'
    emp_str_2 = 'Steve-Smith-540000'
    emp_str_3 = 'Jane-Doe-220000'

    new_emp_1 = Employee.from_string(emp_str_2)
    print(new_emp_1.email) # Steve.Smith@gamil.com
    print(new_emp_1.pay) # 540000
    print(new_emp_1.num_of_emps) # 3
