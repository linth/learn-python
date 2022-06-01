'''
private variable in python (私有)
    - 繼承下來的 child class 不可以抓取 parent class 參數
    - 需要增加 public method 去抓取

Reference:
    - https://www.geeksforgeeks.org/private-variables-python/?ref=gcse
'''

class Shape:    
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        
    def display_sides(self):
        print("Length: ", self.__length)
        print("Breadth: ", self.__breadth)
        

class Rectangle(Shape):    
    def __init__(self, length, breadth):
        # Shape.__init__(self, length, breadth)
        super().__init__(length, breadth)
        
    def cal_area(self):
        print('area: ', self._length * self._breadth)
        
if __name__ == '__main__':
    r = Shape(80, 50)
    r.display_sides()
    print('length', r.__length) # AttributeError: 'Shape' object has no attribute '__length'
    print('breadth', r.__breadth) # AttributeError: 'Shape' object has no attribute '__breadth'
    
    # r = Rectangle(80, 50)
    # r.display_sides()
    # r.cal_area()
    