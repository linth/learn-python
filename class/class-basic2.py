"""
References:
    - https://www.runoob.com/python/python-func-super.html

You will learn something as follows:
    - How to use super() in the class?
    - class inheritance.
"""


class Human:
    # you can use string to show information, error, or warning message, and so on.
    info = ''

    def __init__(self, name, h=0, w=0):
        """ initial for Human. """
        self.name = name
        self.height = h
        self.weight = w

    def bmi(self):
        try:
            return self.weight / ((self.height/100)**2)
        except ZeroDivisionError as e:
            raise ('[Error] zero.', e)
        except Exception as e:
            raise ('[Error]: There is no height or weight information.', e)

    def show_info(self):
        self.info = f'name: {self.name}, height: {self.height}, weight: {self.weight}'


class Woman(Human):
    def __init__(self, name, h, w, bust=0, waist=0, hip=0):
        """ initial for Woman. """
        super().__init__(name, h, w)
        self.bust = bust
        self.waist = waist
        self.hip = hip

    def __str__(self):
        return self.name

    def print_bwh(self):
        """
        Return: show the bust, waist and hip of woman.
        """
        print("bust={}, waist={}, hip={}".format(self.bust, self.waist, self.hip))


class Man(Human):
    def __init__(self, name, h=0, w=0):
        """ initial for Man. """
        super().__init__(name, h, w)
        # self.height = h
        # self.weight = w
        # self.name = name

    def __str__(self):
        return self.name


class Student(Human):
    def __init__(self, id, name):
        super().__init__(name)
        self.id = id

    def show_info(self):
        super().show_info()
        self.info = f'{self.info}, id: {self.id}'
        print(self.info)


if __name__ == '__main__':
    w = Woman(165, 54, 83, 64, 84)
    print('Name = ', w.name, ', BMI = ', w.bmi())
    w.print_bwh()

    w2 = Woman(171, 60, 88, 60, 80, 'Qoo')
    print('Name = ', w2.name, ', BMI = ', w2.bmi())
    w2.print_bwh()

    m = Man('hihi')
    # m.height = 190
    # m.weight = 83
    print(m.name, m.height, m.weight)
    print('BMI = ', m.bmi())

    s = Student('F001', 'haha')
    s.show_info()

