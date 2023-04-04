'''
    Four parts in the unittest.
    - Test case (unit test.)
    - Test fixture (need to check the pre-source before executing one or more testing.)
    - Test suite (a set of user case, packages or both of them.)
    - Test runner (response to execute the test code and provide the results.)

    Reference:
    - http://www.codedata.com.tw/python/python-tutorial-the-6th-class-1-unittest/
    - https://imsardine.wordpress.com/tech/unit-testing-in-python/
'''
# without unittest.
# class Calculator:
#     def mod(self, dividend, divisor):
#         remainder = dividend % divisor
#         quotient = (dividend - remainder) / divisor
#         return quotient, remainder
#
# if __name__ == '__main__':
#     cal = Calculator()
#     assert cal.mod(5, 3) == (1, 2) # 5 / 3 = 1 ... 2
#     assert cal.mod(8, 4) == (1, 0) # 8 / 4 = 2 ... 0

'''
    "unittest" is suitable for executing unit test because of test case must be self-contained.
    That means is that the unittest isn't appropriated for executing funtional test.
'''
import unittest

class Calculator:
    def mod(self, dividend, divisor):
        remainder = dividend % divisor
        quotient = (dividend - remainder) / divisor
        return quotient, remainder

class CalculatorTest(unittest.TestCase):
    def test_mod_with_remainder(self):
        cal = Calculator()
        self.assertEqual(cal.mod(5, 3), (1, 2))

    # def test_mod_with_remainder(self):
    #     cal = Calculator()
    #     self.assertEqual(cal.mod(8, 4), (2, 0))

    def test_mod_divide_by_zero(self):
        cal = Calculator()
        # assertRaises(ZeroDivisionError, cal.mod, 7, 1) # cannot be used.
        self.assertEqual(cal.mod(4, 2), (2, 0))


if __name__ == '__main__':
    # E for Error, F for failure
    unittest.main()
