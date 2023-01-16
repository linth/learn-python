'''
property concepts (重要!)

Reference:
    - https://www.maxlist.xyz/2019/12/25/python-property/
'''
class Bank_account:
    def __init__(self) -> None:
        self._password = 'default password: 0000'
        
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    
    @password.deleter
    def password(self):
        del self._password
        print('delete the password complite.')


if __name__ == '__main__':
    # print the default password.
    b = Bank_account()
    print(b._password)
    
    # set up new password.
    b.password = '1234'
    print(b._password)
    
    # delete password.
    del b.password