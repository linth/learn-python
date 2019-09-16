
import time


class Student:
    def __init__(self, id=1, name='george', sex='boy', age=30, weight=78, height=178):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = weight
        self.height = height

    def get_info_by_id(self, id):
        if id == self.id:
            new_dict = {}
            new_dict['name'] = self.name
            new_dict['sex'] = self.sex
            new_dict['age'] = self.age
            new_dict['weight'] = self.weight
            new_dict['height'] = self.height
            print('Found it for id = {}'.format(id))
            return self
        else:
            print('Not found for id = {}'.format(id))


def calcualte_time():
    t_start = time.time()
    # s = Student()
    # s2 = Student(2, 'Mary', 'girl', 20, 40, 160)
    sum = 0
    for i in range(10000):
        for j in range(10000):
            sum = i + j
    t_end = time.time()
    total_spend_time = t_end - t_start
    return total_spend_time


if __name__ == '__main__':
    res = calcualte_time()
    print('Executing the function, and spending {} sec'.format(res)) # Executing the function, and spending 5.310758590698242 sec


