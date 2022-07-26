'''
實體方法(Instance Method)
    - 至少要有一個self參數
    - 實體方法(Instance Method) 透過self參數可以自由的存取物件 (Object)的屬性 (Attribute)及其他方法(Method)
    
Reference:
    - https://www.learncodewithmike.com/2020/01/python-method.html
'''
class Cars:
    
    # 實體方法(Instance Method)
    def drive(self):
        print('Drive is instance method.')
        

c = Cars()
c.drive()

'''Results:
Drive is instance method.
'''