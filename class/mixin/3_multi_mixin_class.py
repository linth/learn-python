'''
一般傳統 class 寫法
    - 建立多個 mixin class
    - 可以使用 Mixin 來繼承原有的 class 來不變更原有的程式碼下進行擴充功能。
    

Reference:
    - https://github.com/twtrubiks/python-notes/tree/master/what_is_the_mixin
'''

class HelloMixin:
    
    def display(self):
        print('hello')
        


class StrMixin:
    
    def __str__(self):
        return f'{self.x1}_{self.x2}'
    
    

class A(StrMixin, HelloMixin):
    
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        
    
    
if __name__ == '__main__':
    a = A('x1', 'y1')
    print(a)
    a.display()
        
    