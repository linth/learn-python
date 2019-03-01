'''
    class basic concept.
'''


# account example.
class Account:
    # init
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('the amount must be positive.')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('the balance is not enough.')

# student example.
class Student:
    # init:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.sex = ''
        self.age = None
        self.weight = None
        self.height = None

    def set_weight(self, id, weight):
        if self.id == id:
            self.weight = weight
        else:
            print("the studenet's id isn't existed")

if __name__ == '__main__':
    a = Account('123-123-123', 'George')
    print(a.number)
    print(a.name)
    print(a.balance)

    a.deposit(500)
    print('balance', a.balance)
    a.withdraw(100)
    print('the balance value is %s' % (a.balance))


    s = Student('F001', 'George')
    print(s.id)
    print(s.name)
    print(s.sex)
    print(s.age)
    print(s.weight)
    print(s.height)

    s.set_weight('F001', 78)
    s.set_weight('F002', 100) # not found.
    print(s.weight)
