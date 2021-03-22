
# account example.
class Account:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError('the memory of account is not enough.')

    def __str__(self):
        return ("Id: %s, Name: %s, Balance: %s" % (self.id, self.name, str(self.balance)))


class CheckingAccount(Account):
    def __init__(self, id, name):
        # Please check the code equals to `super().__init(id, name)` or not.
        super(CheckingAccount, self).__init__(id, name) # call parent class.
        self.overdraftlimit = 30000

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraftlimit:
            self.balance -= amount
        else:
            raise ValueError('Out of credit.')

    def __str__(self):
        return (super(CheckingAccount, self).__str__() + " Overdraft limit " + str(self.overdraftlimit))


if __name__ == '__main__':
    a = CheckingAccount('E1234', 'George')
    a.deposit(1000)
    a.withdraw(2000)
    print(a)
