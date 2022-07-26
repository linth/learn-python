'''
Constructor Method
    - __init__()
    - 初始值設定
    
    
Reference:
    - https://www.geeksforgeeks.org/constructors-in-python/
    - https://www.learncodewithmike.com/2020/01/python-method.html
'''

class Cars:
    
    # default constructor. 
    def __init__(self):
        self.color = "blue"
        
    # 實體方法 (instance method)
    def drive(self):
        print(f'{self} is {self.color}')
        self.message() # 呼叫其他方法
        
    def message(self):
        print('Message method is called.')
        

c = Cars()
c.drive()

''' Results:
<__main__.Cars object at 0x0000015D63710FD0> is blue
Message method is called.
'''

# Cars.drive()
# TypeError: drive() missing 1 required positional argument: 'self'

