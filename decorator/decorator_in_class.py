"""
Goal: learn how to use @decorator in the class.

Keyword:
    - @classmethod
    - @staticmethod
    - @property

References:
    - https://www.maxlist.xyz/2019/12/25/python-property/
"""


class BankAccountUsingGeneral:
    """ use get or set method to set up your attribute. """

    def __init__(self, account, password):
        self._account = account
        self._password = password

    def get_password(self):
        return self._password

    def set_password(self, pwd):
        self._password = pwd

    def delete_password(self):
        del self._password


class BankAccount:

    def __init__(self, account=None, password='0000'):
        self.__id = 1
        self.account = account
        self._password = password

    @property
    def id(self):
        """
        only read, cannot write the id attribute.
        :return:
        """
        return self.__id

    @property
    def password(self):
        """
        read the password attribute.
        :return: the value of password.
        """
        return self._password

    @password.setter
    def password(self, pwd):
        """
        set up the password attribute.
        :param pwd: password value.
        :return:
        """
        if not isinstance(pwd, str):
            raise ValueError('Password must be string.')
        self._password = pwd

    @password.deleter
    def password(self):
        """
        delete the password attribute.
        :return: {successful/false}
        """
        try:
            del self._password
            return {f'[Successful] the object is deleted.'}
        except Exception as e:
            print(f'[Error] deleter password, {e}')
            return {f'[Error] deleter password, {e}'}


if __name__ == '__main__':
    b = BankAccount('01')
    print(b.account)
    print(b.id, b.account, b.password)

    # FIXME: because we use __<attribute> to protect the attribute.
    # AttributeError: can't set attribute
    # b.id = 2

    b.password = '1111'
    print(b.id, b.account, b.password)
    del b.password
    print(b.id, b.account)

    # FIXME: because of deleting the attribute of password, that's
    #  reason that 'BankAccount' object has no attribute '_password'.
    # AttributeError: 'BankAccount' object has no attribute '_password'
    # print('===>', b.password)