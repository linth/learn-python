"""
References:
    - https://realpython.com/python-exceptions/
"""
error_code = {
    'general_error': 100,
    'zero division error': 101,
    'value error': 102,
}


class CustomException(Exception):
    def __init__(self, error_msg, code):
        self._error_msg = error_msg
        self._status_code = code


class DivisionGame:
    """ This is a division game. """
    def __init__(self):
        self.x = None
        self.y = None
        self.num_of_closing_app = 3

    def division_two_numbers(self):
        try:
            x = int(input('Please type the first number.\n'))
            y = int(input('Please type the second number.\n'))

            res = self.division(x, y)
            print(f'The result of res is {res}')
            print(f'Num of closing app: {self.num_of_closing_app}')
        except ZeroDivisionError as e:
            print(f'It\'s not suitable, please try again.')
            self.close_app()
            # raise CustomException(e, error_code['zero division error'])
        except ValueError as e:
            print(f'It\'s not an integer number, please try again.')
            self.close_app()
            # raise CustomException(e, error_code['value error'])
        except Exception as e:
            print(f'Something wrong, please try again.')
            self.close_app()
            # raise CustomException(e, error_code['general_error'])
        finally:
            if self.num_of_closing_app > 0:
                print(f'You have {self.num_of_closing_app} time to execute the game.')
                self.division_two_numbers()
            else:
                print(f'Game Over! Thank you.')

    def close_app(self):
        self.num_of_closing_app -= 1

    @staticmethod
    def division(a: int, b: int):
        return a / b


if __name__ == '__main__':
    s = DivisionGame()
    s.division_two_numbers()
    # s.input_two_numbers()

    # a = [1, 2, 3, 1, 2, 3, 4, 1]
    # b = set(a)
    # print(b)
