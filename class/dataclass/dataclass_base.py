'''
dataclass example (python 3.7 up)
    - 減少程式碼，更簡潔一點!
    
Reference:
    - https://haosquare.com/python-dataclass/
'''

from dataclasses import dataclass


# 一般寫法
# class Employee:
    
#     def __init__(self, name, job, salary=0):
#         self.name = name
#         self.job = job
#         self.salary = salary


# 使用 dataclass 寫法
@dataclass
class Employee:
    name: str
    job: str
    salary: int = 0
    
    

if __name__ == '__main__':
    emp1 = Employee('George', 'software engineer', 100000)
    print(emp1) # Employee(name='George', job='software engineer', salary=100000)
    


