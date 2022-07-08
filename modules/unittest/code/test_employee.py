'''
test employee class.

Reference:
    - https://www.youtube.com/watch?v=6tNS--WetLI
'''
import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    
    def set_up(self):
        print('set up.')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        
    def tear_down(self):
        print('tear down.')
        pass
    
    def test_email(self):
        print('test eamil.')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')
        
    def test_fullname(self):
        print('test fullname.')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')
        
    def test_appply_raise(self):
        print('test apply raise.')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
    
        
if __name__ == '__main__':
    unittest.main()
    