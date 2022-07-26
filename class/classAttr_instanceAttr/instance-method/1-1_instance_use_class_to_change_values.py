'''
實體方法 (Instance method) 透過 self.__class__屬性(Attribute)來改變類別(Class)的狀態

Reference:
    - https://www.learncodewithmike.com/2020/01/python-method.html
'''
class Cars:
    door = 4 # 類別屬性
    
    # 實體方法 (instance method)
    def drive(self):
        self.__class__.door = 5
        
        
print('Cars original door: ', Cars.door) # 4
print('Cars: ', Cars.drive) # <function Cars.drive at 0x000001A09D3C0790>

c = Cars()
c.drive()
print('Cars new door: ', Cars.door) # 5


'''Results:
Cars original door:  4
Cars:  <function Cars.drive at 0x000001A09D3C0790>
Cars new door:  5
'''

