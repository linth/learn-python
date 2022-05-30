"""
Reference:
    - https://openhome.cc/Gossip/CodeData/PythonTutorial/FunctionModuleClassPackagePy3.html
"""


class Account:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.balance = 0

    def deposit(self, amount: int) -> None:
        """
        deposit the money into the bank.
        :param amount:
        :return:
        """
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        """
        take money away from the bank.
        :param amount:
        :return:
        """
        try:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError('the memory of account is not enough.')
        except Exception as e:
            raise e

    def __str__(self):
        return ("Id: %s, Name: %s, Balance: %s" % (self.id, self.name, str(self.balance)))


class CheckingAccount(Account):
    def __init__(self, id: str, name: str):
        # Please check the code equals to `super().__init(id, name)` or not.
        # super(CheckingAccount, self).__init__(id, name) # call parent class.
        super().__init__(id, name)
        self.overdraftlimit = 30000

    def withdraw(self, amount: int) -> None:
        """
        turn back your money.
        :param amount:
        :return:
        """
        try:
            res = dict()
            if amount <= self.balance + self.overdraftlimit:
                self.balance -= amount
                res['type'] = 'successful'
                res['message'] = self.balance
                return res
            else:
                raise ValueError('Out of credit.')
        except ValueError as ve:
            res['type'] = 'ValueError'
            res['error message'] = ve.__str__()
            # raise ve
            return res
        except Exception as e:
            res['type'] = 'Exception'
            res['error message'] = e.__str__()
            # raise e
            return res

    def __str__(self):
        return (super(CheckingAccount, self).__str__() + " Overdraft limit " + str(self.overdraftlimit))


if __name__ == '__main__':
    a = CheckingAccount('E1234', 'George')
    a.deposit(1000)
    res = a.withdraw(2000)
    print(f'result: {res}')
