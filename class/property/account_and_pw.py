'''
account and password.
TODO: (尚未完成)

Reference:
    - https://www.maxlist.xyz/2019/12/25/python-property/

'''
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    
    def __init__(self):
        self._password = 'default password: 0000'
        self.password_hash = None
        
    @property
    def password(self):
        # return self._password
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        # self._password = value
        self._password = generate_password_hash(password)

    @password.deleter
    def password(self):
        del self._password
        print('delele complite.')
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
        

class A:
    def __init__(self, start, end):
        self.start_age = start
        self.end_age = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        pass


if __name__ == '__main__':
    # andy = User()
    # print(andy.password)
    # andy.password = '1234'
    # print(andy.password)
    # del andy.password # del complite
    
    user_max = User()
    user_max.password = 'max'
    print(user_max._password)
    # print(user_max.password_hash)

    for i in A(1, 10):
        print(i)