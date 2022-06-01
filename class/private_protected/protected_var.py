'''
Protected variable in Python
    - 繼承下來的 child class可以抓取 parent class 參數
    
Reference:
    - https://www.geeksforgeeks.org/protected-variable-in-python/
'''

class Shape:
    
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth
        
    def display_sides(self):
        print("Length: ", self._length)
        print("Breadth: ", self._breadth)
        

class Rectangle(Shape):
    
    def __init__(self, length, breadth):
        # Shape.__init__(self, length, breadth)
        super().__init__(length, breadth)
        
    def cal_area(self):
        print('area: ', self._length * self._breadth)
        
        
if __name__ == '__main__':
    r = Rectangle(80, 50)
    r.display_sides()
    r.cal_area()
    