"""
References:
    - https://www.runoob.com/python/python-func-super.html

You will learn something as follows:
    - How to use super() in the class?
    - class inheritance.
"""


class Human:
    def __init__(self, h=0, w=0):
        """ initial for Human. """
        self.height = h
        self.weight = w

    def bmi(self):
        return self.weight / ((self.height/100)**2)


class Woman(Human):
    def __init__(self, h, w, bust=0, waist=0, hip=0, name='Mary'):
        """ initial for Woman. """
        super().__init__(h, w)
        self.bust = bust
        self.waist = waist
        self.hip = hip
        self.name = name

    def __str__(self):
        """
        Return: the name of woman.
        """
        return self.name

    def print_bwh(self):
        """
        Return: show the bust, waist and hip of woman.
        """
        print("bust={}, waist={}, hip={}".format(self.bust, self.waist, self.hip))


class Man(Human):
    def __init__(self):
        """ initial for Man. """
        super().__init__()
        self.height = 180
        self.weight = 80


if __name__ == '__main__':
    w = Woman(165, 54, 83, 64, 84)
    print('Name = ', w.name, ', BMI = ', w.bmi())
    w.print_bwh()

    w2 = Woman(171, 60, 88, 60, 80, 'Qoo')
    print('Name = ', w2.name, ', BMI = ', w2.bmi())
    w2.print_bwh()

    m = Man()
    m.height = 190
    m.weight = 83
    print(m.height, m.weight)
    print('BMI = ', m.bmi())

