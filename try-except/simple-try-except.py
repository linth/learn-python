"""
References:
    - https://realpython.com/python-exceptions/
"""


class Solution:

    def __init__(self):
        self.x = None
        self.y = None
        self.num_of_closing_app = 3

    def input_two_numbers(self):
        self.close_app()
        try:
            x = int(input('Please type the first number.'))
            y = int(input('Please type the second number.'))

            res = self.division(x, y)
            print('the result of res is ', res)
        except ZeroDivisionError as e:
            print('It\'s not suitable, Please re-try again.')
            print(e)
        except ValueError as e:
            print('It\'s not a number, Please re-try again.')
            print(e)
        finally:
            if self.num_of_closing_app > 0:
                self.input_two_numbers()

    def close_app(self):
        self.num_of_closing_app -= 1

    @staticmethod
    def division(a, b):
        return a / b


if __name__ == '__main__':
    s = Solution()
    s.input_two_numbers()
    # s.input_two_numbers()

    # a = [1, 2, 3, 1, 2, 3, 4, 1]
    # b = set(a)
    # print(b)
